# #### Перше завдання
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime

input_date = input('Введіть дату у форматі РРРР-ММ-ДД: ')

def get_days_from_today(date: str):
    try:
        ### Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
        date = datetime.strptime(date, '%Y-%m-%d')
    
        # Отримайте поточну дату, використовуючи datetime.today().
        current_date = datetime.today()
    
        # Розрахуйте різницю між поточною датою та заданою датою. Повернітьрізницю у днях як ціле число.
        difference = (current_date - date).days
        return difference 
    except ValueError:
        print("Введений формат дати невірний.")
    
result = get_days_from_today(input_date)
print(result)








# Приклад:

# Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути 157, оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року. ####