import json


class Gbook:
    LOGIN = 'admin'
    PASSWORD = '123'
    PATH = r"..\..\gbook\templates"
    LOGIN_FORM_TEMPLATE = PATH + "\loginform.tmp"
    FORM_TEMPLATE = PATH + r"\form.tmp"
    CONTENT_TEMPLATE = PATH + "\content.tmp"
    MESSAGE_TEMPLATE = PATH + "\message"
    DB = PATH + "\messages.json"

    def __init__(self):
        self.message = ''
        self.content = ''
        self.form = ''
        self.login_form = ''

        # присваиваем шаблоны элементов сайта переменным
        with open(self.CONTENT_TEMPLATE, 'r', encoding='utf-8') as f:
            self.content = f.read()
        with open(self.FORM_TEMPLATE, 'r', encoding='utf-8') as f:
            self.form = f.read()
        with open(self.LOGIN_FORM_TEMPLATE, 'r', encoding='utf-8') as f:
            self.login_form = f.read()
        try:
            with open(self.DB, 'r', encoding='utf-8') as f:
                pass
        except FileNotFoundError:
            with open(self.DB, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def read_message(self):
        pass

    def save_message(self, name, email, message):
        pass

    def delete_message(self, id):
        pass

    def login(self, login, password):
        pass

    def logout(self):
        pass
