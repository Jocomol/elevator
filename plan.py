#!/usr/bin/python3
import keywords.defaultKeywords
import traceback
from keywords.defaultKeywords import KeywordFailed


try:
    default = keywords.defaultKeywords.DefaultKeywords()
    default.openBrowser()
    default.openUrl("https://www.admin.ch")
    # element, selector = default.selectElement("link_text=Viola Amherd")
    # default.isVisible(element)
    # default.clickElement(element)
    default.findAndCheckIfVisible("link_text=Viola Amherd")
    default.findAndClickElement("link_text=Viola Amherd")
    print("SUCCESS")

except KeywordFailed:
    print("FAILED")
    traceback.print_exc()

except Exception:
    print("ERROR")
    traceback.print_exc()

finally:
    default.closeBrowser()
