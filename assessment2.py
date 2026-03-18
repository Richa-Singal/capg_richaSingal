import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

 # -----------------------------------TASK1------------------------------------
# driver.get('https://www.facebook.com/')
# wait_obj=WebDriverWait(driver, 20)
# driver.find_element('xpath','//input[@name="email"]').send_keys('##username')
# driver.find_element('xpath','//input[@name="pass"]').send_keys('##password')
# driver.find_element('xpath','//span[text()="Log in"]').click()
# try:
#     wait_obj.until(EC.visibility_of_element_located(('xpath','//span[@id="_R_6lal8pl5bb6ismj5ilipam_"]')))
#     print("Verification Successful")
# except:
#     print("Verification Failed")

# -----------------------------------TASK2------------------------------------
# driver.get("https://www.myntra.com/")
# time.sleep(3)
#
# driver.find_element('class name', 'desktop-searchBar').send_keys("puma")
# time.sleep(3)
#
# driver.find_element('xpath', '//li[text()="Puma Shoes"]').click()
# time.sleep(4)
#
# driver.find_element('xpath', '(//div[@class="product-productMetaInfo"])[1]').click()
# time.sleep(3)
#
# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])
# time.sleep(3)
#
# try:
#     driver.find_element('xpath', '(//div[contains(@class,"size-buttons-size-buttons")]//button)[1]').click()
#     time.sleep(2)
# except:
#     print("Size not required")
#
# driver.find_element('xpath', '(//P[@class="size-buttons-unified-size"])[4]').click()
# driver.find_element('xpath', '//div[contains(@class,"pdp-add-to-bag")]').click()
# print("Product added to cart")

# -----------------------------------TASK3------------------------------------

# driver.get("https://www.icici.bank.in/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element("xpath", "//span[contains(text(),' Accounts')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", '(//a[@class="button-btn button-btn-primary button-btn-medium"])[2]').click()
# time.sleep(3)
#
# driver.switch_to.window(driver.window_handles[1])
#
# driver.find_element("xpath", '//input[@id="name"]').send_keys("hel")
# driver.find_element("xpath", '//input[@name="pan"]').send_keys("PWMPS3412N")
# driver.find_element("xpath", '//input[@name="pincode"]').send_keys("751024")
# driver.find_element("xpath", '//input[@id="mobile_number"]').send_keys("9231313123")
# driver.find_element('xpath','//input[@id="otp"]').send_keys("1234")
# driver.find_element('xpath','//input[@id="checkbox"]').click()
# driver.find_element("xpath", "//button[contains(text(),'Apply')]").click()
# time.sleep(2)
#
# print("Validation message displayed")

# -----------------------------------TASK4------------------------------------

# driver.get("https://www.netmeds.com/")
# time.sleep(3)
#
# ac = ActionChains(driver)
# menu = driver.find_element("xpath", "//a[text()=' Medicine ']")
# ac.move_to_element(menu).perform()
# time.sleep(3)
#
# driver.find_element("xpath", "//a[text()='Order Online']").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//button[text()=' Upload Prescription ']").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@type='file']").send_keys("C:\\Users\\KIIT\\Desktop\\capg_assessment.txt")
# time.sleep(3)
# -----------------------------------TASK5------------------------------------
# driver.get("https://www.netmeds.com/")
# time.sleep(2)
#
# driver.find_element("xpath", '//div[@class="position-relative profile-name"]').click()
# time.sleep(2)
#
# driver.find_element("xpath", '//input[@type="number"]').send_keys("9142610410")
# driver.find_element("xpath", "//button[text()=' Get OTP ']").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@type='tel']").send_keys("123456")
# time.sleep(3)

# -----------------------------------TASK6------------------------------------
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# wait = WebDriverWait(driver, 20)
#
# time.sleep(5)
#
# from_box = wait.until(EC.element_to_be_clickable(
#     ("xpath", "(//input[@role='searchbox'])[1]")
# ))
# from_box.click()
# from_box.send_keys("KOLKATA")
#
# time.sleep(2)
# driver.find_element("xpath", "//span[contains(text(),'KOLKATA')]").click()
#
# to_box = driver.find_element("xpath", "(//input[@role='searchbox'])[2]")
# to_box.click()
# to_box.send_keys("DELHI")
#
# time.sleep(2)
# driver.find_element("xpath", "//span[contains(text(),'DELHI')]").click()
#
# date_box = wait.until(EC.element_to_be_clickable(
#     ("xpath", "(//input[@type='text'])[3]")
# ))
# date_box.click()
#
# time.sleep(2)
#
# driver.find_element("xpath", "//a[text()='25']").click()
#
# search_btn = wait.until(EC.element_to_be_clickable(
#     ("xpath", "//button[contains(text(),'Search')]")
# ))
# search_btn.click()
#
# time.sleep(5)

# -----------------------------------TASK7------------------------------------

# driver.get("https://www.purplle.com/")
# time.sleep(3)
#
# ac = ActionChains(driver)
# menu = driver.find_element("xpath", "//a[contains(text(),'BRANDS')]")
# ac.move_to_element(menu).perform()
#
# driver.find_element("xpath", '//input[@placeholder="Search for brands..."]').send_keys("lakme")
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0,500)")
# driver.find_element("xpath", '''//img[contains(@alt,'Lakme Sunscreen')]")''').click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@placeholder='Enter Pincode']").send_keys("700001")
# time.sleep(2)

# -----------------------------------TASK8------------------------------------
# driver.get("https://lifeinsurance.adityabirlacapital.com/")
# time.sleep(3)
#
# driver.find_element("xpath", '//button[text()="Avail now"]').click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input").send_keys("Richa")
# time.sleep(3)
#
# driver.find_element("xpath", '//input[@id="lastName"]').send_keys("Singal")
# time.sleep(3)
#
# driver.find_element("xpath", '//input[@id="email"]').send_keys("richa12@gmail.com")
# time.sleep(3)
#
# driver.find_element("xpath", '//input[@id="phonenumber"]').send_keys("9142610410")
# time.sleep(3)

# ------------------------------------TASK9------------------------------------

# driver.get("https://www.apollopharmacy.in/")
# time.sleep(5)
#
# driver.find_element("xpath", "//a[contains(text(),'Find Doctors')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//a[contains(text(),'General Physician')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", "(//div[contains(@class,'doctor')])[1]").click()
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Continue"]').click()

# ------------------------------------TASK10------------------------------------
# driver.get("https://porter.in/")
# time.sleep(3)
#
# driver.find_element("xpath", '//p[@class="CitySelector_city-selector-text__hWWNe"]').click()
# time.sleep(2)
#
# driver.find_element('xpath','(//img[@alt="City Image"])[1]').click()
# time.sleep(2)
#
# driver.find_element("xpath", "//div[contains(text(),'Packers')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@placeholder='Pickup']").send_keys("Sailashree vihar2")
# driver.find_element("xpath", "//input[@placeholder='Drop']").send_keys("ranchi")
#
# driver.find_element("xpath", "//input[@type='tel']").send_keys("9999999999")
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@type='date']").send_keys("25-03-2026")
# time.sleep(3)