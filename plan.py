#!/usr/bin/python3
import keywords.defaultKeywords
from keywords.defaultKeywords import * 

try:
    default = keywords.defaultKeywords.DefaultKeywords()
    default.openBrowser()
    default.openUrl("https://www.admin.ch")
    #element = default.selectElement(link_text="Viola Amherd")
    #default.isVisible(element)
    #default.clickElement(element)
    default.findAndCheckIfVisible(link_text="Viola Amherd")
    default.findAndClickElement(link_text="Viola Amherd")
    print("SUCCESS")
except KeywordFailed as e:
    print("FAILED")
    print(str(e))
except Exception as e:
    print("ERROR")
    print(str(e))
finally:
    default.closeBrowser()
    
