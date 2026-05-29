from tkinter import *
import psycopg2
from PIL import Image, ImageTk
from tkinter import messagebox


def connect_db(login, password):
    conn = psycopg2.connect(
        dbname="module4",
        host="localhost",
        user="postgres",
        password="1111",
        port="5433"
    )
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE login = %s and password = %s"
    cursor.execute(query, (login, password))
    return cursor.fetchall()


win = Tk()
win.title("aboba")
win.geometry("500x300")

def auth():
    global try_count
    login = login2.get()
    password = password2.get()
    if login and password:
        data = connect_db(login, password)
        print(data)
        if data:
            if count_captch == 3:#Проверяем нашлось ли совпадение логина и пароля
                if data[0][4] == True: # Проверяем не заблокирован ли пользователь
                    messagebox.showerror("Заблокирован", "Ты запломбирован!!!")
                else:
                    messagebox.showinfo("Успешно", f"Вы авторизовались под {data[0][3]}")
            else:
                messagebox.showinfo("каптча неправильная")
        else:
            if try_count == 3: #Проверка на попытки входа
                try_count = 0
                messagebox.showerror("Блокировка", "Заблокирован за 3 неправильные попытки")
            else:
                messagebox.showerror("Неверные данные", "Ты че нас взломать удумал?")
                try_count += 1
    else:
        messagebox.showerror("Ошибка!!!", "Заполните все поля!")

def mixer():
    global count_captch
    count_captch = count_captch % 4

    img = [[img2, img3, img1, img4],
           [img3, img1, img2, img4],
           [img1, img2, img3, img4],
           [img4, img2, img3, img1]]

    # Исправлено: вызываем config у конкретных лейблов
    label1.config(image=img[count_captch][0])
    label2.config(image=img[count_captch][1])
    label3.config(image=img[count_captch][2])
    label4.config(image=img[count_captch][3])

    count_captch += 1


try_count = 0
count_captch = 0

# фреймы создаем
frame_auth = Frame(win, bg="pink")
frame_captcha = Frame(win, bg="pink")

# авторизация
login = Label(frame_auth, text="Логин", bg="pink")
password = Label(frame_auth, text="Пароль", bg="pink")
btn = Button(frame_auth, text="ok", bg="pink", command=auth)

login2 = Entry(frame_auth)
password2 = Entry(frame_auth)

login.pack(anchor=CENTER, pady=5)
login2.pack(anchor=CENTER, pady=5)
password.pack(anchor=CENTER, pady=5)
password2.pack(anchor=CENTER, pady=5)
btn.pack(anchor=CENTER, pady=10)

# каптча
img1 = ImageTk.PhotoImage(Image.open("/19_06_demo/1.png"))
img2 = ImageTk.PhotoImage(Image.open("/19_06_demo/2.png"))
img3 = ImageTk.PhotoImage(Image.open("/19_06_demo/3.png"))
img4 = ImageTk.PhotoImage(Image.open("/19_06_demo/4.png"))

# Сохраняем ссылки на лейблы
label1 = Label(frame_captcha, image=img1)
label2 = Label(frame_captcha, image=img2)
label3 = Label(frame_captcha, image=img3)
label4 = Label(frame_captcha, image=img4)

label1.grid(row=0, column=0, padx=1)
label2.grid(row=0, column=1, pady=1)
label3.grid(row=1, column=0, padx=1)
label4.grid(row=1, column=1, pady=1)

btn_mix = Button(frame_captcha, text="Перемешать", command=mixer)
btn_good = Button(frame_captcha, text="Готово")

btn_good.grid(row=5, column=0)
btn_mix.grid(row=5, column=1)

# управляем фреймами (после добавления всех элементов!)
frame_auth.pack(side=LEFT, fill=BOTH, expand=True, padx=10)
frame_captcha.pack(side=RIGHT, fill=BOTH, expand=True, padx=10)

win.mainloop()