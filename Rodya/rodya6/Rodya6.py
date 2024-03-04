f = open('file.txt')
a = [int(x) for x in f]
print(a, min(a), max(a))

x = f.readline()
print(x)

f = open('file.txt')
print(max(int(y) for y in f))
