amount = int(input())
shots = []

for i in range(amount):
    shots.append(int(input()))     #добавляем количество выстрелов равное amount

firstshot = shots[0]
max_different = 0

for i in range(len(shots)-1):
    if (shots[i + 1] - firstshot) > max_different:
        max_different = (shots[i + 1] - firstshot)           #ищем максимальную разницу между соседними выстрелами
    firstshot = shots[i + 1]

print(max_different)

min_zn = min(shots)
length_min = 0
length_max = 0

for i in range(len(shots)):
    if shots[i] == min_zn:
        length_min += 1
    else:
        length_max = length_min         #ищем самую длинную последовательность неудач
        length_min = 0
    if length_min > length_max:
        length_max = length_min

print(length_max)

firstshot = shots[0]

for i in range(len(shots) - 1):
    if shots[i + 1] == firstshot:
        length_min += 1
    else:
        length_max = length_min          #ищем самый длинный период
        length_min = 1
    firstshot = shots[i + 1]

if length_min > length_max:
    length_max = length_min

print(length_max)
