#Requirements

1. PyQt5
2. QtLinguist or PyQt5 Tools (install with `sudo apt-get install qttools5-dev-tools`)


#Creation of .ts files

To update the translation run the command <br>
`pylupdate5 warframeAlert.pro` <br>
in the project directory to create the translation files.

#Creation of .qm files
To create the transation file for release run the command <br>
`lrelease warframeAlert.pro` <br>
in the project directory to create the .qm files.
Otherwie, you can use the QLinguist tool (open the file and release).
