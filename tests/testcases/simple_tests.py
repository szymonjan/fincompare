# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER
from wtframework.wtf.utils.test_utils import do_and_ignore
from wtframework.wtf.utils.wait_utils import do_until


from random import randint
import unittest


class BaseTests(WTFBaseTest):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sending_tweet(self):
        pass


if __name__ == '__main__':
    unittest.main()
