from itertools import product, permutations


def f(x, y, z):
    return x <= (y and z)


t = (
    (0, 1, 0, 0),
    (1, 1, 0, 0)
)
if len(t) == len(set(t)):
    for p in permutations('xyz', r=3):
        if all(f(**dict(zip(p, l))) == l[-1] for l in t):
            print(*p)
