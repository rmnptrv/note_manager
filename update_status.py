current_status = "В процессе"

print(f"Текущий статус заметки: {current_status}")

new_status = input("""Выберите новый статус заметки: 
1. Выполнено 
2. В процессе
3. Отложенно
""")

while new_status not in ["1", "2", "3"]:
    print("Неправильный ввод! Пожалуйста выберите число от 1 до 3!")
    new_status = input("""Выберите новый статус заметки: 
    1. Выполнено 
    2. В процессе
    3. Отложенно
    """)

status_option = {'1': "Выполнено", '2': "В процессе", '3': "Отложенно"}

current_status = status_option[new_status]

print(f"Статус заметки обновлен: {current_status}")
