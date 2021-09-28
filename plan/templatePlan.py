#!/usr/bin/python3
import keywords.defaultKeywords
import plan.plan
from keywords.defaultKeywords import KeywordFailed

class Plan(plan.plan.superPlan):
    
    def executeKeywords(self):
        default = keywords.defaultKeywords.DefaultKeywords()
        default.openBrowser(headless=True)
        default.openUrl("")
        default.closeBrowser()

    def __init__(self):
        super().__init__()
        self.setName("planname")
if __name__ == "__main__":
    plan = Plan()
    plan.test()
