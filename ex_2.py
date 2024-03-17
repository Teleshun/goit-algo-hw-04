def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = [{
                "id": line.split(',')[0],
                "name": line.split(',')[1],
                "age": int(line.split(',')[2])
            } for line in file.readlines()]
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