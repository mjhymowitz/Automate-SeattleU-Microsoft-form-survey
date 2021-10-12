#!/usr/bin/env python
# coding: utf-8

from selenium.webdriver import Edge
import time

# variables
EMAIL = '' 			# Enter your SU email here
PASSWORD = '' 	# Enter your SU password here
FORM_URL = "https://forms.office.com/Pages/ResponsePage.aspx?id=UuAQvBywSUiZZ-5-x0_J2JXoEsux15xJh0xDP1C0CuxUQVFHVUJOUDQ3U1dEM1pENDlHRVJRWFdUVi4u"

#AUTOMATION
get_confirmation_div_text = ''
try:
    # Open Browser
    driver = Edge(r".\msedgedriver.exe")
    driver.get(FORM_URL)
    time.sleep(10)

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
    print("Test Was Not Successful")


#Confirm if code worked or not
if ((get_confirmation_div_text.text) == "Please check your Seattle University email for your screening results prior to coming to campus."):
    print ("Test Was Successful")
		return true
return false

driver.close()
