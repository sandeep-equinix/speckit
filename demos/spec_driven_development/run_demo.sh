#!/bin/bash
# Demo runner script for Spec-Driven Development
# Usage: bash run_demo.sh

set -e

echo "============================================"
echo "Spec-Driven Development Demo"
echo "============================================"
echo ""

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "❌ pytest is not installed. Installing..."
    pip install pytest -q
fi

echo "📋 Running Calculator Specs..."
echo ""
pytest specs/test_calculator.py -v --tb=short || true
echo ""

echo "📋 Running Greeter Specs..."
echo ""
pytest specs/test_greeter.py -v --tb=short || true
echo ""

echo "============================================"
echo "✅ Demo Complete!"
echo "============================================"
echo ""
echo "Next Steps:"
echo "  1. Review the specs in specs/test_*.py"
echo "  2. Run: pytest specs/ -v"
echo "  3. Implement specs by editing src/*.py"
echo "  4. Re-run tests to verify implementations"
echo ""
