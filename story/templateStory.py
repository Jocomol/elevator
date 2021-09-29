#!/usr/bin/python3
import story.story as story


class Story(story.superStory):

    def executeActions(self):
        default = self.default  # not nessecary but very useful if you don't want to write self.default.action everytime when using a default action
        default.openBrowser(headless=True)  # start and configure browser
        self.setName("")  # set a name for distinction in the output
        default.closeBrowser()  # close the browser at the end of the successful execution


Story().test()
