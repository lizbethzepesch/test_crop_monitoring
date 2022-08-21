import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()


class Homepage:
    url = os.getenv('URL')

    first_name_field = '//input[data-id="first_name"]'
    last_name_field = '//input[data-id="last_name"]'
    email_field = '//input[data-id="email"]'
    pswd_field = '//input[data-id="password"]'
    agree_checkbox = '//input[id="mat-checkbox-2-input"]'
    signup_button = '//button[data-id="sign-up-btn"]'

    sign_in_switch = '//button[data-id="sign-in-button"]'
    signin_button = '//button["data-id="sign-in-btn"]'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get(os.getenv('URL'))

    def enter_name(self, first_name, last_name):
        first_name_field = self.driver.find_element(By.XPATH, self.first_name_field)
        first_name_field.send_keys(first_name)
        last_name_field = self.driver.find_element(By.XPATH, self.last_name_field)
        last_name_field.send_keys(last_name)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.XPATH, self.email_field)
        email_field.send_keys(email)

    def enter_pswd(self, pswd):
        pswd_field = self.driver.find_element(By.XPATH, self.pswd_field)
        pswd_field.send_keys(pswd)

    def submit(self, type_of_auth):
        if type_of_auth == 'login':
            button = self.driver.find_element(By.XPATH, self.signin_button)
        else:
            button = self.driver.find_element(By.XPATH, self.signup_button)
        button.click()

    def switch_to_sign_in(self):
        button = self.driver.find_element(By.XPATH, self.sign_in_switch)
        button.click()
