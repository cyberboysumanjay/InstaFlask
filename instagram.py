#!/usr/bin/env python3
import argparse
import re
import sys
import requests

def getID(username):
    url = "https://www.instagram.com/{}"
    r = requests.get(url.format(username))
    html = r.text
    if r.ok:
        return re.findall('"id":"(.*?)",', html)[0]
    else:
        return "invalid_username"

def userDetails(userID):
    url = "https://i.instagram.com/api/v1/users/{}/info/"
    r = requests.get(url.format(userID))
    if r.ok:
        data = r.json()
        return data
    else:
        return "NULL"
