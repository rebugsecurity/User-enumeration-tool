# User-enumeration-tool
This code takes a list of usernames and a URL template as input, and checks each username by appending it to the end of the URL template and sending a GET request. If the response status code is 200 (OK), then the username is considered to exist, otherwise it is considered not found.

``You can modify the usernames list with the list of usernames you want to check, and change the url_template variable to the format of the URLs you want to check against.``

``DISCLAIMER & Note: that this is just a simple example and there are many more advanced username enumeration tools and libraries available in Python. Also, be aware that username enumeration can be used as part of social engineering attacks and should be used responsibly and with permission.``

# installing requirements.
``pip3 install -r requirements.txt``

# usage
``python3 enumtool.py``

# displaying
![alt text](https://github.com/rebugsecurity/User-enumeration-tool/blob/a11c45d95ece97d9c9a3ec2c0b42fabe0f17bfc0/user-enum-tool-working.png)
