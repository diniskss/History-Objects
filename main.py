from tkinter import *
from tkinter import ttk
import threading 
import time
import mysql.connector as mariadb
from mysql.connector import Error
import json


#Чтение из файла bd_login.json данных для получения доступа к БД
with open("bd_login.json", "r") as my_file:
	bd_login_json = my_file.read()
	
bd_login = json.loads(bd_login_json)

try:
    connection = mariadb.connect(user=bd_login["user"],
    password=bd_login["password"],
    database=bd_login["database"],
    host=bd_login["host"],
    port=bd_login["port"])
        
    print('Подключение к базе данных выполнено успешно')
except Error as error:
    print(f'Ошибка подключения к БД: {error}')

def execute_read_query(connection_bd, query):
    cursor = connection_bd.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

#def update_table(): 
#    time.sleep(0.2) # имитируем выполнение долгой задачи
#    try:
#		tree.insert("", END, values=person)
#	except Error as error:
#		print(f'Ошибка обновления таблицы: {error}')
#	threading.Thread(target=task).start() 

#def Programm():
    #program = Tk()
    #program.geometry("1000x500")
    #program.title('ИС Исторические объекты')
    #program.resizable(False, False)
    #program.protocol("WM_DELETE_WINDOW", finish)
    #program['bg'] = 'black'

	# определяем данные для отображения
	#table = [(), (), ()]
	 
	# определяем столбцы
	#columns = ("id", "name", "category", "place")
	 
	#tree = ttk.Treeview(columns=columns, show="headings")
	#tree.pack(fill=BOTH, expand=1)
	 
	# определяем заголовки
	#tree.heading("id", text="id")
	#tree.heading("name", text="Имя")
	#tree.heading("category", text="Категория")
	#tree.heading("place", text="Место нахождения")
	 

def Login():
    username = username_entry.get()
    password = user_password_entry.get()
    login_password_from_db = execute_read_query(connection, "SELECT login, password FROM user;")

    for row in login_password_from_db:
        if username == row[0] and password == row[1]:
            print(f'Вы вошли логин {username} и пароль {password}')
            root.destroy()
            Programm()
            return 0
        else:
            print(f'Логин или пароль не подошел')
            incorrect_label = Label(root, text='Логин или пароль неверны', font='Arial 10 ', bg='black', fg='gray',
                                    pady=12)
            incorrect_label.pack()


root = Tk()
root.geometry("300x250")
root.title('ИС Исторические объекты')
root.resizable(False, False)
root['bg'] = 'black'

main_label = Label(root, text='Авторизация', font='Arial 15 bold', bg='black', fg='white')  # Текст авторизация
main_label.pack()

username_label = Label(root, text='Логин', font='Arial 12 bold', bg='black', fg='white', pady=12)  # Текст логин
username_label.pack()

username_entry = Entry(root, font='Arial 12 bold', bg='black', fg='white')  # Поле логин
username_entry.config(insertbackground='white')
username_entry.pack()

user_password_label = Label(root, text='Пароль', font='Arial 12 bold', bg='black', fg='white', pady=12)  # Текст пароль
user_password_label.pack()

user_password_entry = Entry(root, font='Arial 12 bold', bg='black', fg='white')  # Поле пароль
user_password_entry.config(insertbackground='white')
user_password_entry.pack()

send_btn = Button(root, text='Вход', command=Login, font='Arial 12 bold', bg='black', fg='white')  # Кнопка вход
send_btn.pack(pady=8)
root.mainloop()
