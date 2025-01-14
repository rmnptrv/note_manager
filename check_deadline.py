# Проверка дедлайнов
from datetime import datetime # Импортируем модуль из библиотеки, это поможет нам для работы с датами


current_datetime = datetime.now() # Получаем текущую дату

formatted_datetime = current_datetime.strftime("%d.%m.%Y") # Преобразовываем дату в нужный нам формат, исключая время

current_date = datetime.strptime(formatted_datetime, "%d.%m.%Y") # Преобразовываем строку в объект datetime,
# понадобится, чтобы в дальше применить в вычислениях

print(f"Текущая дата: {formatted_datetime}") #Выводим текущу дату на консоль

while True: # Начало цикла, будет продолжаться, пока ПЗ не введет корректную дату, в случае ошибки, повторяется
    try: # Запускаем блок проверки ошибок
        issue_date = input("Введите дату дедлайна (в формате дд.мм.гггг, например 25.12.2024): " ) # Просим ввести дату
        # в правильном формате

        issue_date_ = datetime.strptime(issue_date,"%d.%m.%Y") # Преобразуем дату(строку) в объект datetime,
        # необходимо для вычеслений

        time_difference = issue_date_ - current_date # Вычесляем раницу между датой дедлайна и текущей датой
        days_difference = time_difference.days # Извлекаем разницу в днях

        if days_difference > 0: # Проверка разница и вывод в консоль соотвествующего значения
            print(f"До делайна осталось {days_difference} дней!")
        elif days_difference < 0:
            print(f"Дедлайн истек {abs(days_difference)} дней назад!")
        else:
            print("Дедлайн сегодня!")

        break # Выходим из цикла при выполнение условий

    except ValueError: # Обработка ошибки неверного формата даты
        print("Неверный формат даты! Пожалуйста, введи правильный формат даты, например 25.12.2024!")
