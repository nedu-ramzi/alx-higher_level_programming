#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge."""

import requests
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)

    r = requests.get(url)
    res_json = r.json()
    try:
        for commit in  res_json[:10]:
            sha = commit .get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
