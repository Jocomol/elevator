#!/usr/bin/python3
import keywords.defaultKeywords
import plan.plan
from keywords.defaultKeywords import KeywordFailed

class Plan(plan.plan.superPlan):
    
    def executeKeywords(self):
        default = keywords.defaultKeywords.DefaultKeywords()
        default.openBrowser(headless=True)
        default.openUrl("https://www.admin.ch")
        default.findAndCheckIfVisible("link_text", "Viola Amherd")
        default.findAndClickElement("link_text", "Viola Amherd")
        default.findAndCheckIfVisible("h1", "Das Eidgenössische Departement für Verteidigung, Bevölkerungsschutz und Sport (VBS)")
        default.findAndCheckIfVisible("h2", "Wahl in den Bundesrat")
        default.checkText("id", "social_share", "Social share")
        default.closeBrowser()

    def __init__(self):
        super().__init__()
        self.setName("admin.ch-001")
if __name__ == "__main__":
    plan = Plan()
    plan.test()
