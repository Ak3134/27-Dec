# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open Chrome
driver = webdriver.Chrome(
	'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')

# Open URL
driver.get(
	'http://demo.automationtesting.in/FileDownload.html')

# Enter text
driver.find_element_by_id('textbox').send_keys("Hello world")

# Generate Text File
driver.find_element_by_id('createTxt').click()

# Click on Download Button
driver.find_element_by_id('link-to-download').click()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random

# Login Credentials
username = input('Enter your Username ')
password = input('Enter your Password ')
url = 'https://instagram.com/' + input('Enter username of user whome you want to send message')
