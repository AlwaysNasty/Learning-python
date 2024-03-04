# for j in [1, 2, 3, 4]:
#     print(j)
#
# for k in 'abcde':
#     print(k)

while True:
    x = int(input())
    if x == 3:
        break

arr = [1, 4]
for i in arr:
    if i == 2:
        continue
    if i == 3:
        break
    print("Это не 2 и не 3")
else:
    print("В массиве не было ни одной цифры 2")
