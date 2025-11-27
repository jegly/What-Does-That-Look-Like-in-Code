# WDLIC Quick Start Guide

Get up and running with "What Does That Look Like in Code" in 5 minutes!


---

## Option 1: Full Installation

### Step 1: Install Dependencies

```bash
cd wdlic
bash setup.sh
```

This will:
- Check Python version (3.8+ required)
- Install all required packages
- Download spaCy language model
- Set up the project

### Step 2: Run Your First Example

```bash
python main.py "A person decides whether to take a risk"
```

You'll see:
1. **Category**: Auto-detected domain (e.g., Psychology)
2. **Confidence**: How certain the system is
3. **Assumptions**: What the model assumes
4. **IR Preview**: Structured representation
5. **Pseudo-Code**: Conceptual logic
6. **Python Code**: Fully executable code!

---

## Quick Examples

### Psychology

```bash
python main.py "Someone overcomes fear of public speaking"
```

### Physics

```bash
python main.py "A ball is thrown at 20 m/s at 45 degrees"
```

### Mathematics

```bash
python main.py "Find the derivative of x squared"
```

### Social Dynamics

```bash
python main.py "Group opinions converge through discussion"
```

---

## Command Options

### Get Only Python Code

```bash
python main.py "Your scenario" --format python
```

### Get Only Pseudo-Code

```bash
python main.py "Your scenario" --format pseudo
```

### Force a Category

```bash
python main.py "Optimize the process" --category optimization
```

### Save to File

```bash
python main.py "Your scenario" --format python > my_code.py
python my_code.py
```

---

## What Can WDLIC Do?

### ✅ Supported Domains

- **Psychology**: Mental states, decision-making, emotions
- **Physics**: Motion, forces, energy, trajectories
- **Mathematics**: Calculus, algebra, probability, optimization
- **Social Dynamics**: Group behavior, influence, consensus
- **Game Theory**: Strategy, competition, cooperation
- **Business**: Profit, costs, market dynamics
- **Rules/Logic**: Conditionals, constraints, requirements

### 🎯 What Makes WDLIC Different

1. **No Coding Required**: Just describe your scenario in plain English
2. **Multiple Outputs**: Get both conceptual (pseudo-code) and executable (Python) versions
3. **Cross-Domain**: Works for psychology, physics, math, social science, and more
4. **Educational**: Learn how concepts translate to code
5. **Extensible**: Add your own domains and generators

---

## Example Workflow

### 1. Describe Your Scenario

```
"A person gains confidence after repeated successes"
```

### 2. WDLIC Analyzes It

- Detects psychology domain
- Identifies key variables (confidence, success rate)
- Maps to psychological models

### 3. Get Pseudo-Code

```
Actor: Person
  - confidence_level: 0.7
  - success_count: 0

Decision Logic:
  IF attempt succeeds:
    confidence_level += 0.1
    success_count += 1
  ELSE:
    confidence_level -= 0.05
```

### 4. Get Python Code

```python
class PsychologicalAgent:
    def __init__(self, name):
        self.name = name
        self.confidence = 0.7
    
    def attempt_task(self):
        success = random.random() < self.confidence
        if success:
            self.confidence = min(1.0, self.confidence + 0.1)
        return success
```

### 5. Run It!

```bash
python my_simulation.py
```

---

## Tips for Best Results

### 1. Be Specific

❌ "Something moves"
✅ "A ball is thrown at 20 m/s"

### 2. Use Domain Keywords

- Psychology: "confidence", "fear", "desire", "motivation"
- Physics: "velocity", "force", "energy", "mass"
- Math: "optimize", "calculate", "derive"

### 3. Describe Dynamics

❌ "A person"
✅ "A person gains confidence over time"

### 4. Include Numbers When Relevant

❌ "Throw a ball"
✅ "Throw a ball at 20 m/s at 45 degrees"

---

## Next Steps

### Learn More

- Read [README.md](README.md) for complete documentation
- Browse [EXAMPLES.md](EXAMPLES.md) for more scenarios
- Check [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for architecture

### Customize

1. Add your own categories in `router.py`
2. Create custom generators in `codegen/`
3. Extend the IR schema in `ir.py`

### Contribute

Found a bug? Have an idea? WDLIC is designed to be extensible!

---

## Troubleshooting

### "spaCy model not found"

```bash
python -m spacy download en_core_web_sm
```

### "Module not found"

```bash
pip install --break-system-packages -r requirements.txt
```

### "Demo not working"

The standalone demo (`demo.py`) requires no external dependencies and always works!

---

## Common Use Cases

### 1. Learning

"I want to understand how psychological decision-making works in code"
→ Run WDLIC on psychology scenarios

### 2. Prototyping

"I need a quick simulation for my research"
→ Generate code, modify parameters, iterate

### 3. Teaching

"I want to show students how concepts translate to code"
→ Use WDLIC examples in class

### 4. Exploration

"I'm curious how X would look as code"
→ Just ask WDLIC!

---

## Your First 5 Minutes

```bash
# 1. Run the demo
python demo.py

# 2. Try your own example
python main.py "A person decides to speak up in a meeting"

# 3. Get just the code
python main.py "A ball falls from 50 meters" --format python

# 4. Save and run it
python main.py "Calculate compound interest" --format python > calc.py
python calc.py

# 5. Experiment!
python main.py "Your creative scenario here"
```

---

______/\\\\\\\\\\\__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\\__/\\\______________/\\\________/\\\_        
 _____\/////\\\///__\/\\\///////////____/\\\//////////__\/\\\_____________\///\\\____/\\\/__       
  _________\/\\\_____\/\\\______________/\\\_____________\/\\\_______________\///\\\/\\\/____      
   _________\/\\\_____\/\\\\\\\\\\\_____\/\\\____/\\\\\\\_\/\\\_________________\///\\\/______     
    _________\/\\\_____\/\\\///////______\/\\\___\/////\\\_\/\\\___________________\/\\\_______    
     _________\/\\\_____\/\\\_____________\/\\\_______\/\\\_\/\\\___________________\/\\\_______   
      __/\\\___\/\\\_____\/\\\_____________\/\\\_______\/\\\_\/\\\___________________\/\\\_______  
       _\//\\\\\\\\\______\/\\\\\\\\\\\\\\\_\//\\\\\\\\\\\\/__\/\\\\\\\\\\\\\\\_______\/\\\_______ 
        __\/////////_______\///////////////___\////////////____\///////////////________\///________

