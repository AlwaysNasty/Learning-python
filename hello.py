age = 26
name = 'Swaroop'
print('Возраст {} -- {} лет.'.format(name, age))
print('Почему {} забавляется с этим Python?'.format(name))

###################################################################
number = 11
running = True

while running:
    guess = int(input('Введите целое число: '))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
##################################################################
while True:
    s = input('Введите что-нибудь : ')

    if s == 'выход':
        break
    print('Длина строки:', len(s))
print('Завершение')
##################################################################
while True:
    text = input('enter text: ')

    if text == 'exit':
        break
    if len(text) < 3:
        print('malo blyad')
        continue
    print('norm blyad')
#################################################################
#bubble sort
arr = [9,8,7,6,5,4,3,2,1,0]
print(arr)

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]

print(arr)

def outer_func():
    x = 10
    print(x)

    def inner_func():
        nonlocal x
        x = 5

    inner_func()
    print(x)

outer_func()


