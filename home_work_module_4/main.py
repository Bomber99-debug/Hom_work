from utils import total_salary, get_cats_info
from pathlib import Path
from pprint import pprint

def main():
    tabl = f"\n{'-'*100}\n"

    BASE_DIR = Path(__file__).resolve().parent
    FILE_NAME = BASE_DIR / 'info.txt'

    try:
        total, average  = total_salary(FILE_NAME)
        print(f"\nЗагальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(f"Некоректні дані: {e}")
        print(f"Загальна сума заробітної плати: 0, Середня заробітна плата: 0")

    print(tabl)

    FILE_NAME = BASE_DIR / 'cat.txt'
    try:
        cats_info = get_cats_info(FILE_NAME)
        pprint(cats_info)
    except Exception as e:
        print(f"Некоректні дані: {e}")


if __name__ in "__main__":
    main()