



#conding:utf-8
#第一步导入webdriver模块
import time
from selenium import webdriver
import os
#第二步打开浏览器
driver = webdriver.Chrome()
#第三步打开百度
driver.get("http://www.baidu.com")
#等待3秒后刷新页面
time.sleep(3)
driver.refresh()
#设置窗口大小为540×960
driver.set_window_size(540,960)
time.sleep(3)
#将浏览器窗口最大化
time.sleep(2)
driver.maximize_window()


#截屏
driver.get_screenshot_as_file("D:\\test1.jpg")
#退出关闭页面
driver.quit()

