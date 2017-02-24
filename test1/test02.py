#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//input[@id='kw']").send_keys("test")
time.sleep(5)

driver.set_window_size(480,800)
driver.get_screenshot_as_file("D:\\test2.png")
time.sleep(2)
driver.refresh()
driver.find_element_by_xpath("//input[@id='su']").click()
driver.quit()
