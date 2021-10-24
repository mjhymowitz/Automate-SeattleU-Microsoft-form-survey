#!/usr/bin/env python
# coding: utf-8

from selenium.webdriver import Edge
import time

# variables
EMAIL = '' 	# Enter your SU email here
PASSWORD = '' 	# Enter your SU password here
SEATTLEU_COVID = "https://www.seattleu.edu/coronavirus/screening/"

#AUTOMATION
get_confirmation_div_text = ''
# Open Browser
driver = Edge(r".\msedgedriver.exe")
try:
    # Open School Website
    driver.get(SEATTLEU_COVID)
    form_url = driver.find_element_by_xpath('//*[@id="id1647669"]/div/div/ul/li[1]/a') 
    time.sleep(2)
    driver.get(form_url.get_attribute('href'))
    time.sleep(8)

    # Enter Username
    user = driver.find_element_by_xpath('//*[@id="i0116"]')
    user.send_keys(EMAIL)

    # Submit Username
    submit_user = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    submit_user.click()
    time.sleep(2)

    # Enter Password
    user = driver.find_element_by_xpath('//*[@id="i0118"]')
    user.send_keys(PASSWORD)

    # Submit Password
    submit_user = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    submit_user.click()
    time.sleep(2)

    # Stay signed in?
    submit_user = driver.find_element_by_xpath('//*[@id="idBtn_Back"]')
    submit_user.click()
    time.sleep(2)

    # Filling out form
    RadioButtonPeriod = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/input')
    RadioButtonPeriod.click()

    RadioButtonPeriod = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/input')
    RadioButtonPeriod.click()

    RadioButtonPeriod = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/label/input')
    RadioButtonPeriod.click()

    RadioButtonPeriod = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]/div/label/input')
    RadioButtonPeriod.click()

    RadioButtonPeriod = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div/div[2]/div/div[4]/div/label/input')
    RadioButtonPeriod.click()

    RadioButtonPeriod = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/label/input')
    RadioButtonPeriod.click()

    # Stay signed in?
    submit_user = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div')
    submit_user.click()
    time.sleep(2)

    # Confirm if code worked or not
    get_confirmation_div_text = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[2]/div[1]/div[2]/span')
except Exception:
    print("---------------------------------------------------------------------------------")
    print("Test Was Not Successful")

print("---------------------------------------------------------------------------------")
#Confirm if code worked or not
if ((get_confirmation_div_text) != ''):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")

driver.close()
exit()
