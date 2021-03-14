from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\MASH\\PycharmProjects\\SeleniumProject01\\drivers\\chromedriver.exe")
driver.get("http://127.0.0.1:8000/accounts/login/")

driver.find_element_by_name("username").send_keys("rumman18")
driver.find_element_by_name("password").send_keys("ub%#ir_.yE8D") #wrong password

driver.find_element_by_name("signin").send_keys(Keys.ENTER)

driver.find_element_by_name("username").clear()
driver.find_element_by_name("password").clear()
time.sleep(3)
driver.find_element_by_name("username").send_keys("rumman18")
driver.find_element_by_name("password").send_keys("ub%#ir_.yE8DnXK")

driver.find_element_by_name("signin").send_keys(Keys.ENTER)

time.sleep(3)
driver.close()
print("sample test case successfully completed")