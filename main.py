from geometric_figures.geometric_figures import Circle, Square, Triangle

c1 = Circle(1)
s1 = Square(1)

j1 = c1 + s1

print(c1)
print(s1)
print(j1)

print(100 * "#")

j2 = s1 + c1

print(c1)
print(s1)
print(j2)

t1 = Triangle(2)
t2 = Triangle(3)
t3 = t1 + t2
print(round(t3.area, 2))
