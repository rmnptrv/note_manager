from datetime import datetime

current_datetime = datetime.now()

day = current_datetime.day
month = current_datetime.month
year = current_datetime.year
format_datetime = f"{day}.{month}.{year}"

print(format_datetime) #Не знаю, как сделать формать ДД.ММ.ГГГГ, при этом, чтобы было 01.01, а не просто 1.1

issue_date = input("Дедлайн (в формате дд.мм.гг): ")
while issue_date != f"{day}.{month}.{year}":
    print("Ошибка! Формат даты дд.мм.гг")
    issue_date = input("Дедлайн (в формате дд.мм.гг): ")

