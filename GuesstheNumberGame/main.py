def guessnumber():
    from random import randrange
    print('Попробуй отгадать число от 1 до 20 которое загадал компьютер! У тебя 5 попыток!')
    
    win_number = randrange(1,21)
    i = 0
    print()
    while i !=5:
        print()
        print(f'Попытка {i+1}')

        try:
            user_number = int(input("Введите число: "))
        except ValueError:
            print("Введите целое число")
            continue
        if not 1<=user_number<=20:
            print("Введите число от 1 до 20")
        else:
            if user_number == win_number:
                print("Вау ты угадал! Поздравляю")
                break
            else:
                print('Ты не угадал! Попробуй снова')
                if user_number < win_number:
                    print("Загаданное число больше!")
                elif user_number > win_number:
                    print("Загаданное число меньше!")
                i+=1
    else:
        print(f"Попытки закончились! Загаданное число было: {win_number}")


guessnumber()
