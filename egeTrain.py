a = 17
b = 5
print(a%b)
###########################
for i in range(0,10,1):
    print(i)
###########################
arr = [1,2,3,4,5,6]

print(arr[0:3])
print(arr[-1])
print(arr[::-1])

arr.append(7)
print(arr)
del(arr[3])
print(arr)
#####################################
unsorted = [9,22,64,12,1,74,3,24]
unsorted.sort(reverse=True)
print(unsorted)
####################################
arr2 = []
for i in range(100):
    arr2.append(i)
print(arr2)
####################################
arr3 =[0]*10
print(arr3)
####################################
for i in unsorted:
    print(i)
####################################
f = open("problem1.py")
s = f.readline()
print(s)
####################################
s = '123123123'
print(int(s))
print(s+ "999")
print("23" in s)
print(s.count('123'))
revs = s.replace("2", "5")
print(revs)
####################################
s1 = "artem555 kruto pivo"
ssp = s1.split('t')
print(ssp)
print("t".join(ssp))
####################################
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(6))
###############################
print(bin(14))