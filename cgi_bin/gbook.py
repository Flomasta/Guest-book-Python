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
