import unittest

from jira import Issue

from dymo_kanban_labels.lib import jira_api


class TestJiraAPI(unittest.TestCase):
    def test_get_issue(self):
        issue = jira_api.get_issue("DKL-2")
        print issue
        self.assertEqual(Issue, type(issue))
        self.assertEqual(issue.key, "DKL-2")


if __name__ == '__main__':
    unittest.main()
