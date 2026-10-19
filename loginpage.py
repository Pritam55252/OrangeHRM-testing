from selenium.webdriver.common.by import By
from selenium import webdriver
from dashboard import Dashboard
class Login:
    def __init__(self,driver):
        self.driver=driver
        self.username=(By.XPATH,"//input[@name='username']")
        self.password=(By.XPATH,"//input[@type='password']")
        self.login=(By.XPATH,"//button[@type='submit']")

    def logins(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login).click()
        dash_board= Dashboard(self.driver)
        return dash_board
        print("m")
        print("q")


