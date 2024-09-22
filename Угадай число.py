import random

mainLoop = True
answer = 0
startScore = 100
countInput = 0

while mainLoop  # ошибка 1
    digit = random.randint(10, 50   # ошибка 2
    print(digit)
    startScore = 100
    countInput = 0
    print('Компьютер загадал число. Попробуйте отгадать!')
    while answer != digit and startScore > 0:
        countInput + 1  # ошибка 3
        answer = int(input('\nВведите число от 10 до 50: '))
        if answer == digit:
            print('Победа! Поздравляем!')
        els:  # ошибка 4

            if countInput >= 5 and countInput < 10:
                startScore -= 15
                if startScore <= 0:
                    print(f'Увы, у вас закончились очки. Компьютер загадал число {digit}')
                    brea  # ошибка 5
                print('Вы ошиблись. Угадывайте дальше!')
                print(f'У вас осталось {startScore} очков')
                if answer > digit:
                    print('Загаданное число МЕНЬШЕ вашего')
                    continue
                else:
                    print('Загаданное число БОЛЬШЕ вашего')
                    continue
            else:
                print('Вы ошиблись. Угадывайте дальше!')
                startScore -= 10
                print(f'У вас осталось {startScore} очков')


    if (input('\nEnter - сыграть еще раз, 0 - выход ') == '0'):
        print('\nСпасибо, что воспользовались нашей игрой! Всего хорошего =)')
        mainLoop = False