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

def load_label(label_path):
    labelCom = Dispatch('Dymo.DymoAddIn')
    labelText = Dispatch('Dymo.DymoLabels')
    isOpen = labelCom.Open(label_path)
    print isOpen

    selectPrinter = 'DYMO LabelWriter 450'
    labelCom.SelectPrinter(selectPrinter)

    labelText.SetField('issue_key', "TST-123")
    labelText.SetField('TEXT4', )

    labelCom.StartPrintJob()
    labelCom.Print(1, False)
    labelCom.EndPrintJob()

class JiraLabel:
    def __init__(self, issue):
        self.issue = issue

        pythoncom.CoInitialize()

        self.labelCom = Dispatch('Dymo.DymoAddIn')

        label_path = get_label_path(self.issue.fields.issuetype)
        self.isOpen = self.labelCom.Open(label_path)

        print self.isOpen

        self.prepared = False
        self.prepare()

    def __del__(self):
        pythoncom.CoUninitialize()

    def wrap_summary(self, long_line, three_row_line=35, two_row_line=25):
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


    def prepare(self):
        labelText = Dispatch('Dymo.DymoLabels')

        fields = self.issue.fields

        labelText.SetField('issue_key', self.issue.key)
        labelText.SetField('issue_summary', self.wrap_summary(fields.summary, three_row_line=35, two_row_line=25))
        labelText.SetField('issue_description', self.wrap_summary(fields.description,
                                                                  three_row_line=45, two_row_line=35))
        try:
            labelText.SetField('issue_size', fields.customfield_10021.__int__())
        except AttributeError:
            labelText.SetField('issue_size', '')

        if fields.issuetype.name == 'Story':
            labelText.SetField('issue_size_unit', 'sp')
            labelText.SetField('parent_issue_key', fields.customfield_10017)

        elif fields.issuetype.name in ('Task', 'Sub-task', 'Bug'):
            labelText.SetField('issue_size_unit', 'hours')
            labelText.SetField('parent_issue_key', fields.parent.key)

        self.labelText = labelText
        self.prepared = True


    def print_label(self):
        if not self.prepared:
            raise Exception("Label has not been prepared. (Call label.prepare())")

        self.labelCom.SelectPrinter('DYMO LabelWriter 450')
        self.labelCom.StartPrintJob()
        self.labelCom.Print(1, False)
        self.labelCom.EndPrintJob()

    def save_label(self, filename):
        self.labelCom.SaveAs(filename)
        print self
        print filename



