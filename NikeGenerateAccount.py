import time
import requests
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def chooseSize(size):
    buttonList = driver.find_elements_by_tag_name('button')
    for i in buttonList:
        if i.text == size:
            i.click()

desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
# option = ChromeOptions()
# ip = 'ip：port'
# option.add_argument('--proxy-server=' + ip)
# options=option
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.nike.com/cn/")
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="AccountNavigationContainer"]/button').click()
# time.sleep(3)
# driver.find_element_by_partial_link_text("使用电子邮件登录。").click()
# time.sleep(2)
# driver.find_element_by_name("emailAddress").send_keys('wwzwwe@forstbite.me')
# driver.find_element_by_name("password").send_keys('Wwz990220')
# time.sleep(2)
# driver.find_element_by_css_selector("[value='登录']").click()
# time.sleep(5)
driver.get('https://www.nike.com/cn/launch/t/lebron-18-sisterhood-cn')
time.sleep(5)
chooseSize('41') 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/button').click()
