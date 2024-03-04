from itertools import product, permutations


def f(x, y, z, w):
    return (w or y) and (x <= (not z)) and (not w)


ans = []
for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (x1, 0, x2, 0, 1),
        (1, x2, x3, x4, 1),
        (1, 1, 0, 0, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                ans.append(p)
print(len(set(ans)))
