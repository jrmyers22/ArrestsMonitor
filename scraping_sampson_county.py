# Uses Selenium to start the Chrome browser in the background,
# displays the last 56 arrests in Sampson county,
# searches for the perp's name, then displays a dialog if found.

import sys, os
import selenium as se
from selenium 			    import webdriver
from selenium.common.exceptions     import TimeoutException
from selenium.webdriver.common.keys import Keys

# Case Sensitive
criminal_name = 'Firstname Lastname'
arrests_records_url = 'https://northcarolina.arrests.org/index.php?county=862&page=1&results=56'

# Run via the Chrome browser in background
# Running headless also prevents from being blacklisted
options = se.webdriver.ChromeOptions()
options.add_argument('headless')
driver = se.webdriver.Chrome(chrome_options=options)
driver.get(arrests_records_url)

# Get the html source substring of just the arrests
try:
	html_source = driver.page_source
	html_source = html_source.encode('utf-8')
	html_source = html_source[html_source.index('search-results'):html_source.index('arrests-ribbon')]
except:
	print('Error: Couldn\'t get the HTML source')
	quit()

# Search for the name of our perp
if criminal_name in html_source:
    print('Found, displaying dialog')
    os.system('open ./ALERT.app')
else:
    print('No results for ' + criminal_name)
