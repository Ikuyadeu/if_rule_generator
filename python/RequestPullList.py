"""
Usage: python3 python/RequestPullList.py apiurl owner project user password
"""
import sys
import json
import requests

def main():
    """
    Main
    """
    args = sys.argv
    api = args[1]
    owner = args[2]
    project = args[3]
    user = args[4]
    password = args[5]
    page = 1
    pages = []
    header = api + "/repos/" + owner + "/" + project + "/"
    while True:
        url = header + "pulls?state=all&sort=created&per_page=300"
        resp = requests.get(url + '&page=' + str(page),
                            auth=requests.auth.HTTPBasicAuth(user, password))
        data = json.loads(resp.content.decode('utf-8'))
        if len(data) <= 1:
            break
        page += 1
        pages.extend(data)
    with open(project + "/pulls.json", "w") as file:
        json.dump(pages, file, indent=4)

if __name__ == '__main__':
    main()
