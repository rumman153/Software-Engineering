from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\MASH\\PycharmProjects\\SeleniumProject01\\drivers\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("UAP")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
driver.close()
print("sample test case successfully completed")