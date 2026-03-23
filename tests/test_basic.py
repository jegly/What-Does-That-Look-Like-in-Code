"""
tests/test_basic.py - Basic unit tests for WDLIC
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# FIX: import from text_parser, not parser (parser.py shadows stdlib `parser` module)
from text_parser import TextParser, ParsedFeatures
from router import CategoryRouter, CategoryScore
from ir import IRBuilder, IntermediateRepresentation
from codegen import get_registry


def test_parser_import():
    """Test that parser imports correctly"""
    parser = TextParser()
    assert parser is not None
    assert parser.nlp is not None


def test_parser_basic():
    """Test basic parsing functionality"""
    parser = TextParser()
    text = "A person walks to the store."
    features = parser.parse(text)

    assert isinstance(features, ParsedFeatures)
    assert features.raw_text == text
    assert len(features.actions) > 0
    assert "walk" in features.actions or "walks" in [a.lower() for a in features.actions]


def test_router_psychology():
    """Test routing to psychology category"""
    parser = TextParser()
    router = CategoryRouter()

    text = "Someone feels anxious about making a decision."
    features = parser.parse(text)
    category = router.get_primary_category(features)

    assert isinstance(category, CategoryScore)
    assert category.name in ["psychology", "social"]
    assert category.confidence > 0


def test_router_physics():
    """Test routing to physics category"""
    parser = TextParser()
    router = CategoryRouter()

    text = "A ball falls due to gravity with acceleration."
    features = parser.parse(text)
    category = router.get_primary_category(features)

    assert isinstance(category, CategoryScore)
    assert category.name in ["physics", "generic"]


def test_ir_builder():
    """Test IR builder"""
    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()

    text = "A person decides to act."
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)

    assert isinstance(ir, IntermediateRepresentation)
    assert ir.raw_text == text
    assert ir.category is not None
    # FIX: original test assumed assumptions were always populated, but generic
    # category now provides a fallback assumption, so this is always true.
    assert len(ir.assumptions) > 0


def test_ir_builder_detail_stored():
    """Test that detail level is stored in IR"""
    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()

    text = "A person thinks carefully."
    features = parser.parse(text)
    category = router.get_primary_category(features)

    for detail in ("low", "med", "high"):
        ir = builder.build(features, category, detail=detail)
        assert ir.detail == detail


def test_code_generation_pseudo():
    """Test pseudo-code generation"""
    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()
    registry = get_registry()

    text = "Someone overcomes fear."
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)

    pseudo = registry.generate_pseudo(ir)

    assert isinstance(pseudo, str)
    assert len(pseudo) > 0
    assert "//" in pseudo or "LOGIC" in pseudo


def test_code_generation_python():
    """Test Python code generation"""
    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()
    registry = get_registry()

    text = "A ball is thrown."
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)

    python_code = registry.generate_python(ir)

    assert isinstance(python_code, str)
    assert len(python_code) > 0
    assert "def " in python_code or "class " in python_code or "import " in python_code


def test_multiple_categories():
    """Test that router can identify multiple possible categories"""
    parser = TextParser()
    router = CategoryRouter()

    text = "Calculate the force needed to optimize trajectory."
    features = parser.parse(text)
    categories = router.route(features)

    assert len(categories) >= 1
    category_names = [c.name for c in categories]
    assert any(cat in ["physics", "mathematics", "optimization"] for cat in category_names)


def test_all_registered_categories_generate():
    """Test that every registered category produces non-empty output"""
    registry = get_registry()
    for cat_name in registry.generators:
        ir = IntermediateRepresentation(
            raw_text=f"Test scenario for {cat_name}",
            category=cat_name,
            confidence=1.0,
        )
        pseudo = registry.generate_pseudo(ir)
        python = registry.generate_python(ir)
        assert len(pseudo) > 0, f"Empty pseudo for category: {cat_name}"
        assert len(python) > 0, f"Empty python for category: {cat_name}"


def test_end_to_end_psychology():
    """End-to-end test for psychology scenario"""
    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()
    registry = get_registry()

    text = "A person gains confidence after success."
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)
    pseudo = registry.generate_pseudo(ir)
    python = registry.generate_python(ir)

    assert category.name in ["psychology", "social", "generic"]
    assert len(pseudo) > 0
    assert len(python) > 0
    assert "confidence" in python.lower() or "Psychological" in python


def test_end_to_end_physics():
    """End-to-end test for physics scenario"""
    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()
    registry = get_registry()

    text = "A projectile moves with velocity and acceleration."
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)
    pseudo = registry.generate_pseudo(ir)
    python = registry.generate_python(ir)

    assert len(pseudo) > 0
    assert len(python) > 0
    assert "velocity" in python.lower() or "physics" in python.lower() or "import numpy" in python


def test_physics_generated_code_uses_floats():
    """Ensure generated physics call site uses numeric literals, not strings"""
    from codegen.physics import PhysicsGenerator

    ir = IntermediateRepresentation(
        raw_text="A ball thrown at 30 m/s at 60 degrees.",
        category="physics",
    )
    python = PhysicsGenerator.generate_python(ir)
    # The call line must contain float literals, not quoted strings
    call_line = next(l for l in python.splitlines() if "projectile_motion" in l and "v0=" in l)
    assert '"' not in call_line and "'" not in call_line, (
        f"String literal found in generated call: {call_line}"
    )


def test_social_variance_uses_true_mean():
    """Ensure social dynamics variance is computed with the true mean"""
    from codegen.psychology import SocialGenerator

    ir = IntermediateRepresentation(
        raw_text="Group of people discussing an issue.",
        category="social",
    )
    python = SocialGenerator.generate_python(ir)
    # Must calculate mean_opinion before variance
    assert "mean_opinion" in python
    lines = python.splitlines()
    mean_line_idx = next(i for i, l in enumerate(lines) if "mean_opinion" in l)
    var_line_idx  = next(i for i, l in enumerate(lines) if "variance" in l and "mean_opinion" in l)
    assert mean_line_idx < var_line_idx


if __name__ == "__main__":
    print("Running basic tests...")

    test_parser_import();              print("✓ Parser import")
    test_parser_basic();               print("✓ Parser basic")
    test_router_psychology();          print("✓ Router psychology")
    test_router_physics();             print("✓ Router physics")
    test_ir_builder();                 print("✓ IR builder")
    test_ir_builder_detail_stored();   print("✓ IR builder detail level")
    test_code_generation_pseudo();     print("✓ Code generation (pseudo)")
    test_code_generation_python();     print("✓ Code generation (python)")
    test_multiple_categories();        print("✓ Multiple categories")
    test_all_registered_categories_generate(); print("✓ All categories generate")
    test_end_to_end_psychology();      print("✓ End-to-end (psychology)")
    test_end_to_end_physics();         print("✓ End-to-end (physics)")
    test_physics_generated_code_uses_floats(); print("✓ Physics float literals")
    test_social_variance_uses_true_mean();     print("✓ Social variance formula")

    print("\n✓ All tests passed!")
