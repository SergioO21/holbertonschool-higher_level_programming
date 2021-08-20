#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the
    value of the variable X-Request-Id in the response header.
"""


def main():
    """ Main Function """
    import requests

    req = requests.get("https://intranet.hbtn.io/status")

    print(req.headers["X-Request-Id"])

if __name__ == "__main__":
    main()
