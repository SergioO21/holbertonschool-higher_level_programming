#!/usr/bin/python3
""" Takes in a URL and an email address, sends a POST request
    to the passed URL with the email as a parameter, and finally
    displays the body of the response.
"""


def main():
    """ Main Function """
    import requests
    from sys import argv

    req = requests.post(argv[1], {"email": argv[2]})

    print(req.text)


if __name__ == "__main__":
    main()
