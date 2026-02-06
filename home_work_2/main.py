from progres import total_salary

FILE_NAME = 'info.txt'
total, average  = total_salary(FILE_NAME)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")