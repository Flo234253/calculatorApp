import pytest
from calculator import CalcGridLayout


class MockDisplay:
    def __init__(self):
        self.text = ""


@pytest.fixture
def calc():
    calc = CalcGridLayout()
    calc.display = MockDisplay()
    return calc


def test_calculate_valid_expression(calc):
    calc.calculate("2+3")
    assert calc.display.text == "5"


def test_calculate_invalid_expression(calc):
    calc.calculate("2/0")
    assert calc.display.text == "Error"


def test_calculate_empty_expression(calc):
    calc.calculate("")
    assert calc.display.text == "Error"


def test_calculate_float_result(calc):
    calc.calculate("10/4")
    assert calc.display.text == "2.5"


def test_calculate_integer_result(calc):
    calc.calculate("10/2")
    assert calc.display.text == "5"
