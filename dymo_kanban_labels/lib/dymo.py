import sys
import textwrap
from os import path
from datetime import datetime, timedelta
from win32com.client import Dispatch
import pythoncom


def get_label_path(issue_type):
    current_dir = None
    if getattr(sys, 'frozen', False):
        # frozen
        current_dir = path.dirname(sys.executable)
    else:
        # unfrozen
        current_dir = path.dirname(path.abspath(__file__))

    print "Current dir: %s" % current_dir

    if issue_type.name == 'Story':
        label_filename = 'jira_story.label'
    elif issue_type.name in ('Sub-task', 'Task'):
        label_filename = 'jira_task.label'

    print label_filename
    label_path = path.join(current_dir, '..', 'labels', label_filename)

    if not path.isfile(label_path):
        raise IOError("%s is not a file" % label_path)
    else:
        return label_path

def wrap_summary(long_line, three_row_line=35, two_row_line=25):
    l = len(long_line)

    if (l > (three_row_line * 3)):
        long_line = long_line[0:(three_row_line*3)]
        l = len(long_line)

    if (l <= (three_row_line * 3)) and (l > (two_row_line * 2)):
        wrapped = "\n".join(textwrap.wrap(long_line, width=three_row_line)[0:3])
    elif (l <= (two_row_line * 2)) and (l > two_row_line):
        wrapped = "\n".join(textwrap.wrap(long_line, width=two_row_line)[0:2])
    else:
        wrapped = long_line
    return wrapped


def prepare_label_fields(issue):
    label_fields = {
        'issue_key': issue.key,
        'issue_summary': wrap_summary(issue.fields.summary, three_row_line=35, two_row_line=25),
        'issue_description': wrap_summary(issue.fields.description, three_row_line=45, two_row_line=35),
        'issue_size': '',
        'issue_type': issue.fields.issuetype.name
    }

    try:
        label_fields['issue_size'] = issue.fields.customfield_10021.__int__()  # Story points
    except AttributeError:
        pass

    if issue.fields.issuetype.name == 'Story':
        label_fields['issue_size_unit'] = 'sp'
        label_fields['parent_issue_key'] = issue.fields.customfield_10017

    elif issue.fields.issuetype.name in ('Task', 'Sub-task', 'Bug'):
        label_fields['issue_size_unit'] = 'hours'
        label_fields['parent_issue_key'] = issue.fields.parent.key

    return label_fields


class JiraLabel:
    def __init__(self, issue):
        pythoncom.CoInitialize()
        self.issue = issue
        self.label_com = Dispatch('Dymo.DymoAddIn')
        label_path = get_label_path(self.issue.fields.issuetype)
        self.isOpen = self.label_com.Open(label_path)
        self.label_fields = prepare_label_fields(self.issue)
        self.label = self.complete_label(self.label_fields)

    def __del__(self):
        pythoncom.CoUninitialize()

    def print_label(self):
        print "Printed label"
        exit()

        if not self.label:
            raise Exception("Label has not been prepared. Nothing to print.")

        self.label_com.SelectPrinter('DYMO LabelWriter 450')
        self.label_com.StartPrintJob()
        self.label_com.Print(1, False)
        self.label_com.EndPrintJob()

    def save_label(self, filename):
        success = self.label_com.SaveAs(filename)
        print filename
        return success

    def complete_label(self, label_fields):
        label = Dispatch('Dymo.DymoLabels')
        for k in label_fields:
            label.SetField(k, label_fields[k])

        return label



