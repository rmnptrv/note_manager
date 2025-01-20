# Обновление заметок
# Импортируем модуль из библиотеки, это поможет нам для работы с датами
from datetime import datetime


# Вызываем функцию обновления заметки, в котором за аргумент принимается note
def update_note(note):
    print("Текущие данные заметки: ", note)

    # Критерии заметки, которые будут подележать обновлению
    criteria = ["username", "title", "content", "status", "issue_date"]

    # Запускаем цикл, в котором ПЗ надо выбрать критейрий для обновления
    while True:
        criteria_to_update = input("Какие данные вы хотите обновить? (username, title, content, status, issue_date): ").lower()

        # Если поле остается пустым или выбирается критерий не из списка, то выходит просьба выбрать правильный критерий
        if criteria_to_update not in criteria:
            print("Пожалуйста, выберите одно из следующих полей: username, title, content, status, issue_date!")
            continue

        # Когда ПЗ выбрал нужный критерий, просим ввести новое значение
        new_value = input(f"Введите новое значение для {criteria_to_update}: ")

        # Если в качестве критерия выбрана дата дедлайна, то запускаем блок на проверку ошибок и ввода правильного формата
        if criteria_to_update == "issue_date":
            try:
                datetime.strptime(new_value, "%d.%m.%Y")
            # Если формат введен не правильно, то надпись с просьбой вести правильный формат
            except ValueError:
                    print("Неверный формат даты! Пожалуйста, введи правильный формат даты, например 25.12.2024!")
                    continue

        # Присваем новое значение для словаря, выводим обновление на консоль и возвращаем обновленный словарь
        note[criteria_to_update] = new_value
        print("Заметка обновлена: ")
        print(note)
        return note

# Присваем словарю начальные данные ключ-значение
if __name__ == "__main__":
    note = {
        'username': 'Роман',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27.11.2024',
        'issue_date': '30.11.2024'
    }

    if __name__ == "__main__":
        updated_note = update_note(note)
        print("\nОбновлённая заметка:")
        print(updated_note)