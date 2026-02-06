from pathlib import Path

def total_salary(path: str, type_read:str = 'r', encoding: str = 'utf-8') -> dict:
    p = Path(path)
    if p.exists():
        with open(path, type_read, encoding=encoding) as file:
            salary_list = [
                int(line.strip().split(',')[1])
                for line in file
                if line.strip()
            ]

        total_salary  = sum(salary_list)
        avg_salary = round(total_salary / len(salary_list))

        return total_salary, avg_salary

    print("Файл не знайденно ")
    return 0, 0