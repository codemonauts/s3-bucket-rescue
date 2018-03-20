#! /usr/bin/env python3

import json
import sys
from pprint import pprint

data = json.load(sys.stdin)

all_versions = {}

for entry in data["Versions"]:
    print("Found file {}".format(entry["Key"]))
    filepath = entry["Key"]

    try:
        all_versions[filepath].append(entry)
    except KeyError:
        all_versions[filepath] = []
        all_versions[filepath].append(entry)

for filepath in all_versions:

    # filter empty files
    not_empty = [e for e in all_versions[filepath]]

    # find newest version
    newest = sorted(not_empty, key=lambda k: k['LastModified'], reverse=True)[0]

    print("{}|{}".format(newest["Key"], newest["VersionId"]))


