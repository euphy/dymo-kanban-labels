from dymo_kanban_labels.lib.jira_api import get_issue
from dymo_kanban_labels.lib.dymo import JiraLabel

def get_jl(key):
    issue = get_issue(key)
    jl = JiraLabel(issue)
    return jl

