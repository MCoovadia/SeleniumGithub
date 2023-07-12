"""Selenium testing on Github"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

username_box = browser.find_element(By.ID,"login_field")
username_box.send_keys("ninjacoder22")
password_box = browser.find_element(By.ID,"login_field")
password_box.send_keys("todayismonday1")
password_box.submit()

assert "ninjacoder22" in browser.page_source

profile_link = browser.find_element(By.CLASS_NAME, "user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "ninjacoder22" in link_label

browser.quit()
