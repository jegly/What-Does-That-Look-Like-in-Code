"""
codegen/psychology.py - Psychology/Social behavior code generation
"""


class PsychologyGenerator:
    """Generates code for psychological scenarios"""

    @staticmethod
    def generate_pseudo(ir) -> str:
        """Generate pseudo-code for psychology scenario"""
        pseudo = [
            "// PSYCHOLOGICAL MODEL",
            "// Represents mental states and decision-making",
            "",
        ]

        for entity in ir.entities:
            pseudo += [
                f"Actor: {entity.name}",
                "  - confidence_level: 0.7 (0-1 scale)",
                "  - desire_to_act: 0.8",
                "  - fear_of_rejection: 0.4",
                "  - self_awareness: 0.6",
                "",
            ]

        pseudo += [
            "Decision Logic:",
            "  motivation = desire_to_act × confidence_level",
            "  inhibition = fear_of_rejection × (1 - self_awareness)",
            "  ",
            "  IF motivation > inhibition:",
            "    EXECUTE action",
            "  ELSE:",
            "    SUPPRESS action",
            "",
            "Outcome Evaluation:",
            "  IF action successful:",
            "    confidence_level += 0.1",
            "    fear_of_rejection -= 0.05",
            "  ELSE:",
            "    confidence_level -= 0.15",
            "    fear_of_rejection += 0.1",
        ]
        return "\n".join(pseudo)

    @staticmethod
    def generate_python(ir) -> str:
        """Generate executable Python code for psychology scenario"""
        code = [
            '"""',
            f"Psychological Model: {ir.raw_text}",
            '"""',
            "import random",
            "",
            "",
            "class PsychologicalAgent:",
            '    """Represents an agent with psychological states"""',
            "    ",
            "    def __init__(self, name, confidence=0.7, desire=0.8, fear=0.4):",
            "        self.name = name",
            "        self.confidence_level = confidence",
            "        self.desire_to_act = desire",
            "        self.fear_of_rejection = fear",
            "        self.self_awareness = 0.6",
            "    ",
            "    def decide_to_act(self) -> bool:",
            '        """Psychological decision-making logic"""',
            "        motivation = self.desire_to_act * self.confidence_level",
            "        inhibition = self.fear_of_rejection * (1 - self.self_awareness)",
            "        noise = random.uniform(-0.1, 0.1)",
            "        return (motivation - inhibition + noise) > 0.5",
            "    ",
            "    def update_after_outcome(self, success: bool):",
            '        """Update psychological state based on outcome"""',
            "        if success:",
            "            self.confidence_level = min(1.0, self.confidence_level + 0.1)",
            "            self.fear_of_rejection = max(0.0, self.fear_of_rejection - 0.05)",
            '            print(f"{self.name}: Confidence increased!")',
            "        else:",
            "            self.confidence_level = max(0.0, self.confidence_level - 0.15)",
            "            self.fear_of_rejection = min(1.0, self.fear_of_rejection + 0.1)",
            '            print(f"{self.name}: Experienced setback.")',
            "",
            "",
            "# Simulation",
            'if __name__ == "__main__":',
        ]

        agent_name = ir.entities[0].name if ir.entities else "Agent"
        code += [
            f'    agent = PsychologicalAgent("{agent_name}")',
            "    ",
            '    print(f"Initial state: confidence={agent.confidence_level:.2f}, '
            'fear={agent.fear_of_rejection:.2f}")',
            "    ",
            "    if agent.decide_to_act():",
            '        print(f"{agent.name} decides to ACT")',
            "        success = random.random() < 0.6",
            "        agent.update_after_outcome(success)",
            "    else:",
            '        print(f"{agent.name} decides NOT to act (inhibition too high)")',
            "    ",
            '    print(f"Final state: confidence={agent.confidence_level:.2f}, '
            'fear={agent.fear_of_rejection:.2f}")',
        ]
        return "\n".join(code)


class SocialGenerator:
    """Generates code for social dynamics scenarios"""

    @staticmethod
    def generate_pseudo(ir) -> str:
        return "\n".join([
            "// SOCIAL DYNAMICS MODEL",
            "// Group behavior and social influence",
            "",
            "Group Members: [Member1, Member2, Member3, ...]",
            "",
            "FOR EACH member:",
            "  - opinion: initial_value",
            "  - conformity_tendency: 0.6",
            "  - influence_on_others: 0.5",
            "",
            "Social Influence Loop:",
            "  FOR iteration in 1..N:",
            "    FOR EACH member:",
            "      peer_opinions = GET opinions from connected peers",
            "      average_peer_opinion = MEAN(peer_opinions)",
            "      ",
            "      // Update opinion based on social influence",
            "      member.opinion = member.opinion × (1 - conformity_tendency) +",
            "                       average_peer_opinion × conformity_tendency",
            "",
            "  RETURN final_opinions",
        ])

    @staticmethod
    def generate_python(ir) -> str:
        code = [
            '"""',
            f"Social Dynamics Model: {ir.raw_text}",
            '"""',
            "import random",
            "from typing import List",
            "",
            "",
            "class SocialAgent:",
            '    """Agent in a social network"""',
            "    ",
            "    def __init__(self, name: str, initial_opinion: float = 0.5):",
            "        self.name = name",
            "        self.opinion = initial_opinion",
            "        self.conformity_tendency = random.uniform(0.3, 0.8)",
            "        self.influence_strength = random.uniform(0.3, 0.7)",
            "    ",
            "    def update_opinion(self, peer_opinions: List[float]):",
            '        """Update opinion based on social influence"""',
            "        if not peer_opinions:",
            "            return",
            "        avg_peer_opinion = sum(peer_opinions) / len(peer_opinions)",
            "        self.opinion = (self.opinion * (1 - self.conformity_tendency) +",
            "                        avg_peer_opinion * self.conformity_tendency)",
            "",
            "",
            "class SocialNetwork:",
            '    """Simulates social dynamics"""',
            "    ",
            "    def __init__(self, num_agents: int = 5):",
            "        self.agents = [",
            "            SocialAgent(f'Agent{i}', random.uniform(0.2, 0.8))",
            "            for i in range(num_agents)",
            "        ]",
            "    ",
            "    def simulate(self, iterations: int = 10):",
            '        """Run social influence simulation"""',
            "        print(f\"Initial opinions: {[f'{a.opinion:.2f}' for a in self.agents]}\")",
            "        ",
            "        for _ in range(iterations):",
            "            for agent in self.agents:",
            "                peer_opinions = [o.opinion for o in self.agents if o is not agent]",
            "                agent.update_opinion(peer_opinions)",
            "        ",
            "        print(f\"Final opinions:   {[f'{a.opinion:.2f}' for a in self.agents]}\")",
            "        ",
            "        # FIX: original variance compared each agent to agents[0] (wrong mean).",
            "        # Correct population variance uses the true mean.",
            "        mean_opinion = sum(a.opinion for a in self.agents) / len(self.agents)",
            "        variance = sum((a.opinion - mean_opinion) ** 2 for a in self.agents) / len(self.agents)",
            "        if variance < 0.01:",
            "            print('→ Consensus reached!')",
            "        else:",
            "            print(f'→ Opinions still diverse (variance={variance:.4f})')",
            "",
            "",
            "# Run simulation",
            'if __name__ == "__main__":',
            "    network = SocialNetwork(num_agents=6)",
            "    network.simulate(iterations=15)",
        ]
        return "\n".join(code)


if __name__ == "__main__":
    from ir import IntermediateRepresentation

    ir = IntermediateRepresentation(
        raw_text="A guy decides whether to approach someone.",
        category="psychology",
    )

    gen = PsychologyGenerator()
    print(gen.generate_pseudo(ir))
    print("\n" + "=" * 60 + "\n")
    print(gen.generate_python(ir))
