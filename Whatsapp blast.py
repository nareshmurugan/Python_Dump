from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome(r'chromedriver')
browser.get('https://web.whatsapp.com')
friend=input('Enter friend name:')
searchbox=browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchbox.send_keys(friend)
searchbox.send_keys(Keys.ENTER)
a='              '
for j in range(3000):
    message_box=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    message_box.send_keys(a+"Good morining da pundaingala")
    message_box.send_keys(Keys.ENTER)
    a+=a
