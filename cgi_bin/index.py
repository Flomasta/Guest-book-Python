#!C:\Users\floma\AppData\Local\Programs\Python\Python310\python.exe
import cgitb,json
from os import environ
from http import cookies
from gbook import Gbook

#отладчик
cgitb.enable()
# Устанавливаем куки
cookie = cookies.SimpleCookie()
cookie['name'] = 'Mike'
cookie['name']['httponly'] = 1
# передаём заголовки
print(cookie.output())
print('Content-Type: text/html; charset =  utf-8\n')

MY_FILE = r"..\..\gbook\templates\messages.json"
# get для словаря  в  случае  отсутствия элемента  вернёт None, а не exception с ошибой KeyError
getting_cookie = environ.get('HTTP_COOKIE')
getting_cookie = cookies.SimpleCookie(getting_cookie)
getting_cookie_str = getting_cookie.get("name").value
json.dump(getting_cookie_str, open(MY_FILE, 'w', encoding='utf-8'))

print(json.load(open(MY_FILE, 'r', encoding='utf-8')))

print(Gbook.LOGIN,Gbook.PASSWORD,Gbook.CONTENT_TEMPLATE)
