from enum import Enum

class GitHubResource(Enum):
"""GitHub CLI resource types used by GitHubWrapper."""
    WORKFLOWS = "workflow"
    RELEASES = "release"
    ISSUES = "issue"
    PULL_REQUESTS = "pr"
    REPOSITORIES = "repo"
    WORKFLOWRUNS = "run"
    GISTS = "gist"
    LABLES = "lable"
    SECRETS = "secret"
    PROJECTS = "project"
    ORGANIZATIONS = "org"
    BRANCHES = "branch"
