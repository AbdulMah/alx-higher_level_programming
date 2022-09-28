#!/usr/bin/python3

"""
    Python script that takes in a string and sends a search
    request to the Star Wars API
"""

if __name__ == '__main__':
    import requests
    import sys

    repository_name = sys.argv[1]
    owner = sys.argv[2]
    headers = {
              'Accept': 'application/vnd.github.v3+json',
              }
    params = {
        'per_page': 10,
    }

    respons = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
                      owner, repository_name),
                      headers=headers, params=params)
    json_response = respons.json()
    for commit in json_response:
        print(commit['sha'] + ':', commit['commit']['author']['name'])
