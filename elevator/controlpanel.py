#!/usr/bin/python3 -B
import argparse
from os.path import isfile, join, isdir, abspath
from os import listdir
from importlib.machinery import SourceFileLoader


parser = argparse.ArgumentParser(description="WIP")
parser.add_argument("-r", "--redo", help="redo failed stories", default=False, action="store_true")
parser.add_argument("-S", "--shabbat", help="Shabbat mode; executes all stories", default=False, action="store_true")
parser.add_argument("-s", "--stories", type=str, nargs="+", help="Path do to be executed stories", default="")


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
    if args.shabbat:
        stories = loadStories(listdir("."))
    elif args.redo:
        with open("/tmp/failedStories", "r") as f:
            for story in f.read().split(";"):
                stories.append(story)
    else:
        stories = loadStories(args.stories)
    for story in stories:
        exitCode = 2
        try:
            exitCode = SourceFileLoader("storyModule", abspath(story)).load_module().Story().test()
        except AttributeError:
            pass
        if exitCode > 0:
            failedStories.append(story)

    FAILED_STORIES = ""
    for story in failedStories:
        FAILED_STORIES += story + ";"
    with open("/tmp/failedStories", "w") as f:
        f.write(FAILED_STORIES)


main()
