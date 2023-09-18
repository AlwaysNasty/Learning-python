x = 7724
s = 0

for i in range (0,4):
    s = s + (x%10)*8**i
    x//=10

print(s+1)