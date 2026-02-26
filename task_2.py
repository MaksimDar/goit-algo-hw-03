# Друге завдання
import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    numbers = []
    final_list = []
    # Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
    if min < 1 or max > 1000 or not (quantity > 0 and quantity <= (max - min + 1)):
       print('Вхідні параметри не відповідають заданим обмеженням.')
    else: 
        counter = min
        while max >= counter:
            numbers.append(counter)
            counter = counter + 1
        
        # Відповідність вимогам: результат має бути у вигляді відсортованого списку.
        final_list = sorted(random.sample(numbers, quantity))
    
    return final_list
    

try :
    min = int(input('Введіть min значення не менше 1: '))
    max = int(input('Введіть max значення не більше 1000: '))
    quantity = int(input('Введіть quantity значення в інтервалі між min та max значеннями: '))
    lottery_numbers = get_numbers_ticket(min,max,quantity)
    print(f"Ваші лотерейні числа: {lottery_numbers}")
except ValueError:
    print("Введений формат значень невірний.")



