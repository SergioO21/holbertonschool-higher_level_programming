#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


def main():
    """ Main Function """
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    q = argv[1] if len(argv) > 1 else ""

    try:
        req = requests.post(url, {"q": q}).json()

        if "id" in req and "name" in req:
            print("[{}] {}".format(req["id"], req["name"]))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
