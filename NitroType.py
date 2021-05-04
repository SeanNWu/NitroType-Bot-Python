from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import pyautogui as mouse
path = "C:\Program Files (x86)\chromedriver.exe" 


driver = webdriver.Chrome(path) #choose browser and choose the driver which is path
'''
"https://www.nitrotype.com/race/e857900e32ba55b225f8825d939f1d9a"  #ENTER THE LINK OF YOUR RACE
'''
driver.get("https://www.nitrotype.com") #opens website
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/header/div/div[2]/div[3]/div/div[1]/a'))
    )
    element.click()

    two = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/section/div[2]/div/div[1]/ul/li[3]/a'))
    )
    user = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    user.send_keys("ENTER USERNAME")
    password = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password.send_keys("ENTER PASSWORD")

    button = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/section/div[2]/div/div[3]/form/button'))
    )
    button.click()


    mouse.click(469,106)
    mouse.write('https://www.nitrotype.com/race/e857900e32ba55b225f8825d939f1d9a') #NITROTYPE LINK
    mouse.press('enter')
    whole = WebDriverWait(driver,300).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'dash-copy'))
    )
    print('flag')
    '''
    words = whole.find_element_by_class_name('dash-word')
    print('flag')
    '''
    
    keyboard.wait('esc')
    keyboard.write(whole.text,delay = 0.05)
    print('flag')








except:
    print("failed")
