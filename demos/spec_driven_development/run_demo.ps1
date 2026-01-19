# Demo runner script for Spec-Driven Development
# Usage: .\run_demo.ps1

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Spec-Driven Development Demo" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check if pytest is installed
try {
    pytest --version | Out-Null
}
catch {
    Write-Host "❌ pytest is not installed. Installing..." -ForegroundColor Yellow
    pip install pytest -q
}

Write-Host "📋 Running Calculator Specs..." -ForegroundColor Green
Write-Host ""
pytest specs/test_calculator.py -v --tb=short
Write-Host ""

Write-Host "📋 Running Greeter Specs..." -ForegroundColor Green
Write-Host ""
pytest specs/test_greeter.py -v --tb=short
Write-Host ""

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "✅ Demo Complete!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. Review the specs in specs/test_*.py"
Write-Host "  2. Run: pytest specs/ -v"
Write-Host "  3. Implement specs by editing src/*.py"
Write-Host "  4. Re-run tests to verify implementations"
Write-Host ""
