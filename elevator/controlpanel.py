#!/usr/bin/python3 -B
import argparse
from os.path import isfile, join, isdir
from os import listdir
import importlib.util as importer


parser = argparse.ArgumentParser(description="WIP")
parser.add_argument("-S", "--shabbat", help="Shabbat mode, do all stories automatically", default=False, action="store_true")
parser.add_argument("-r", "--redo", help="redo failed stories", default=False, action="store_true")
parser.add_argument("-s", "--stories", type=str, nargs="+", help="Path do to be executed stories", default="")


def loadStories(paths):
    stories = []
    story_paths = []
    for path in paths:
        if isdir(path):
            for item in listdir(path):
                filePath = join(path, item)
                if isfile(filePath):
                    story_paths.append(filePath)
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
        storyFile = importer.spec_from_file_location("storyFile", story)
        storyClass = importer.module_from_spec(storyFile)
        exitCode = storyFile.loader.exec_module(storyClass)
        if exitCode > 0:
            failedStories.append(story)

    FAILED_STORIES = ""
    for story in failedStories:
        FAILED_STORIES += story + ";"
    with open("/tmp/failedStories", "w") as f:
        f.write(FAILED_STORIES)


if __name__ == "__main__":
    main()
