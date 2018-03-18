"""
Usage:
First use GetData.py and ready project-pulls.json
python/python3 GetDiffs.py project user password

pullfile: github pull file from GetData.py (e.g. project-pulls.json)
outdir: output directory
user: your github id
password: your github password
"""

import sys
import os
import csv

def main():
    """
    Main function
    """
    args = sys.argv
    project = args[1]
    user = args[2]
    password = args[3]
    diffs_file = project + "/diffs.csv"
    outdir = project + "/diffs/"

    with open(diffs_file, "r", encoding="utf-8") as diffs:
        reader = csv.DictReader(diffs)
        for i, diff in enumerate(reader):
            sys.stdout.write("\r%d commits" % i)
            os.system("curl -s -u " +\
            user + ":" + password +\
            " -H \"Accept: application/vnd.github.v3.patch\" "
            + diff["url"] + " -o " + outdir + str(i) + ".diff")

if __name__ == '__main__':
    main()
