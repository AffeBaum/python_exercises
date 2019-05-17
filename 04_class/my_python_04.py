# -*- coding: utf-8 -*-
import unittest
import re

class Bot():

    def __init__(self, owner_name):
        self.pattern = re.compile("Hi,.*"+owner_name)

    def reply(self, call):
        if self.pattern.match(call):
            return "Hello my Boss!"
        else:
            return "Hello"


class TestBot(unittest.TestCase):

    def test_bot_reply(self):
        bot = Bot("Angy")
        self.assertEqual("Hello", bot.reply("Hi, I'm Bill.'"))
        self.assertEqual("Hello my Boss!", bot.reply("Hi, I'm Angy."))


if __name__ == "__main__":
    unittest.main()