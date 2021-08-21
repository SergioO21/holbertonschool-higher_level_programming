#!/usr/bin/python3
""" 
"""


def main():
    """ Main Function """
    import requests
    from sys import argv

    req = requests.get(argv[1])

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)


if __name__ == "__main__":
    main()
