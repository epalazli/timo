from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.timo24.de/login/')

firma = driver.find_element_by_name('f')
firma.send_keys('WIT')

username = driver.find_element_by_name('u')
username.send_keys('enes.palazli')

#Get PW from file 'pw.txt'
credential_file = open('pw.txt', 'r')
password_text = credential_file.read()

#Send password
password = driver.find_element_by_name('p')
password.send_keys(password_text)

time.sleep(2)
login_button = driver.find_element_by_class_name('login100-form-btn')
login_button.click()

time.sleep(3)
driver.get('https://wit.timo24.de/timo/index.jsp#wTNormalView')

time.sleep(3)

time_stamp = driver.find_element_by_id('button-1278-btnIconEl')
time_stamp.click()

print('Stempeln wurde durchgeführt')
driver.quit()
