"""
Greeter implementation.
Implements the specs defined in specs/test_greeter.py
"""
from datetime import datetime


class Greeter:
    """A friendly greeter that produces personalized greetings."""

    def greet(self, name, formal=False):
        """Greet a person by name.
        
        Args:
            name: Person's name
            formal: Whether to use formal greeting style (default: False)
            
        Returns:
            A greeting string
        """
        if formal:
            return f"Good day, {name}. It is a pleasure to meet you."
        else:
            return f"Hi {name}! How are you today?"

    def greet_with_time(self, name, time=None):
        """Greet a person with a time-appropriate greeting.
        
        Args:
            name: Person's name
            time: datetime object (default: current time)
            
        Returns:
            A time-appropriate greeting string
        """
        if time is None:
            time = datetime.now()

        hour = time.hour

        if 5 <= hour < 12:
            period = "morning"
        elif 12 <= hour < 17:
            period = "afternoon"
        elif 17 <= hour < 21:
            period = "evening"
        else:
            period = "night"

        return f"Good {period}, {name}! Welcome!"
