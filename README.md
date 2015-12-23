# Dymo Kanban Labels

Use a Dymo Labelwriter 450 to print your sprint.

A scrummaster might spend a long time writing out neat cards for the Scrum board. This project shows a  way of collecting a sprint's-worth of issues from JIRA and printing them all off onto labels.

You can stick the labels where you like. I like dry-wipeable magnetic plastic sheet.

Dymo labels are well-behaved, peel off easily and don't leave residual glue.

First versions look like this:

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/euphy/23825207382/in/dateposted-public/" title="JIRA to Dymo label printing: Epic and Story"><img src="https://farm6.staticflickr.com/5823/23825207382_fdc20ab4b9.jpg" width="500" height="375" alt="JIRA to Dymo label printing: Epic and Story"></a>

## Bad news

Dymo provide an SDK that requires the Dymo Label Software (DLS) to be installed.  This currently is available for
Windows and MacOS only. On both cases it requires OS-specific work to access (COM in Windows), so this project is
for Windows only.

There are CUPS drivers for Linux, so I guess the label could be built as postscript and fired off that way.
Little more work, and besides I'm developing on Windows right now. It's the holidays, give me a break.


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


## Usage

Run dkl.py, it'll start a web server.


    GET localhost:5000/api/print/issue/<JIRA key>

And check out dkl.py for a couple of other routes. I've just realised I've not committed some nice changes, so that'll happen after Christmas.
