_PATH = r"..\..\gbook\templates"
_LOGIN_FORM_TEMPLATE = _PATH + "\loginform.tmp"
_FORM_TEMPLATE = _PATH + r"\form.tmp"
_CONTENT_TEMPLATE = _PATH + "\content.tmp"
_MESSAGE_TEMPLATE = _PATH + "\message.tmp"
_NO_RECORDS_TEMPLATE = _PATH + r"\no_messages_record.tmp"

# присваиваем шаблоны элементов сайта переменным
with open(_CONTENT_TEMPLATE, 'r', encoding='utf-8') as f:
    content = f.read()
with open(_FORM_TEMPLATE, 'r', encoding='utf-8') as f:
    form = f.read()
with open(_LOGIN_FORM_TEMPLATE, 'r', encoding='utf-8') as f:
    login_form = f.read()
with open(_NO_RECORDS_TEMPLATE, 'r', encoding='utf-8') as f:
    no_messages = f.read()
with open(_MESSAGE_TEMPLATE, 'r', encoding='utf-8') as f:
    message = f.read()

