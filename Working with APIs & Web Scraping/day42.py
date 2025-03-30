# Day 42: Automating Web Tasks  

'''
In this day, we will learn about automating web tasks using Selenium in Python. Selenium is a popular library for automating web browsers.
'''

# Automating Web Tasks


'''''
Selenium is a library for automating web browsers. It allows you to navigate a webpage and extract data from it.
'''

# Example
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://keyurbhatiya.netlify.app/#contact")

# Locate the input fields and submit button
name_input = driver.find_element(By.NAME, "Name")
email_input = driver.find_element(By.NAME, "email")
message_input = driver.find_element(By.NAME, "Message")
submit_button = driver.find_element(By.CSS_SELECTOR, "button.main-btn.secondary-btn.border-white.mb-3")

# Fill in the form
name_input.send_keys("Keyur Bhatiya")
email_input.send_keys("n2q3F@example.com")
message_input.send_keys("Hello, how are you? form API test")

# Scroll to the submit button (in case it’s not visible)
actions = ActionChains(driver)
actions.move_to_element(submit_button).perform()

# Submit the form
submit_button.click()

print("Form submitted successfully! Check your email for a response.")