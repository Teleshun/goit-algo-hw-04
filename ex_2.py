def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cats_info.append({
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2].strip()  # Retaining age as a string
                    })
                else:
                    print("Невірний формат рядка:", line)


    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except (IndexError, ValueError) as e:
        print("Помилка при обробці файлу:", e)
        return []
    except Exception as e:
        print("Невідома помилка:", e)
        return []
    
    return cats_info

cats = get_cats_info("/Users/mariateleshun/Desktop/hm2/cats_information.txt")
print(cats)
