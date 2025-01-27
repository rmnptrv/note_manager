# Формат файла json
# Импортируем модуль json для работы с json форматом
import json


# Создаем функцию, для сохранения заметок в json файл, которая принимает два аргумент
def save_notes_json(notes, filename):
    # Запускаем блок ошибок
    try:
        # Открываем файл в режиме записи(до этого был в режиме создания - х, я изменил далее)
        with open(filename, "w", encoding='utf-8') as file:
            # Записываем заметки в формате json
            # ensure_ascii=False позволяет сохранять текст в UTF-8
            # indent=4 добавляет отступы для улучшения читаемости JSON
            json.dump(notes, file, ensure_ascii=False, indent=4)
    # Обработка ошибок, когда нет прав для записи файла
    except PermissionError:
        print(f"Ошибка: Нет прав для записи в файл '{filename}'.")
    # Обработка всех прочих ошибок
    except Exception as e:
        print(f"Произошла ошибка при записи в файл '{filename}': {e}")

if __name__ == '__main__':
    # Список заметок, где каждая заметка является словарём
    notes_to_save = [
    {'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27.11.2024',
    'issue_date': '30.11.2024'},
    ]

    # Вызываем функцию для сохранения заметок в файл
    save_notes_json(notes_to_save, "notes.json")
