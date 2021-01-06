from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import os

def login():
    username = driver.find_element_by_id("session_key")
    username.send_keys(os.environ.get('linkedin_id'))
    password = driver.find_element_by_id("session_password")
    password.send_keys(os.environ.get('linkedin_pw'))
    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    print("LOGGED IN LINKED IN!")

def dsti_alumni():
    driver.get("curl")

def robo():
    for _ in range(0,5):
    
        for i in range (0,20):
            #pyautogui.moveTo(1150, 385) 
            pyautogui.click(1150, 385)
            #pyautogui.moveTo(1250, 380) #1220 #373
            pyautogui.click(1250, 380)      
            pyautogui.scroll(-66) #65
            print(str(i) + 'requests sent')

#print('still active')
        pyautogui.click(1181, 571) 
    

driver = webdriver.Chrome(r"C:\Users\verce\Downloads\chromedriver.exe")
url = "http://linkedin.com/"
curl = "CUSTOM LINKEDIN PATH"

driver = webdriver.Chrome(r"DRIVER PATH")
driver.get(url)
driver.maximize_window()
login()
dsti_alumni()

robo()
