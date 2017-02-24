# -*- coding: utf-8 -*-
# -*- coding:gb18030 -*-
#!/usr/bin/python3
from appium import webdriver
import time
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
