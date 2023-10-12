from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome(r'chromedriver')
browser.get('https://web.whatsapp.com')
friendl={'ragul.r':8610982833,'ragul.g':9600784913,'rajamanikkam':7339147556,'ranjith':6381787960,'subramanian':
        8778482870,'sulaiman':8344107037,'surya':6374570440,'varatharajan':6383334060,'vimal':7708452379,'hari.g':
        8870453113,'harikrishanan':9566377667,'karthikeyan':8248173050,'raman':9943149436,'sivasuriyan':8760287239,
        'srinivas':9345308520,'hariharan':8220469369,'anbarasan':9787638123,'jayapriyan':7868932481,'arun kumar':6374582389,'natraj':9994300450
        }
friends=list(friendl.values())
#message='https://meet.google.com/lookup/blclwckukg?authuser=0&hs=179'
message='hi'
for j in range(len(friends)):
    searchbox=browser.find_elements_by_tag_name('<div class="_2_1wd copyable-text selectable-text" contenteditable="true" data-tab="3" dir="ltr"></div>')
    searchbox.send_keys(friends[j])
    searchbox.send_keys(Keys.ENTER)
    message_box=browser.find_element_by_xpath('<div class="_2_1wd copyable-text selectable-text" contenteditable="true" data-tab="6" dir="ltr" spellcheck="true"></div>')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    
