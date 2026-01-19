tasks = []


def add_task():
    print('Это твой доступный журнал заметок и дел\n')
    task_name = input('Введите название вашей заметки -- ')
    task_description = input('Введите описание -- ')
    task_endtime = input('Желаемая дата завершения -- ')
    task = {
        'название': task_name,
        'описание': task_description,
        'дата_завершения': task_endtime,
        'статус': 'не выполнено'
    }
    tasks.append(task)
    print(f'\nЗаметка "{task_name}" успешно добавлена!')
    print(f'Всего заметок: {len(tasks)}')


