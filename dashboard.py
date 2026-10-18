from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dashboard:
    def __init__(self,driver):
        self.driver=driver
        self.assignleave=(By.XPATH,"//button[@class='oxd-icon-button']")
        self.leavelist=(By.XPATH,"//button[@title='Leave List']")
        self.timesheets=(By.XPATH,"//div[@title='Timesheets']")
        self.applyleave=(By.XPATH,"//button[@title='Apply Leave']")
        self.myleave=(By.XPATH,"//button[@title='My Leave']")
        self.mytimesheet=(By.XPATH,"//button[@title='My Timesheet']")
        self.employeesleaveontoday=(By.XPATH,"//div/i[@class='oxd-icon bi-gear-fill orangehrm-leave-card-icon']")
        self.clickonswitch=(By.XPATH,"//div/div[@class='oxd-switch-wrapper']")
        self.save=(By.XPATH,"//button[@type='submit']")
        self.alert=(By.XPATH,"//div[@class='oxd-toast-container oxd-toast-container--bottom']")

    def quicklaunch(self):
        buttons = [
            ("Assign Leave", self.assignleave),
            ("Leave List", self.leavelist),
            ("Timesheets", self.timesheets),
            ("Apply Leave", self.applyleave),
            ("My Leave", self.myleave),
            ("My Timesheet", self.mytimesheet)
        ]

        for name, locator in buttons:
            print("Checking button:", name)

            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )

            print("Button is clickable:", name)

    def employeeleaveontoday(self):
        wait = WebDriverWait(self.driver, 30)

        # Click Employee Leave Today
        wait.until(
            EC.element_to_be_clickable(self.employeesleaveontoday)
        ).click()

        # Wait for loader to disappear
        wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, ".oxd-form-loader")
            )
        )

        # Wait for switch to become clickable
        switch = wait.until(
            EC.element_to_be_clickable(self.clickonswitch)
        )

        # Scroll switch into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            switch
        )

        # Check loader again before clicking
        wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, ".oxd-form-loader")
            )
        )

        wait.until(
            EC.element_to_be_clickable(self.clickonswitch)
        ).click()

        # Click Save
        wait.until(
            EC.element_to_be_clickable(self.save)
        ).click()

        # Verify success message
        message = wait.until(
            EC.visibility_of_element_located(self.alert)
        )

        assert "Success" in message.text


