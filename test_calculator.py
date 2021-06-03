"""
Tests for calculator app using pytest syntax
"""

import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 2 == calculator.add(1, 1)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)
