#!C:\Users\floma\AppData\Local\Programs\Python\Python310\python.exe
import html
from http import cookies
import cgitb, json
from gbook import Gbook
from os import environ
from cgi import FieldStorage


# отладчик
cgitb.enable()

# Устанавливаем куки
cookie = cookies.SimpleCookie()
cookie['name'] = 'Mike'
cookie['name']['httponly'] = 1
# передаём заголовки
print(cookie.output())
print('Content-Type: text/html; charset =  utf-8\n')

gbook = Gbook()


parameters = FieldStorage()

if environ.get('REQUEST_METHOD') == 'POST':
    if parameters.getvalue('operation') == 'message':
        name = html.escape(parameters.getvalue('name'))
        email = html.escape(parameters.getvalue('email'))
        msg = html.escape(parameters.getvalue('msg'))
        gbook.save_message(name, email, msg)
    elif parameters.getvalue('operation') == 'login':
        login = html.escape(parameters.getvalue('login'))
        password = html.escape(parameters.getvalue('password'))
    elif parameters.getvalue('operation') == 'logout':
        pass
gbook.read_message()
print(gbook.content.format(login_form=gbook.login_form, form=gbook.form, messages=gbook.message))
# MY_FILE = r"..\..\gbook\templates\messages.json"
# get для словаря  в  случае  отсутствия элемента  вернёт None, а не exception с ошибой KeyError
# getting_cookie = environ.get('HTTP_COOKIE')
# getting_cookie = cookies.SimpleCookie(getting_cookie)
# getting_cookie_str = getting_cookie.get("name").value
# json.dump(getting_cookie_str, open(MY_FILE, 'w', encoding='utf-8'))
#
# print(json.load(open(MY_FILE, 'r', encoding='utf-8')))
