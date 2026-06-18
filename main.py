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

#Pythonはポリモーフィズムがある。point3dと2dのそれぞれのオブジェクトに準拠して計算される。
class Point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        dz = self.z - p.z
        return math.sqrt(dx*dx + dy*dy + dz*dz)
p3 = Point3d(0, 0, 0)
p4 = Point3d(10, 10, 10)
print(p3.distance(p4))
#print(p3.distance(p1 or p2)) -> error!!

#variable in class to use common var or const var
class bar:
    z = 1
print(bar.z)

#class method
class qux:
    z = 222
    @classmethod
    def get_z(cls): return cls.z
    @classmethod
    def set_z(cls, x): cls.z = x

print(qux.get_z())
qux.set_z(100)
print(qux.get_z())

#inheritance : 親子関係 -> 継承は、メソッドとクラス変数だけ
#super class は　()で指定する。
#多重継承可
class america:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_a(self): return self.a
    def get_b(self): return self.b

class japan(america):
    def __init__(self, a, b, c):
        super().__init__(a, b) #override
        self.c = c
    def get_c(self): return self.c

a1 = america(47, 78)
b1 = japan(11, 22, 33)
print(a1.get_a())
print(a1.get_b())
print(b1.get_a())
print(b1.get_b())

class japan3(america):
    def get_c(self): return self.a + self.b

c1 = japan3(200, 300)
print(c1.get_c())

#isinstance()でクラスかサブクラスであればTrueを返す
class pan:
    pass
class kome(pan):
    pass
class men(kome):
    pass
t = pan()
y = kome()
u = men()
print(isinstance(u, pan))