# WDLIC - Documentation Index

Complete guide to all documentation and code files.

## 📚 Start Here

### For New Users
1. **[QUICKSTART.md](QUICKSTART.md)** - Get running in 5 minutes
2. **[README.md](README.md)** - Complete overview and features
3. **[EXAMPLES.md](EXAMPLES.md)** - Usage examples and scenarios

### For Developers
1. **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Architecture deep-dive
2. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Executive summary
3. **Source code** - Well-commented Python modules

---

## 📖 Documentation Files

### QUICKSTART.md
**Purpose**: Get started immediately  
**Length**: ~5 minute read  
**Contains**:
- Instant demo instructions
- Installation steps
- First examples
- Command options
- Tips for best results

**Start here if**: You want to try WDLIC right now

---

### README.md
**Purpose**: Complete feature documentation  
**Length**: ~15 minute read  
**Contains**:
- Feature overview
- Installation guide
- Usage instructions
- Command-line options
- Supported categories
- Architecture overview
- Contributing guidelines

**Read this if**: You want to understand what WDLIC can do

---

### EXAMPLES.md
**Purpose**: Comprehensive usage examples  
**Length**: ~10 minute read  
**Contains**:
- Psychology examples
- Physics examples
- Mathematics examples
- Social dynamics examples
- Mixed domain examples
- Advanced scenarios
- Integration examples
- Tips and tricks

**Use this if**: You want to see real examples and learn patterns

---

### PROJECT_STRUCTURE.md
**Purpose**: Technical architecture guide  
**Length**: ~20 minute read  
**Contains**:
- Directory layout
- Component descriptions
- Data flow diagrams
- Extension points
- Testing strategy
- Performance considerations
- Development guidelines

**Read this if**: You want to understand or extend the codebase

---

### PROJECT_SUMMARY.md
**Purpose**: Executive overview  
**Length**: ~10 minute read  
**Contains**:
- High-level concept
- Key features
- Technical architecture
- Design philosophy
- Use cases
- Roadmap
- Success metrics

**Read this if**: You want a complete overview without diving into code

---

## 💻 Source Code Files

### Core Modules

#### main.py
**Purpose**: CLI entry point  
**Lines**: ~150  
**Key Features**:
- Click-based command-line interface
- Pipeline orchestration
- Output format control
- Interactive mode

#### parser.py
**Purpose**: NLP text parsing  
**Lines**: ~120  
**Key Features**:
- spaCy integration
- Feature extraction
- Domain signal detection
- ParsedFeatures data class

#### router.py
**Purpose**: Category classification  
**Lines**: ~110  
**Key Features**:
- Multi-category routing
- Keyword matching
- Confidence scoring
- CategoryScore output

#### ir.py
**Purpose**: Intermediate representation  
**Lines**: ~200  
**Key Features**:
- Pydantic data models
- IR builder logic
- JSON serialization
- Schema validation

#### render.py
**Purpose**: Output formatting  
**Lines**: ~120  
**Key Features**:
- Rich terminal formatting
- Syntax highlighting
- Structured panels
- Color-coded output

---

### Code Generators (codegen/)

#### codegen/__init__.py
**Purpose**: Generator registry  
**Lines**: ~80  
**Key Features**:
- Generator dispatch
- Registry management
- Fallback handling

#### codegen/psychology.py
**Purpose**: Psychology code generation  
**Lines**: ~150  
**Key Features**:
- PsychologyGenerator class
- SocialGenerator class
- Agent-based models
- Decision-making logic

#### codegen/physics.py
**Purpose**: Physics code generation  
**Lines**: ~130  
**Key Features**:
- PhysicsGenerator class
- Projectile motion
- Kinematics
- Energy conservation

#### codegen/mathematics.py
**Purpose**: Math code generation  
**Lines**: ~140  
**Key Features**:
- MathematicsGenerator class
- Symbolic computation
- Optimization
- Probability calculations

---

### Utilities

#### demo.py
**Purpose**: Standalone demonstration  
**Lines**: ~350  
**Key Features**:
- No external dependencies
- Built-in examples
- Self-contained generators
- Multiple scenarios

#### setup.sh
**Purpose**: Installation script  
**Lines**: ~40  
**Key Features**:
- Dependency installation
- spaCy model download
- Setup verification

#### requirements.txt
**Purpose**: Python dependencies  
**Lines**: ~20  
**Contains**: All required and optional packages

---

### Tests

#### tests/test_basic.py
**Purpose**: Unit and integration tests  
**Lines**: ~250  
**Key Features**:
- Parser tests
- Router tests
- IR builder tests
- Code generation tests
- End-to-end scenarios

---

## 🗺️ Navigation Guide

### I want to...

#### "...try WDLIC immediately"
1. Run `python demo.py`
2. Read [QUICKSTART.md](QUICKSTART.md)

#### "...install and use WDLIC"
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Run `bash setup.sh`
3. Browse [EXAMPLES.md](EXAMPLES.md)

#### "...understand what WDLIC does"
1. Read [README.md](README.md)
2. Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
3. Try examples from [EXAMPLES.md](EXAMPLES.md)

#### "...add a new domain/category"
1. Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) → Extension Points
2. Look at `codegen/psychology.py` as template
3. Add keywords to `router.py`
4. Create generator in `codegen/your_domain.py`
5. Register in `codegen/__init__.py`

#### "...understand the code structure"
1. Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
2. Review data flow diagrams
3. Examine source code files

#### "...contribute to the project"
1. Read [README.md](README.md) → Contributing
2. Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
3. Review existing generators as examples
4. Write tests in `tests/`

#### "...use WDLIC in my project"
1. Read [EXAMPLES.md](EXAMPLES.md) → Integration examples
2. Import modules directly from Python
3. Customize generators as needed

---

## 📊 File Statistics

```
Documentation:
  - 5 Markdown files
  - ~70 pages total
  - Comprehensive coverage

Source Code:
  - 11 Python files
  - ~1,500 lines of code
  - Well-commented
  - Type-hinted

Tests:
  - 1 test file
  - 10 test functions
  - Coverage: Core functionality

Total Project:
  - 18 files
  - Clean architecture
  - Fully documented
```

---

## 🔍 Quick Reference

### Common Commands

```bash
# Run demo
python demo.py

# Basic usage
python main.py "Your scenario"

# Get pseudo-code only
python main.py "Your scenario" --format pseudo

# Get Python only
python main.py "Your scenario" --format python

# Force category
python main.py "Your scenario" --category physics

# Save output
python main.py "Your scenario" --format python > output.py

# Run tests
python tests/test_basic.py
```

### File Locations

- **Main code**: Root directory (`main.py`, `parser.py`, etc.)
- **Generators**: `codegen/` directory
- **Tests**: `tests/` directory
- **Docs**: Root directory (`.md` files)
- **Config**: `requirements.txt`, `setup.sh`

---

## 📋 Checklist for New Users

- [ ] Read QUICKSTART.md
- [ ] Run demo.py
- [ ] Install dependencies (setup.sh)
- [ ] Try first example
- [ ] Browse EXAMPLES.md
- [ ] Read README.md for details
- [ ] Experiment with own scenarios
- [ ] Check PROJECT_STRUCTURE.md if extending

---

## 📋 Checklist for Developers

- [ ] Read PROJECT_SUMMARY.md
- [ ] Read PROJECT_STRUCTURE.md
- [ ] Review source code architecture
- [ ] Understand data flow pipeline
- [ ] Examine existing generators
- [ ] Run tests
- [ ] Plan extensions
- [ ] Write new tests

---

## 🎯 Quick Links

| Topic | File |
|-------|------|
| Getting Started | [QUICKSTART.md](QUICKSTART.md) |
| Full Documentation | [README.md](README.md) |
| Examples | [EXAMPLES.md](EXAMPLES.md) |
| Architecture | [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) |
| Overview | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |
| Source Code | `*.py` files |
| Tests | `tests/test_basic.py` |

---

## 💡 Tips

### For Reading Documentation
1. Start with QUICKSTART.md
2. Try the demo
3. Read sections of interest
4. Refer back as needed

### For Using WDLIC
1. Start simple
2. Use domain keywords
3. Be specific with numbers
4. Iterate and refine

### For Extending WDLIC
1. Understand existing patterns
2. Follow code style
3. Write tests
4. Document changes

---

## 🚀 Next Steps

After reviewing this index:

1. **New User**: → [QUICKSTART.md](QUICKSTART.md)
2. **Curious**: → [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
3. **Developer**: → [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
4. **Learner**: → [EXAMPLES.md](EXAMPLES.md)

---

**Happy exploring!** 🎉

Everything you need is documented. Everything can be expressed in code!
