#!/usr/bin/python3
import traceback
from keywords.defaultKeywords import KeywordFailed
import colorful
import keywords.defaultKeywords


class superPlan:

    def __init__(self):
        self.default = keywords.defaultKeywords.DefaultKeywords()

    def test(self):
        exitCode = 2
        try:
            self.executeKeywords()
            print(self.planName + ": " + colorful.green("SUCCESS"))
            exitCode = 0
        except KeywordFailed as e:
            print(self.planName + ": " + colorful.red("FAILED") + "\n" + str(e))
            exitCode = 1
            self.default.closeBrowser()
        except Exception:
            print(self.planName + ": " + colorful.black("ERROR"))
            traceback.print_exc()
            self.default.closeBrowser()
        finally:
            return exitCode

    def executeKeywords(self):
        print("WARNING: Empty Plan")
        pass

    def setName(self, name):
        self.planName = name
