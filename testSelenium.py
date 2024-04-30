from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PASS = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
SEACH_ELEMENT = "Group name or person"

browser = webdriver.Chrome("C:\chromeDriver\chromedriver.exe")
browser.get("https://www.messenger.com")

time.sleep(1)

login = browser.find_element_by_id("email")
login.send_keys(EMAIL)

password = browser.find_element_by_id("pass")
password.send_keys(PASS)

submit = browser.find_element_by_id("loginbutton")
submit.send_keys(Keys.RETURN)

time.sleep(5)

searchBar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input')
searchBar.send_keys(SEACH_ELEMENT)

time.sleep(1)

group = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div')
group.click()

time.sleep(1)

script = open("testPython\shrek.txt", "r")

for phrase in script:
    if phrase == "\n":
        continue
    message = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div')
    message.send_keys(phrase)
    message = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div')
    message.send_keys(Keys.RETURN)
    time.sleep(3)

time.sleep(5)
browser. quit()
