from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome(r'chromedriver.exe')
browser.get('https://web.whatsapp.com')
friend=input('Enter friend name:')
message=['* * *   * * *','*     *     *','*         *','*       *',' *   * '   ,'  * ']
number=int(input('Enter the number'))
searchbox=browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchbox.sent_keys(friend)
searchbox.send_keys(Keys.ENTER)
for i in range(number):
    message_box=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for i in range(len(message)):
        message_box.send_keys(message[i])
        message_box.send_keys(Keys.ENTER)
