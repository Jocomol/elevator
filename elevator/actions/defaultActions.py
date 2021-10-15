#!/usr/bin/python3 -B
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time


class ActionFailed(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UrlNotOpenedError(ActionFailed):

    def __init__(self, error, message="Url wasn't opened"):
        self.message = message
        super().__init__(self.message + error)


class BrowserNotRunning(ActionFailed):

    def __init__(self, message="Browser is not running"):
        super().__init__(message)


class ElementNotFound(ActionFailed):

    def __init__(self, element, selector):
        super().__init__("element: \"" + element + "\" with selector: \"" + selector + "\" was not found")


class InvalidArgument(ActionFailed):

    def __init__(self, argument):
        super().__init__("argument: " + argument + " is invalid, please refer to the documentation")


class ElementFoundButNotVisible(ActionFailed):
    def __init__(self, element, selector):
        super().__init__("element: \"" + element + "\" with selector: \"" + selector + "\" is not visible")


class ElementNotVisible(ActionFailed):
    def __init__(self, element):
        super().__init__("element: \"" + element + "\" is not visible")


class TextNotMatching(ActionFailed):
    def __init__(self, selector, selectorValue, expectedText, actualText):
        super().__init__("element: \"" + selectorValue + "\" with selector: \"" + selector + "\" doesn't have the expected text: \"" + expectedText + "\" but the text: \"" + actualText + "\".")


class DefaultActions:

    browser = None

    def openBrowser(self, headless=False):
        options = Options()
        options.headless = headless
        self.browser = webdriver.Firefox(options=options)

    def openUrl(self, url):
        if self.browser is not None:
            self.browser.get(url)
        else:
            raise BrowserNotRunning

    def closeBrowser(self):
        self.browser.close()

    def selectElement(self, selector, selectorValue):
        element = None
        try:
            if selector == "id":
                element = self.browser.find_element_by_id(selectorValue)
            elif selector == "xpath":
                element = self.browser.find_element_by_xpath(selectorValue)
            elif selector == "link_text":
                element = self.browser.find_element_by_link_text(selectorValue)
            elif selector == "partial_link_text":
                element = self.browser.find_element_by_partial_link_text(selectorValue)
            elif selector == "name":
                element = self.browser.find_element_by_name(selectorValue)
            elif selector == "class_name":
                element = self.browser.find_element_by_class_name(selectorValue)
            elif selector == "css_selector":
                element = self.browser.find_element_by_css_selector(selectorValue)
            else:
                elements = self.browser.find_elements_by_tag_name(selector)
                for potentialElement in elements:
                    if potentialElement.text == selectorValue:
                        element = potentialElement
        except NoSuchElementException:
            raise ElementNotFound(selectorValue, selector)
        else:
            if element is None:
                raise ElementNotFound(selectorValue, selector)
            return element, selectorValue, selector

    def findAndClickElement(self, selector, selectorValue):
        self.selectElement(selector, selectorValue)[0].click()

    def clickElement(self, element):
        element.click()

    def findAndCheckIfVisible(self, selector, selectorValue):
        element, selectorValue, selector = self.selectElement(selector, selectorValue)
        if not element.is_displayed():
            raise ElementFoundButNotVisible(selectorValue, selector)

    def elementIsVisible(self, element):
        if not element.is_displayed():
            raise ElementNotVisible(element.text)

    def findAndGetText(self, selector, selectorValue):
        return self.selectElement(selector, selectorValue)[0].text

    def getText(self, element):
        return element.text

    def checkText(self, selector, selectorValue, expectedText):
        element, selectorValue, selector = self.selectElement(selector, selectorValue)
        if element.text != expectedText:
            raise TextNotMatching(selector, selectorValue, expectedText, element.text)

    def write(self, selector, selectorValue, text):
        element, selectorValue, selector = self.selectElement(selector, selectorValue)
        element.send_keys(text)

    def getSource(self):
        print(self.browser.page_source)

    def sleep(self, seconds):
        time.sleep(seconds)
