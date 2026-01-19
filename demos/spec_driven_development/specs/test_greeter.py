"""
Specs for Greeter module.
These are executable specifications that define what the Greeter should do.
"""
import pytest
from datetime import datetime
from src.greeter import Greeter


class TestGreeter:
    """Greeter behavior specifications."""

    @pytest.fixture
    def greeter(self):
        """Provide a Greeter instance for each test."""
        return Greeter()

    def test_greet_with_name(self, greeter):
        """Spec: Greet should return a greeting with the person's name."""
        greeting = greeter.greet("Alice")
        assert "Alice" in greeting
        assert "Hello" in greeting or "Hi" in greeting

    def test_greet_different_names(self, greeter):
        """Spec: Greet should work with different names."""
        assert "Bob" in greeter.greet("Bob")
        assert "Charlie" in greeter.greet("Charlie")

    def test_greet_with_time_morning(self, greeter):
        """Spec: Greet should return morning greeting for morning times."""
        morning_time = datetime(2026, 1, 19, 8, 0)  # 8 AM
        greeting = greeter.greet_with_time("Alice", morning_time)
        assert "Alice" in greeting
        assert "morning" in greeting.lower()

    def test_greet_with_time_afternoon(self, greeter):
        """Spec: Greet should return afternoon greeting for afternoon times."""
        afternoon_time = datetime(2026, 1, 19, 14, 0)  # 2 PM
        greeting = greeter.greet_with_time("Bob", afternoon_time)
        assert "Bob" in greeting
        assert "afternoon" in greeting.lower()

    def test_greet_with_time_evening(self, greeter):
        """Spec: Greet should return evening greeting for evening times."""
        evening_time = datetime(2026, 1, 19, 20, 0)  # 8 PM
        greeting = greeter.greet_with_time("Charlie", evening_time)
        assert "Charlie" in greeting
        assert "evening" in greeting.lower()

    def test_greet_with_time_midnight(self, greeter):
        """Spec: Greet should handle midnight appropriately."""
        midnight_time = datetime(2026, 1, 19, 0, 0)  # Midnight
        greeting = greeter.greet_with_time("Diana", midnight_time)
        assert "Diana" in greeting

    def test_greet_formal_style(self, greeter):
        """Spec: Greet should support formal greeting style."""
        greeting = greeter.greet("Dr. Smith", formal=True)
        assert "Dr. Smith" in greeting
        # Formal greetings might use "Good day" or "Greetings"
        assert any(word in greeting.lower() for word in ["good", "greetings"])

    def test_greet_casual_style(self, greeter):
        """Spec: Greet should support casual greeting style."""
        greeting = greeter.greet("Alice", formal=False)
        assert "Alice" in greeting
        # Casual might use "Hey" or "Hi"
        assert any(word in greeting.lower() for word in ["hey", "hi", "hello"])
