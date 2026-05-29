import json
import csv

# открываем JSON
with open('C:/овчинникова/demo_ex/19_06_demo/Заказчики.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# получаем названия колонок
headers = data[0].keys()

# создаём CSV
with open('clients.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=';')
    writer.writeheader()

    for row in data:
        writer.writerow(row)

print("Файл успешно конвертирован в CSV")