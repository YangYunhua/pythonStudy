#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.126.com")
time.sleep(10)
driver.find_element_by_xpath("//input[@name='email']").send_keys("h1332850274")
print("test1")
