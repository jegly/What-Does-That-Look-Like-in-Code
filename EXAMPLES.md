# WDLIC Examples

Comprehensive examples demonstrating WDLIC's capabilities across different domains.

## Psychology Examples

### Example 1: Decision Making Under Uncertainty

**Input:**
```
A person decides whether to speak up in a meeting despite fear of judgment
```

**What WDLIC generates:**
- Psychological variables: confidence, fear_of_judgment, desire_to_contribute
- Decision model: motivation vs. inhibition threshold
- Outcome updates: confidence adjustment based on success/failure

**Run it:**
```bash
python main.py "A person decides whether to speak up in a meeting despite fear of judgment"
```

### Example 2: Social Validation

**Input:**
```
Someone gains confidence after receiving positive feedback from peers
```

**Generated code includes:**
- Confidence tracking over time
- Feedback processing mechanism
- Self-esteem updates based on validation

---

## Physics Examples

### Example 1: Projectile Motion

**Input:**
```
A ball is thrown at 25 m/s at a 60 degree angle
```

**What WDLIC generates:**
- Kinematic equations for projectile motion
- Time-stepped simulation
- Calculation of max height, range, and flight time
- Energy conservation checks

**Run it:**
```bash
python main.py "A ball is thrown at 25 m/s at a 60 degree angle" --category physics
```

### Example 2: Free Fall

**Input:**
```
An object falls from 100 meters under gravity
```

**Generated code:**
- Velocity and position updates
- Acceleration due to gravity (9.81 m/s²)
- Impact velocity calculation

---

## Mathematics Examples

### Example 1: Function Optimization

**Input:**
```
Find the minimum of f(x) = x² - 4x + 3
```

**What WDLIC generates:**
- Symbolic differentiation using SymPy
- Critical point calculation
- Second derivative test for classification
- Numerical evaluation

**Run it:**
```bash
python main.py "Find the minimum of a quadratic function" --category math
```

### Example 2: Probability

**Input:**
```
Calculate the probability of getting exactly 6 heads in 10 coin flips
```

**Generated code:**
- Binomial probability formula
- Combination calculation
- Monte Carlo simulation option

---

## Social Dynamics Examples

### Example 1: Opinion Convergence

**Input:**
```
Five people with different opinions discuss and influence each other
```

**What WDLIC generates:**
- Agent-based social network model
- Conformity and peer influence parameters
- Opinion update dynamics
- Consensus detection

**Run it:**
```bash
python main.py "Group members influence each other's opinions" --category social
```

### Example 2: Information Spread

**Input:**
```
A rumor spreads through a social network with varying trust levels
```

**Generated code:**
- Network propagation model
- Trust-weighted influence
- Cascade detection

---

## Mixed Domain Examples

### Example 1: Psychology + Social

**Input:**
```
A shy person gradually builds confidence through repeated social interactions
```

**What WDLIC generates:**
- Combines psychological state tracking
- Social feedback loops
- Confidence evolution over multiple interactions

### Example 2: Physics + Optimization

**Input:**
```
Find the optimal angle to maximize the range of a projectile
```

**What WDLIC generates:**
- Physics simulation for different angles
- Optimization loop to find maximum
- Trade-off analysis

---

## Advanced Examples

### Example 1: Multi-Agent Interaction

**Input:**
```
Three agents compete for resources while trying to cooperate
```

**Generated features:**
- Game-theoretic decision making
- Cooperation vs. competition dynamics
- Nash equilibrium approximation

### Example 2: Time-Series Evolution

**Input:**
```
A population's average belief changes over time due to media influence
```

**Generated features:**
- Temporal dynamics
- External influence modeling
- Equilibrium analysis

---

## Business/Optimization Examples

### Example 1: Profit Maximization

**Input:**
```
Maximize profit given production costs and market demand constraints
```

**What WDLIC generates:**
- Objective function definition
- Constraint modeling
- Optimization using calculus or numerical methods

### Example 2: Resource Allocation

**Input:**
```
Allocate limited budget across multiple projects to maximize ROI
```

**Generated code:**
- Portfolio optimization
- Risk-return tradeoff
- Constraint satisfaction

---

## Using Generated Code

All generated Python code is executable. Here's how to use it:

### 1. Save and Run Directly

```bash
# Generate and save
python main.py "Your scenario" --format python > my_simulation.py

# Run it
python my_simulation.py
```

### 2. Modify and Experiment

```python
# The generated code is well-structured and documented
# You can easily modify parameters:

if __name__ == "__main__":
    # Original
    agent = PsychologicalAgent("Person")
    
    # Your modification
    agent = PsychologicalAgent("Alice")
    agent.confidence = 0.9  # Start with high confidence
    agent.anxiety = 0.2     # Lower anxiety
```

### 3. Integrate into Projects

```python
# Import generated classes
from my_simulation import PhysicsSimulator

# Use in your code
sim = PhysicsSimulator()
result = sim.projectile_trajectory(v0=30, angle_deg=45)
```

---

## Format Options

### Get Only Pseudo-Code

```bash
python main.py "Your scenario" --format pseudo
```

Shows conceptual logic without implementation details.

### Get Only Python Code

```bash
python main.py "Your scenario" --format python
```

Shows only executable code, no IR or pseudo-code.

### Get Everything (Default)

```bash
python main.py "Your scenario" --format all
```

Shows category, assumptions, IR preview, pseudo-code, and Python code.

---

## Category Override

Force a specific interpretation:

```bash
# Force psychology interpretation
python main.py "Calculate optimal strategy" --category psychology

# Force physics interpretation  
python main.py "Person moves through space" --category physics

# Force math interpretation
python main.py "Find the solution" --category math
```

---

## Tips for Best Results

1. **Be Specific**: Include numbers, relationships, and context
   - Good: "A ball thrown at 20 m/s at 45 degrees"
   - Less good: "Something moves"

2. **Use Domain Keywords**: Help the router identify category
   - Psychology: "confidence", "fear", "desire", "motivation"
   - Physics: "velocity", "force", "energy", "acceleration"
   - Math: "optimize", "calculate", "derive", "prove"

3. **Describe Dynamics**: Mention how things change
   - "Person gains confidence over time"
   - "Velocity increases due to acceleration"
   - "Opinions converge through discussion"

4. **Set Context**: Explain the scenario's purpose
   - "In a job interview, someone decides whether to negotiate"
   - "To win the game, a player must optimize their strategy"

---

## Combining with Other Tools

### With Data Science

```python
import pandas as pd
from my_simulation import SocialNetwork

# Run multiple simulations
results = []
for trial in range(100):
    net = SocialNetwork(n_agents=10)
    net.simulate(iterations=20)
    results.append(net.get_final_variance())

df = pd.DataFrame(results)
df.describe()
```

### With Visualization

```python
import matplotlib.pyplot as plt
from my_simulation import PhysicsSimulator

sim = PhysicsSimulator()
positions, velocities, time = sim.projectile_trajectory(v0=25, angle_deg=45)

plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Trajectory")
plt.show()
```

---

## Educational Use

WDLIC is great for:

1. **Teaching computational thinking**
   - Shows how natural language maps to logic
   - Demonstrates domain-specific modeling

2. **Learning by experimentation**
   - Modify generated code to see effects
   - Compare different scenarios

3. **Rapid prototyping**
   - Quickly test ideas in code
   - Iterate on models without starting from scratch

---

## More Examples to Try

```bash
# Psychology
python main.py "Overcoming procrastination through small wins"
python main.py "Building trust in a new relationship"
python main.py "Managing anxiety before a presentation"

# Physics
python main.py "A pendulum swings with decreasing amplitude"
python main.py "Two objects collide elastically"
python main.py "Circular motion with centripetal force"

# Mathematics
python main.py "Solve the equation x² - 5x + 6 = 0"
python main.py "Find the area under a curve"
python main.py "Calculate compound interest over 10 years"

# Social
python main.py "Innovation spreads through a community"
python main.py "Establishing group norms through interaction"
python main.py "Resolving conflict through compromise"

# Business
python main.py "Pricing strategy for maximum revenue"
python main.py "Balancing risk and return in investments"
python main.py "Supply chain optimization"
```

---

Happy coding! 
______/\\\\\\\\\\\__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\\__/\\\______________/\\\________/\\\_        
 _____\/////\\\///__\/\\\///////////____/\\\//////////__\/\\\_____________\///\\\____/\\\/__       
  _________\/\\\_____\/\\\______________/\\\_____________\/\\\_______________\///\\\/\\\/____      
   _________\/\\\_____\/\\\\\\\\\\\_____\/\\\____/\\\\\\\_\/\\\_________________\///\\\/______     
    _________\/\\\_____\/\\\///////______\/\\\___\/////\\\_\/\\\___________________\/\\\_______    
     _________\/\\\_____\/\\\_____________\/\\\_______\/\\\_\/\\\___________________\/\\\_______   
      __/\\\___\/\\\_____\/\\\_____________\/\\\_______\/\\\_\/\\\___________________\/\\\_______  
       _\//\\\\\\\\\______\/\\\\\\\\\\\\\\\_\//\\\\\\\\\\\\/__\/\\\\\\\\\\\\\\\_______\/\\\_______ 
        __\/////////_______\///////////////___\////////////____\///////////////________\///________

