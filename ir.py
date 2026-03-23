"""
ir.py - Intermediate Representation (IR) Builder
"""
import re
import json
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class Entity(BaseModel):
    """Represents an entity in the scenario"""
    name: str
    type: str  # person, object, concept, force, etc.
    properties: Dict[str, Any] = Field(default_factory=dict)


class Action(BaseModel):
    """Represents an action or event"""
    verb: str
    actor: Optional[str] = None
    target: Optional[str] = None
    modifiers: List[str] = Field(default_factory=list)


class Relation(BaseModel):
    """Represents a relationship between entities"""
    source: str
    relation_type: str
    target: str
    strength: float = 1.0


class State(BaseModel):
    """Represents a state or condition"""
    variable: str
    value: Any
    unit: Optional[str] = None


class Goal(BaseModel):
    """Represents an objective or goal"""
    description: str
    target: Optional[str] = None
    success_criteria: Optional[str] = None


class Rule(BaseModel):
    """Represents a rule or constraint"""
    condition: str
    action: str
    priority: int = 1


class IntermediateRepresentation(BaseModel):
    """
    Language-agnostic intermediate representation of a scenario
    """
    # Core elements
    entities: List[Entity] = Field(default_factory=list)
    actions: List[Action] = Field(default_factory=list)
    relations: List[Relation] = Field(default_factory=list)
    states: List[State] = Field(default_factory=list)
    goals: List[Goal] = Field(default_factory=list)
    rules: List[Rule] = Field(default_factory=list)

    # Context
    environment: Dict[str, Any] = Field(default_factory=dict)
    assumptions: List[str] = Field(default_factory=list)
    uncertainty: float = 0.0

    # Metadata
    category: str = "generic"
    confidence: float = 0.5
    raw_text: str = ""
    # FIX: detail level stored so generators can adapt verbosity
    detail: str = "med"

    # Domain-specific enrichments
    psychology_vars: Dict[str, float] = Field(default_factory=dict)
    social_vars: Dict[str, float] = Field(default_factory=dict)
    physics_vars: Dict[str, float] = Field(default_factory=dict)
    math_vars: Dict[str, Any] = Field(default_factory=dict)
    philosophy_vars: Dict[str, float] = Field(default_factory=dict)
    optimization_vars: Dict[str, Any] = Field(default_factory=dict)
    game_vars: Dict[str, Any] = Field(default_factory=dict)
    business_vars: Dict[str, Any] = Field(default_factory=dict)

    def to_json(self) -> str:
        """Convert IR to JSON string"""
        return self.model_dump_json(indent=2)

    def to_compact_json(self) -> str:
        """Convert IR to compact JSON, omitting empty collections"""
        data = self.model_dump()
        compact = {
            k: v for k, v in data.items()
            if v or v == 0.0  # keep numeric zeros
            if not isinstance(v, (list, dict)) or len(v) > 0
        }
        return json.dumps(compact, indent=2)


class IRBuilder:
    """Builds IR from parsed features"""

    def build(self, features, category_score,
              detail: str = "med") -> IntermediateRepresentation:
        """Construct IR from parsed features and category"""
        ir = IntermediateRepresentation(
            raw_text=features.raw_text,
            category=category_score.name,
            confidence=category_score.confidence,
            uncertainty=features.uncertainty,
            detail=detail,
        )

        # Extract entities
        for actor in features.actors:
            ir.entities.append(Entity(name=actor, type="person", properties={}))

        # Extract actions
        for action_verb in features.actions:
            ir.actions.append(Action(verb=action_verb, modifiers=[]))

        # ── Per-category assumptions & domain vars ────────────────────────────
        cat = category_score.name

        if cat == "psychology":
            ir.assumptions.extend([
                "Actors have internal mental states",
                "Behavior is driven by psychological motivations",
                "Emotions and cognitions influence actions",
            ])
            text_lower = features.raw_text.lower()
            if "confidence" in text_lower:
                ir.psychology_vars["confidence_level"] = 0.7
            if "desire" in text_lower or "want" in text_lower:
                ir.psychology_vars["desire_strength"] = 0.8
            if "fear" in text_lower or "anxiety" in text_lower:
                ir.psychology_vars["anxiety_level"] = 0.6

        elif cat == "social":
            ir.assumptions.extend([
                "Social interactions follow group dynamics",
                "Peer influence affects individual behavior",
                "Social proof can create cascading effects",
            ])
            ir.social_vars["group_influence"] = 0.7
            ir.social_vars["social_proof_sensitivity"] = 0.6

        elif cat == "physics":
            ir.assumptions.extend([
                "Physical laws govern motion and forces",
                "Conservation principles apply",
                "Continuous or discrete time evolution",
            ])
            # FIX: store extracted values as float, not raw string list
            numbers = re.findall(r"\d+\.?\d*", features.raw_text)
            if numbers:
                ir.physics_vars["extracted_values"] = [float(n) for n in numbers]

        elif cat == "mathematics":
            ir.assumptions.extend([
                "Mathematical operations are precise",
                "Functions are well-defined",
                "Solutions exist within constraints",
            ])

        elif cat == "philosophy":
            ir.assumptions.extend([
                "Abstract concepts have logical structure",
                "Harmony and balance are measurable",
                "Paradoxes may be intentional",
            ])
            if features.philosophy_signals:
                ir.philosophy_vars["harmony_index"] = 0.8
                ir.philosophy_vars["paradox_tolerance"] = 0.7

        # FIX: these categories had no handling at all — program fell through to
        # an empty IR with no assumptions, silently producing useless output.
        elif cat == "optimization":
            ir.assumptions.extend([
                "An objective function can be defined",
                "Constraints bound the feasible region",
                "A global or local optimum exists",
            ])
            ir.optimization_vars["objective"] = "maximize"
            ir.optimization_vars["constraint_count"] = 0

        elif cat == "game":
            ir.assumptions.extend([
                "Players act rationally to maximise their payoff",
                "Game state transitions are well-defined",
                "Win/loss conditions are deterministic",
            ])
            ir.game_vars["player_count"] = 2
            ir.game_vars["turn_based"] = True

        elif cat == "business":
            ir.assumptions.extend([
                "Profit = revenue − costs",
                "Market forces influence pricing",
                "Strategy is constrained by resources",
            ])
            ir.business_vars["revenue"] = 0.0
            ir.business_vars["cost"] = 0.0

        elif cat == "ui":
            ir.assumptions.extend([
                "User interactions trigger state changes",
                "UI components react to events",
                "Accessibility and responsiveness matter",
            ])

        elif cat == "rules":
            ir.assumptions.extend([
                "Rules are evaluated in priority order",
                "Conditions are boolean expressions",
                "Actions execute when conditions are met",
            ])

        elif cat in ("technology", "biology", "art"):
            ir.assumptions.extend([
                f"Domain-specific knowledge governs {cat} reasoning",
                "Patterns can be abstracted into code structures",
            ])

        else:  # generic fallback
            ir.assumptions.extend([
                "Inputs map to outputs via a defined process",
                "State transitions are deterministic unless specified",
            ])

        return ir


if __name__ == "__main__":
    from text_parser import TextParser
    from router import CategoryRouter

    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()

    text = "A guy flexes his muscles to impress girls."
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)

    print(ir.to_compact_json())
