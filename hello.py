# print('hello world')
#
# age = 26
# name = 'Swaroop'
# print('Возраст {} -- {} лет.'.format(name, age))
# print('Почему {} забавляется с этим Python?'.format(name))


# number = 23
# guess = int(input('Введите целое число : '))
#
# if guess == number:
#         print('vi ugadali')
# elif guess < number:
#     print('bolshe')
# else:
#     print('menshe')


# number = 11
# running = True
#
# while running:
#     guess = int(input('Введите целое число: '))
#     if guess == number:
#         print('Поздравляю, вы угадали.')
#         running = False
#     elif guess < number:
#         print('Нет, загаданное число немного больше этого.')
#     else:
#         print('Нет, загаданное число немного меньше этого.')
#
#
# while True:
#     s = input('Введите что-нибудь : ')
#
#     if s == 'выход':
#         break
#     print('Длина строки:', len(s))
# print('Завершение')
#
#
# while True:
#     text = input('enter text: ')
#
#     if text == 'exit':
#         break
#     if len(text) < 3:
#         print('malo blyad')
#         continue
#     print('norm blyad')
#
#
# for i in range(50):
#     print(i)
#     if i == 25:
#         print('hvatit')
#         break



#bubble sort

arr = [2,4,1,3,6,8,5,7,0,9]
print(arr)

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]

print(arr)
