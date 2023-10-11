from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome(r'chromedriver')
browser.get('https://www.hackerrank.com/login')
searchbox=browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[1]/div/div/div/input')
searchbox.send_keys("k.gokulappaduraikjgv@gmail.com")
searchbox.send_keys(Keys.ENTER)
searchbox=browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[2]/div/div/div/input')
searchbox.send_keys("PYTHON@k.gad02")
searchbox=browser.find_element_by_xpath('//*[@id="tab-1-content-1"]/div[1]/form/div[4]/button').click()



