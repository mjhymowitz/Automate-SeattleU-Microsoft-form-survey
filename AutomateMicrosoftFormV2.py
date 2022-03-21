
#!/usr/bin/env python
# coding: utf-8

from config import *

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import FirefoxOptions

#from selenium.webdriver import Edge
#from selenium.webdriver.edge.service import Service as EdgeService
#from selenium.webdriver.edge.options import Options as EdgeOptions
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# variables
SEATTLEU_COVID = "https://www.seattleu.edu/coronavirus/screening/"
COVID_FORM_URL_XPATH = '/html/body/div[6]/div/div[3]/div[2]/div/div/ul/li[1]/a'
USERNAME_INPUT_XPATH = '//*[@id="i0116"]'
USERNAME_SUBMIT_BUTTON_XPATH = '//*[@id="idSIButton9"]'
PASSWORD_INPUT_XPATH = '//*[@id="i0118"]'
PASSWORD_SUBMIT_BUTTON_XPATH = '//*[@id="idSIButton9"]'
STAY_SIGN_IN_XPATH = '//*[@id="idBtn_Back"]'
FORM_QUESTION_ONE_XPATH = '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/input'
FORM_QUESTION_TWO_XPATH = '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/input'
FORM_QUESTION_THREE_XPATH = '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/label/input'
FORM_QUESTION_FOUR_XPATH = '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]/div/label/input'
FORM_QUESTION_FIVE_XPATH = '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div/div[2]/div/div[4]/div/label/input'
FORM_QUESTION_SIX_XPATH ='/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/label/input'
FORM_SUBMIT_BUTTON_XPATH = '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div'
CONFIRMATION_XPATH = '/html/body/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/span'
get_confirmation_div_text = ''

options = FirefoxOptions()
options.headless = True
#options.set_headless()


#AUTOMATION

# Open Browser
#service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
#driver = Edge(service=service, options=EdgeOptions())
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = Firefox(service=service, options=options)# Open School Website
try:
    # Go To SU Website
    print("access school Website -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    driver.get(SEATTLEU_COVID)
    WebDriverWait(driver, browser_long_delay).until(EC.presence_of_element_located((By.XPATH,COVID_FORM_URL_XPATH)))
    form_url = driver.find_element(By.XPATH, COVID_FORM_URL_XPATH)
    driver.get(form_url.get_attribute('href'))

    # Enter Username
    print("enter username -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    WebDriverWait(driver, browser_long_delay).until(EC.presence_of_element_located((By.XPATH,USERNAME_INPUT_XPATH)))
    username = driver.find_element(By.XPATH, USERNAME_INPUT_XPATH)
    username.send_keys(EMAIL)

    # Submit Username
    print("submit username -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    WebDriverWait(driver, browser_long_delay).until(EC.presence_of_element_located((By.XPATH,USERNAME_SUBMIT_BUTTON_XPATH)))
    submit_username = driver.find_element(By.XPATH, USERNAME_SUBMIT_BUTTON_XPATH)
    submit_username.click()

    # Enter Password
    print("enter password -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    WebDriverWait(driver, browser_long_delay).until(EC.presence_of_element_located((By.XPATH,PASSWORD_INPUT_XPATH)))
    sleep(browser_short_delay)
    password = driver.find_element(By.XPATH, PASSWORD_INPUT_XPATH)
    password.send_keys(PASSWORD)

    # Submit Password
    print("submit password -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    sleep(browser_short_delay)
    submit_password = driver.find_element(By.XPATH, PASSWORD_SUBMIT_BUTTON_XPATH)
    sleep(browser_short_delay)
    submit_password.click()

    # Stay signed in?
    WebDriverWait(driver, browser_long_delay).until(EC.presence_of_element_located((By.XPATH,STAY_SIGN_IN_XPATH)))
    submit_user = driver.find_element(By.XPATH, STAY_SIGN_IN_XPATH)
    submit_user.click()

    # Filling out form
    print("Fill out Form -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    sleep(browser_short_delay)
    RadioButtonPeriod = driver.find_element(By.XPATH, FORM_QUESTION_ONE_XPATH)
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()

    sleep(browser_short_delay)
    RadioButtonPeriod = driver.find_element(By.XPATH, FORM_QUESTION_TWO_XPATH)
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()

    sleep(browser_short_delay)
    RadioButtonPeriod = driver.find_element(By.XPATH, FORM_QUESTION_THREE_XPATH)
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()

    sleep(browser_short_delay)
    RadioButtonPeriod = driver.find_element(By.XPATH, FORM_QUESTION_FOUR_XPATH)
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()

    sleep(browser_short_delay)
    RadioButtonPeriod = driver.find_element(By.XPATH, FORM_QUESTION_FIVE_XPATH)
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()

    sleep(browser_short_delay)
    RadioButtonPeriod = driver.find_element(By.XPATH, FORM_QUESTION_SIX_XPATH)
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()
    RadioButtonPeriod.click()

    # Submit form
    sleep(browser_short_delay)
    submit_user = driver.find_element(By.XPATH, FORM_SUBMIT_BUTTON_XPATH)
    submit_user.click()

    # Confirm if code worked or not
    sleep(browser_short_delay)
    get_confirmation_div_text = driver.find_element(By.XPATH, CONFIRMATION_XPATH)
except Exception:
    print("---------------------------------------------------------------------------------")
    print("Test Was Not Successful")
    print(Exception.with_traceback)
    print(" ")
    driver.delete_all_cookies()
    driver.quit()

print("---------------------------------------------------------------------------------")
#Confirm if code worked or not
if ((get_confirmation_div_text) != ''):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")

#Close Everything
driver.delete_all_cookies()
driver.close()
driver.quit()
exit()