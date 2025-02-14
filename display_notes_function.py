# Отображение заметок
# Вызываем функцию отображения заметок, аргументом здесь выступает notes
def display_notes(notes):
    # Если заметок нет, то у нас выходят характерная надпись и функция прекращает свою работу
    if not notes:
        print("У вас нет сохранённых заметок.\n")
        return

    # Если список не пуст, то выходит надпись и разделительная линия
    print("Список заметок:")
    print("-----------------------------")

    # Изпользуем цикл for для перебора всех заметок, с помощью enumerate, для нумерация с числа 1
    for i, note in enumerate(notes, start=1):
        print(f"\nЗаметка №{i}:")
        print(f" Имя: {note['username']}")
        print(f" Заголовок: {note['title']}")
        print(f" Описание: {note['content']}")
        print(f" Статус: {note['status']}")
        print(f" Дата создания: {note['created_date']}")
        print(f" Дедлайн: {note['issue_date']}")
        print("-----------------------------")

# Список со вложенными словорями, если разкоментировать, то на консоле будет пронумерованный список
# notes = [
#     {
#         'username': 'Роман',
#         'title': 'Список покупок',
#         'content': 'Купить продукты на неделю',
#         'status': 'новая',
#         'created_date': '27.11.2024',
#         'issue_date': '30.11.2024'
#     },
#     {
#         'username': 'Екатерина',
#         'title': 'Учеба',
#         'content': 'Подготовиться к экзамену',
#         'status': 'в процессе',
#         'created_date': '25.11.2024',
#         'issue_date': '01.12.2024'
#     },
#     {
#         'username': 'Алексей',
#         'title': 'Путешествие',
#         'content': 'Спланировать поездку в Италию',
#         'status': 'завершена',
#         'created_date': '20.11.2024',
#         'issue_date': '15.12.2024'
#     }
# ] if __name__ == "__main__" else []

# Проверяем определен ли список локально, если определенно, то выводится весь список со словарями внутри
# Если список не определен и не найден, то присваивается постой список
notes = notes if 'notes' in locals() else []

# Запускаем функцию
if __name__ == "__main__":
    display_notes(notes)