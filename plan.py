#!/usr/bin/python3
import keywords.defaultKeywords
default = keywords.defaultKeywords.DefaultKeywords()
default.openBrowser()
default.openUrl("https://www.admin.ch")
default.sleep(5)
default.closeBrowser()
