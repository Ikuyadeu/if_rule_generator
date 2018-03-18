"""
Usage: python3 python/RequestDissList.py owner project user password
"""
import sys
import json
import requests
import csv

def main():
    """
    Main function
    """
    args = sys.argv
    owner = args[1]
    project = args[2]
    user = args[3]
    password = args[4]
    pulls_file = project + "/pulls.json"
    commits_file = project + "/diffs.csv"
    url_header = "https://github.com/" + owner + "/" + project + "/compare/"
    # out_dir = project + "/commits/"
    sha_fields = ["merge_commit_sha", "first_commit_sha", "url"]
    with open(pulls_file, "r", encoding="utf-8") as pulls:
        pulls = [x for x in json.load(pulls)
                    if x["closed_at"] is not None and x["merge_commit_sha"] is not None]

    commits_urls = [(x["_links"]["commits"]["href"], x["merge_commit_sha"]) for x in pulls]

    shas = []
    for patch_url, merge_commit_sha in commits_urls:
        resp = requests.get(patch_url, auth=requests.auth.HTTPBasicAuth(user, password))
        data = json.loads(resp.content.decode('utf-8'))
        first_commit_sha = data[0]["sha"]
        shas.append({"first_commit_sha": first_commit_sha,
        "merge_commit_sha": merge_commit_sha,
        "url": url_header + first_commit_sha + "..." + merge_commit_sha + ".diff"})
        
    with open(commits_file, "w", encoding="utf-8") as commits:
        writer = csv.DictWriter(commits, sha_fields)
        writer.writeheader()
        writer.writerows(shas)

if __name__ == '__main__':
    main()
