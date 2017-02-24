import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp

login_xls = common.get_xls("userCase.xlsx", "login")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):
    def setParameters(self, case_name, method, url, email, password, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param url:
        :param email:
        :param password:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        self.email = str(email)
        self.password = str(password)
        self.code = str(code)
        self.msg = str(msg)
        self.return_json = None
        self.info = None

    def description(self):
        self.case_name

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testLogin(self):
        # set url
        configHttp.set_url(self.url)

        # get visitor token
        token = localReadConfig.get_headers("token_v")

        # set headers
        header = {"token": str(token)}
        configHttp.set_headers(header)

        # set params
        data = {"email": self.email, "password": self.password}
        configHttp.set_data(data)

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
        info = self.info
        if info['info'] is not None:
            # get uer token
            token_u = common.get_value_from_return_json(info, 'member', 'token')
            # set user token to config file
            localReadConfig.set_headers("TOKEN_U", token_u)
        else:
            pass

    def checkResult(self):
        self.info = self.return_json.json()
        if self.info['code'] == self.code:
            self.assertEqual(self.info['msg'], self.msg)
            self.log.build_OK_line(self.case_name, self.code, self.msg)
        else:
            self.log.build_NG_line(self.case_name, self.info['code'], self.info['msg'])
