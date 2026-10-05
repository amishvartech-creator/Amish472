"""Examples of math in Python.

This module shows common mathematical operations and functions using Python's
built-in operators and the math module.
"""

import math


def arithmetic_examples():
    """Show basic arithmetic operations."""
    a = 12
    b = 5

    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
        "floor_division": a // b,
        "modulus": a % b,
        "power": a ** b,
    }


def comparison_examples():
    """Show comparisons and boolean math logic."""
    x = 10
    y = 20

    return {
        "x_equal_y": x == y,
        "x_less_than_y": x < y,
        "x_greater_than_y": x > y,
        "x_less_equal_y": x <= y,
        "x_greater_equal_y": x >= y,
    }


def absolute_and_rounding_examples():
    """Demonstrate abs() and round()."""
    value = -15.678
    return {
        "absolute_value": abs(value),
        "rounded_to_2_decimals": round(value, 2),
        "rounded_integer": round(value),
    }


def factorial_and_gcd_examples(number, another_number):
    """Compute factorial and gcd."""
    return {
        "factorial": math.factorial(number),
        "gcd": math.gcd(number, another_number),
        "lcm": (number * another_number) // math.gcd(number, another_number),
    }


def square_root_and_power_examples(value, power):
    """Compute square roots and powers."""
    return {
        "square_root": math.sqrt(value),
        "power": math.pow(value, power),
        "exponential": math.exp(2),
    }


def trigonometry_examples(angle_degrees):
    """Convert degrees to radians and compute trig values."""
    angle_radians = math.radians(angle_degrees)
    return {
        "angle_degrees": angle_degrees,
        "angle_radians": angle_radians,
        "sin": math.sin(angle_radians),
        "cos": math.cos(angle_radians),
        "tan": math.tan(angle_radians),
    }


def logarithm_examples(value):
    """Examples using log functions."""
    return {
        "natural_log": math.log(value),
        "log_base_10": math.log10(value),
        "log_base_2": math.log2(value),
    }


def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2


def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


def simple_interest(principal, rate, time):
    """Simple interest formula: I = P * R * T."""
    return principal * rate * time


def compound_interest(principal, rate, time, compounds_per_year=1):
    """Compound interest formula: A = P(1 + r/n)^(nt)."""
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    return amount


def quadratic_roots(a, b, c):
    """Solve a quadratic equation ax^2 + bx + c = 0."""
    if a == 0:
        raise ValueError("'a' cannot be zero in a quadratic equation.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        raise ValueError("The equation has no real roots.")

    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2


def percentage_change(previous, current):
    """Return percentage change from previous to current value."""
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100


def print_examples():
    """Print all example results in a friendly way."""
    print("Arithmetic examples:", arithmetic_examples())
    print("Comparison examples:", comparison_examples())
    print("Absolute and rounding examples:", absolute_and_rounding_examples())
    print("Factorial and gcd examples:", factorial_and_gcd_examples(6, 15))
    print("Square root and power examples:", square_root_and_power_examples(16, 3))
    print("Trigonometry examples:", trigonometry_examples(30))
    print("Logarithm examples:", logarithm_examples(100))
    print("Circle area:", circle_area(5))
    print("Rectangle area:", rectangle_area(8, 4))
    print("Simple interest:", simple_interest(1000, 0.05, 2))
    print("Compound interest:", compound_interest(1000, 0.05, 2, 4))
    print("Quadratic roots:", quadratic_roots(1, -3, 2))
    print("Percentage change:", percentage_change(80, 100))


if __name__ == "__main__":
    print_examples()
