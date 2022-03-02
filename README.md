# Votable Issues

[![Refresh Votable Issues](https://github.com/SciTools/votable_issues/actions/workflows/refresh-votable-issues.yml/badge.svg)](https://github.com/SciTools/votable_issues/actions/workflows/refresh-votable-issues.yml)

This repository is the home of the tool that will query the GitHub API
for the Iris issues that are votable and update a json file held in the repo.
This json file may then be used in the Iris documentation to view the
votable issues.

This is essentially a workaround as the GitHub Issue browser on the web
site only allows sorting by the number of comments, not by the number of likes
on the issue header.


### Dependencies

* pyGitHub.  See https://pygithub.readthedocs.io/en/latest/introduction.html


### Usage

In order to run successfully the GH_TOKEN shell variable needs to be a valid
GItHub token value.

```
$ export GH_TOKEN=********************
$ python query_gh_votable_issues.py
```
