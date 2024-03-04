import itertools

x = 10
x_2 = bin(x)[2:]
print(x, x_2)

x_8 = oct(x)[2:]
x_16 = hex(x)[2:]
print(x_8, x_16)

a = list(itertools.product('ABC', repeat=3))
print(a)
b = list(itertools.permutations('ABC', r=3))
print(b)
