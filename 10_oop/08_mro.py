class A:
    label = "A: Base class"


class B(A):
    label = "B: Derived class"


class C(A):
    label = "C: Derived class"


class D(B, C):
    label = "D: Derived class"
    # pass


d = D()
print(d.label)
print(D.mro())

