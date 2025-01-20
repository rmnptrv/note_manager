# Поиск заметок
# Реализуем функцию для поиска заметок по критериям
def search_notes(notes, keyword=None, status=None):
    # Проверяем, если список заметок соответвующий критериям, если нет, то возвращаем пустой список и выводим надпись
    if not notes:
        print("Заметки, соответствующие запросу, не найдены.")
        return []

    # Создаем пустой список для хранения найденных заметок по критериям
    found_notes = []

    # Перебираем каждую заметку в списке
    for note in notes:
        # Проверяем условия поиска для ключевого слова и статуса
        if keyword and status:
            # Поиск если оба параметры указаны, ключевое слово и статус
            if (keyword.lower() in note['title'].lower() or
                keyword.lower() in note['content'].lower() or
                keyword.lower() in note['username'].lower()) and note['status'].lower() == status.lower():
                # Если критерии совпдает, то добавляется в список found_notes
                found_notes.append(note)
        elif keyword:
            # Поиск только по ключевому слову
            if (keyword.lower() in note['title'].lower() or
                keyword.lower() in note['content'].lower() or
                keyword.lower() in note['username'].lower()):
                found_notes.append(note)
        elif status:
            # Поиск только по статусу
            if note['status'].lower() == status.lower():
                found_notes.append(note)

    # Возвращаем список найденных заметок
    return found_notes

# Пример списка из задания
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
] if __name__ == "__main__" else []

# Ввод и поиск по ключевому слову
if __name__ == "__main__":
    keyword = input("Введите ключевое слово для поиска: ")
    found_notes = search_notes(notes, keyword=keyword)
    if found_notes:
        print("Найдены заметки:")
        for i, note in enumerate(found_notes, start=1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}\n")
    else:
        print("Заметки, соответствующие запросу, не найдены.")

    # Ввод и поиск по статусу
    status = input("Введите статус для поиска: ")
    found_notes = search_notes(notes, status=status)
    if found_notes:
        print("Найдены заметки:")
        for i, note in enumerate(found_notes, start=1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}\n")
    else:
        print("Заметки, соответствующие запросу, не найдены.")

    # Ввод и поиск по ключевому слову и статусу
    keyword = input("Введите ключевое слово для поиска: ")
    status = input("Введите статус для поиска: ")
    found_notes = search_notes(notes, keyword=keyword, status=status)
    if found_notes:
        print("Найдены заметки:")
        for i, note in enumerate(found_notes, start=1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}\n")
    else:
        print("Заметки, соответствующие запросу, не найдены.")