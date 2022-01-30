from datetime import datetime
from http import cookies
import time

import dateutil.parser

import templates
import messages_store

class Gbook:
    LOGIN = 'admin'
    PASSWORD = '123'

    def read_messages(self, admin):
        if not messages_store.messages:
            return templates.no_messages

        _rendered_messages = ''
        for time, name, email, msg in messages_store.by_date():
            date = time.strftime('%d-%M-%Y %H:%m:%S')
            _rendered_messages += templates.message.format(datetime=date,
                                                           msg=msg,
                                                           email=email,
                                                           name=name)
            if admin:
                _rendered_messages += "<p><a href='index.py?del={}' >Delete</a></p>".format(time)
        return _rendered_messages

    def save_message(self, name, email, message):
        return messages_store.add_message(name, email, message)

    def delete_message(self, time):
        if not isinstance(time, (datetime, int)):
            time  =  dateutil.parser.parse(time)

        messages_store.delete_message(time)


    def login(self, login, password):
        if login == self.LOGIN and password == self.PASSWORD:
            cookie = cookies.SimpleCookie()
            cookie['token'] = "123412341234123412341"
            cookie['admin'] = "1"
            cookie['admin']['httponly'] = "1"
            print(cookie.output())
            return True
        return False

    def logout(self):
        cookie = cookies.SimpleCookie()
        cookie['admin'] = "1"
        cookie['admin']['httponly'] = "1"
        expired = time.gmtime(time.time() - 3600)
        expired = time.strftime("%a,%d %b %Y %T GMT", expired)
        cookie['admin']['expires'] = expired
        print(cookie.output())
