#!/usr/bin/python3
import keywords.defaultKeywords
import traceback
from keywords.defaultKeywords import KeywordFailed


try:
    default = keywords.defaultKeywords.DefaultKeywords()
    default.openBrowser(headless=True)
    default.openUrl("https://www.admin.ch")
    default.findAndCheckIfVisible("link_text", "Viola Amherd")
    default.findAndClickElement("link_text", "Viola Amherd")
    default.findAndCheckIfVisible("h1", "Das Eidgenössische Departement für Verteidigung, Bevölkerungsschutz und Sport (VBS)")
    default.findAndCheckIfVisible("h2", "Wahl in den Bundesrat")
    default.checkText("id", "social_share", "Social share")
    print("SUCCESS")
except KeywordFailed:
    print("FAILED")
    traceback.print_exc()

except Exception:
    print("ERROR")
    traceback.print_exc()

finally:
    default.closeBrowser()
