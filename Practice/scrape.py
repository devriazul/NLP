from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up Chrome driver options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Disable sandbox mode
options.add_argument('--disable-dev-shm-usage')  # Disable /dev/shm usage
options.add_argument('--disable-extensions')  # Disable extensions
options.add_argument('--disable-popup-blocking')  # Disable popup blocking
options.add_argument('--disable-notifications')  # Disable notifications
options.add_argument('--disable-infobars')  # Disable infobars
options.add_argument('--ignore-certificate-errors')  # Ignore certificate errors
options.add_argument('--ignore-ssl-errors')  # Ignore SSL errors

# Set up Chrome driver
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get('https://www.example.com')

# Wait for the page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    logging.info('Page loaded successfully')
except TimeoutException:
    logging.error('Page failed to load')
    driver.quit()
    exit()

# Perform actions on the page
# ...