#!/usr/bin/python3

"""
    Python script that takes your Github credentials (username and password)
    and uses the Github API to display your id
"""

if __name__ == '__main__':
    import requests
    import sys
    
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(user, passwd)).json()

    if "id" in response:
        print(response['id'])
    else:
        print('None')
