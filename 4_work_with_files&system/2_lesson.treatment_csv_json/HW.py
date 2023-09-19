# import csv                                                  # Чтение и запись csv файлов

# with open("example.csv", "r") as f:
#     reader = csv.reader(f)

#     with open("exmpl.csv", "w") as file:
#         writer = csv.writer(file)

#         for line in reader:
#             writer.writerow(line)



import json                                                    # Работа с json
from random import randint

# with open("data.json", "r") as f:
#     data1 = json.loads(f.read())

#     print(data1)

# with open("dt.json", "w") as file:
#     data2 = json.dump(data1, file)

# with open("dat.json", "w") as file1:
#     file1.write(json.dumps(data1, indent=4))



with open("test.json", "r", encoding="utf-8") as f:             # Указываем кодировку для корректного отображения кириллицы
    data = json.load(f)

    for item in data["members"]:
        del item["age"]
        item["likes"] = randint(100, 500)

    print(data["members"])

with open("test2.json", "w", encoding="utf-8") as file:
    data1 = json.dumps(data, indent=4, ensure_ascii=False)      # Отключаем аскии так же для корректной записи кириллицы без юникода
    file.write(data1)
    print(data1)