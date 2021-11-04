<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import threading
import time
from faker import Faker
faker = Faker('zh_TW')
from random import randrange

'''
def loggin():
    options = Options()
    options.add_argument("--disable-notifications")
    url = 'https://tms-ap.awayspeed.com/login.aspx'
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url)
    time.sleep(2)
    logcompany = chrome.find_element_by_id("txtdept")
    logcompany.send_keys("adata_test")
    logaccount = chrome.find_element_by_id("txtaccount")
    logaccount.send_key("adata_test")
    logpasswd = chrome.find_element_by_id("txtpassword")
    logpasswd.send_keys("0000")

    input('請手動登入')
    url = 'https://tms-ap.awayspeed.com/p3_4.aspx'
    chrome.get(url)
    print("done")
'''
class driveradd():
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        url = 'https://tms-ap.awayspeed.com/login.aspx'
        self.chrome = webdriver.Chrome('./chromedriver')
        self.chrome.get(url)

        logcompany = self.chrome.find_element_by_id("txtdept")
        logcompany.send_keys("test10")
        logpasswd = self.chrome.find_element_by_id("txtpassword")
        logpasswd.send_keys("0000")
        logaccount = self.chrome.find_element_by_id("txtaccount")
        logaccount.send_keys("admin")
        input('請手動登入')

        #########
    def setupvariable(self,appaccount, apppasswd, station, name, phonenumber, worktimelimit):
        #變數設定
        self.appaccount = appaccount
        self.apppasswd = apppasswd
        self.station = station
        self.name = name
        self.phonenumber = phonenumber
        self.worktimelimit = worktimelimit
        ########
    def execuadddriver(self):
        #輸入執行

        self.chrome.get("https://tms-ap.awayspeed.com/index.aspx")
        self.chrome.get('https://tms-ap.awayspeed.com/p3_4.aspx')

        self.o_driveradd = self.chrome.find_element_by_id("ContentPlaceHolder1_btnDriverAdd")
        self.o_driveradd.click()
        time.sleep(1)
        self.o_appaccount = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtuser_no")
        self.o_appaccount.send_keys(self.appaccount)

        self.o_apppasswd = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtuser_pwd")
        self.o_apppasswd.send_keys(self.apppasswd)

        self.o_name = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtuser_name")
        self.o_name.send_keys(self.name)

        self.o_phonenumber = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtmobile")
        self.o_phonenumber.send_keys(self.phonenumber)

        self.o_worktimelimit = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtmax_worktime")
        self.o_worktimelimit.send_keys(self.worktimelimit)

        self.o_authority = self.chrome.find_element_by_id("chkfunS")
        self.o_authority.click()



        #self.o_vehicle = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_ddlcar_id_chosen")
        #self.o_vehicle.click()
        #time.sleep(3)
        self.chrome.execute_script("document.getElementById('ContentPlaceHolder1_ucDriver1_ddlcar_id').style.display='inline-block';")
        time.sleep(0.5)
        self.chrome.execute_script("document.getElementById('ContentPlaceHolder1_ucDriver1_ddlcar_id').style.display='inline-block';")
        time.sleep(0.5)
        self.chrome.execute_script("document.getElementById('ContentPlaceHolder1_ucDriver1_ddlcar_id').style.display='inline-block';")
        #self.o_vehicle_select = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_ddlcar_id")
        #self.o_vehicle.send_keys(Keys.DOWN)
        #self.o_vehicle.send_keys(Keys.ENTER)
        #action_key_down = ActionChains(self.chrome).move_to_element(self.o_vehicle_select).key_down(Keys.DOWN).key_up(Keys.DOWN)
        #action_key_enter = ActionChains(self.chrome).move_to_element(self.o_vehicle_select).key_down(Keys.RETURN)
        #action_key_down
        #action_key_enter
        self.o_vehicle_slect = Select(self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_ddlcar_id"))
        self.o_vehicle_slect.select_by_index(1)
        #self.o_vehicle_slect.click()

        self.o_station = Select(self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_ddlstation_id"))
        self.o_station.select_by_index(1)

        time.sleep(1)
        self.o_responsibility_zone = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_cb_All")
        self.o_responsibility_zone.click()

        self.o_save = self.chrome.find_element_by_id("ContentPlaceHolder1_btnSave01")
        self.o_save.click()
        time.sleep(1.5)
        self.chrome.switch_to_alert().accept()

def foraddthread():
    driver = driveradd()
    for i in range(100):
        appaccount = "driver_" + str(i)
        apppasswd = "0000"
        station = "a"
        name = faker.name()
        phonenumber = '09' + "".join([str(randrange(0, 10)) for _ in range(8)])
        worktimelimit = "40"

        driver.setupvariable(appaccount, apppasswd, station, name, phonenumber, worktimelimit)
        driver.execuadddriver()


if __name__ == '__main__':
    addthread = []
    foraddthread()
    """
    for i in range(1):
        addthread.append(threading.Thread(target = foraddthread()))
        addthread[i].start()
    """
=======
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import threading
import time
from faker import Faker
faker = Faker('zh_TW')
from random import randrange

'''
def loggin():
    options = Options()
    options.add_argument("--disable-notifications")
    url = 'https://tms-ap.awayspeed.com/login.aspx'
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url)
    time.sleep(2)
    logcompany = chrome.find_element_by_id("txtdept")
    logcompany.send_keys("adata_test")
    logaccount = chrome.find_element_by_id("txtaccount")
    logaccount.send_key("adata_test")
    logpasswd = chrome.find_element_by_id("txtpassword")
    logpasswd.send_keys("0000")

    input('請手動登入')
    url = 'https://tms-ap.awayspeed.com/p3_4.aspx'
    chrome.get(url)
    print("done")
'''
class driveradd():
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        url = 'https://tms-ap.awayspeed.com/login.aspx'
        self.chrome = webdriver.Chrome('./chromedriver')
        self.chrome.get(url)

        logcompany = self.chrome.find_element_by_id("txtdept")
        logcompany.send_keys("test10")
        logpasswd = self.chrome.find_element_by_id("txtpassword")
        logpasswd.send_keys("0000")
        logaccount = self.chrome.find_element_by_id("txtaccount")
        logaccount.send_keys("admin")
        input('請手動登入')

        #########
    def setupvariable(self,appaccount, apppasswd, station, name, phonenumber, worktimelimit):
        #變數設定
        self.appaccount = appaccount
        self.apppasswd = apppasswd
        self.station = station
        self.name = name
        self.phonenumber = phonenumber
        self.worktimelimit = worktimelimit
        ########
    def execuadddriver(self):
        #輸入執行

        self.chrome.get("https://tms-ap.awayspeed.com/index.aspx")
        self.chrome.get('https://tms-ap.awayspeed.com/p3_4.aspx')

        self.o_driveradd = self.chrome.find_element_by_id("ContentPlaceHolder1_btnDriverAdd")
        self.o_driveradd.click()
        time.sleep(1)
        self.o_appaccount = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtuser_no")
        self.o_appaccount.send_keys(self.appaccount)

        self.o_apppasswd = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtuser_pwd")
        self.o_apppasswd.send_keys(self.apppasswd)

        self.o_name = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtuser_name")
        self.o_name.send_keys(self.name)

        self.o_phonenumber = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtmobile")
        self.o_phonenumber.send_keys(self.phonenumber)

        self.o_worktimelimit = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_txtmax_worktime")
        self.o_worktimelimit.send_keys(self.worktimelimit)

        self.o_authority = self.chrome.find_element_by_id("chkfunS")
        self.o_authority.click()



        #self.o_vehicle = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_ddlcar_id_chosen")
        #self.o_vehicle.click()
        #time.sleep(3)
        self.chrome.execute_script("document.getElementById('ContentPlaceHolder1_ucDriver1_ddlcar_id').style.display='inline-block';")
        time.sleep(0.5)
        self.chrome.execute_script("document.getElementById('ContentPlaceHolder1_ucDriver1_ddlcar_id').style.display='inline-block';")
        time.sleep(0.5)
        self.chrome.execute_script("document.getElementById('ContentPlaceHolder1_ucDriver1_ddlcar_id').style.display='inline-block';")
        #self.o_vehicle_select = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_ddlcar_id")
        #self.o_vehicle.send_keys(Keys.DOWN)
        #self.o_vehicle.send_keys(Keys.ENTER)
        #action_key_down = ActionChains(self.chrome).move_to_element(self.o_vehicle_select).key_down(Keys.DOWN).key_up(Keys.DOWN)
        #action_key_enter = ActionChains(self.chrome).move_to_element(self.o_vehicle_select).key_down(Keys.RETURN)
        #action_key_down
        #action_key_enter
        self.o_vehicle_slect = Select(self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_ddlcar_id"))
        self.o_vehicle_slect.select_by_index(1)
        #self.o_vehicle_slect.click()

        self.o_station = Select(self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_ddlstation_id"))
        self.o_station.select_by_index(1)

        time.sleep(1)
        self.o_responsibility_zone = self.chrome.find_element_by_id("ContentPlaceHolder1_ucDriver1_cb_All")
        self.o_responsibility_zone.click()

        self.o_save = self.chrome.find_element_by_id("ContentPlaceHolder1_btnSave01")
        self.o_save.click()
        time.sleep(1.5)
        self.chrome.switch_to_alert().accept()

def foraddthread():
    driver = driveradd()
    for i in range(100):
        appaccount = "driver_" + str(i)
        apppasswd = "0000"
        station = "a"
        name = faker.name()
        phonenumber = '09' + "".join([str(randrange(0, 10)) for _ in range(8)])
        worktimelimit = "40"

        driver.setupvariable(appaccount, apppasswd, station, name, phonenumber, worktimelimit)
        driver.execuadddriver()


if __name__ == '__main__':
    addthread = []
    foraddthread()
    """
    for i in range(1):
        addthread.append(threading.Thread(target = foraddthread()))
        addthread[i].start()
    """
>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
