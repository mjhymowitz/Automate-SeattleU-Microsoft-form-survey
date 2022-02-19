#!/usr/bin/env python
# coding: utf-8
#from click import option
from config import *
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
import time

# variables
SEATTLEU_COVID = "https://www.seattleu.edu/coronavirus/screening/"

options = Options()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("disable-gpu")

#AUTOMATION
get_confirmation_div_text = ''
# Open Browser
driver = Edge(webdriver_path, options=options)
try:
    # Open School Website
    driver.get(SEATTLEU_COVID)
    form_url = driver.find_element_by_xpath('//*[@id="id1647669"]/div/div/ul/li[1]/a') 
    time.sleep(short_sleep)
    driver.get(form_url.get_attribute('href'))
    time.sleep(long_sleep)

    # Enter Username
    user = driver.find_element_by_xpath('//*[@id="i0116"]')
    user.send_keys(EMAIL)

    # Submit Username
    submit_user = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    submit_user.click()
    time.sleep(short_sleep)

    # Enter Password
    user = driver.find_element_by_xpath('//*[@id="i0118"]')
    user.send_keys(PASSWORD)

    # Submit Password
    submit_user = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    submit_user.click()
    time.sleep(short_sleep)

    # Stay signed in?
    submit_user = driver.find_element_by_xpath('//*[@id="idBtn_Back"]')
    submit_user.click()
    time.sleep(short_sleep)

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
    time.sleep(short_sleep)

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
