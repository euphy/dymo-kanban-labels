from flask import Flask

from dymo_kanban_labels.lib import jira_api

app = Flask(__name__)


@app.route("/")
def hello():
    return "You have contacted the DKL."


@app.route("/api/print/issue/<issue_id>")
def print_issue(issue_key):
    # Look up issue from JIRA
    issue = jira_api.get_issue(issue_key=issue_key)

    # Load jira_issue.label from Dymo Label Software (DLS)
    # Condense JIRA info
    # Put JIRA into into label
    # Enumerate and contact label printer
    # Print label

    return "Print issue %s" % issue_key


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')  # Listen on all public IPs
