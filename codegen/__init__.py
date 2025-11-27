"""
codegen/__init__.py - Code generation registry and dispatcher
"""
from typing import Dict, Any, Callable
from codegen.psychology import PsychologyGenerator, SocialGenerator
from codegen.physics import PhysicsGenerator
from codegen.mathematics import MathematicsGenerator


class GenericGenerator:
    """Fallback generator for unspecialized categories"""
    
    @staticmethod
    def generate_pseudo(ir) -> str:
        pseudo = []
        pseudo.append("// GENERIC LOGIC")
        pseudo.append(f"// Scenario: {ir.raw_text}")
        pseudo.append("")
        pseudo.append("Input Processing:")
        
        if ir.entities:
            pseudo.append(f"  Entities: {', '.join([e.name for e in ir.entities])}")
        if ir.actions:
            pseudo.append(f"  Actions: {', '.join([a.verb for a in ir.actions])}")
        
        pseudo.append("")
        pseudo.append("Logic Flow:")
        pseudo.append("  1. Parse input")
        pseudo.append("  2. Execute actions")
        pseudo.append("  3. Update state")
        pseudo.append("  4. Return output")
        
        return "\n".join(pseudo)
    
    @staticmethod
    def generate_python(ir) -> str:
        code = []
        code.append('"""')
        code.append(f'Generic Model: {ir.raw_text}')
        code.append('"""')
        code.append('')
        code.append('def process_scenario():')
        code.append('    """Generic scenario processing"""')
        code.append(f'    scenario = "{ir.raw_text}"')
        code.append('    ')
        code.append('    print(f"Processing: {scenario}")')
        code.append('    ')
        
        if ir.entities:
            code.append('    entities = [')
            for entity in ir.entities:
                code.append(f'        "{entity.name}",')
            code.append('    ]')
            code.append('    print(f"Entities: {entities}")')
        
        if ir.actions:
            code.append('    actions = [')
            for action in ir.actions:
                code.append(f'        "{action.verb}",')
            code.append('    ]')
            code.append('    print(f"Actions: {actions}")')
        
        code.append('    ')
        code.append('    print("\\nScenario processing complete.")')
        code.append('')
        code.append('')
        code.append('if __name__ == "__main__":')
        code.append('    process_scenario()')
        
        return "\n".join(code)


class CodeGeneratorRegistry:
    """Central registry for code generators"""
    
    def __init__(self):
        self.generators = {
            "psychology": PsychologyGenerator,
            "social": SocialGenerator,
            "physics": PhysicsGenerator,
            "mathematics": MathematicsGenerator,
            "math": MathematicsGenerator,  # alias
            "generic": GenericGenerator,
        }
    
    def get_generator(self, category: str):
        """Get generator for category, with fallback to generic"""
        return self.generators.get(category.lower(), GenericGenerator)
    
    def generate_pseudo(self, ir) -> str:
        """Generate pseudo-code for IR"""
        generator_class = self.get_generator(ir.category)
        return generator_class.generate_pseudo(ir)
    
    def generate_python(self, ir) -> str:
        """Generate Python code for IR"""
        generator_class = self.get_generator(ir.category)
        return generator_class.generate_python(ir)
    
    def register_generator(self, category: str, generator_class):
        """Register a new generator (for extensibility)"""
        self.generators[category.lower()] = generator_class


# Singleton instance
_registry = CodeGeneratorRegistry()


def get_registry() -> CodeGeneratorRegistry:
    """Get the global generator registry"""
    return _registry
