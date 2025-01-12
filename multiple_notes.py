from datetime import datetime

notes = []

print('Добро пожаловатьв "Менеджер заметок!"')

while True:
    choice = input("Хотите добавить новую заметку? (да/нет): ").lower()

    if choice == "нет":
        print("Хорошего дня!")
        break

    elif choice == "да":
        while True:
            username = input("Ваше имя: ")
            if not username:
                print("Имя пользователя не может быть пустым! Пожалуйста, введите ваше имя!")
            else:
                break

        while True:
            title = input("Заголовок заметки: ")
            if not title:
                print("Заголовок не может быть пустым! Пожалуйста, введите заголовок заметки!")
            else:
                break

        while True:
            content = input("Описание заметки: ")
            if not content:
                print("Описание не может быть пустым! Пожалуйста, введите описание заметки!")
            else:
                break

        while True:
            status = input("Статус заметки: ")
            if not status:
                print("Статус не может быть пустым! Пожалуйста, введите статус заметки!")
            else:
                break

        while True:
            created_date = input("Дата создания (в формате дд.мм.гггг): ")
            try:
                datetime.strptime(created_date, "%d.%m.%Y")
                break
            except ValueError:
                print("Некорректный формат даты. Пожалуйста, введите дату в формате дд.мм.гггг.")

        while True:
            issue_date = input("Дедлайн (в формате дд.мм.гггг): ")
            try:
                datetime.strptime(issue_date, "%d.%m.%Y")
                break
            except ValueError:
                print("Неверный формат даты! Пожалуйста, введи правильный формат даты, например 25.12.2024!")

        note = {"Имя": username,
                "Заголовок": title,
                "Описание": content,
                "Статус": status,
                "Дата создания": created_date,
                "Дедлайн": issue_date}

        notes.append(note)

        print("Заметка успешно добавлена!")

    else:
         print("Пожалуйста, введите да или нет!")

print("\nСписок заметок:")
for i, note in enumerate(notes, start=1):
    print(f"\nЗаметка {i}:")
    for key, value in note.items():
        print(f"  {key}: {value}")
