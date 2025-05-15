import os


def merge_files(input_files, output_file):
    files_info = []
    for filename in input_files:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                files_info.append({
                    'name': os.path.basename(filename),  # Только имя файла (без пути)
                    'line_count': len(lines),
                    'content': lines
                })
        except FileNotFoundError:
            print(f"Файл {filename} не найден! Пропускаем...")

    files_info.sort(key=lambda x: x['line_count'])

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_info in files_info:
            out_file.write(f"{file_info['name']}\n")
            out_file.write(f"{file_info['line_count']}\n")
            out_file.writelines(file_info['content'])


if __name__ == "__main__":
    # Проверяем текущую папку
    print("Текущая папка:", os.getcwd())
    print("Доступные файлы:", os.listdir())

    # Запрашиваем пути у пользователя
    input_files = []
    while True:
        file_path = input("Введите путь к файлу (или 'готово' для завершения): ")
        if file_path.lower() == 'готово':
            break
        input_files.append(file_path)

    output_file = input("Введите имя итогового файла (например, merged.txt): ")

    merge_files(input_files, output_file)
    print(f"Файлы объединены в {output_file}")