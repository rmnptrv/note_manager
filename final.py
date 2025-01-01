username = input("Ваше имя: ")
content = input("Описание заметки: ")
status = input("Текущий статус: ")
created_date = input("Начало заметки (в формате дд.мм.гг): ")
issue_date = input("Дедлайн (в формате дд.мм.гг): ")

title1 = input("Введите заголовок заметки: ")
title2 = input("Введите заголовок заметки: ")
title3 = input("Введите заголовок заметки: ")
title_list = [title1, title2, title3]

note = [username, content, status, created_date[0:5], issue_date[0:5], title_list]

print(note)