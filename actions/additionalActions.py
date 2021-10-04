#!/usr/bin/python3 -B
import actions.defaultActions


class AdditionalActions:

    browser = None

    def __init__(self, browser, default):
        self.browser = browser
        self.default = default

