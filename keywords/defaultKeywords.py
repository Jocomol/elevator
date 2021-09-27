#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class KeywordFailed(Exception):
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class UrlNotOpenedError(KeywordFailed):
    
    def __init__(self, error, message="Url wasn't opened"):
        self.message = message
        super().__init__(self.message + error)

class BrowserNotRunning(KeywordFailed):
    
    def __init__(self, message="Browser is not running"):
        super().__init__(message)

class ElementNotFound(KeywordFailed):

    def __init__(self, element, selector):
        super().__init__("element: \"" + element + "\" with selector: \"" + selector + "\" was not found")

class InvalidArgument(KeywordFailed):

    def __init__(self, argument):
        super().__init__("argument: " + argument + " is invalid, please refer to the documentation")

class ElementFoundButNotVisible(KeywordFailed):
    def __init__(self, element, selector):
        super().__init__("element: \"" + element + "\" with selector: \"" + selector + "\" is not visible")

class ElementNotVisible(KeywordFailed):
    def __init__(self, element, selector):
        super().__init__("element: \"" + element + "\" is not visible")
class DefaultKeywords: 

    browser = None

    def openBrowser(self):
        self.browser = webdriver.Firefox()
    
    def openUrl(self,url):
        if self.browser is not None:
            self.browser.get(url)
        else:
            raise BrowserNotRunning

    def closeBrowser(self):
        self.browser.close()

    def selectElement(self, ID=None, xpath=None, link_text=None, partial_link_text=None, name=None, tag_name=None, css_selector=None, class_name=None):
        element = None
        if ID is not None:
            try:
                element = self.browser.find_element_by_id(ID)
            except NoSuchElementException:
                raise ElementNotFound(ID, "id")
        if xpath is not None:
            try:
                element = self.browser.find_element_by_xpath(xpath)
            except NoSuchElementException:
                raise ElementNotFound(xpath, "xpath")
        if link_text is not None:
            try:
                element = self.browser.find_element_by_link_text(link_text)
            except NoSuchElementException:
                raise ElementNotFound(link_text, "link_text")
        if partial_link_text is not None:
            try:
                element = self.browser.find_element_by_partial_link_text(partial_link_text)
            except NoSuchElementException:
                raise ElementNotFound(ID, "partial_link_text")
        if name is not None:
            try:
                element = self.browser.find_element_by_name(name)
            except NoSuchElementException:
                raise ElementNotFound(name, "name")
        if tag_name is not None:
            try:
                element = self.browser.find_element_by_tag_name(tag_name)
            except NoSuchElementException:
                raise ElementNotFound(tag_name, "tag_name")
        if class_name is not None:
            try:
                element = self.browser.find_element_by_class_name(class_name)
            except NoSuchElementException:
                raise ElementNotFound(class_name, "class_name")
        if css_selector is not None:
            try:
                element = self.browser.find_element_by_css_selector(css_selector)
            except NoSuchElementException:
                raise ElementNotFound(css_selector, "css_selector")
        return element
            
    def findAndClickElement(self, ID=None, xpath=None, link_text=None, partial_link_text=None, name=None, tag_name=None, css_selector=None, class_name=None):
        self.selectElement(ID=ID, xpath=xpath, link_text=link_text, partial_link_text=partial_link_text, name=name, tag_name=tag_name, css_selector=css_selector, class_name=class_name).click()
        
    def clickElement(self, element):
        element.click()

    def findAndCheckIfVisible(self, ID=None, xpath=None, link_text=None, partial_link_text=None, name=None, tag_name=None, css_selector=None, class_name=None):
        if not self.selectElement(ID=ID, xpath=xpath, link_text=link_text, partial_link_text=partial_link_text, name=name, tag_name=tag_name, css_selector=css_selector, class_name=class_name).is_displayed():
            selector = None
            flags = [ID, xpath, link_text, partial_link_text, name, tag_name, css_selector, class_name]
            for flag in flags:
                if not None:
                    selector = flag
            raise ElementFoundButNotVisible(element, flag)

    def elementIsVisible(self, element):
        if not element.is_displayed():
            raise ElementIsNotVisible(element)

    def isVisible(self, path):
        pass
    
    def sleep(self, seconds):
        time.sleep(seconds)
