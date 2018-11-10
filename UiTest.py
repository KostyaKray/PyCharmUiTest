from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.yahoo.com/")
#driver.fullscreen_window()
driver.find_element_by_id("uh-signin").click()
sleep(1)
# вводим логин
driver.find_element_by_id("login-username").send_keys("kostyakray@yahoo.com")
driver.find_element_by_name("signin").click()
sleep(2)

# вводим пароль
driver.find_element_by_name("password").send_keys("asferrouitest")
driver.find_element_by_name("verifyPassword").click()
sleep(1)

# нажимаем кнопку Mail
driver.find_element_by_xpath("//a[@id='uh-mail-link']").click()
sleep(1)

#После успешного логина нажимаем кнопку создать письмо
driver.find_element_by_css_selector("[data-test-id='compose-button']").click()

#Ввожу почту получателя, тему письма и текст письма, и нажимаю отправить
driver.find_element_by_id("message-to-field").send_keys("kostyakray@yahoo.com")
driver.find_element_by_xpath("//*[@aria-label='Тема']").send_keys("hello1")
driver.find_element_by_xpath("//div[@role='textbox']").send_keys("hellooooooy")
driver.find_element_by_css_selector("[data-test-id='compose-send-button']").click()


#Проверяем что письмо доставлено#
sleep(15)
driver.refresh()
element = driver.find_element_by_css_selector("[title='hello1']")
if element.is_displayed(): 
    print('Письмо успешно доставлено')
else: 
    print('Письмо не доставлено')

driver.quit()





