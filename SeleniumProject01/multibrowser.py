from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\MASH\\PycharmProjects\\SeleniumProject01\\drivers\\chromedriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()

elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." not in driver.page_source
driver.close()
print("sample test case successfully completed")
