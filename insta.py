from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Function to generate a random string for the username
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Set up Chrome options for Termux
options = Options()
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
options.add_argument("--disable-gpu")  # Applicable for headless browsing
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

# Initialize WebDriver without specifying a path
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the Instagram signup page
driver.get('https://www.instagram.com/accounts/emailsignup/')

# Wait for the elements to load
time.sleep(5)

# Ask for the user's email
email = input("Please enter your email: ")

# Generate a random username
generated_username = random_string(8) # Random username

# Set the default password
default_password = 'none@12345'

# Fill the email, full name, username, and password fields
driver.find_element_by_name('emailOrPhone').send_keys(email)
driver.find_element_by_name('fullName').send_keys(random_string(10)) # Random full name
driver.find_element_by_name('username').send_keys(generated_username)
driver.find_element_by_name('password').send_keys(default_password)

# Submit the form to move to the next page
driver.find_element_by_xpath('//button[text()="Sign up"]').click()

# Wait for the date of birth page to load
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

# Click the 'Next' button after entering the date of birth
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[text()="Next"]'))
)
next_button.click()

# Wait for the OTP input field to appear
otp_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'otpCode'))
)

# Ask the user for the OTP
otp_code = input("Please enter the OTP sent to your email: ")

# Enter the OTP in the input field
otp_input.send_keys(otp_code)

# Find and click the Verify button
verify_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[text()="Verify"]'))
)
verify_button.click()

# After successful verification, print the username and password
print(f"Username: {generated_username}")
print(f"Password: {default_password}")

# Continue with the rest of the signup process as needed
