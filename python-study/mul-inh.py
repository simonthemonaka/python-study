#multiple inheritance
class A:
    def method(self):
        super().method()
        print('A')

class B:
    def method(self):
        print('B')

class C(A, B):
    def method(self):
        super().method()
        print("C")

print(C.mro())
c = C()
c.method()