x = 3000
s = 0

for i in range (0,4):
    s = s + (x%10)*5**i
    x//=10

print(s+1)