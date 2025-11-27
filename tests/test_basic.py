"""
tests/test_basic.py - Basic unit tests for WDLIC
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from parser import TextParser, ParsedFeatures
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
    # Should detect physics keywords
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
    assert len(ir.assumptions) > 0


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
    # Should contain Python syntax
    assert "def " in python_code or "class " in python_code or "import " in python_code


def test_multiple_categories():
    """Test that router can identify multiple possible categories"""
    parser = TextParser()
    router = CategoryRouter()
    
    text = "Calculate the force needed to optimize trajectory."
    features = parser.parse(text)
    categories = router.route(features)
    
    assert len(categories) >= 1
    # Should find both physics and math/optimization signals
    category_names = [c.name for c in categories]
    assert any(cat in ["physics", "mathematics", "optimization"] for cat in category_names)


def test_end_to_end_psychology():
    """End-to-end test for psychology scenario"""
    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()
    registry = get_registry()
    
    text = "A person gains confidence after success."
    
    # Full pipeline
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)
    pseudo = registry.generate_pseudo(ir)
    python = registry.generate_python(ir)
    
    # Verify outputs
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
    
    # Full pipeline
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)
    pseudo = registry.generate_pseudo(ir)
    python = registry.generate_python(ir)
    
    # Verify outputs
    assert len(pseudo) > 0
    assert len(python) > 0
    # Should contain physics-related terms
    assert "velocity" in python.lower() or "physics" in python.lower() or "import numpy" in python


if __name__ == "__main__":
    # Run tests manually
    print("Running basic tests...")
    
    test_parser_import()
    print("✓ Parser import")
    
    test_parser_basic()
    print("✓ Parser basic")
    
    test_router_psychology()
    print("✓ Router psychology")
    
    test_router_physics()
    print("✓ Router physics")
    
    test_ir_builder()
    print("✓ IR builder")
    
    test_code_generation_pseudo()
    print("✓ Code generation (pseudo)")
    
    test_code_generation_python()
    print("✓ Code generation (python)")
    
    test_multiple_categories()
    print("✓ Multiple categories")
    
    test_end_to_end_psychology()
    print("✓ End-to-end (psychology)")
    
    test_end_to_end_physics()
    print("✓ End-to-end (physics)")
    
    print("\n✓ All tests passed!")
