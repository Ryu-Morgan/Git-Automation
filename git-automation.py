# Description: This program helps automate the process of creating a new branch and committing changes
# Name: Ryu Morgan
# Language: Python3

import subprocess
from sys import argv

class gitAutomation:
    def __init__(self):
        self.branch_name = argv[1]
        self.commit_message = argv[2]


    # Method to create a new branch
    def createNewBranch(self):
        subprocess.run(["git","checkout","-b",self.branch_name])
        

    # Method to commit changes
    def commitChanges(self):
        subprocess.run(["git","add","."])
        subprocess.run(["git", "commit", "-m", self.commit_message])


    # Method to push changes to remote repository
    def pushChanges(self):
        subprocess.run(["git","push","origin",self.branch_name])
        

if __name__ == "__main__":
    # init GitAutomation class
    automate = gitAutomation()
    # Create new branch
    automate.createNewBranch()
    # commit changes
    automate.commitChanges()
    # push changes
    automate.pushChanges()


