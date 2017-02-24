import unittest
import paramunittest
from common import common
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp

productInfo_xls = common.get_xls("productCase.xlsx", "getProductInfo")
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()


@paramunittest.parametrized(*productInfo_xls)
class ProductInfo(unittest.TestCase):
    def setParameters(self, case_name, url, goods_id, code, msg, hope):
        """
        set params
        :param case_name:
        :param url:
        :param goods_id:
        :param code:
        :param msg:
        :param hope:
        :return:
        """
        self.case_name = str(case_name)
        self.url = str(url)
        self.goodsId = str(goods_id)
        self.code = code
        self.msg = str(msg)
        self.hope = hope
        self.response = None
        self.info = None

    def description(self):
        self.case_name

    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def tearDown(self):
        pass

    def testGetProductInfo(self):
        try:
            # set uel
            localConfigHttp.set_url(self.url)
            # set params
            params = {"goods_id": self.goodsId}
            localConfigHttp.set_params(params)
            # set headers
            token_v = localReadConfig.get_headers("TOKEN_V")
            headers = {"token": str(token_v)}
            localConfigHttp.set_headers(headers)
            # get http
            self.response = localConfigHttp.get()
            # check result
            self.checkResult()

        except Exception as ex:
            self.logger.error(str(ex))

    def checkResult(self):
        self.info = self.response.json()
        if self.info['code'] == self.code and self.info['info']['Product'] is not None:
            goods_id = common.get_value_from_return_json(self.info, "Product", "goods_id")
            self.assertEqual(self.goodsId, goods_id)
            self.log.build_OK_line(self.case_name, self.code, self.msg)
        else:
            self.log.build_NG_line(self.case_name, self.info['code'], self.info['msg'])
