# Spec-Driven Development Demo

This demo showcases **Spec-Driven Development** (SDD) using the `speckit` package—a methodology where you write executable specifications first, then implement code to satisfy them.

## What is Spec-Driven Development?

Spec-Driven Development is a variant of **Behavior-Driven Development (BDD)** and **Test-Driven Development (TDD)** where:

1. **Write Specs**: Define what the code should do in human-readable specifications
2. **Run Tests**: Use pytest to verify specs (initially failing)
3. **Implement Code**: Write minimal code to satisfy each spec
4. **Refactor**: Clean up while keeping specs passing

## Project Structure

```
demos/spec_driven_development/
├── README.md                    # This file
├── specs/                       # Executable specifications (pytest tests)
│   ├── __init__.py
│   ├── test_calculator.py       # Math specs
│   └── test_greeter.py          # Greeting specs
├── src/                         # Implementation code
│   ├── __init__.py
│   ├── calculator.py            # Calculator implementation
│   └── greeter.py               # Greeter implementation
├── pytest.ini                   # pytest configuration
└── run_demo.sh / run_demo.ps1   # Demo runner
```

## Specs Included

### 1. Calculator Specs (`specs/test_calculator.py`)
- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers (with zero-division error)

### 2. Greeter Specs (`specs/test_greeter.py`)
- Greet with name
- Greet at morning
- Greet at evening

## Running the Demo

### Option 1: Run All Tests
```bash
pytest specs/ -v
```

### Option 2: Run Specific Spec
```bash
pytest specs/test_calculator.py::test_add -v
pytest specs/test_greeter.py::test_greet_with_name -v
```

### Option 3: Run with Coverage
```bash
pytest specs/ --cov=src --cov-report=html
```

### Option 4: Use the Runner Script
**On PowerShell:**
```powershell
.\run_demo.ps1
```

**On Linux/Mac:**
```bash
bash run_demo.sh
```

## Workflow Example

### Step 1: Read a Spec (Red Phase)
```python
def test_add():
    """Spec: Adding two numbers returns their sum."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
```

### Step 2: Run and See it Fail
```
FAILED specs/test_calculator.py::test_add - ModuleNotFoundError
```

### Step 3: Implement (Green Phase)
```python
class Calculator:
    def add(self, a, b):
        return a + b
```

### Step 4: Run and See it Pass
```
PASSED specs/test_calculator.py::test_add
```

### Step 5: Refactor (Refactor Phase)
Optimize and clean up while keeping specs passing.

## Next Steps

1. **Explore Specs**: Read through `specs/test_calculator.py` and `specs/test_greeter.py`
2. **Run Tests**: Execute `pytest specs/ -v` to see which specs pass/fail
3. **Implement Features**: Add missing methods to `src/calculator.py` and `src/greeter.py`
4. **Extend Specs**: Add your own specs in the `specs/` directory
5. **Refactor Code**: Improve implementations while keeping specs passing

## Key Principles

✅ **Specs First**: Write specs before code  
✅ **Executable**: Specs are runnable pytest tests  
✅ **Clear Intent**: Specs document what code should do  
✅ **Regression-Safe**: Specs catch breaking changes  
✅ **Refactor Safely**: Specs ensure you don't break functionality  

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Behavior-Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development)
- [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)

---

**Ready to spec-driven develop?** Run `pytest specs/ -v` and start implementing!
