#!/usr/bin/python3
""" Takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id.
"""


def main():
    """ Main Function """
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/repos/{}/{}/commits"

    req = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2])).json()

    print(req.get("id"))


if __name__ == "__main__":
    main()
