#!/usr/bin/python3
import traceback
from keywords.defaultKeywords import KeywordFailed

class supersuperPPlan:
    
    browser = None
    
    planName = None
    
    def test(self):
        exitCode = 2
        try:
            self.executeKeywords()
            print("SUCCESS")
            exitCode = 0
        except KeywordFailed as e:
            print(str(e))
            print("FAILED")
            exitCode = 1
        except Exception:
            traceback.print_exc()
            print("ERROR")
        finally:
            return exitCode
    
    def executeKeywords(self):
        print("WARNING: Empty Plan")
        pass

    def setName(self, name):
        planName = name

    def setBrowser(self, browser):
        self.browser = browser
