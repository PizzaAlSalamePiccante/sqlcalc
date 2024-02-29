import sqlite3
c = sqlite3.connect('data.db')
cur = c.cursor() 

def init():

    cur.execute('CREATE TABLE IF NOT EXISTS users(login TEXT UNIQUE, password TEXT, fullname TEXT)')
    c.commit()
def registration():
    login = input(f'=========================\nВведите логин\n>>> ')
    passwonrd = input(f'=========================\nВведите пароль\n>>> ')
    fullname = input(f'=========================\nВведите ФИО\n>>> ')
    try:
        cur.execute('INSERT INTO users (login, password, fullname) VALUES (?,?,?)', (login, passwonrd, fullname))
        c.commit()
    except sqlite3.IntegrityError:
        print(f"=========================\nПользователь {login} с таким именем уже существует")
def login():
    login = input(f'=========================\nВведите логин\n>>> ')
    password = input(f'=========================\nВведите пароль\n>>> ')
    cur.execute('SELECT login, password, fullname FROM users WHERE login = ? AND password = ?', (login, password))
    user_info = cur.fetchall()
    if user_info:
        for info in user_info:
            print(f'------------------\nДобро пожаловать {info[2]}\n------------------')
            return True
    else: 
        print('=========================\nТакого пользователя не существует')
        return False
