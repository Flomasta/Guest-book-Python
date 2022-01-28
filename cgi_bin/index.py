#!C:\Users\floma\AppData\Local\Programs\Python\Python310\python.exe
import html
import os
from http import cookies
import cgitb, json
from gbook import Gbook
from os import environ
from cgi import FieldStorage

# отладчик
cgitb.enable()


# передаём заголовки



gbook = Gbook()
admin = False
parameters = FieldStorage()

if 'HTTP_COOKIE' in os.environ:
    cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE')).get('admin')
    if cookie is not None:
        admin = True
if environ.get('REQUEST_METHOD') == 'POST':
    operation = parameters.getvalue('operation')
    if operation == 'message':
        name = html.escape(parameters.getvalue('name'))
        email = html.escape(parameters.getvalue('email'))
        msg = html.escape(parameters.getvalue('msg'))
        gbook.save_message(name, email, msg)
    elif operation == 'login':
        login = html.escape(parameters.getvalue('login'))
        password = html.escape(parameters.getvalue('password'))
        admin = gbook.login(login, password)

    elif operation == 'logout':
        gbook.logout()
        admin = False

if 'del' in parameters:
    id = parameters.getvalue('del')
    if id:
        gbook.delete_message(id)

gbook.read_message(admin)
print('Content-Type: text/html; charset =  utf-8\n')

print(gbook.content.format(login_form=gbook.login_form, form=gbook.form, messages=gbook.message))
print(parameters)

# MY_FILE = r"..\..\gbook\templates\messages.json"
# get для словаря  в  случае  отсутствия элемента  вернёт None, а не exception с ошибой KeyError
# getting_cookie = environ.get('HTTP_COOKIE')
# getting_cookie = cookies.SimpleCookie(getting_cookie)
# getting_cookie_str = getting_cookie.get("name").value
# json.dump(getting_cookie_str, open(MY_FILE, 'w', encoding='utf-8'))
#
# print(json.load(open(MY_FILE, 'r', encoding='utf-8')))
