# Higher Order Functions
def outer(f):
    def inner(n1, n2):
        result = f(n1, n2)
        return result ** 2
    return inner

@outer
def num(n1, n2):
    return n1 + n2 + 5

print(num(19, 4))
