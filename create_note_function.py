# Введение функций
# Импортируем модуль из библиотеки, это поможет нам для работы с датами
from datetime import datetime

# Получаем текущую дату
current_datetime = datetime.now()

# Преобразовываем дату в нужный нам формат, исключая время
formatted_datetime = current_datetime.strftime("%d.%m.%Y")

# Вызываем функцию
def create_note():
    # Запускаем цикл ввода и проверки на пустое значение
    while True:
        username = input("Ваше имя: ")
        if not username:
            print("Имя пользователя не может быть пустым! Пожалуйста, введите ваше имя!")
        else:
            break

    while True:
        title = input("Заголовок заметки: ")
        if not title:
            print("Заголовок не может быть пустым! Пожалуйста, введите ваше заголовок!")
        else:
            break

    while True:
        content = input("Описание заметки: ")
        if not content:
            print("Описание не может быть пустым! Пожалуйста, введите описание!")
        else:
            break

    # Проверяем, чтобы статус заметки был по ключевым словам
    while True:
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").lower()
        while status not in ["новая", "в процессе", "выполнено"]:
            print("Пожалуйста, выберите статус заметки из предложенных вариантов! Новая, в процессе или выполнено.")
            status = input("Введите статус заметки (новая, в процессе, выполнено): ").lower()
        else:
            break

    # Автоматически выводим дату создания заметки
    created_date = formatted_datetime
    print("Дата создания заметки :", formatted_datetime)

    # Проверяем дату делайна на ошибки, чтобы всё было согласно указаному формату
    while True:
        try:
            issue_date = input(f"Введите дату дедлайна (в формате дд.мм.гггг, например 25.12.2024): ")
            issue_date_ = datetime.strptime(issue_date, "%d.%m.%Y")
            break

        except ValueError:
            print("Неверный формат даты! Пожалуйста, введи правильный формат даты, например 25.12.2024!")

    # Добавляем введеные значения в словарь
    note = {'username': username,
             'title': title,
             'content': content,
             'status': status,
             'created_date': created_date,
             'issue_date': issue_date}

    # Возвращаем созданный словарь из функции
    return note

# Все результаты функции присваиваются в переменную new_note
new_note = create_note()
# Выводит словарь на консоль
print("Заметка создана: ", new_note)
