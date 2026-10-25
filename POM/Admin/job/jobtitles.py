from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Jobtitle:
    def __init__(self,driver):
        self.driver=driver
        self.admin=(By.XPATH,"//a[@class='oxd-main-menu-item active']")
        self.job=(By.XPATH,"//span[normalize-space()='Job']")
        self.list=(By.XPATH,"//a[normalize-space()='Job Titles']")
        self.name=(By.XPATH,"//div[@class='oxd-table-row oxd-table-row--with-border']")
        self.checkbox=(By.XPATH,"//div[@class='oxd-table-card-cell-checkbox']")
        self.delete_selected=(By.XPATH,"//i[@class='oxd-icon bi-trash-fill oxd-button-icon']")
        self.yes_delete=(By.XPATH,"//i[@class='oxd-icon bi-trash oxd-button-icon']")
        self.add_jobtitle=(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']")
        self.jobtitle_name=(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        self.jobdescription=(By.XPATH,"//div/textarea[@placeholder='Type description here']")
        self.add_document=(By.XPATH,"//input[@type='file']")
        self.addnote=(By.XPATH,"//div/textarea[@placeholder='Add note']")
        self.save=(By.XPATH,"//button[text()=' Save ']")


    def jobbutton(self):
        self.driver.find_element(*self.admin).click()
        n=WebDriverWait(self.driver,15)
        n.until(EC.element_to_be_clickable(self.job)).click()
        n.until(EC.element_to_be_clickable(self.list)).click()
    def delete_jobtittle(self):
        k=self.driver.find_elements(*self.name)
        for m in k:
            if m.text.strip()=="Chief Technical Officer":
                m.find_element(*self.checkbox).click()
        n=WebDriverWait(self.driver,15)
        n.until(EC.element_to_be_clickable(self.delete_selected)).click()
        n.until(EC.element_to_be_clickable(self.yes_delete)).click()
        n.until(EC.element_to_be_clickable(self.add_jobtitle)).click()
    def addjobtitle(self):
        self.driver.find_element(*self.jobtitle_name).send_keys("automation tester")
        self.driver.find_element(*self.jobdescription).send_keys("selenium,python,jenkins")
        c=self.driver.find_element(*self.add_document)
        c.send_keys(r"C:\Users\prita\Downloads\Pritam_Kumar_Pradhan_v2.pdf")
        self.driver.find_element(*self.addnote).send_keys("hii pritam")
        self.driver.find_element(*self.save).click()

    def capture_message(self):
        end_time = time.time() + 10

        while time.time() < end_time:
            text = self.driver.find_element(By.TAG_NAME, "body").text

            if "Successfully Saved" in text:
                print("Popup message found:", text)
                return text

            time.sleep(0.1)

        raise AssertionError("Expected message not found")



















