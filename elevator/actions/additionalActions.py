#i!/usr/bin/python3 -B
from pykeepass import PyKeePass
from os import popen

class AdditionalActions:

    browser = None

    def __init__(self, browser, default, path=None, password=None, passEntry=None):
        self.browser = browser
        self.default = default
        self.kp = self.loadPasswords(path, password, passEntry)

    def loadPasswords(self, path, password=None, passEntry=None):
        if passEntry:
            password = popen("pass " + passEntry).read().strip("\n")
        return PyKeePass(path, password=password)

    def getUsername(self, title):
        return self.kp.find_entries(title=title, first=True).username

    def getPassword(self, title):
        return self.kp.find_entries(title=title, first=True).password
