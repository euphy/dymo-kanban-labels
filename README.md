# dymo-kanban-labels
Use a Dymo Labelwriter 450 to print your sprint.

A scrummaster might spend a long time writing out neat cards for the Scrum board. This will be a way of harvesting a sprint's-worth of issues from JIRA and printing them all off onto labels.

You can stick the labels where you like. I like dry-wipeable magnetic plastic sheet.

This will involve:

* Collecting user input to specify the issue (or issues) to print
* Accessing JIRA to collect the ticket information
* Condensing the ticket information
* Formatting the information into a printable layout
* Initialising the label printer
* Printing the labels
* Partying

Install pywin32 with

    easy_install pywin32-219.win32-py2.7.exe

Or use a different "bitted-ness" or python version chosen from
http://sourceforge.net/projects/pywin32/files/pywin32/

