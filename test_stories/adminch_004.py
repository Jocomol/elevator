#!/usr/bin/python3 -B
import story.story as story


class Story(story.superStory):

    def executeActions(self):
        default = self.default
        default.openBrowser(headless=True)
        self.setName("admin.ch-004")
        default.openUrl("https://www.admin.ch")
        default.findAndCheckIfVisible("link_text", "Vila Amherd")
        default.findAndClickElement("link_text", "Viola Amherd")
        default.findAndCheckIfVisible("h1", "Das Eidgenössische Departement für Verteidigung, Bevölkerungsschutz und Sport (VBS)")
        default.findAndCheckIfVisible("h2", "Wahl in den Bundesrat")
        default.checkText("id", "social_share", "Social share")
        default.closeBrowser()
