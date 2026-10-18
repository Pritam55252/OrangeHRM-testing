from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import Sidesearch
class Usermanagementadmins:
    def __init__(self,driver):
        self.driver=driver
        self.common = Sidesearch(driver)
        self.adding=(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.username=(By.XPATH,"//label[normalize-space()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.userrole= (By.XPATH,"//label[normalize-space()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
        self.employeehint=(By.XPATH,"//input[@placeholder='Type for hints...']")
        self.employeedropdown = (
            By.XPATH,
            "//div[@role='listbox' and contains(@class,'oxd-autocomplete-dropdown')]"
        )
        self.status=(By.XPATH,"//label[normalize-space()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
        self.password=(By.XPATH,"//label[normalize-space()='Password']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.confirm_password=(By.XPATH,"//label[normalize-space()='Confirm Password']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.save=(By.XPATH,"// button[@type = 'submit']")

    def search_admin(self):
        self.common.searchbar("Admin")

    def add(self):
        wait = WebDriverWait(self.driver, 15)

        button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[normalize-space()='Add']"
            ))
        )
        button.click()
    def adduser(self):
        wait = WebDriverWait(self.driver, 15)

        # 1. User Role dropdown open karo
        wait.until(
            EC.element_to_be_clickable(self.userrole)
        ).click()

        # 2. ESS option ka wait karke click karo
        wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@role='option']//span[normalize-space()='ESS']"
            ))
        ).click()
        employee = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.employeehint)
        )
        employee.send_keys("a")

        # Wait for autocomplete dropdown
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.employeedropdown)
        )

        # Select matching employee suggestion
        employee_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@role='listbox']//span[normalize-space()='Peter Mac Anderson']"
            ))
        )
        employee_option.click()

        wait.until(
            EC.element_to_be_clickable(self.status)
        ).click()

        # 6. Enabled option select karo
        wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@role='option']//span[normalize-space()='Enabled']"
            ))
        ).click()

        self.driver.find_element(*self.username).send_keys("Pritam9889")
        self.driver.find_element(*self.password).send_keys("Pritam@9889")
        self.driver.find_element(*self.confirm_password).send_keys("Pritam@9889")
        self.driver.find_element(*self.save).click()








