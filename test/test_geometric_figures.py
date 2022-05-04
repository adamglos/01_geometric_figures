import pytest
from geometric_figures.geometric_figures import Circle, Square, Triangle


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


def test_circle_comparison():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(2)
    c4 = Circle(4)

    assert c2 == c3
    assert c2 >= c3
    assert c3 <= c2
    assert c1 < c2 < c4
    assert c4 > c3 > c1


def test_circle_addition():
    c1 = Circle(1)
    c2 = Circle(1)
    c3 = c1 + c2
    assert type(c3) == Circle
    assert round(c3.area, 2) == round(c1.area + c2.area, 2)


def test_square_area():
    s1 = Square(2)
    s2 = Square(3)
    assert s1.area == 4
    assert s2.area != 4
    s1.side = 3
    assert s1.side == s2.side


# TODO test_negative_side_raises_exception():


def test_square_comparison():
    s1 = Square(1)
    s2 = Square(2)
    s3 = Square(2)
    s4 = Square(4)

    assert s2 == s3
    assert s2 >= s3
    assert s3 <= s2
    assert s1 < s2 < s4
    assert s4 > s3 > s1


def test_square_addition():
    s1 = Square(2)
    s2 = Square(3)
    s3 = s1 + s2
    assert type(s3) == Square
    assert round(s3.area, 0) == round(s1.area + s2.area, 0) == 13


def test_circle_square_addition():
    s1 = Square(2)
    c1 = Circle(2)
    j1 = s1 + c1
    assert type(j1) == type(s1)
    j2 = c1 + s1
    assert type(j2) == type(c1)


def test_triangle_comparison():
    t1 = Triangle(1)
    t2 = Triangle(2)
    t3 = Triangle(2)
    t4 = Triangle(4)

    assert t2 == t3
    assert t2 >= t3
    assert t3 <= t2
    assert t1 < t2 < t4
    assert t4 > t3 > t1


def test_triangle_addition():
    t1 = Triangle(2)
    t2 = Triangle(3)
    t3 = t1 + t2
    assert type(t3) == Triangle
    assert round(t3.area, 0) == round(t1.area + t2.area, 0) == 13


def test_circle_triangle_addition():
    t1 = Triangle(2)
    c1 = Circle(2)
    j1 = t1 + c1
    assert type(j1) == type(t1)
    j2 = c1 + t1
    assert type(j2) == type(c1)
