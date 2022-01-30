import unittest

import messages_store
from .gbook import Gbook


class GbookTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.gbook = Gbook()

    def test_read_messages(self):
        self.gbook.read_messages(admin=True)
        self.gbook.read_messages(admin=False)
    def test_save_delete_message(self):
        # save
        old_len = len(messages_store.by_date())
        time_at = self.gbook.save_message('TestName', 'test@gmail.com', 'Hello!')
        new_len = len(messages_store.by_date())
        self.assertEqual(old_len + 1, new_len)

        # delete
        self.gbook.delete_message(time_at)
        self.assertEqual(old_len, len(messages_store.by_date()))


    def test_test_del_by_timestamp(self):
        time_at = self.gbook.save_message('t', '12', 'hello!')
        self.gbook.delete_message(int(time_at.timestamp()))

    def test_del_by_strange(self):
        time_at = self.gbook.save_message('t', 't', 't')
        self.gbook.delete_message(str(time_at))


    def test_save_message_empty(self):
        self.gbook.save_message('TestName', '', 'Hello!')