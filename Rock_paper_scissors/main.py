from random import choice

def game():
    print('Привет! Давай сыграем "Камень, Ножницы, Бумага"!\n')
    game_list = ['Камень', 'Ножницы', 'Бумага']
    while True:
        computer_choice = choice(game_list)
        user_choice = input('Что ты выберишь? Напиши сюда: ').capitalize()
        if computer_choice == user_choice:
            print('Ничья! Попробуй ещё раз\n')

        else:
            if (computer_choice == 'Камень' and user_choice == 'Ножницы'):
                print('Ты проиграл! Попробуй снова\n')
                continue
            elif (computer_choice == 'Ножницы' and user_choice == 'Камень'):
                print('Ты выиграл\n')
                break

            elif (computer_choice == 'Камень' and user_choice == 'Бумага'):
                print('Ты выиграл!\n')
                break
            elif (computer_choice == 'Бумага' and user_choice == 'Камень'):
                print('Ты проиграл! Попробуй снова\n')
                continue

            elif (computer_choice == 'Ножницы' and user_choice == 'Бумага'):
                print('Ты проиграл! Попробуй снова\n')
                continue
            elif (computer_choice == 'Бумага' and user_choice == 'Ножницы'):
                print('Ты выиграл!\n')
                break

            print(f'У твоего оппонента был/была - {computer_choice}')
    print('Игра окончена!\n')
    reset_game()

def reset_game():
    reset_name = input('Если хочешь поиграть снова напиши да/нет ')
    if reset_name == 'да':
        game()
    else:
        print('Окей, видимо тебе надоело. Пока!')

game()