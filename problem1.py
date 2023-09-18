x = 30102
s = 0
for i in range(0, 5):
 s = s + (x % 10)*4**i
 x //= 10

topor = s+1
print(topor)

y = 20103
f = 0
for i in range(0, 5):
 f = f + (y % 10)*4**i
 y //= 10

ropot = f+1
print(ropot)

print(topor-ropot + 1)


