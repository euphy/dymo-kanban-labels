from flask import Flask, render_template

from dymo_kanban_labels.lib import jira_api
from dymo_kanban_labels.lib.dymo import JiraLabel

app = Flask(__name__)


@app.route("/")
def home():
    return "You have contacted the DKL."


@app.route("/api/preview/issue/<issue_key>", methods=['GET'])
def preview_issue(issue_key):
    issue = jira_api.get_issue(issue_key=issue_key)
    jl = JiraLabel(issue)
    print "Print issue %s" % jl.label_fields
    return render_template('label_fields.html', label_fields=jl.label_fields)


@app.route("/api/print/issue/<issue_key>", methods=['POST'])
def print_issue(issue_key):
    issue = jira_api.get_issue(issue_key=issue_key)
    jl = JiraLabel(issue)
    jl.save_label("%s.label" % issue_key)
    jl.print_label()

    return "Print issue %s: %s" % (issue_key, issue.__str__())

@app.route("/api/save/issue/<issue_key>", methods=['GET'])
def return_label(issue_key):
    issue = jira_api.get_issue(issue_key=issue_key)
    jl = JiraLabel(issue)
    jl.save_label("%s.label" % issue_key)

    return "Print issue %s: %s" % (issue_key, issue.__str__())


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')  # Listen on all public IPs
