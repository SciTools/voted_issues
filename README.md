# Votable Issues

[![Refresh Voted Issues](https://github.com/SciTools/voted_issues/actions/workflows/refresh-voted-issues.yml/badge.svg)](https://github.com/SciTools/voted_issues/actions/workflows/refresh-voted-issues.yml)

This repository is the home of the tool that will query the GitHub API
for the Iris issues that have been voted on and update a json file held in the
repo.  This json file may then be used in the Iris documentation to view the
voted issues.

This tool is run via a GitHub Action named [refresh-voted-issues.yml](https://github.com/SciTools/voted_issues/blob/main/.github/workflows/refresh-voted-issues.yml)
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

### CLA

The [**CLA**](https://cla-assistant.io/SciTools/) check will run on pull
requests, as with the rest of SciTools, but the CLA is NOT part of any
branch protection rule as this would block the workflow of merging directly
to `main`.
