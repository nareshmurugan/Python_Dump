from selenium import webdriver
import password
import time
from selenium.webdriver.chrome.options import Options
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
#pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs",{"profile.defakt_content_setting_values.meida.stream_mic":1,
    "profile.default_content_setting_values.media_stream_camera":1,
    "profile.default_content_setting_values.geolocation":1,
    "profile.default_content_setting_values.notifications":1,})
driver=webdriver.Chrome(chrome_options=opt,executable_path=r'chromedriver')
driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
username=driver.find_element_by_xpath('//*[@id="Email"]')
username.send_keys('k.gokulappaduraikjgv@gmail.com')
next=driver.find_element_by_xpath('//*[@id="next"]')
next.click()
time.sleep(5)
password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys('9489228333')
next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next.click()
time.sleep(15)
