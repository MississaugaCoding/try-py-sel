from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# start Chrome session
browser = webdriver.Chrome()

# opening web site
url = 'https://www.booking.com/'
browser.get(url)

# type in location
search_input_el = browser.find_element_by_name('ss')
search_input_el.send_keys('Mississauga Ontario')

# click search button
search_btn_el = browser.find_element_by_css_selector('button.sb-searchbox__button')
search_btn_el.click()
time.sleep(1)  

# read results
result_els = browser.find_elements_by_css_selector('div.sr_item')
for result in result_els:    
    name = result.find_element_by_class_name('sr-hotel__name')

    try:
        stars = result.find_element_by_class_name('bui-rating')
        score = result.find_element_by_class_name('bui-review-score__badge')
        reviews = result.find_element_by_class_name('bui-review-score__text')
        print( name.text )
        print( '{} stars'.format(stars.get_attribute('aria-label')) )
        print( reviews.get_attribute('innerHTML').strip() )
        print( score.get_attribute('innerHTML').strip() ) 
        print('---------------')
    except:
        pass
        
# close Chrome session
browser.quit()