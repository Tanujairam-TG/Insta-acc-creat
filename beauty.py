import requests
from bs4 import BeautifulSoup

# Function to generate a random string
def random_string(length):
    import random
    import string
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Ask for the user's email
email = input("Please enter your email: ")

# Generate a random username and password
generated_username = random_string(8)
default_password = 'none@12345'

# The URL you want to scrape or interact with
url = 'https://example.com/signup'

# Data payload for the POST request
data = {
    'email': email,
    'fullName': random_string(10),
    'username': generated_username,
    'password': default_password
}

# Make a POST request to the signup page
response = requests.post(url, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Perform actions based on the content
    # For example, find a confirmation message or next steps
    confirmation_message = soup.find('p', class_='confirmation').text
    print(confirmation_message)
else:
    print("Failed to sign up. Status code:", response.status_code)

# Continue with the rest of the process as needed
