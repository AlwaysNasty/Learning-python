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


while True:
    s = input('Введите что-нибудь : ')

    if s == 'выход':
        break
    print('Длина строки:', len(s))
print('Завершение')


while True:
    text = input('enter text: ')

    if text == 'exit':
        break
    if len(text) < 3:
        print('malo blyad')
        continue
    print('norm blyad')


