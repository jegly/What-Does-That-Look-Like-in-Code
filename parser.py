"""
parser.py - NLP Parser for extracting features from natural language input
"""
import spacy
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

# Keyword maps for heuristic enrichment
BELIEF_KEYWORDS = {"belief", "faith", "religion", "indoctrination", "upbringing", "schooling"}
IDENTITY_KEYWORDS = {"self", "identity", "perception", "fragmented", "stable", "awareness"}
MORALITY_KEYWORDS = {"justice", "fairness", "forgiveness", "dilemma", "moral", "immoral", "law"}
PHILOSOPHY_KEYWORDS = {"yin", "yang", "wu", "wei", "dao", "paradox", "harmony", "goddess", "cosmic"}
PSYCHOLOGY_KEYWORDS = {"fear", "anxiety", "impulse", "coping", "resilience", "stress", "support", "confidence", "desire", "impress", "validation", "status"}
SOCIAL_KEYWORDS = {"empathy", "trust", "group", "hierarchy", "validation", "status", "conformity", "social", "proof"}
PHYSICS_KEYWORDS = {"spin", "gravity", "force", "mass", "velocity", "acceleration", "momentum", "energy", "field", "rotation", "torque"}
MATH_KEYWORDS = {"proof", "optimize", "minimize", "probability", "equation", "function", "derivative", "integral", "sum"}

@dataclass
class ParsedFeatures:
    """Structured representation of parsed text features"""
    actors: List[str] = field(default_factory=list)
    objects: List[str] = field(default_factory=list)
    actions: List[str] = field(default_factory=list)
    relations: List[str] = field(default_factory=list)
    intents: List[str] = field(default_factory=list)
    conditions: List[str] = field(default_factory=list)
    environment: Dict[str, Any] = field(default_factory=dict)
    uncertainty: float = 0.0
    
    # Extended enrichers
    beliefs: List[str] = field(default_factory=list)
    identity_signals: List[str] = field(default_factory=list)
    morality_signals: List[str] = field(default_factory=list)
    philosophy_signals: List[str] = field(default_factory=list)
    psychology_signals: List[str] = field(default_factory=list)
    social_signals: List[str] = field(default_factory=list)
    physics_signals: List[str] = field(default_factory=list)
    math_signals: List[str] = field(default_factory=list)
    
    raw_text: str = ""


class TextParser:
    """Parser using spaCy for NLP analysis"""
    
    def __init__(self, model_name: str = "en_core_web_sm"):
        """Initialize parser with spaCy model"""
        try:
            self.nlp = spacy.load(model_name)
        except OSError:
            print(f"spaCy model '{model_name}' not found. Downloading...")
            import subprocess
            subprocess.run(["python", "-m", "spacy", "download", model_name])
            self.nlp = spacy.load(model_name)
    
    def parse(self, text: str) -> ParsedFeatures:
        """Parse text and extract structured features"""
        doc = self.nlp(text)
        
        # Basic extraction
        actors = [ent.text for ent in doc.ents if ent.label_ in ("PERSON", "ORG")]
        objects = [chunk.text for chunk in doc.noun_chunks]
        actions = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        relations = [f"{tok.head.text} → {tok.text}" for tok in doc if tok.dep_ in ("nsubj", "dobj")]
        conditions = [tok.text for tok in doc if tok.dep_ == "advcl"]
        intents = [tok.text for tok in doc if tok.text.lower() in ("want", "need", "should", "must")]
        
        # Heuristic enrichers
        text_lower = text.lower()
        beliefs = [tok.text for tok in doc if tok.text.lower() in BELIEF_KEYWORDS]
        identity_signals = [tok.text for tok in doc if tok.text.lower() in IDENTITY_KEYWORDS]
        morality_signals = [tok.text for tok in doc if tok.text.lower() in MORALITY_KEYWORDS]
        philosophy_signals = [tok.text for tok in doc if tok.text.lower() in PHILOSOPHY_KEYWORDS]
        psychology_signals = [tok.text for tok in doc if tok.text.lower() in PSYCHOLOGY_KEYWORDS]
        social_signals = [tok.text for tok in doc if tok.text.lower() in SOCIAL_KEYWORDS]
        physics_signals = [tok.text for tok in doc if tok.text.lower() in PHYSICS_KEYWORDS]
        math_signals = [tok.text for tok in doc if tok.text.lower() in MATH_KEYWORDS]
        
        # Simple uncertainty heuristic: more modal verbs → higher uncertainty
        modal_count = sum(1 for tok in doc if tok.tag_ in ("MD", "VB"))
        uncertainty = modal_count / max(len(doc), 1)
        
        return ParsedFeatures(
            actors=actors,
            objects=objects,
            actions=actions,
            relations=relations,
            intents=intents,
            conditions=conditions,
            environment={},
            uncertainty=uncertainty,
            beliefs=beliefs,
            identity_signals=identity_signals,
            morality_signals=morality_signals,
            philosophy_signals=philosophy_signals,
            psychology_signals=psychology_signals,
            social_signals=social_signals,
            physics_signals=physics_signals,
            math_signals=math_signals,
            raw_text=text
        )


if __name__ == "__main__":
    # Test the parser
    parser = TextParser()
    sample = "The goddess Themis weighs justice and forgiveness, while fear and anxiety test identity."
    parsed = parser.parse(sample)
    print(parsed)
