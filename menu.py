# Меню действий
# Импортируем функции из других файлов, это поможет использовать нам эти функции в этом файле
from create_note_function import create_note
from display_notes_function import display_notes
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes
# Также был обновлен файл delete_note, я добавил туда возможность вызова функции
from delete_note import delete_note


# Вызываем функцию с аргументом notes, наш список заметок, также выводим на консоль наше меню
def display_menu(notes):
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")

        # Запускаем блок на провершку ошибок, а также возможность ввода для выбора меню от 1 до 6
        try:
            choice_menu = input("Ваш выбор: ")
            # Если ПЗ выбрал 1, то вызывается функция create_note и создается новая заметка, обновляется список notes
            if choice_menu == "1":
                notes = create_note(notes)
            # Если ПЗ выбрал 2, то показывается все заметки
            elif choice_menu == "2":
                display_notes(notes)
            # Если ПЗ выбрал 3, проверяется есть ли заметки
            elif choice_menu == "3":
                # Если есть, то показывается все доступне заметки, ПЗ выбирает номер заметки для обновления
                if notes:
                    display_notes(notes)
                    # Преобразуем введенное значение в целое число и уменьшаем на 1, чтобы соответвовать индексации
                    index = int(input("Введите номер заметки для обновления: ")) - 1
                    # Проверяем находится ли число в диапазоне индексации
                    if 0 <= index < len(notes):
                        # Если номер введен правильно, то вызывается функция update_note, обновленная заметка
                        # сохраняется в список notes
                        notes[index] = update_note(notes[index])
                    else:
                        # Если номер заметки неверный, то выходит надпись
                        print("\nНеверный номер заметки.")
                else:
                    # Если заметок не было изначально, то выходит надпись
                    print("\nСписок заметок пуст.")
            # Если ПЗ выбрал 4, то вызывается функция delete_note, которая удаляет заметку
            elif choice_menu == "4":
                notes = delete_note(notes)
            # Если ПЗ выбрал 5, то ПЗ надо выбрать ключевое слово и статус, затем вызывает функция search_notes,
            # которая ищет заметку по введенным критериям и после выводит нужную заметку
            elif choice_menu == "5":
                keyword = input("Введите ключевое слово для поиска: ")
                status = input("Введите статус для поиска (или оставьте пустым): ")
                found_notes = search_notes(notes, keyword, status)
                display_notes(found_notes)
            # Если ПЗ выбрал 6, то программа завершается и выходит из цикла
            elif choice_menu == "6":
                print("\nПрограмма завершена. Спасибо за использование!")
                break
            # Если выбрано что-то иное кроме 1-6, то выходит сообщение
            else:
                print("\nНеверный выбор. Пожалуйста, выберите действие из списка.")
        # Если есть ошибка ввода, то выходит сообщение
        except ValueError:
            print("\nНеверный выбор. Пожалуйста, выберите действие из списка.")

# Функция для создания пустого списка заметки и запуска функции display_menu
def main():
    notes = []
    display_menu(notes)

# Точка входа
if __name__ == "__main__":
    main()