"""
ir.py - Intermediate Representation (IR) Builder
"""
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
import json


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
    
    # Domain-specific enrichments
    psychology_vars: Dict[str, float] = Field(default_factory=dict)
    social_vars: Dict[str, float] = Field(default_factory=dict)
    physics_vars: Dict[str, float] = Field(default_factory=dict)
    math_vars: Dict[str, Any] = Field(default_factory=dict)
    philosophy_vars: Dict[str, float] = Field(default_factory=dict)
    
    def to_json(self) -> str:
        """Convert IR to JSON string"""
        return self.model_dump_json(indent=2)
    
    def to_compact_json(self) -> str:
        """Convert IR to compact JSON"""
        data = self.model_dump()
        # Remove empty lists/dicts for brevity
        compact = {k: v for k, v in data.items() 
                   if v and (not isinstance(v, (list, dict)) or len(v) > 0)}
        return json.dumps(compact, indent=2)


class IRBuilder:
    """Builds IR from parsed features"""
    
    def build(self, features, category_score) -> IntermediateRepresentation:
        """Construct IR from parsed features and category"""
        ir = IntermediateRepresentation(
            raw_text=features.raw_text,
            category=category_score.name,
            confidence=category_score.confidence,
            uncertainty=features.uncertainty
        )
        
        # Extract entities
        for actor in features.actors:
            ir.entities.append(Entity(
                name=actor,
                type="person",
                properties={}
            ))
        
        # Extract actions
        for action_verb in features.actions:
            ir.actions.append(Action(
                verb=action_verb,
                modifiers=[]
            ))
        
        # Add assumptions based on category
        if category_score.name == "psychology":
            ir.assumptions.extend([
                "Actors have internal mental states",
                "Behavior is driven by psychological motivations",
                "Emotions and cognitions influence actions"
            ])
            # Add psychology variables
            if "confidence" in features.raw_text.lower():
                ir.psychology_vars["confidence_level"] = 0.7
            if "desire" in features.raw_text.lower() or "want" in features.raw_text.lower():
                ir.psychology_vars["desire_strength"] = 0.8
            if "fear" in features.raw_text.lower() or "anxiety" in features.raw_text.lower():
                ir.psychology_vars["anxiety_level"] = 0.6
        
        elif category_score.name == "social":
            ir.assumptions.extend([
                "Social interactions follow group dynamics",
                "Peer influence affects individual behavior",
                "Social proof can create cascading effects"
            ])
            ir.social_vars["group_influence"] = 0.7
            ir.social_vars["social_proof_sensitivity"] = 0.6
        
        elif category_score.name == "physics":
            ir.assumptions.extend([
                "Physical laws govern motion and forces",
                "Conservation principles apply",
                "Continuous or discrete time evolution"
            ])
            # Extract any numerical values
            import re
            numbers = re.findall(r'\d+\.?\d*', features.raw_text)
            if numbers:
                ir.physics_vars["extracted_values"] = [float(n) for n in numbers]
        
        elif category_score.name == "mathematics":
            ir.assumptions.extend([
                "Mathematical operations are precise",
                "Functions are well-defined",
                "Solutions exist within constraints"
            ])
        
        elif category_score.name == "philosophy":
            ir.assumptions.extend([
                "Abstract concepts have logical structure",
                "Harmony and balance are measurable",
                "Paradoxes may be intentional"
            ])
            if features.philosophy_signals:
                ir.philosophy_vars["harmony_index"] = 0.8
                ir.philosophy_vars["paradox_tolerance"] = 0.7
        
        return ir


if __name__ == "__main__":
    from parser import TextParser
    from router import CategoryRouter
    
    parser = TextParser()
    router = CategoryRouter()
    builder = IRBuilder()
    
    text = "A guy flexes his muscles to impress girls."
    features = parser.parse(text)
    category = router.get_primary_category(features)
    ir = builder.build(features, category)
    
    print(ir.to_compact_json())
