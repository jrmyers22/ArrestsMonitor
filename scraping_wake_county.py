import sys, os
import selenium as se
from selenium 			    import webdriver
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
from selenium.webdriver.common.by   import By
from selenium.common.exceptions     import TimeoutException
from selenium.webdriver.common.keys import Keys

# Case Sensitive
# TODO: Be able to input first middle and last
criminal_name = 'LASTNAME'

# Run via the Chrome browser in the background
options = se.webdriver.ChromeOptions()
# Make it run in the background
options.add_argument('headless')
driver = se.webdriver.Chrome(chrome_options=options)
#driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
driver.get("https://dwslivescan.co.wake.nc.us/mug/Disclaimer.aspx")

# Find the agree button and press it,
# Navigate to arrests in last 48 hours
agreeButton = driver.find_element_by_name('btnAgree')
agreeButton.send_keys(Keys.RETURN)
driver.implicitly_wait(10) # seconds
driver.find_element_by_link_text('Last 48 Hours of Arrests').click()
html_source = driver.page_source
if criminal_name in html_source: # Case Sensitive
    print('Found, displaying dialog')
    os.system('open ./ALERT.app')
else:
    print('No results for ' + criminal_name)
