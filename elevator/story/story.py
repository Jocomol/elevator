#!/usr/bin/python3 -B
import traceback
from elevator.actions.defaultActions import ActionFailed
import colorful
import elevator.actions.defaultActions
from importlib.machinery import SourceFileLoader
from os.path import abspath
import logging


class superStory:

    def __init__(self):
        self.default = elevator.actions.defaultActions.DefaultActions()

    def test(self):
        exitCode = 2
        try:
            logging.debug("Starting execution")
            self.executeActions()
            logging.info(self.storyName + ": " + colorful.green("SUCCESS"))
            print(self.storyName + ": " + colorful.green("SUCCESS"))
            exitCode = 0
        except ActionFailed as e:
            logging.error(self.storyName + ": " + colorful.red("FAILED") + "\n" + str(e))
            exitCode = 1
            self.default.closeBrowser()
        except Exception:
            logging.exception(self.storyName + ": " + colorful.black("ERROR"))
            self.default.closeBrowser()
        finally:
            return exitCode

    def executeActions(self):
        logging.warning("Empty Story")

    def setName(self, name):
        self.storyName = name

    def loadActions(self, path):
        path = abspath(path)
        try:
            actionsClass = SourceFileLoader("actionModule", abspath(path)).load_module().Actions
        except Exception:
            logging.exception("Actions at " + path + " weren't able to be loaded.")
        logging.info("Module at: " + path +  " was loaded")
        return actionsClass
