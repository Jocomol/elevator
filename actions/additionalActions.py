#!/usr/bin/python3 -B
from pykeepass import PyKeePass


class AdditionalActions:

    browser = None

    def __init__(self, browser, default, path=None, password=None):
        self.browser = browser
        self.default = default
        if password and path:
            self.loadPasswords(path, password)

    def loadPasswords(self, path, password):
        self.kp = PyKeePass(path, password=password)

    def getUsername(self, title):
        return self.kp.find_entries(title=title, first=True).username

    def getPassword(self, title):
        return self.kp.find_entries(title=title, first=True).password
