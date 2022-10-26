import re
import requests
import urllib
import json


# Menu to allow the user to quit the phishing program
def menu():
    print("Option [0], Option 0 - Exit the Program")
    print("Option [1], Option 1 - Start Phishing Scanner")


menu()

option = int(input("Enter your Option: "))


# Function to validate URL
# using regular expression
def isValidURL(str):
    # Regex to check valid URL
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if str == None:
        return False

    # Return if the string
    # matched the ReGex
    if re.search(p, str):
        return True
    else:
        return False




while option != 0:
    if option == 1:
        url = input("Enter Suspicious URL: ")
        encoded_url = urllib.parse.quote(url, safe='')
        api_url = api_url = "https://ipqualityscore.com/api/json/url/n1ww7DuSQnJctAAkuyWi3fE758gCSJiX/"
        data = requests.get(api_url + encoded_url)
        print(json.dumps(data.json(), indent=4))
        print("Regex Check:")

        if isValidURL(url):
            print("This Link's Regex is Okay")
        else:
            print("Regex is not Okay")

        pass
    else:
        print("Invalid option")

    print()
    menu()
    option = int(input("Enter your Option: "))
