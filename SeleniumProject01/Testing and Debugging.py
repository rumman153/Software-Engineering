from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Users\\MASH\\PycharmProjects\\SeleniumProject01\\drivers\\chromedriver.exe")

#Test-1: Visit url and print it
driver.get("http://rumman.pythonanywhere.com/")
print(driver.current_url)

#Test-2: Get the url title
print(driver.title)

#Test-3: Click on "About us" to go to that page

driver.find_element(By.XPATH,"//a[contains(text(),'About Us')]").click()
time.sleep(2)

#Test-4: Search for sajek
driver.find_element_by_name("search").send_keys("sajek")



