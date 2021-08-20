#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """


def main():
    """ Main Function """
    import urllib.request

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:

        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("UTF-8")))


if __name__ == "__main__":
    main()
