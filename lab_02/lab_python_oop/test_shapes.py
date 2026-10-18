from math import pi
import pytest
from . import Rectangle, Circle, Square
from .figure import Figure
from .color import Color


def test_variant_22():
    assert Rectangle(22, 22, "синий").area() == 484
    assert Square(22).area() == 484
    assert Circle(22, "зелёный").area() == pytest.approx(484 * pi)


def test_inheritance_and_class_name():
    assert isinstance(Square(22), Rectangle)
    assert Square.get_name() == "Квадрат"
    with pytest.raises(TypeError):
        Figure()


@pytest.mark.parametrize("size", [0, -1, float("nan"), float("inf")])
def test_invalid_size(size):
    with pytest.raises(ValueError):
        Circle(size, "зелёный")


def test_color_property_and_representation():
    figure = Square(22)
    figure.color.value = "синий"
    assert "синий" in repr(figure)
    assert "484.0000" in repr(figure)
    with pytest.raises(ValueError):
        Color("")
