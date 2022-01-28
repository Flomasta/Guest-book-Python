import json
from datetime import datetime
import time


class Gbook:
    LOGIN = 'admin'
    PASSWORD = '123'
    PATH = r"..\..\gbook\templates"
    LOGIN_FORM_TEMPLATE = PATH + "\loginform.tmp"
    FORM_TEMPLATE = PATH + r"\form.tmp"
    CONTENT_TEMPLATE = PATH + "\content.tmp"
    MESSAGE_TEMPLATE = PATH + "\message.tmp"
    NO_RECORDS_TEMPLATE = PATH + r"\no_messages_record.tmp"
    DB = PATH + "\messages.json"

    def __init__(self):
        self.message = ''
        self.content = ''
        self.form = ''
        self.login_form = ''
        self.no_records = ''

        # присваиваем шаблоны элементов сайта переменным
        with open(self.CONTENT_TEMPLATE, 'r', encoding='utf-8') as f:
            self.content = f.read()
        with open(self.FORM_TEMPLATE, 'r', encoding='utf-8') as f:
            self.form = f.read()
        with open(self.NO_RECORDS_TEMPLATE, 'r', encoding='utf-8') as f:
            self.no_records = f.read()
        with open(self.LOGIN_FORM_TEMPLATE, 'r', encoding='utf-8') as f:
            self.login_form = f.read()
        try:
            with open(self.DB, 'r', encoding='utf-8') as f:
                pass
        except FileNotFoundError:
            with open(self.DB, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def read_message(self):
        with open(self.DB, 'r', encoding='utf-8') as f:
            message = json.load(f)
        if not message:
            self.message = self.no_records
            return
        with open(self.MESSAGE_TEMPLATE, 'r', encoding='utf-8') as f:
            message_template = f.read()
            for id in sorted(message.keys(), reverse=True):
                date = datetime.fromtimestamp(int(id)).strftime('%d-%M-%Y %H:%m:%S')
                self.message += message_template.format(datetime=date, msg=message[id]['msg'],email=message[id]['email'], name=message[id]['name'])

    def save_message(self, name, email, message):
        dt = int(time.time())
        with open(self.DB, 'r', encoding='utf-8') as f:
            m = json.load(f)
        m[dt] = {"name": name, "email": email, "msg": message}
        with open(self.DB, 'w', encoding='utf-8') as f:
            json.dump(m, f)


def delete_message(self, id):
    pass


def login(self, login, password):
    pass


def logout(self):
    pass
