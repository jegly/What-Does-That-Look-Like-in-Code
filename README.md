#   What Does That Look Like in Code

### 

---


---

##  WHAT EVEN IS THIS?? 



**BOOM.** That's WDLIC.

Type words. Get code. It's like magic but dumber. 

---

##  INSTALLATION

### Step 1:
```bash
# You: "I'll just install it normally"
pip install stuff

# Linux: "lol no"
error: externally-managed-environment

# You: "WHAT"
```

### Step 2: Actually Install It (The Real Way™)

```bash
# Install the venv thingy (because apparently Python is too cool for regular installs now)
sudo apt install python3.12-venv

# Make a little Python house
python3 -m venv venv

# Go inside the house
source venv/bin/activate

# NOW you can install stuff like a PEASANT
pip install spacy pydantic numpy rich click sympy scipy matplotlib pytest

# Download the brain
python -m spacy download en_core_web_sm

# Your terminal now looks like this:
(venv) you@computer:~$ 
# ^ that "(venv)" means you're in the Python house
```

### Step 3: Realize You Have to Do This EVERY TIME

```bash
# Next time you open terminal:
cd ~/Documents/wdlic
source venv/bin/activate  # ← YOU WILL FORGET THIS. EVERYONE DOES.

# Then you can use it:
python3 main.py "your silly scenario"
```

---

## 🎪 now time to use the dumb code


```bash
# This will make the computer angry:
python3 main.py why is water wet
# Error: Got unexpected extra arguments (is water wet)
# Computer: "USE QUOTES DUMMY"

# This is too simple:
python3 main.py water
# Output: *sad generic code noises*

# This is a QUESTION not a SCENARIO:
python3 main.py "what is the meaning of life"
# WDLIC: "I... I don't know man, I just make code"
```

### ✅ RIGHT WAYS (Be Specific! Be Dramatic!)

```bash
# YES - Psychology drama
python3 main.py "A person musters courage to text their crush"

# YES - Physics chaos  
python3 main.py "A cat knocks a cup off a table and watches it fall"

# YES - Social dynamics
python3 main.py "Five people argue about where to eat and eventually give up"

# YES - Math stuff
python3 main.py "Calculate how long until I can afford a house (spoiler: never)"
```

---

## 🎭 EXAMPLE SCENARIOS

### The Relatable Ones

```bash
python3 main.py "Someone scrolls social media at 3am instead of sleeping"

python3 main.py "A person tries to parallel park and gives up after 47 attempts"

python3 main.py "Two people both wait for the other to text first for 3 weeks"

python3 main.py "Someone builds confidence by pretending to know what they're doing"
```

### The Physics Ones 

```bash
python3 main.py "A pizza box slides off a car roof at 30 mph"

python3 main.py "A phone falls out of pocket in slow motion while you watch in horror"

python3 main.py "Calculate how hard you need to throw something to reach the moon (very)"
```

### The Social Chaos Ones

```bash
python3 main.py "Group chat descends into chaos over whether water is wet"

python3 main.py "Everyone pretends to understand the math homework"

python3 main.py "Trust issues develop after someone spoils Endgame"
```

### ODDballs

```bash
python3 main.py "Molecules vibrate faster because they had too much coffee"

python3 main.py "Entropy increases because I haven't cleaned my room in 3 months"

python3 main.py "Calculate the probability of accidentally liking an old Instagram photo"
```

---

## 🤔 WHAT WDLIC IS GOOD AT.. NOTHING

✅ Turning scenarios into code  
✅ Making you feel smart  
✅ Generating code that actually runs  
✅ Teaching computational thinking  
✅ Being oddly satisfying  

## 😵 WHAT WDLIC IS BAD AT.. EVERYTHING

❌ Answering "why is water wet"  
❌ Explaining the meaning of life  
❌ Doing your homework (but it can help?)  
❌ Making good life decisions  
❌ Predicting the stock market  
❌ Ordering pizza (we tried)  

---

## 

### Tip 1: USE QUOTES
```bash
# NO
python3 main.py why is the sun hot

# YES  
python3 main.py "why is the sun hot"
```

### Tip 2: Be Specific With Numbers
```bash
# Meh
python3 main.py "something falls"

# CHEF'S KISS
python3 main.py "A bowling ball falls from 100 meters at 9.81 m/s²"
```

### Tip 3: Think "What Would This Look Like as a Simulation?"
- Not: "What is anxiety?"
- Yes: "A person's anxiety increases before giving a presentation"

### Tip 4: Remember to Activate the venv
```bash
# You, every single time:
python3 main.py "thing"
# Error: ModuleNotFoundError: No module named 'spacy'

# Fix:
source venv/bin/activate
# NOW it works
```

---

## 🎪 CATEGORIES WDLIC UNDERSTANDS

| Category | What It Means | Example |
|----------|---------------|---------|
| **Psychology** | Brain stuff, feelings, decisions | "Someone panics before a job interview" |
| **Physics** | Things falling, moving, breaking | "A watermelon explodes when dropped" |
| **Math** | Numbers, optimization, equations | "Find the maximum number of cookies I can eat" |
| **Social** | Groups, drama, opinions | "Friend group splits over pineapple on pizza debate" |
| **Generic** | When WDLIC is confused | "water" ← you did this to yourself |

---

## 🎨 OUTPUT FORMATS

### Get Everything (Default)
```bash
python3 main.py "your scenario"
# Shows: category, assumptions, pseudo-code, Python code, EVERYTHING
```

### Just Pseudo-Code (For Humans)
```bash
python3 main.py "your scenario" --format pseudo
# Just the logic in plain language
```

### Just Python (For Running It)
```bash
python3 main.py "your scenario" --format python > my_code.py
python3 my_code.py
# IT ACTUALLY RUNS!
```

---

##  COMMON ERRORS & HOW TO FIX

### sudo rm -rf / ###
### "ModuleNotFoundError: No module named 'spacy'"
**Translation:** You forgot to activate the venv, dummy  
**Fix:** `source venv/bin/activate`

### "Got unexpected extra arguments"
**Translation:** YOU FORGOT THE QUOTES  
**Fix:** Put quotes around your text like `"this"`

### "GENERIC (confidence: 50%)"
**Translation:** WDLIC has no idea what you want  
**Fix:** Be more specific! Add actors, actions, numbers!

### "externally-managed-environment"
**Translation:** Your system Python is locked down  
**Fix:** Use venv like we told you in Step 2

---

## 🎭 REAL USER TESTIMONIALS (Probably Made Up)

> "I described my relationship problems and got working code. Now I understand why I'm single." - Anonymous

> "Finally, a tool that's as confused as I am!" - Confused Student

> "I asked it why water is wet and it gave me generic code. 10/10 would ask dumb questions again." - That One User (you) that really happened.

> "My therapist told me to journal. I used WDLIC instead. Now I have Python classes for my trauma." - Definitely Real Person

> "Instructions unclear, accidentally learned how code works." - Reformed Non-Programmer

---

## 🎯 THE WHOLE POINT

WDLIC turns **"what if..."** into **"here's the code for that"**

It's not good for:
- Learning how things work
- Prototyping ideas quickly
- Understanding computational thinking
- Procrastinating on actual work
- Asking silly questions and getting silly code

It sure aint NOT for:
- Production systems (please god no)
- Your thesis (unless your advisor is cool)
- Predicting the future
- Answering philosophical questions
- Replacing Stack Overflow

---

## 📚 FILES YOU MIGHT ACTUALLY READ

- `START_HERE.md` - The boring normal README
- `QUICKSTART.md` - How to actually use this thing
- `EXAMPLES.md` - Good examples (not the dumb ones you tried)
- `interactive_demo.py` - No installation needed! USE THIS IF LAZY!

---

## 🎪 INTERACTIVE MODE (For the Lazy)

Don't wanna type commands? Fine.

```bash
python3 interactive_demo.py
```

Then just type scenarios when it asks. It's like ChatGPT but worse and it only makes code, and its bad code. logical people will hate it.

---

## 🏆 ACHIEVEMENT UNLOCKED

If you made it this far in the README, you're either:
1. Very bored
2. Very thorough
3. A stalker
4. All of the above

**Congrats!** Now go make some silly code scenarios, or make the code better i don't know. 

---

## 

Remember:
- **Always activate the venv** (you won't, but try)
- **Use quotes** around your text
- **Be specific** with scenarios
- **Have fun** breaking things
- **Don't ask it philosophical questions** (it will judge you)
- **and if that fails sudo rm**

Now go forth and turn your weird shower thoughts into Python code!

---

## 💬 SUPPORT. sorry no figure it out.

**Q: It doesn't work!**  
A: Did you activate the venv? Did you use quotes? Did you read any of this README?

**Q: Can it do [impossible thing]?**  
A: No. But try it anyway, you might be surprised.

**Q: Is water wet?**  
A: We're not doing this again. lol

**Q: Where can I learn more?**  
A: Read the actual documentation like a responsible human.

---

**Made with ❤️, 😅, and way too much caffeine and nooooptropics **

*WDLIC: Because sometimes you just need to see what your weird ideas look like in code.*

______/\\\\\\\\\\\__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\\__/\\\______________/\\\________/\\\_        
 _____\/////\\\///__\/\\\///////////____/\\\//////////__\/\\\_____________\///\\\____/\\\/__       
  _________\/\\\_____\/\\\______________/\\\_____________\/\\\_______________\///\\\/\\\/____      
   _________\/\\\_____\/\\\\\\\\\\\_____\/\\\____/\\\\\\\_\/\\\_________________\///\\\/______     
    _________\/\\\_____\/\\\///////______\/\\\___\/////\\\_\/\\\___________________\/\\\_______    
     _________\/\\\_____\/\\\_____________\/\\\_______\/\\\_\/\\\___________________\/\\\_______   
      __/\\\___\/\\\_____\/\\\_____________\/\\\_______\/\\\_\/\\\___________________\/\\\_______  
       _\//\\\\\\\\\______\/\\\\\\\\\\\\\\\_\//\\\\\\\\\\\\/__\/\\\\\\\\\\\\\\\_______\/\\\_______ 
        __\/////////_______\///////////////___\////////////____\///////////////________\///________


