#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")

#删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#输入空格键+“教程”

driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

#crtl+a全选输入内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

#crtl+x剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

#crtl+v粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

#通过回车键来代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)

time.sleep(20)
driver.quit()
