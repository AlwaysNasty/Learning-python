def f(a, b, c, d):
    return ((a and b) == (not c)) and (b <= d)


t = (
    (1, 0, 0, 0, 1),
    (1, 0, 1, 0, 1),
    (1, 0, 1, 1, 1),
    (1, 1, 0, 0, 1)
)
if len(t) == len(set(t)):
    p = 'cadb'
    if all(f(**dict(zip(p, l))) == l[-1] for l in t):
        print('yes')
    else:
        print("no")
