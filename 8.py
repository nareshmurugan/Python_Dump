from selenium import webdriver
browser=webdriver.Chrome(r'D:/PYTHON/chromedriver')
browser.get('https://web.whatsapp.com')
searchbox=browser.find_element_by_xpath()
searchbox.send_keys(Keys.ENTER)
message_box.send_keys(Keys.ENTER)






