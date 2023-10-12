from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import emoji
browser=webdriver.Chrome('chromedriver.exe')
browser.get('https://web.whatsapp.com')
ch="yes"
while(ch=="yes"):
    friend=input('Enter friend name:')
    searchbox=browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    searchbox.send_keys(friend)
    searchbox.send_keys(Keys.ENTER)
    for i in range(0,10):
        message_box=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        message_box.send_keys(Keys.TAB)
        message_box.send_keys(Keys.TAB)
        message_box.send_keys(Keys.TAB)
        message_box.send_keys(Keys.TAB)
        message_box.send_keys(Keys.ENTER)
        message_box.send_keys(Keys.ENTER)
    ch = input("DO YOU WANT TO FIND ANOTHER SOLUTION......")
else:
    print('OK THANK YOU FOR YOUR WORKING')

