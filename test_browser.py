import time
import json
import pytest
from loginpage import Login
from conftest import Sidesearch
from POM.Admin.usermanagementadmin import Usermanagementadmins

test_data_path="Data/Data.json"
with open(test_data_path)as f:
    test_data=json.load(f)
    login_data=test_data["logincredential"]
s="file:///C:/Users/prita/Downloads/Pritam_Kumar_Pradhan_v2.pdf"
@pytest.mark.parametrize("login_test_list",login_data)
def testinstancebrowser(browserinstance, login_test_list):
    driver=browserinstance
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)
    loginpage=Login(driver)
    dash_board=loginpage.logins(login_test_list["username"],login_test_list["password"])
    dash_board.quicklaunch()
    dash_board.employeeleaveontoday()
    common=Sidesearch(driver)
    options=[
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard",
        "Directory"
    ]
    for option in options:
        common.search(option)

        if option == "Admin":
            # Admin search result par click
            common.clicksearchresult("Admin")

            # Admin page par Add button click
            usermanageadmin = Usermanagementadmins(driver)
            usermanageadmin.add()
            jobtitle=usermanageadmin.adduser()

            # Loop stop
            break


    jobtitle.jobbutton()
    jobtitle.delete_jobtittle()
    jobtitle.addjobtitle()
    jobtitle.capture_message()

    driver.close()









