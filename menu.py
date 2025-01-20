# Меню действий
from create_note_function import create_note
from display_notes_function import display_notes
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes
from delete_note import delete_note


def display_menu(notes):
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")

        try:
            choice_menu = input("Ваш выбор: ")
            if choice_menu == "1":
                notes = create_note(notes)
            elif choice_menu == "2":
                display_notes(notes)
            elif choice_menu == "3":
                if notes:
                    display_notes(notes)
                    index = int(input("Введите номер заметки для обновления: ")) - 1
                    if 0 <= index < len(notes):
                        notes[index] = update_note(notes[index])
                    else:
                        print("\nНеверный номер заметки.")
                else:
                    print("\nСписок заметок пуст.")
            elif choice_menu == "4":
                notes = delete_note(notes)
            elif choice_menu == "5":
                search_notes(notes)
            elif choice_menu == "6":
                print("\nПрограмма завершена. Спасибо за использование!")
                break
            else:
                print("\nНеверный выбор. Пожалуйста, выберите действие из списка.")
        except ValueError:
            print("\nНеверный выбор. Пожалуйста, выберите действие из списка.")

def main():
    notes = []
    display_menu(notes)

if __name__ == "__main__":
    main()

