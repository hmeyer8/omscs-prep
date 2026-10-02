# def fib(n):
#     """docstring documentation"""
#     a,b = 0,1
#     while a<n:
#         print(a, end = ' ')
#         a,b = b, a + b
#     print(a)

# print(fib)


def make_incrementor(n):
    return lambda x:x+n

f = make_incrementor(42)
print(f(3))

