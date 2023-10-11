from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome(r'chromedriver')
browser.get('https://web.whatsapp.com')
ch="yes"
while(ch=="yes"):
    def message_text(friend,message):
        global browser
        searchbox=browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.send_keys(friend)
        searchbox.send_keys(Keys.ENTER)
        message_box=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
    friend=input('Enter friend name:')
    message=input('Enter the message')
    message_text(friend,message)
    ch = input("DO YOU WANT TO FIND ANOTHER SOLUTION......")
else:
    print('OK THANK YOU FOR YOUR WORKING')

