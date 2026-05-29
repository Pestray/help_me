# паттерны для разных валидаций
# r'^[\w\.-]+@[\w\.-]+\.\w+$' - почта
# r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$' - телефон для формата +7(999)123-45-67
# r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$' - пароль 8 символов 1 буква 1 цифра
# r'^https?://[\w\.-]+\.\w+$'  - url ссылка
# r'^\d{2}\.\d{2}\.\d{4}$'  - формат даты но не проверяет наличие даты в календаре
# r'^(\d{1,3}\.){3}\d{1,3}$' - ip адресс
# r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$' - mac адрес
# r'^\d{4} \d{6}$' - паспорт

import requests
import re
from tkinter import *
from docx import Document

def get_check():
    url = "http://127.0.0.1:4444/TransferSimulator/fullName"
    a = requests.get(url).json()['value']
    print(a)

    lbl1.config(text = a)
    pattern = r'[а-яА-ЯёЁ]+ [а-яА-ЯёЁ]+ [а-яА-ЯёЁ]+'

    check = re.fullmatch(pattern, a)
    if check != None:
        lbl2.config(text= "Валидные данные")
    else:
        lbl2.config(text= "ФИО содержит запрещенные символы")

def send_result():
    doc = Document("C:/овчинникова/demo_ex/28_05_demo/ТестКейс.docx") #открваем документ
    table = doc.tables[0] #берем первую попавшуюся таблицу
    row = table.add_row().cells #создаем новую строчку

    #аполняем ячейку
    row[0].text = lbl1.cget("text")
    row[1].text = lbl2.cget("text")
    row[2].text = "Успешно"
    doc.save("C:/овчинникова/demo_ex/28_05_demo/ТестКейс.docx")

win = Tk()
win.title("aboba")
win.geometry("600x200")
win.resizable(False, False)

frame1 = Frame(win, bg = "pink")
frame2 = Frame(win, bg = "pink")

lbl1 = Label(frame2, text = "", bg = "pink", font= "Arial, 9")
lbl2 = Label(frame2, text = "", bg = "pink", font= "Arial, 9")

btn1 = Button(frame1, text = "Получить данные", width = 25, command = get_check, bg = "pink", font= "Arial, 9")
btn2 = Button(frame1, text = "Отправить результат теста", width = 25, bg = "pink", font= "Arial, 9", command= send_result)

frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=2)
frame2.pack(side=RIGHT, fill=BOTH, expand=True, padx= 2)
lbl1.grid(row = 0, column = 1, padx=10, pady=10)
lbl2.grid(row = 1, column = 1, padx=10, pady=10)
btn1.grid(row = 0, column = 0, padx=10, pady=10)
btn2.grid(row = 1, column = 0, padx=10, pady=10)

win.mainloop()
