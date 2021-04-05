import random
import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

report = Report()
driver = webdriver.Chrome(
    executable_path="C:\\Users\\MASH\\PycharmProjects\\SeleniumProject01\\drivers\\chromedriver.exe")
report.setup(
    report_folder=r'Reports',
    module_name='Login Module',
    release_name='Release 1',
    selenium_driver=driver
)
driver.get('http://rumman.pythonanywhere.com/')

#Test case 1

try:
    # Start of Test
    report.write_step(
        'Navigate to Sign Up Page',
        status=report.status.Start,
        test_number=1
    )
    login = driver.find_element(By.LINK_TEXT,"Sign Up").click();


    results = driver.current_url
    print(results)
    assert "http://rumman.pythonanywhere.com/" == results
    report.write_step(
        'Successfully Navigate to Sign Up',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Naviagte Sign Up',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 2

try:
    # Start of Test
    report.write_step(
        'Sign Up Test',
        status=report.status.Start,
        test_number=2
    )
    username = driver.find_element_by_name("username")
    username.send_keys("wrong user name")
    password = driver.find_element_by_name("password1")
    password.send_keys("1234")
    password = driver.find_element_by_name("password2")
    password.send_keys("1234")
    driver.find_element_by_xpath("//button[@class='btn btn-outline-info']").click()

    time.sleep(2)
    results = driver.current_url
    print(results)
    assert "Success" in driver.page_source
    report.write_step(
        'Successfully Sign Up',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Sign Up',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 3

try:
    # Start of Test
    report.write_step(
        'Homepage to Login Page',
        status=report.status.Start,
        test_number=3
    )
    login = driver.find_element(By.LINK_TEXT,"Login").click();
    result = driver.current_url
    assert "login" in result
    report.write_step(
        'Successfully on Login page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to reach Login page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 4

try:
    # Start of Test
    report.write_step(
        'Login Test',
        status=report.status.Start,
        test_number=4
    )

    username = driver.find_element_by_name("username")
    username.send_keys('rumman18')
    password = driver.find_element_by_name("password")
    password.send_keys('ub%#ir_.yE8DnXK')
    driver.find_element_by_xpath("//button[@class='btn btn-outline-info']").click()
    time.sleep(5)

    results = driver.current_url

    assert "dashboard" in results
    report.write_step(
        'Successfully on Post',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to reach Post',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test Case 5
try:
    # Start of Test
    report.write_step(
        'Logout Test',
        status=report.status.Start,
        test_number=5
    )

    logout = driver.find_element(By.LINK_TEXT,"Logout").click();
    logout.send_keys(Keys.ENTER)

    results = driver.current_url
    print(results)
    assert "http://rumman.pythonanywhere.com/accounts/login/" == results
    report.write_step(
        'Successfully Logged out',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Logout',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 6

try:
    # Start of Test
    report.write_step(
        'Login to Insert a Post',
        status=report.status.Start,
        test_number=6
    )

    username = driver.find_element_by_name("username")
    username.send_keys('rumman18')
    password = driver.find_element_by_name("password")
    password.send_keys('ub%#ir_.yE8DnXK')
    driver.find_element_by_xpath("//button[@class='btn btn-outline-info']").click()
    time.sleep(5)
    driver.find_element_by_id("postDropdown").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Insert Post").click()
    time.sleep(2)

    results = driver.current_url

    assert "http://rumman.pythonanywhere.com/insertpost/" == results
    report.write_step(
        'Successfully on Insert Post Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to navigate Insert Post Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test Case 7

try:
    # Start of Test
    report.write_step(
        'Create A Post',
        status=report.status.Start,
        test_number=7
    )
    driver.find_element_by_name("Post_title").send_keys("This is the post title")
    driver.find_element_by_name("Post_location").send_keys("Dhaka")
    driver.find_element_by_id("id_Post_catagory").click()
    driver.find_element_by_name("Post_tags").send_keys("Dhaka,Testing")
    driver.find_element_by_name("Post_image").send_keys("C:\\Users\\MASH\\Desktop\\dhaka.jpg");
    time.sleep(5)
    driver.find_element_by_name("Post_description").send_keys("This is the content about dhaka city. It's a testing of inserting a post on travelmama")
    time.sleep(5)
    driver.find_element_by_name("insert_post_btn").click()

    results = driver.current_url

    assert "Post was successfully created" in driver.page_source
    report.write_step(
        'Successfully on Post Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to navigate Post Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 8

try:
    # Start of Test
    report.write_step(
        'Navigate to My Post',
        status=report.status.Start,
        test_number=8
    )
    mypost = driver.find_element(By.LINK_TEXT,"My Posts").click();


    results = driver.current_url
    print(results)
    assert "http://rumman.pythonanywhere.com/my_post/" == results
    report.write_step(
        'Successfully Navigate to My post',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Navigate My post',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 9

try:
    # Start of Test
    report.write_step(
        'Go to Update Profile',
        status=report.status.Start,
        test_number=9
    )
    driver.find_element_by_id("profileDropdown").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Show Profile").click()
    time.sleep(2)

    results = driver.current_url

    print(results)
    assert "http://rumman.pythonanywhere.com/profile/" == results
    report.write_step(
        'Successfully Navigate to Update Profile',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Navigate Update Profile',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 10

try:
    # Start of Test
    report.write_step(
        'Log out and go to About Us',
        status=report.status.Start,
        test_number=10
    )
    logout = driver.find_element(By.LINK_TEXT, "Logout").click();
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "About Us").click();
    time.sleep(2)
    results = driver.current_url
    print(results)
    assert "http://rumman.pythonanywhere.com/about-us/" == results
    report.write_step(
        'Successfully Logged out and visit about page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Logout and visit about page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 11

try:
    # Start of Test
    report.write_step(
        'Go to Sign Up',
        status=report.status.Start,
        test_number=11
    )
    logout = driver.find_element(By.LINK_TEXT, "Sign Up").click();
    time.sleep(2)

    results = driver.current_url
    print(results)
    assert "http://rumman.pythonanywhere.com/registration/" == results
    report.write_step(
        'Successfully visited sign up',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to visit sign up',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 12

try:
    # Start of Test
    report.write_step(
        'New Sign Up Test',
        status=report.status.Start,
        test_number=12
    )

    username = driver.find_element_by_name("username")
    username.send_keys("mashnew18")
    password = driver.find_element_by_name("password1")
    password.send_keys("mashnew18mashnew18")
    password = driver.find_element_by_name("password2")
    password.send_keys("mashnew18mashnew18")
    driver.find_element_by_xpath("//button[@class='btn btn-outline-info']").click()

    time.sleep(2)
    results = driver.current_url
    print(results)
    assert "Success" in driver.page_source
    report.write_step(
        'Successfully Sign Up',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Sign Up',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )
#Test case 13

try:
    # Start of Test
    report.write_step(
        'Go to Login Page',
        status=report.status.Start,
        test_number=13
    )
    login = driver.find_element(By.LINK_TEXT,"Login").click();
    result = driver.current_url
    assert "login" in result
    report.write_step(
        'Successfully on Login page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to reach Login page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test case 14

try:
    # Start of Test
    report.write_step(
        'Login Test',
        status=report.status.Start,
        test_number=14
    )

    username = driver.find_element_by_name("username")
    username.send_keys('mashnew18')
    password = driver.find_element_by_name("password")
    password.send_keys('mashnew18mashnew18')
    driver.find_element_by_xpath("//button[@class='btn btn-outline-info']").click()
    time.sleep(5)

    results = driver.current_url

    assert "dashboard" in results
    report.write_step(
        'Successfully on Post',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to reach Post',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Report Generation
report.generate_report()
driver.quit()