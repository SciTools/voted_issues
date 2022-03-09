# Copyright Iris contributors
#
# This file is part of Iris and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
"""
A standalone python script to guery the GitHub API and create a json file
of all voted for issues with their details.

In order for this to run the GH_TOKEN shell variable must be set.
For example::

  export GH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxx

This script can be run from the command line but needs a single non standard
package names GitHub (package to help queiry the GitHub API).
"""

from github import Github
import github
import json
import logging
import os
from pathlib import Path

# set logging level (NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.basicConfig(level=logging.INFO)

GH_TOKEN_NAME = "GH_TOKEN"
OUTPUT_JSON = "voted-issues.json"
ISSUE_RST = ":issue_only:`{number}`"
AUTHOR_RST = ":author:`{author}`"

ISSUE_HREF = "<a href='https://github.com/SciTools/iris/issues/{number}'>#{number}</a>"
AUTHOR_HREF = "<a href='https://github.com/{author}'>@{author}</a>"


def autolog_info(message):
    # Dump the message + the name of this function to the log.
    logging.info(" --> {}".format(message))


gh_token = os.getenv(GH_TOKEN_NAME)

if gh_token is None:
    raise Exception(f"GitHub API: ERROR, {GH_TOKEN_NAME} not set.")

if len(gh_token) > 5:
    gh_token_obscure = gh_token[:5] + ((len(gh_token) - 5) * "*")
else:
    gh_token_obscure = "*****"

autolog_info(f"GitHub API: Token={gh_token_obscure} len={len(gh_token)}")

# https://pygithub.readthedocs.io/en/latest/github.html?highlight=page
g = Github(gh_token, per_page=100)

# -- get issues --------------------------------------------------------------
# curl -i "https://api.github.com/repos/scitools/iris/issues"
repo = g.get_repo("scitools/iris")

# https://pygithub.readthedocs.io/en/latest/github_objects/Issue.html#github.Issue.Issue
issues = repo.get_issues(state="open")
total_issues = issues.totalCount

autolog_info(f"GitHub API: Issues (including pull requests) to process: {total_issues}")
autolog_info(f"GitHub API: Only issues that have 1 or more votes will be used.")

voted_json = {}
voted_list = []
total_issues_only = 0

for i, issue in enumerate(issues):
    # ignore pull requests
    if issue._pull_request is github.GithubObject.NotSet:
        plus_one_count = 0

        for r in issue.get_reactions():
            if r.content == "+1":
                plus_one_count += 1

        if plus_one_count > 0:
            total_issues_only += 1

            autolog_info(
                f"Number = {issue.number :>5}  "
                f"Likes = {plus_one_count :>4}  "
                f"Author = {issue.user.login :<20}  "
                f"Title = {issue.title}"
            )

            voted_list.append(
                [
                    plus_one_count,
                    ISSUE_HREF.format(number=issue.number),
                    AUTHOR_HREF.format(author=issue.user.login),
                    issue.title,
                ]
            )

autolog_info(f"GitHub API: Issues Only Total with > 0 votes: {total_issues_only}")

voted_json["data"] = voted_list

autolog_info(f"Writing JSON: {OUTPUT_JSON}")

with open(OUTPUT_JSON, "w") as f:
    json.dump(voted_json, f, indent=2)
