class foo:
    pass

a = foo
a.x = 123
print(a.x)

import math
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)
    
p1 = point(0, 0)
p2 = point(10, 10)
print(p1.x, p2.y)
print(p1.distance(p2))