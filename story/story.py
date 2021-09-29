#!/usr/bin/python3 -B
import traceback
from actions.defaultActions import ActionFailed
import colorful
import actions.defaultActions


class superStory:

    def __init__(self):
        self.default = actions.defaultActions.DefaultActions()

    def test(self):
        exitCode = 2
        try:
            self.executeActions()
            print(self.storyName + ": " + colorful.green("SUCCESS"))
            exitCode = 0
        except ActionFailed as e:
            print(self.storyName + ": " + colorful.red("FAILED") + "\n" + str(e))
            exitCode = 1
            self.default.closeBrowser()
        except Exception:
            print(self.storyName + ": " + colorful.black("ERROR"))
            traceback.print_exc()
            self.default.closeBrowser()
        finally:
            return exitCode

    def executeActions(self):
        print("WARNING: Empty Story")
        pass

    def setName(self, name):
        self.storyName = name
