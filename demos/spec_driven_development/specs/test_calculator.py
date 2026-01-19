"""
Specs for Calculator module.
These are executable specifications that define what the Calculator should do.
"""
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Calculator behavior specifications."""

    @pytest.fixture
    def calc(self):
        """Provide a Calculator instance for each test."""
        return Calculator()

    def test_add_two_positive_numbers(self, calc):
        """Spec: Adding two positive numbers returns their sum."""
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self, calc):
        """Spec: Adding negative numbers works correctly."""
        assert calc.add(-2, -3) == -5

    def test_add_positive_and_negative(self, calc):
        """Spec: Adding positive and negative numbers works correctly."""
        assert calc.add(10, -3) == 7

    def test_subtract_two_positive_numbers(self, calc):
        """Spec: Subtracting two positive numbers returns their difference."""
        assert calc.subtract(10, 3) == 7

    def test_subtract_negative_numbers(self, calc):
        """Spec: Subtracting negative numbers works correctly."""
        assert calc.subtract(-2, -3) == 1

    def test_multiply_two_positive_numbers(self, calc):
        """Spec: Multiplying two positive numbers returns their product."""
        assert calc.multiply(4, 5) == 20

    def test_multiply_by_zero(self, calc):
        """Spec: Multiplying by zero returns zero."""
        assert calc.multiply(100, 0) == 0

    def test_multiply_negative_numbers(self, calc):
        """Spec: Multiplying negative numbers works correctly."""
        assert calc.multiply(-3, -4) == 12

    def test_divide_two_positive_numbers(self, calc):
        """Spec: Dividing two positive numbers returns their quotient."""
        assert calc.divide(10, 2) == 5

    def test_divide_with_remainder(self, calc):
        """Spec: Dividing with remainder returns float result."""
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self, calc):
        """Spec: Dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_divide_negative_numbers(self, calc):
        """Spec: Dividing negative numbers works correctly."""
        assert calc.divide(-10, 2) == -5
