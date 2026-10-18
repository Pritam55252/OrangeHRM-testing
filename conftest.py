import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import os
import time
driver=None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="Chrome",help="browser selection"
    )
@pytest.fixture(scope="function")
def browserinstance(request):
    global driver
    browsers_name=request.config.getoption("browser_name")
    if browsers_name=="Chrome":
        driver=webdriver.Chrome()
        driver.implicitly_wait(2)
        driver.maximize_window()
    elif browsers_name=="firefox":
        driver=webdriver.Firefox()
        driver.implicitly_wait(2)
        driver.maximize_window()
    yield driver

class Sidesearch:

    def __init__(self, driver):
        self.driver = driver
        self.searchbar = (By.XPATH, "//input[@placeholder='Search']")

    def search(self, optionname):
        wait = WebDriverWait(self.driver, 10)

        searchbox = wait.until(
            EC.visibility_of_element_located(self.searchbar)
        )

        searchbox.clear()
        searchbox.send_keys(optionname)

    def clicksearchresult(self, option):
        wait = WebDriverWait(self.driver, 10)

        result = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//span[normalize-space()='{option}']"
            ))
        )

        result.click()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browserinstance")

        if driver is None:
            return

        reports_dir = os.path.join(os.path.dirname(__file__), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        file_name = os.path.join(
            reports_dir,
            report.nodeid.replace("::", "_") + ".png"
        )

        driver.save_screenshot(file_name)
        print(f"Screenshot saved: {file_name}")

        pytest_html = item.config.pluginmanager.getplugin("html")

        if pytest_html:
            extras = getattr(report, "extras", [])
            extras.append(
                pytest_html.extras.image(
                    driver.get_screenshot_as_base64(),
                    name="Failure screenshot"
                )
            )
            report.extras = extras
            driver.close()

