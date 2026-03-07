import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
c_driver=webdriver.Chrome(options=opts)
ac=ActionChains(c_driver)

c_driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

#QUESTION 1
c_driver.find_element('xpath','(//a[contains(text(),"Books")])[1]').click()
ac.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
c_driver.find_element('xpath','//input[@value="Add to cart"]').click()
time.sleep(2)
ac.send_keys(Keys.PAGE_UP).perform()
time.sleep(2)
c_driver.find_element('xpath','//span[text()="Shopping cart"]').click()


#QUESTION 2
# c_driver.find_element('xpath','(//a[contains(text(),"Electronics")])[1]').click()
# time.sleep(2)
# c_driver.find_element('xpath','(//a[contains(text(),"Cell phones")])[3]').click()
# time.sleep(2)

#QUESTION 3

# c_driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# time.sleep(2)
#
# c_driver.find_element('xpath','//button[text()="Start"]').click()
# time.sleep(6)
# text = c_driver.find_element("xpath", '//h4[text()="Hello World!"]').text
# print("Text displayed:", text)

#QUESTION 4
# c_driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# time.sleep(2)
# c_driver.find_element("xpath", "//button[text()='Remove']").click()
# time.sleep(5)

# c_driver.find_element("xpath", "//button[text()='Add']").click()

#QUESTION 5
# c_driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
# dropdown = c_driver.find_element("xpath", "//div[@id='withOptGroup']")
# dropdown.click()
# time.sleep(2)
# c_driver.find_element("xpath", "//div[text()='Group 2, option 1']").click()

#Question 6
# c_driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
#
# c_driver.execute_script("window.scrollBy(0,600)")
# time.sleep(2)
#
# multi = Select(c_driver.find_element("xpath", "//select[@id='cars']"))
#
# multi.select_by_visible_text("Volvo")
# multi.select_by_visible_text("Saab")
# multi.select_by_visible_text("Opel")
#
# for option in multi.all_selected_options:
#     print(option.text)

#QUESTION 7
# c_driver.get("https://demoqa.com/menu/")
# time.sleep(2)
#
# action = ActionChains(c_driver)
#
# main = c_driver.find_element("xpath", "//a[text()='Main Item 2']")
# action.move_to_element(main).perform()
# time.sleep(2)
#
# sub = c_driver.find_element("xpath", "//a[text()='SUB SUB LIST »']")
# action.move_to_element(sub).perform()
# time.sleep(2)
#
# item = c_driver.find_element("xpath", "//a[text()='Sub Sub Item 1']")
# item.click()

#QUESTION 8
# c_driver.get("https://demoqa.com/droppable")
# time.sleep(3)
#
# drag = c_driver.find_element("xpath", "//div[@id='draggable']")
# drop = c_driver.find_element("xpath", "//div[@id='droppable']")
#
# action = ActionChains(c_driver)
#
# action.click_and_hold(drag).move_to_element(drop).release().perform()
#
# time.sleep(2)
#
# result = c_driver.find_element("xpath", "//div[@id='droppable']").text
# print(result)

#QUESTION 9

# c_driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(2)
#
# c_driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()
#
# alert = c_driver.switch_to.alert
# alert.accept()
#
# result = c_driver.find_element("xpath", "//p[@id='result']").text
# print(result)


#QUESTION 10
# c_driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(2)
#
# c_driver.find_element("xpath", "//input[@id='file-upload']").send_keys("C:\\Users\\KIIT\\Desktop\\capg_assessment.txt")
#
# c_driver.find_element("xpath", "//input[@id='file-submit']").click()
#
# print(c_driver.find_element("xpath", "//h3").text)
