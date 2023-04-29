#!/usr/bin/python3
"""
   script that fetches https://alx-intranet.hbtn.io/status
   using the request package
"""
import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    body = r.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
