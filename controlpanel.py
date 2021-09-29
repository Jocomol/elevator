#!/usr/bin/python3 -B
from pydoc import locate
import argparse
from os.path import isfile, join, isdir
from os import listdir


parser = argparse.ArgumentParser(description="WIP")
parser.add_argument("-S", "--shabbat", help="Shabbat mode, do all stories automatically", default=False, action="store_true")
parser.add_argument("-r", "--redo", help="redo failed stories", default=False, action="store_true")  # add function
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
    if args.shabbat:
        stories = loadStories(listdir("."))
    else:
        stories = loadStories(args.stories)
    for story in stories:  # TODO sort for orderly execution
        try:
            story = story.strip(".").split(".")[0].replace("/", ".").strip(".")
            exitCode = locate(story + ".Story")().test()
            if exitCode > 0:
                failedStories.append(story)
        except TypeError:
            pass
    for story in failedStories:
        print(story)  # TODO Add to env variable


if __name__ == "__main__":
    main()
