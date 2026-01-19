import time

def madlibs():
    print("Привет! Это игра Mad libs! Мне нужно от тебя только несколько слов!\n")
    adjective_list = adjective()
    print()
    noun_list = noun()
    print()
    verb_list = verb()
    print()
    print("Отлично все слова я получил!\n")
    id_choice = int(input("Давай выберем с тобой рандомную историю! Напиши число от 1 до 4: \n"))
    stories = {
     
        1: f'Однажды {adjective_list[0]} путешественник отправился в {adjective_list[1]} лес.\nВнезапно он увидел огромный {noun_list[0]}, который начал {verb_list[0]} прямо на тропинке.\nПутешественник решил {verb_list[1]} через ближайший {noun_list[1]}, но споткнулся о {adjective_list[2]} {noun_list[2]}.\nПришлось ему быстро {verb_list[2]} к выходу из леса!', 
        2: f'На {adjective_list[0]} космическом корабле капитан обнаружил {adjective_list[1]} сигнал с планеты {noun_list[0]}.\nЭкипаж должен был {verb_list[0]} к неизвестному {noun_list[1]}, но сначала пришлось {verb_list[1]} {adjective_list[2]} двигатель.\nВнезапно из тумана появилось гигантское {noun_list[2]}, заставившее всех {verb_list[2]} в ужасе!',
        3: f'В {adjective_list[0]} королевстве жил {adjective_list[1]} рыцарь.\nОднажды король приказал ему {verb_list[0]} к волшебному {noun_list[0]}.\nПо пути рыцарь встретил говорящий {noun_list[1]}, который мог {verb_list[1]} {adjective_list[2]} заклинания.\nВместе они отправились {verb_list[2]} за таинственным {noun_list[2]}, чтобы спасти королевство.',
        4: f'В {adjective_list[0]} пятницу утром мой {adjective_list[1]} сосед решил {verb_list[0]} свой новый {noun_list[0]}.\nОн так увлекся, что начал {verb_list[1]} как сумасшедший, случайно разбив {adjective_list[2]} {noun_list[1]}.\nПришлось срочно {verb_list[2]} за скотчем, чтобы починить эту {noun_list[2]}!',
    }
    story = stories[id_choice]
    input('Отлично ты выбрал историю! Нажми "Enter" и получишь результат\n')
    simple_progress(100)
    print(story)


def adjective() -> list:
    print('Прилагательные. Мне нужно от тебя 3 прилогательных.\n')
    i = 0
    lst_adjective = []
    while i!=3:
            print(f'Пригательное {i+1}')
            adjective = input("Введите: ")
            lst_adjective.append(adjective)
            i+=1
    return lst_adjective

def noun() -> list:
    print('Существительные или нарицательные. Мне нужно от тебя 3 существительных.')
    i = 0
    lst_noun = []
    while i!=3:
        print(f'Существительное {i+1}')
        noun = input("Введите: ")
        lst_noun.append(noun)
        i+=1
    return lst_noun
    
def verb() -> list:
    print("Глаголы. Мне нужно от тебя 3 глагола.")
    i = 0
    lst_verb = []
    while i!=3:
        print(f'Глагол {i+1}')
        verb = input("Введите: ")
        lst_verb.append(verb)
        i+=1
    return lst_verb

def simple_progress(total=100):
    for i in range(total + 1):
        
        print(f'\rProgress: {i}%', end='')
        time.sleep(0.05)
    print()


madlibs()