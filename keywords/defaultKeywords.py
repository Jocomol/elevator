#!/usr/bin/python3
from selenium import webdriver
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
    def __init__(self, element):
        super().__init__("element: \"" + element + "\" is not visible")


class TextNotMatching(KeywordFailed):
    def __init__(self, element, selector, expectedText, actualText):
        super().__init__("element: \"" + element + "\" with selector: \"" + selector + "\" doesn't have the expected text: \"" + expectedText + "\" but the text: \"" + actualText + "\".")


class DefaultKeywords:

    browser = None

    def openBrowser(self, headless=False):
        fireFoxOptions = webdriver.FirefoxOptions()
        if headless:
            fireFoxOptions.set_headless()
        self.browser = webdriver.Firefox(firefox_options=fireFoxOptions)

    def openUrl(self, url):
        if self.browser is not None:
            self.browser.get(url)
        else:
            raise BrowserNotRunning

    def closeBrowser(self):
        self.browser.close()

    def selectElement(self, selector):
        selectorValue = selector.split("=")[1]
        selector = selector.split("=")[0]
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
            elif selector == "tag":
                element = self.browser.find_element_by_tag(selectorValue)
        except NoSuchElementException:
            raise ElementNotFound(selectorValue, selector)
        else:
            return element, selectorValue, selector

    def findAndClickElement(self, selector):
        self.selectElement(selector)[0].click()

    def clickElement(self, element):
        element.click()

    def findAndCheckIfVisible(self, selector):
        element, selectorValue, selector = self.selectElement(selector)
        if not element.is_displayed():
            raise ElementFoundButNotVisible(selectorValue, selector)

    def elementIsVisible(self, element):
        if not element.is_displayed():
            raise ElementNotVisible(element.text)

    def findAndGetText(self, selector):
        return self.selectElement(selector)[0].text

    def getText(self, element):
        return element.text

    def checkText(self, selector, expectedText):
        element, selectorValue, selector = self.selectElement(selector)
        if element.text != expectedText:
            raise TextNotMatching(self, element, selectorValue, expectedText, element.text)

    def sleep(self, seconds):
        time.sleep(seconds)
