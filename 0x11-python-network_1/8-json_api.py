#!/usr/bin/python3
"""
   script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'
    payload = {"q": letter}

    r = requests.post(url, data=payload)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
