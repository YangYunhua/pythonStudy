#!/usr/bin/python3
# -*- coding: utf-8 -*-
import HTMLTestRunner

__author__ = 'yangyh'

import requests,unittest,json
class Testbaidu(unittest.TestCase):
    def setUp(self):
        url="http://fanyi.baidu.com/v2transapi"

    def testzhen(self):
        #接口参数
        params = {
        "from":"en",
        "to":"zh",
        "query":"study"
     }
        url="http://fanyi.baidu.com/v2transapi"
        #发送参数
        r = requests.request("post",url,params=params)
        r = json.loads(r.text)
        assert (u'学习'in r['liju_result']['tag'])
"""
    def testzhen2(self):
        params = {
            "from":"en",
            "to":"h",
            "query":"stud"
        }
        url="http://fanyi.baidu.com/v2transapi"
        #发送参数
        r = requests.request("post",url,params=params)
        r = json.loads(r.text)
        assert (u'学'in r['liju_result']['tag'])

     def tearDown(self):
        pass
"""
if __name__ == '__main__':
    report_dir=r's.html'
    re_open=open(report_dir,'wb')
    suite=unittest.TestLoader().loadTestsFromTestCase(Testbaidu)
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=re_open,
        title=u'百度翻译api接口测试',
        description=u'百度翻译api接口测试详情'
    )
    runner.run(suite)