#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'yangyh'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
# as 关键字将 expected_conditions 重命名为EC，并调用presence_of_element_located()方法判断元素是否存在
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#WebDriverWait 是由WebDriver提供的等待方法.
#在设置时间内,默认每隔一段时间检测一次当前页面元素是否存在,如果超过设置时间检测不到 则抛出异常
#具体格式:WebDriverWait(driver, timeout, poll_frequrncy=0.5, ignored_exceptions=None)
#Ddriver 浏览器驱动
#timeout：最长超时时间，默认以s为单位
#poll_frequency: 检测的间隔（步长）时间，默认为0.5s。
#ignored_exceptions:超时后的异常信息，默认情况下抛NotSuchElementException异常
#WebDriverWait一般由until（）或until_not（）方法配合使用
#until(method, message=''):调用该方法提供的驱动程序作为一个参数，直到返回值为True
#until_not(method, mrssage=''):调用该方法提供的驱动程序作为一个参数，直到返回值为False。
""" 等待并检查元素是否存在，不代表该元素一定可见"""
element = WebDriverWait(driver, 5, 0.5).until(
                    EC.presence_of_all_elements_located((By.ID, "kw"))
                    )
driver.find_element_by_id('kw').send_keys('selenium')

time.sleep(20)
driver.quit()

