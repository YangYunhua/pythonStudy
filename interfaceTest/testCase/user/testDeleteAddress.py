import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp

deleteAddress_xls = common.get_xls("userCase.xlsx", "deleteAddress")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*deleteAddress_xls)
class DeleteAddress(unittest.TestCase):
    def setParameters(self, case_name, method, url, address_id, code, result):
        """
        set params
        :param case_name:
        :param method:
        :param url:
        :param address_id:
        :param code:
        :param result:
        :return:
        """
        self.case_name = str(case_name)
        self.url = str(url)
        self.method = str(method)
        self.address_id = str(address_id)
        self.code = str(code)
        self.result = result
        self.info = None

    def description(self):
        self.case_name

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testGetAddressList(self):
        # set url
        configHttp.set_url(self.url)

        # get visitor token
        token = localReadConfig.get_headers("TOKEN_U")

        # set headers
        header = {"token": str(token)}
        configHttp.set_headers(header)

        # set params
        params = {"address_id": self.address_id}
        configHttp.set_params(params)

        # test interface
        if self.method == 'get':
            self.return_json = configHttp.get()
        elif self.method == 'post':
            self.return_json = configHttp.post()
        else:
            self.logger.info("No this interface's method:" + self.method)
        # check result
        self.checkResult()

    def tearDown(self):
        pass

    def checkResult(self):
        self.info = self.return_json.json()
        if self.info['code'] == self.code:
            value = self.info['info']['result']
            self.assertEqual(str(value), self.result)
            self.log.build_OK_line(self.case_name, self.code, self.msg)
        else:
            self.log.build_NG_line(self.case_name, self.info['code'], self.info['msg'])
