#!/usr/bin/python3 -B
import argparse
from os.path import isfile, join, isdir, abspath
from os import listdir
from importlib.machinery import SourceFileLoader
import logging


parser = argparse.ArgumentParser(description="WIP")
parser.add_argument("-r", "--redo", help="redo failed stories", default=False, action="store_true")
parser.add_argument("-S", "--shabbat", help="Shabbat mode; executes all stories", default=False, action="store_true")
parser.add_argument("-s", "--stories", type=str, nargs="+", help="Path do to be executed stories", default="")
parser.add_argument("-l", "--log", type=str, help="Path of log file", default="./elevator.log")


def loadStories(paths):
    stories = []
    story_paths = []
    for path in paths:
        if isdir(path):
            for story in loadDirectory(path):
                story_paths.append(story)
        elif isfile(path):
            story_paths.append(path)
    for path in story_paths:
        if isfile(path):
            stories.append(path)
    cleaned_stories = stories[:]
    for story in stories:
        if "__pycache__" in story or "__init__.py" in story or ".py" not in story:
            cleaned_stories.remove(story)
    return cleaned_stories

def loadDirectory(directory):
    story_paths = []
    for item in listdir(directory):
        filePath = join(directory, item)
        if isfile(filePath):
            story_paths.append(filePath)
        elif isdir(filePath):
            for story in loadDirectory(filePath):
                story_paths.append(story)
    return story_paths

def main():
    failedStories = []
    args = parser.parse_args()
    stories = []
    logging.basicConfig(filename=args.log, filemode="w", level=logging.DEBUG)
    logging.debug("Logging started")
    if args.shabbat:
        stories = loadStories(listdir("."))
        logging.debug("Found files: " + str(stories))
    elif args.redo:
        logging.debug("redo enabled")
        with open("/tmp/failedStories", "r") as f:
            for story in f.read().split(";"):
                logging.debug("added story " + story + " to the to be executed stories")
                stories.append(story)
    else:
        logging.debug("Using: " + str(args.stories))
        stories = loadStories(args.stories)

    logging.info("The following stories will be executed: " + str(stories))

    for story in stories:
        exitCode = 2
        try:
            logging.info("Started:" + story)
            storyObject = SourceFileLoader("storyModule", abspath(story)).load_module().Story()
            exitCode = storyObject.test()
        except (AttributeError, ValueError):
            logging.debug(story + " is not a story")

        if exitCode > 0:
            failedStories.append(story)

    FAILED_STORIES = ""
    for story in failedStories:
        FAILED_STORIES += story + ";"
    with open("/tmp/failedStories", "w") as f:
        f.write(FAILED_STORIES)


main()
