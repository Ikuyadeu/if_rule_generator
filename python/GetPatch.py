"""
Usage:
First use GetData.py and ready project-pulls.json
python3 GetPatch.py pull_file outdir user password

pullfile: github pull file from GetData.py (e.g. project-pulls.json)
outdir: output directory
user: your github id
password: your github password
"""

import sys
import json
import os

def main():
    """
    Main function
    """
    args = sys.argv
    pulls_file = args[1]
    outdir = args[2]
    user = args[3]
    password = args[4]

    with open(pulls_file, "r", encoding="utf-8") as pulls:
        pulls = [x for x in json.load(pulls)
                 if x["closed_at"] is not None and x["merge_commit_sha"] is not None]

    patch_urls = [(x["base"]["repo"]["url"] + "/commits/" + x["merge_commit_sha"], x["number"])
                  for x in pulls]

    for patch_url, number in patch_urls:
        os.system("curl -u " + user + ":" + password + " -H \"Accept: application/vnd.github.v3.patch\" " + patch_url + " -o " + outdir + "/" + str(number) + ".patch")

if __name__ == '__main__':
    main()
