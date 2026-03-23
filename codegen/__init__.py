"""
codegen/__init__.py - Code generation registry and dispatcher
"""
from codegen.psychology import PsychologyGenerator, SocialGenerator
from codegen.physics import PhysicsGenerator
from codegen.mathematics import MathematicsGenerator


class GenericGenerator:
    """Fallback generator for unspecialised categories"""

    @staticmethod
    def generate_pseudo(ir) -> str:
        pseudo = [
            "// GENERIC LOGIC",
            f"// Scenario: {ir.raw_text}",
            "",
            "Input Processing:",
        ]
        if ir.entities:
            pseudo.append(f"  Entities: {', '.join([e.name for e in ir.entities])}")
        if ir.actions:
            pseudo.append(f"  Actions: {', '.join([a.verb for a in ir.actions])}")
        pseudo += [
            "",
            "Logic Flow:",
            "  1. Parse input",
            "  2. Execute actions",
            "  3. Update state",
            "  4. Return output",
        ]
        return "\n".join(pseudo)

    @staticmethod
    def generate_python(ir) -> str:
        code = [
            '"""',
            f"Generic Model: {ir.raw_text}",
            '"""',
            "",
            "def process_scenario():",
            '    """Generic scenario processing"""',
            f'    scenario = "{ir.raw_text}"',
            "    ",
            '    print(f"Processing: {scenario}")',
            "    ",
        ]
        if ir.entities:
            code.append("    entities = [")
            for entity in ir.entities:
                code.append(f'        "{entity.name}",')
            code += ["    ]", '    print(f"Entities: {entities}")']
        if ir.actions:
            code.append("    actions = [")
            for action in ir.actions:
                code.append(f'        "{action.verb}",')
            code += ["    ]", '    print(f"Actions: {actions}")']
        code += [
            "    ",
            '    print("\\nScenario processing complete.")',
            "",
            "",
            'if __name__ == "__main__":',
            "    process_scenario()",
        ]
        return "\n".join(code)


class OptimizationGenerator:
    """Generates code for optimisation scenarios"""

    @staticmethod
    def generate_pseudo(ir) -> str:
        return "\n".join([
            "// OPTIMISATION MODEL",
            f"// Scenario: {ir.raw_text}",
            "",
            "Define:",
            "  objective_function f(x)",
            "  constraints g(x) <= 0",
            "",
            "Solve:",
            "  IF unconstrained: gradient_descent(f)",
            "  ELSE: constrained_optimisation(f, g)",
            "",
            "Return: optimal x, f(x)",
        ])

    @staticmethod
    def generate_python(ir) -> str:
        return "\n".join([
            '"""',
            f"Optimisation: {ir.raw_text}",
            '"""',
            "from scipy.optimize import minimize",
            "import numpy as np",
            "",
            "",
            "def objective(x):",
            "    # Define your objective function here",
            "    return x[0]**2 + x[1]**2  # example: minimise distance from origin",
            "",
            "",
            "def run_optimisation():",
            "    x0 = np.array([1.0, 1.0])  # initial guess",
            "    result = minimize(objective, x0, method='BFGS')",
            "    print(f'Optimal x: {result.x}')",
            "    print(f'Optimal f(x): {result.fun:.6f}')",
            "    print(f'Converged: {result.success}')",
            "",
            "",
            'if __name__ == "__main__":',
            "    run_optimisation()",
        ])


class RulesGenerator:
    """Generates code for rule-based / expert-system scenarios"""

    @staticmethod
    def generate_pseudo(ir) -> str:
        return "\n".join([
            "// RULE ENGINE",
            f"// Scenario: {ir.raw_text}",
            "",
            "FOR EACH rule IN rules (sorted by priority DESC):",
            "  IF evaluate(rule.condition, state):",
            "    execute(rule.action)",
            "    IF rule.is_terminal: STOP",
            "",
            "RETURN updated_state",
        ])

    @staticmethod
    def generate_python(ir) -> str:
        return "\n".join([
            '"""',
            f"Rule Engine: {ir.raw_text}",
            '"""',
            "from dataclasses import dataclass, field",
            "from typing import Callable, Any",
            "",
            "",
            "@dataclass",
            "class Rule:",
            "    name: str",
            "    condition: Callable[[dict], bool]",
            "    action: Callable[[dict], None]",
            "    priority: int = 1",
            "",
            "",
            "class RuleEngine:",
            '    """Simple forward-chaining rule engine"""',
            "",
            "    def __init__(self):",
            "        self.rules: list[Rule] = []",
            "",
            "    def add_rule(self, rule: Rule):",
            "        self.rules.append(rule)",
            "        self.rules.sort(key=lambda r: r.priority, reverse=True)",
            "",
            "    def run(self, state: dict) -> dict:",
            "        for rule in self.rules:",
            "            if rule.condition(state):",
            "                rule.action(state)",
            "        return state",
            "",
            "",
            'if __name__ == "__main__":',
            "    engine = RuleEngine()",
            "    engine.add_rule(Rule(",
            '        name="example",',
            "        condition=lambda s: s.get('x', 0) > 10,",
            "        action=lambda s: s.update({'triggered': True}),",
            "        priority=1,",
            "    ))",
            "    result = engine.run({'x': 15})",
            "    print(result)",
        ])


class CodeGeneratorRegistry:
    """Central registry for code generators"""

    def __init__(self):
        # FIX: all categories the router can produce now have an explicit entry.
        # Previously biology/technology/art/philosophy/rules/game/business/ui/optimization
        # were silently falling through to GenericGenerator without being listed here,
        # making the mapping opaque and impossible to override individually.
        self.generators: dict = {
            "psychology":   PsychologyGenerator,
            "social":       SocialGenerator,
            "physics":      PhysicsGenerator,
            "mathematics":  MathematicsGenerator,
            "math":         MathematicsGenerator,   # alias
            "optimization": OptimizationGenerator,
            "opt":          OptimizationGenerator,  # alias
            "rules":        RulesGenerator,
            # These categories fall back to GenericGenerator but are listed explicitly
            # so they can be swapped out without touching the routing logic.
            "game":         GenericGenerator,
            "business":     GenericGenerator,
            "ui":           GenericGenerator,
            "philosophy":   GenericGenerator,
            "biology":      GenericGenerator,
            "technology":   GenericGenerator,
            "art":          GenericGenerator,
            "generic":      GenericGenerator,
        }

    def get_generator(self, category: str):
        """Get generator for category, falling back to GenericGenerator"""
        return self.generators.get(category.lower(), GenericGenerator)

    def generate_pseudo(self, ir) -> str:
        """Generate pseudo-code for IR"""
        return self.get_generator(ir.category).generate_pseudo(ir)

    def generate_python(self, ir) -> str:
        """Generate Python code for IR"""
        return self.get_generator(ir.category).generate_python(ir)

    def register_generator(self, category: str, generator_class):
        """Register a new generator (for extensibility)"""
        self.generators[category.lower()] = generator_class


# Singleton instance
_registry = CodeGeneratorRegistry()


def get_registry() -> CodeGeneratorRegistry:
    """Get the global generator registry"""
    return _registry
