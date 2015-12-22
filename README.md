# Dymo Kanban Labels

Use a Dymo Labelwriter 450 to print your sprint.

A scrummaster might spend a long time writing out neat cards for the Scrum board. This will be a way of harvesting a sprint's-worth of issues from JIRA and printing them all off onto labels.

You can stick the labels where you like. I like dry-wipeable magnetic plastic sheet.


## Bad news

Dymo provide an SDK that requires the Dymo Label Software (DLS) to be installed.  This currently is available for
Windows and MacOS only. On both cases it requires OS-specific work to access (COM in Windows), so this project is
for Windows only.


## Installation

    pip install -r requirements.txt

You may be able to install pywin32 using pip (give it a go), but it doesn't work well with virtualenvs.

Instead, install with:

    easy_install pywin32-219.win32-py2.7.exe

Or use a different "bitted-ness" or python version chosen from
http://sourceforge.net/projects/pywin32/files/pywin32/


## JIRA credentials

DKL uses basic authentication. Put your details into ``lib/user.py``. Harvesting these from the user at runtime
may be a better way of doing this, if batch size can be increased.

