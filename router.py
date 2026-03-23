# router.py - Category Router for classifying input into domains
from dataclasses import dataclass
from typing import List

# FIX: import from text_parser, not parser (parser.py shadows stdlib `parser` module)
from text_parser import ParsedFeatures


@dataclass
class CategoryScore:
    """Represents a category with confidence score"""
    name: str
    confidence: float
    signals: List[str]


class CategoryRouter:
    """Routes parsed features to appropriate categories"""

    CATEGORIES = {
        "psychology": {
            "keywords": [
                "fear", "anxiety", "confidence", "desire", "impress", "validation",
                "status", "self-esteem", "motivation", "emotion", "feeling",
                "stress", "trauma", "coping", "resilience", "memory", "attention",
                "perception", "behavior", "thought", "belief", "impulse", "support",
            ],
            "weight": 1.0,
        },
        "social": {
            "keywords": [
                "group", "social", "conformity", "hierarchy", "empathy", "trust",
                "relationship", "interaction", "community", "peer", "network",
                "society", "culture", "friendship", "cooperation", "solidarity",
            ],
            "weight": 1.0,
        },
        "physics": {
            "keywords": [
                "force", "mass", "velocity", "acceleration", "gravity", "energy",
                "momentum", "rotation", "spin", "field", "torque",
                "wave", "quantum", "relativity", "particle", "thermodynamics",
                "friction", "pressure", "density", "current", "voltage",
            ],
            "weight": 1.0,
        },
        "mathematics": {
            "keywords": [
                "equation", "function", "derivative", "integral", "optimize",
                "minimize", "probability", "proof", "sum", "calculate",
                "algebra", "geometry", "statistics", "logic", "theorem",
                "matrix", "vector", "graph", "number", "analysis",
            ],
            "weight": 1.0,
        },
        "rules": {
            "keywords": [
                "rule", "if", "then", "when", "condition", "constraint",
                "requirement", "must", "should", "forbidden", "policy",
                "guideline", "standard", "protocol", "procedure",
            ],
            "weight": 0.8,
        },
        "optimization": {
            "keywords": [
                "optimize", "maximize", "minimize", "best", "efficient",
                "tradeoff", "constraint", "goal", "objective", "improve",
                "refine", "enhance", "streamline", "performance",
            ],
            "weight": 0.9,
        },
        "game": {
            "keywords": [
                "game", "play", "win", "lose", "score", "player", "opponent",
                "strategy", "move", "turn", "competition", "match", "tournament",
                "challenge", "quest", "puzzle", "level",
            ],
            "weight": 0.8,
        },
        "business": {
            "keywords": [
                "profit", "revenue", "cost", "market", "customer", "product",
                "strategy", "competition", "pricing", "management", "finance",
                "investment", "sales", "growth", "startup", "entrepreneurship",
            ],
            "weight": 0.7,
        },
        "ui": {
            "keywords": [
                "button", "click", "display", "show", "interface", "screen",
                "user", "input", "output", "menu", "window", "dialog",
                "icon", "layout", "navigation", "widget",
            ],
            "weight": 0.7,
        },
        "philosophy": {
            "keywords": [
                "dao", "yin", "yang", "harmony", "paradox", "wu", "wei",
                "cosmic", "existence", "meaning", "ethics", "morality",
                "logic", "reason", "metaphysics", "ontology", "epistemology",
            ],
            "weight": 0.9,
        },
        "biology": {
            "keywords": [
                "cell", "gene", "dna", "rna", "protein", "enzyme", "mutation",
                "evolution", "species", "ecosystem", "organism", "biology",
                "genetics", "microbe", "bacteria", "virus",
            ],
            "weight": 0.9,
        },
        "technology": {
            "keywords": [
                "algorithm", "data", "network", "cloud", "ai", "machine",
                "learning", "automation", "robotics", "cybersecurity",
                "software", "hardware", "programming", "innovation", "digital",
            ],
            "weight": 0.9,
        },
        "art": {
            "keywords": [
                "painting", "sculpture", "music", "dance", "literature",
                "poetry", "theater", "cinema", "design", "aesthetics",
                "drawing", "creative", "expression", "artwork",
            ],
            "weight": 0.8,
        },
    }

    def route(self, features: ParsedFeatures) -> List[CategoryScore]:
        """Classify parsed features into categories with confidence scores"""
        scores = []

        # Combine all text signals for matching
        all_text = " ".join([
            features.raw_text.lower(),
            " ".join(features.actions),
            " ".join(features.psychology_signals),
            " ".join(features.social_signals),
            " ".join(features.physics_signals),
            " ".join(features.math_signals),
            " ".join(features.philosophy_signals),
        ]).lower()

        for category, config in self.CATEGORIES.items():
            matches = [kw for kw in config["keywords"] if kw in all_text]

            if matches:
                base_confidence = len(matches) / len(config["keywords"])
                confidence = min(base_confidence * config["weight"] * 2, 1.0)

                # Boost from specialized parser signals
                boosts = {
                    "psychology": features.psychology_signals,
                    "social":     features.social_signals,
                    "physics":    features.physics_signals,
                    "mathematics": features.math_signals,
                    "philosophy": features.philosophy_signals,
                }
                if category in boosts and boosts[category]:
                    confidence = min(confidence + 0.2, 1.0)

                scores.append(CategoryScore(
                    name=category,
                    confidence=confidence,
                    signals=matches,
                ))

        scores.sort(key=lambda x: x.confidence, reverse=True)

        if not scores:
            scores.append(CategoryScore(name="generic", confidence=0.5, signals=[]))

        return scores

    def get_primary_category(self, features: ParsedFeatures) -> CategoryScore:
        """Get the single highest-confidence category"""
        return self.route(features)[0]


if __name__ == "__main__":
    from text_parser import TextParser

    parser = TextParser()
    router = CategoryRouter()

    tests = [
        "A guy flexes his muscles to impress girls at the gym.",
        "Calculate the trajectory of a ball thrown at 20 m/s at 45 degrees.",
        "The goddess weighs justice in perfect harmony.",
        "DNA mutations drive evolution across species.",
        "AI algorithms optimize cloud network performance.",
    ]

    for test in tests:
        features = parser.parse(test)
        category = router.get_primary_category(features)
        print(f"\nInput: {test}")
        print(f"Category: {category.name} (confidence: {category.confidence:.2f})")
        print(f"Signals: {category.signals}")
