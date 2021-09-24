#!/usr/bin/python3
from selenium import webdriver
import time

class DefaultKeywords: 

    browser=None

    def openBrowser(self):
        self.browser = webdriver.Firefox()
        return True
    
    def openUrl(self,url):
        if self.browser is not None:
            self.browser.get(url)
            return True
        else:
            return False

    def closeBrowser(self):
        self.browser.close()
        return True
    
    def sleep(self, seconds):
        time.sleep(seconds)
        return True
