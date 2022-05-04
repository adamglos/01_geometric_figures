import pytest
from geometric_figures.geometric_figures import Circle


def test_circle_area():
    c1 = Circle(2)
    c2 = Circle(3)
    assert round(c1.area, 2) == 12.57
    assert round(c2.area, 2) != 12.57
    assert c1 != c2
    c1.radius = 3
    assert c1.radius == c2.radius


def test_circle_radius_diameter():
    c = Circle(1)
    assert c.radius * 2 == c.diameter == 2
    c.radius = 5
    assert c.radius * 2 == c.diameter == 10
    c.diameter = 20
    assert c.radius * 2 == c.diameter == 20


def test_negative_radius_raises_exception():
    with pytest.raises(ValueError):
        c = Circle(5)
        c.radius = -2
