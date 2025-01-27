# Сохранение заметок в файл
# Импортируем модуль из библиотеки, это поможет нам для работы с датами
from datetime import datetime


# Создаем функцию, которая принимает два аргумента
def save_notes_to_file(notes, filename):
    # Открываем файл для записи, определяем кодировку
    with open(filename, 'w', encoding='utf-8') as file:
        # С помощью цикла проходит по каждой заметке в списке
        for note in notes:
            # Для каждой заметки создаем строку, которая содержит информацию о заметке
            content = (
                f"Имя пользователя: {note['username']}\n"
                f"Заголовок: {note['title']}\n"
                f"Описание: {note['content']}\n"
                f"Статус: {note['status']}\n"
                f"Дата создания: {note['created_date']}\n"
                f"Дедлайн: {note['issue_date']}"
                f"\n---\n"
            )
            # Записываем строку в файл
            file.write(content)


if __name__ == '__main__':
    # Получаем текущую дату и время и преобразуем в строку(но на данном этапе это не требуется)
    current_date = str(datetime.now())
    # Пример списка заметок
    notes = [
    {'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27.11.2024',
    'issue_date': '30.11.2024'},
    ]

    # Вызываем функцию для сохранения списка заметок
    save_notes_to_file(notes, "notes.txt")

