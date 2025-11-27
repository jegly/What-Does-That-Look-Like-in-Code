"""
codegen/psychology.py - Psychology/Social behavior code generation
"""
from typing import Dict, Any


class PsychologyGenerator:
    """Generates code for psychological scenarios"""
    
    @staticmethod
    def generate_pseudo(ir) -> str:
        """Generate pseudo-code for psychology scenario"""
        pseudo = []
        pseudo.append("// PSYCHOLOGICAL MODEL")
        pseudo.append("// Represents mental states and decision-making")
        pseudo.append("")
        
        # Define actors with psychological variables
        if ir.entities:
            for entity in ir.entities:
                pseudo.append(f"Actor: {entity.name}")
                pseudo.append(f"  - confidence_level: 0.7 (0-1 scale)")
                pseudo.append(f"  - desire_to_act: 0.8")
                pseudo.append(f"  - fear_of_rejection: 0.4")
                pseudo.append(f"  - self_awareness: 0.6")
                pseudo.append("")
        
        # Decision logic
        pseudo.append("Decision Logic:")
        pseudo.append("  motivation = desire_to_act × confidence_level")
        pseudo.append("  inhibition = fear_of_rejection × (1 - self_awareness)")
        pseudo.append("  ")
        pseudo.append("  IF motivation > inhibition:")
        pseudo.append("    EXECUTE action")
        pseudo.append("  ELSE:")
        pseudo.append("    SUPPRESS action")
        pseudo.append("")
        
        # Outcome evaluation
        pseudo.append("Outcome Evaluation:")
        pseudo.append("  IF action successful:")
        pseudo.append("    confidence_level += 0.1")
        pseudo.append("    fear_of_rejection -= 0.05")
        pseudo.append("  ELSE:")
        pseudo.append("    confidence_level -= 0.15")
        pseudo.append("    fear_of_rejection += 0.1")
        
        return "\n".join(pseudo)
    
    @staticmethod
    def generate_python(ir) -> str:
        """Generate executable Python code for psychology scenario"""
        code = []
        code.append('"""')
        code.append(f'Psychological Model: {ir.raw_text}')
        code.append('"""')
        code.append('import random')
        code.append('')
        code.append('')
        code.append('class PsychologicalAgent:')
        code.append('    """Represents an agent with psychological states"""')
        code.append('    ')
        code.append('    def __init__(self, name, confidence=0.7, desire=0.8, fear=0.4):')
        code.append('        self.name = name')
        code.append('        self.confidence_level = confidence')
        code.append('        self.desire_to_act = desire')
        code.append('        self.fear_of_rejection = fear')
        code.append('        self.self_awareness = 0.6')
        code.append('    ')
        code.append('    def decide_to_act(self) -> bool:')
        code.append('        """Psychological decision-making logic"""')
        code.append('        motivation = self.desire_to_act * self.confidence_level')
        code.append('        inhibition = self.fear_of_rejection * (1 - self.self_awareness)')
        code.append('        ')
        code.append('        # Add some randomness for realism')
        code.append('        noise = random.uniform(-0.1, 0.1)')
        code.append('        ')
        code.append('        decision_threshold = motivation - inhibition + noise')
        code.append('        return decision_threshold > 0.5')
        code.append('    ')
        code.append('    def update_after_outcome(self, success: bool):')
        code.append('        """Update psychological state based on outcome"""')
        code.append('        if success:')
        code.append('            self.confidence_level = min(1.0, self.confidence_level + 0.1)')
        code.append('            self.fear_of_rejection = max(0.0, self.fear_of_rejection - 0.05)')
        code.append('            print(f"{self.name}: Confidence increased!")')
        code.append('        else:')
        code.append('            self.confidence_level = max(0.0, self.confidence_level - 0.15)')
        code.append('            self.fear_of_rejection = min(1.0, self.fear_of_rejection + 0.1)')
        code.append('            print(f"{self.name}: Experienced setback.")')
        code.append('')
        code.append('')
        code.append('# Simulation')
        code.append('if __name__ == "__main__":')
        
        # Create agents based on entities
        if ir.entities:
            code.append(f'    agent = PsychologicalAgent("{ir.entities[0].name}")')
        else:
            code.append('    agent = PsychologicalAgent("Agent")')
        
        code.append('    ')
        code.append('    print(f"Initial state: confidence={agent.confidence_level:.2f}, fear={agent.fear_of_rejection:.2f}")')
        code.append('    ')
        code.append('    # Simulate decision')
        code.append('    if agent.decide_to_act():')
        code.append('        print(f"{agent.name} decides to ACT")')
        code.append('        ')
        code.append('        # Simulate outcome (60% success rate)')
        code.append('        success = random.random() < 0.6')
        code.append('        agent.update_after_outcome(success)')
        code.append('    else:')
        code.append('        print(f"{agent.name} decides NOT to act (inhibition too high)")')
        code.append('    ')
        code.append('    print(f"Final state: confidence={agent.confidence_level:.2f}, fear={agent.fear_of_rejection:.2f}")')
        
        return "\n".join(code)


class SocialGenerator:
    """Generates code for social dynamics scenarios"""
    
    @staticmethod
    def generate_pseudo(ir) -> str:
        """Generate pseudo-code for social scenario"""
        pseudo = []
        pseudo.append("// SOCIAL DYNAMICS MODEL")
        pseudo.append("// Group behavior and social influence")
        pseudo.append("")
        pseudo.append("Group Members: [Member1, Member2, Member3, ...]")
        pseudo.append("")
        pseudo.append("FOR EACH member:")
        pseudo.append("  - opinion: initial_value")
        pseudo.append("  - conformity_tendency: 0.6")
        pseudo.append("  - influence_on_others: 0.5")
        pseudo.append("")
        pseudo.append("Social Influence Loop:")
        pseudo.append("  FOR iteration in 1..N:")
        pseudo.append("    FOR EACH member:")
        pseudo.append("      peer_opinions = GET opinions from connected peers")
        pseudo.append("      average_peer_opinion = MEAN(peer_opinions)")
        pseudo.append("      ")
        pseudo.append("      // Update opinion based on social influence")
        pseudo.append("      member.opinion = member.opinion × (1 - conformity_tendency) +")
        pseudo.append("                       average_peer_opinion × conformity_tendency")
        pseudo.append("")
        pseudo.append("  RETURN final_opinions")
        
        return "\n".join(pseudo)
    
    @staticmethod
    def generate_python(ir) -> str:
        """Generate executable Python code for social scenario"""
        code = []
        code.append('"""')
        code.append(f'Social Dynamics Model: {ir.raw_text}')
        code.append('"""')
        code.append('import random')
        code.append('from typing import List, Dict')
        code.append('')
        code.append('')
        code.append('class SocialAgent:')
        code.append('    """Agent in a social network"""')
        code.append('    ')
        code.append('    def __init__(self, name: str, initial_opinion: float = 0.5):')
        code.append('        self.name = name')
        code.append('        self.opinion = initial_opinion  # 0-1 scale')
        code.append('        self.conformity_tendency = random.uniform(0.3, 0.8)')
        code.append('        self.influence_strength = random.uniform(0.3, 0.7)')
        code.append('    ')
        code.append('    def update_opinion(self, peer_opinions: List[float]):')
        code.append('        """Update opinion based on social influence"""')
        code.append('        if not peer_opinions:')
        code.append('            return')
        code.append('        ')
        code.append('        avg_peer_opinion = sum(peer_opinions) / len(peer_opinions)')
        code.append('        ')
        code.append('        # Blend own opinion with peer average')
        code.append('        self.opinion = (self.opinion * (1 - self.conformity_tendency) +')
        code.append('                       avg_peer_opinion * self.conformity_tendency)')
        code.append('')
        code.append('')
        code.append('class SocialNetwork:')
        code.append('    """Simulates social dynamics"""')
        code.append('    ')
        code.append('    def __init__(self, num_agents: int = 5):')
        code.append('        self.agents = [')
        code.append('            SocialAgent(f"Agent{i}", random.uniform(0.2, 0.8))')
        code.append('            for i in range(num_agents)')
        code.append('        ]')
        code.append('    ')
        code.append('    def simulate(self, iterations: int = 10):')
        code.append('        """Run social influence simulation"""')
        code.append('        print(f"Initial opinions: {[f\'{a.opinion:.2f}\' for a in self.agents]}")')
        code.append('        ')
        code.append('        for t in range(iterations):')
        code.append('            # Each agent observes all others (fully connected)')
        code.append('            for agent in self.agents:')
        code.append('                peer_opinions = [other.opinion for other in self.agents if other != agent]')
        code.append('                agent.update_opinion(peer_opinions)')
        code.append('        ')
        code.append('        print(f"Final opinions:   {[f\'{a.opinion:.2f}\' for a in self.agents]}")')
        code.append('        ')
        code.append('        # Check for consensus')
        code.append('        variance = sum((a.opinion - self.agents[0].opinion)**2 for a in self.agents) / len(self.agents)')
        code.append('        if variance < 0.01:')
        code.append('            print("→ Consensus reached!")')
        code.append('        else:')
        code.append('            print(f"→ Opinions still diverse (variance={variance:.4f})")')
        code.append('')
        code.append('')
        code.append('# Run simulation')
        code.append('if __name__ == "__main__":')
        code.append('    network = SocialNetwork(num_agents=6)')
        code.append('    network.simulate(iterations=15)')
        
        return "\n".join(code)


if __name__ == "__main__":
    # Test
    from ir import IntermediateRepresentation
    
    ir = IntermediateRepresentation(
        raw_text="A guy decides whether to approach someone.",
        category="psychology"
    )
    
    gen = PsychologyGenerator()
    print(gen.generate_pseudo(ir))
    print("\n" + "="*60 + "\n")
    print(gen.generate_python(ir))
