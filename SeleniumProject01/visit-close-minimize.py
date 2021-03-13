from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="C:\\Users\\MASH\\PycharmProjects\\SeleniumProject01\\drivers\\chromedriver.exe")
driver.get("https://www.uap-bd.edu/")
print(driver.current_url)
#print("\n")
#print(driver.title)
time.sleep(2)
#driver.maximize_window() # maximize out table

driver.get("https://www.python.org/")
print(driver.current_url)
time.sleep(2)

driver.back() #uap
print(driver.current_url)
time.sleep(2)

driver.forward() #python
print(driver.current_url)
time.sleep(2)

driver.close()
print("Test successful")