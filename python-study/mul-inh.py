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
#MRO:C->A->B したがってmethod()の呼び出しは逆になる
c = C()
c.method()


###例外処理 exception is class : inheritance BaseException
def foo(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error {} / {}'.format(a, b))
        return 0

print(foo(10, 2))
print(foo(1, 0))
