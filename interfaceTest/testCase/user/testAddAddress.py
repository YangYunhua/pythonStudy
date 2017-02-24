import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp

addAddress_xls = common.get_xls("userCase.xlsx", "addAddress")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*addAddress_xls)
class AddAddress(unittest.TestCase):
    def setParameters(self, case_name, method, url, sex, fname, lname, tel, standby_tel, address1, address2, city, state, postcode, country_id, tax_number, company, fax, is_default, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param url:
        :param sex:
        :param fname:
        :param lname:
        :param tel:
        :param standby_tel:
        :param address1:
        :param address2:
        :param city:
        :param state:
        :param postcode:
        :param country_id:
        :param tax_number:
        :param company:
        :param fax:
        :param is_default:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.url = str(url)
        self.method = str(method)
        self.sex = str(sex)
        self.fname = str(fname)
        self.lname = str(lname)
        self.tel = str(tel)
        self.standby_tel = str(standby_tel)
        self.address1 = str(address1)
        self.address2 = str(address2)
        self.city = str(city)
        self.state = str(state)
        self.postcode = str(postcode)
        self.country_id = str(country_id)
        self.tax_number = str(tax_number)
        self.company = str(company)
        self.fax = str(fax)
        self.is_default = str(is_default)
        self.code = str(code)
        self.msg = str(msg)
        self.info = None

    def description(self):
        self.case_name

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testAddAddress(self):
        # set url
        configHttp.set_url(self.url)

        # get visitor token
        token = localReadConfig.get_headers("TOKEN_U")

        # set headers
        header = {"token": str(token)}
        configHttp.set_headers(header)

        # set params
        data = {"sex": self.sex,
                "fname": self.fname,
                "lname": self.lname,
                "tel": self.tel,
                "standby_tel": self.standby_tel,
                "address1": self.address1,
                "address2": self.address2,
                "city": self.city,
                "state": self.state,
                "postcode": self.postcode,
                "country_id": self.country_id,
                "tax_number": self.tax_number,
                "company": self.company,
                "fax": self.fax,
                "is_default": self.is_default}
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
        pass

    def checkResult(self):
        self.info = self.return_json.json()
        if self.info['code'] == self.code:
            self.assertEqual(self.info['msg'], self.msg)
            self.log.build_OK_line(self.case_name, self.code, self.msg)
        else:
            self.log.build_NG_line(self.case_name, self.info['code'], self.info['msg'])
