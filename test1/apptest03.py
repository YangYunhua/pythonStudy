# -*- coding: utf-8 -*-
# -*- coding:gb18030 -*-
#!/usr/bin/python3
from appium import webdriver
import time
import os
import HTMLTestRunner  #需要下载HTMLTestRunner.py文件放在python安装目录的lib下
import unittest

#Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class elementA(unittest.TestCase):
    def test_(self):
        desired_caps={}
        desired_caps['deviceName'] = '6061705e'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1 MMB29M'
        desired_caps['appPackage'] = 'com.duowan.mobile'
        desired_caps['appActivity'] = 'com.yy.mobile.ui.splash.SplashActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps )

        el = driver.find_element_by_name(u"神曲")


desired_caps = {
                'platformName':'Android',
               # 'deviceName':'PJQDU15801002296',
                'deviceName':'6061705e',
                'platformVersion':'6.0.1 MMB29M',
                'appPackage':'com.taobao.taobao',
                'appActivity':'com.taobao.tao.welcome.Welcome',
                'unicodeKeyBoard': True,
                'resetKeyBoard': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps )

print('test1')
time.sleep(9)

driver.find_element_by_id('com.taobao.taobao:id/home_searchedit').click()
print('test2')
time.sleep(20)
driver.find_element_by_id('com.taobao.taobao:id/searchEdit').click()
print('test3')
time.sleep(9)
driver.find_element_by_id('com.taobao.taobao:id/searchEdit').send_keys(u"test")
print('test4')
