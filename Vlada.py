amount = int(input())
shots = []

for i in range(amount):
    shots.append(int(input()))

first = shots[0]
maxdif = 0

for i in range(len(shots)-1):
    if abs(shots[i + 1] - first) > maxdif:
        maxdif = abs(shots[i+1] - first)
    first = shots[i+1]
print(maxdif)

minval = min(shots)
lenmin = 0
maxlen = 0

for i in range(len(shots)):
    if shots[i] == minval:
        lenmin += 1
    else:
        maxlen = lenmin
        lenmin = 0
    if lenmin > maxlen:
        maxlen = lenmin
print(maxlen)

first = shots[0]
for i in range(len(shots) - 1):
    if shots[i + 1] == first:
        lenmin += 1
    else:
        maxlen = lenmin
        lenmin = 1
first = shots[i+1]

if lenmin > maxlen:
    axlen = lenmin
print(maxlen)
