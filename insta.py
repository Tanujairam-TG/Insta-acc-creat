from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string
import time

# Function to generate a random string
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Setup the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Instagram signup page
driver.get('https://www.instagram.com/accounts/emailsignup/')

# Wait for the elements to load
time.sleep(5)

# Ask for the user's email
email = input("Please enter your email: ")

# Fill the email and full name fields
driver.find_element_by_name('emailOrPhone').send_keys(email)
driver.find_element_by_name('fullName').send_keys(random_string(10)) # Random full name

# Fill the username and password fields
driver.find_element_by_name('username').send_keys(random_string(8)) # Random username
driver.find_element_by_name('password').send_keys(random_string(12)) # Random password

# Submit the form to move to the next page
driver.find_element_by_xpath('//button[text()="Sign up"]').click()

# Wait for the second page where the date of birth is asked
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'birthday'))
)

# Set the default date of birth
default_dob = '09-10-2000'

# Fill the date of birth fields on the second page
dob_fields = default_dob.split('-')
driver.find_element_by_name('year').send_keys(dob_fields[2]) # Year
driver.find_element_by_name('month').send_keys(dob_fields[1]) # Month
driver.find_element_by_name('day').send_keys(dob_fields[0]) # Day

# Continue with the rest of the signup process as needed
