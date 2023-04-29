#!/usr/bin/python3
"""
   script that takes your GitHub credentials (username and password)
   and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    http_auth = HTTPBasicAuth("username", "password")

    r = requests.get(url, auth=http_auth)
    res_json = r.json()
    print(res_json.get("id"))
