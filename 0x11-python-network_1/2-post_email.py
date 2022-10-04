#!/usr/bin/python3

"""
    Python script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
"""

if __name__ == '__main__':
    import sys
    from urllib import request, parse

    data: bytes = parse.urlencode({'email': sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as res:
        print(res.read().decode('UTF-8'))
