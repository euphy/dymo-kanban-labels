from jira import JIRA

from dymo_kanban_labels.lib import user


def get_issue(issue_key):
    """ Will contact JIRA and retrieve data for a particular named issue. """

    jira = JIRA(server='http://uptomuch.atlassian.net',
                basic_auth=(user.USERNAME, user.PASSWORD))
    issue = jira.issue(issue_key)
    return issue

