from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

# Function to generate a random string
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Ask for the user's email
email = input("Please enter your email: ")

# Setup the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Instagram signup page
driver.get('https://www.instagram.com/accounts/emailsignup/')

# Wait for the elements to load (you may need to adjust the time)
driver.implicitly_wait(5)

# Fill the form with random data and provided email
driver.find_element_by_name('emailOrPhone').send_keys(email)
driver.find_element_by_name('fullName').send_keys(random_string(10)) # Random full name
driver.find_element_by_name('username').send_keys(random_string(8)) # Random username
driver.find_element_by_name('password').send_keys(random_string(12)) # Random password

# Submit the form (uncomment the next line to enable form submission)
driver.find_element_by_xpath('//button[text()="Sign up"]').click()
