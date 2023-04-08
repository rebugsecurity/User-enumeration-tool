"""
This code takes a list of usernames and a URL template as input, and checks each username by appending it
to the end of the URL template and sending a GET request. If the response status code is 200 (OK),
then the username is considered to exist, otherwise it is considered not found.
"""

import requests

def check_usernames(usernames, url_template):
    for username in usernames:
        url = url_template.format(username)
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"{username}: exists")
        else:
            print(f"{username}: not found")

if __name__ == "__main__":
    usernames = ['admin', 'user1', 'test123']
    url_template = 'http://example.com/users/{}'
    
    check_usernames(usernames, url_template)
