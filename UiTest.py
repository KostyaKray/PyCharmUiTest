from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.yahoo.com/")

driver.find_element_by_id("uh-signin").click()
driver.implicitly_wait(5)
driver.find_element_by_id("login-username").send_keys("kostyakray@yahoo.com")
driver.find_element_by_name("signin").click()
driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys("asferrouitest")
driver.find_element_by_name("verifyPassword").click()

driver.quit()