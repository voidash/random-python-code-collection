import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading

from selenium.webdriver.common.utils import join_host_port

mail_address = [] 
passwords = []

def open_file(filename: str) -> List:
    data = []
    with open(filename,'r') as f:
      data = list(filter(lambda x: x != "" ,map(lambda x : x.strip() ,f.readlines())))
    
    return data

mail_address = open_file('mail_address.txt')
password = open_file('password.txt')


def join_meet(mail_address,password):
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    # disables allow camera and microphone access
    options.add_argument('use-fake-ui-for-media-stream')
    driver = webdriver.Chrome(options=options)
    url = 'https://accounts.google.com/signin/v2/identifier?hl=ne&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    driver.get(url)
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_class_name("VfPpkd-vQzf8d").click()
    time.sleep(2)
    driver.find_element_by_class_name("zHQkBf").send_keys(password)
    driver.find_element_by_class_name("VfPpkd-vQzf8d").click()
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
    meet_url = "https://meet.google.com/shf-yqnp-ymc"
    driver.get(meet_url)
    time.sleep(2)
    driver.get(meet_url)
    time.sleep(2)
    #turn microphone off
    driver.find_element_by_class_name("sUZ4id").click()
    #turn camera off
    driver.find_element_by_xpath("//div[contains(@class,'U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed M9Bg4d')]").click()
    driver.find_element_by_xpath("//span[contains(@class,'NPEfkd RveJvd snByac')]").click()

try:
    my_t = []
    for m,p in zip(mail_address,password):
        join_meet(m,p)
        # x = threading.Thread(target=join_meet, args=(m,p))
        # x.start()
        # my_t.append(x)

    # for l in my_t:
        # l.join()


except:
        print("error")
