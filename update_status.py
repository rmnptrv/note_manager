current_status = "В процессе" #Текущий статус заметки

print(f"Текущий статус заметки: {current_status}") #Выводит на экран текущий статус

new_status = input("""Выберите новый статус заметки:
1. Выполнено 
2. В процессе
3. Отложенно
""") #Запрашивает ввода нового статуса заметки

while new_status not in ["1", "2", "3"]: #Запускает цикл корректности ввода, пока пользователь не выберет 1-3, будет выходить цикличный ввод
    print("Неправильный ввод! Пожалуйста выберите число от 1 до 3!") #
    new_status = input("""Выберите новый статус заметки: 
    1. Выполнено 
    2. В процессе
    3. Отложенно
    """)

status_option = {'1': "Выполнено", '2': "В процессе", '3': "Отложенно"} #Словарь, в котором ключи соотвествуют необходимому значению

current_status = status_option[new_status] #Обновляется текущий статус заметки

print(f"Статус заметки обновлен: {current_status}") #Выводит на экран обновленный статус
