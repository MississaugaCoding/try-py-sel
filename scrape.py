from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# start Chrome session
browser = webdriver.Chrome()

# opening web site
url = 'https://google.ca'
browser.get(url)

# type in search term
search_input_el = browser.find_element_by_name('q')
search_input_el.send_keys('python')
time.sleep(1)  # wait a second

# press Enter
search_input_el.send_keys(Keys.ENTER)
time.sleep(3)  

# read results
result_els = browser.find_elements_by_class_name('yuRUbf')
for result in result_els:
    link_el = result.find_element_by_tag_name('a')
    print( link_el.get_attribute('href') )

# close Chrome session
browser.quit()