from datetime import datetime
from random import sample
import re

def get_days_from_today(date:str):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Некоректна дата. Формат має бути 'РРРР-ММ-ДД'")
        return None
    today = datetime.today().date()
    delta_days = today - date
    if delta_days.days < 1:
        return f'{date_r} на {delta_days.days} днів пізніше від {datetime.today().date()}'
    if delta_days.days > 1:
        return f'{date_r} на {delta_days.days} днів раніше від {datetime.today().date()}'

    return delta_days.days

def get_numbers_ticket(min_value:int, max_value:int, quantity:int) -> list:
    # фільтр невалідних значень
    if not (1 <= min_value and max_value <= 1000):
        return []

    if not (1 <= quantity <= (max_value - min_value +1)):
        return []

    # створюємо список з числами і вибираємо рандомні числа
    numbers = sample(range(min_value, max_value), quantity)
    return sorted(numbers)

def normalize_phone(num:str) -> str:

    form_num = "+380" + re.sub(r"\D", "", num)[-9:]

    return  form_num



date_r = "2027-10-09"
print(get_days_from_today(date_r))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
