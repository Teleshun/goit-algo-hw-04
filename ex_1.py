def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total_salary += int(salary)
                    num_developers += 1
                except ValueError:
                    print(f"Неправильний формат рядка у файлі: {line.strip()}")

        if num_developers == 0:
            return 0, 0  # у випадку, якщо у файлі не має даних

        average_salary = total_salary / num_developers
        return total_salary, average_salary
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("/Users/mariateleshun/Desktop/hm2/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")