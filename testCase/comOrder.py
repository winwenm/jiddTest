# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import xmlrunner
from public import Mod
import HtmlTestRunner


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = "http://tmall.jdsn.com.cn"
        self.driver.maximize_window()

        self.verificationErrors = []
        self.accept_next_alert = True
    def testPass(self):
        pass

    # def test_ComBuyer(self):
    #     """companyOrder"""
    #
    #     driver = self.driver
    #     driver.get(self.base_url+"/login")
    #
    #     Mod.loginModCompany(self)  # 公司买家
    #     # Mod.loginModPerson(self)  #个人买家，需要已经下过单填写了车辆信息、
    #
    #     driver.get(self.base_url + "/items/94")
    #     driver.find_element_by_link_text(u"工厂").click()
    #     driver.find_element_by_link_text(u"自提").click()
    #     time.sleep(1)
    #     target = driver.find_element_by_id("item-quantity")
    #     driver.execute_script("arguments[0].scrollIntoView();", target)
    #     # 移到数量框
    #     driver.find_element_by_id("item-quantity").click()
    #     time.sleep(1)
    #     # driver.find_element_by_id("item-quantity").clear()
    #     # driver.find_element_by_id("item-quantity").send_keys("10")
    #     driver.find_element_by_xpath("//button[@type='button']").click()
    #     driver.find_element_by_id("protocol-checked").click()
    #     time.sleep(1)
    #     driver.find_element_by_xpath("//button[@type='button']").click()
    #
    #     time.sleep(1)
    #     driver.find_element_by_css_selector("li.pay-channel > img").click()
    #     time.sleep(1)
    #     driver.find_element_by_xpath("//button[@type='button']").click()
    #     time.sleep(1)

    #
    # def test_PerBuyer(self):
    #     """personalOrder"""
    #     driver = self.driver
    #     driver.get(self.base_url+"/login")
    #
    #     # Mod.loginModCompany(self)  # 公司买家
    #     Mod.loginModPerson(self)  #个人买家，需要已经下过单填写了车辆信息、
    #
    #     driver.get(self.base_url + "/items/94")
    #     driver.find_element_by_link_text(u"工厂").click()
    #     driver.find_element_by_link_text(u"自提").click()
    #     time.sleep(1)
    #     target = driver.find_element_by_id("item-quantity")
    #     driver.execute_script("arguments[0].scrollIntoView();", target)
    #     # 移到数量框
    #     driver.find_element_by_id("item-quantity").click()
    #     time.sleep(1)
    #     # driver.find_element_by_id("item-quantity").clear()
    #     # driver.find_element_by_id("item-quantity").send_keys("10")
    #     driver.find_element_by_xpath("//button[@type='button']").click()
    #     driver.find_element_by_id("protocol-checked").click()
    #     time.sleep(1)
    #     driver.find_element_by_xpath("//button[@type='button']").click()
    #
    #     time.sleep(1)
    #     driver.find_element_by_css_selector("li.pay-channel > img").click()
    #     time.sleep(1)
    #     driver.find_element_by_xpath("//button[@type='button']").click()
    #     time.sleep(1)

    def estT(self):
        driver = self.driver
        driver.get(self.base_url)

        Mod.loginModCompany(self)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Test("testLogin"))
    testunit.addTest(Test("test_ComBuyer"))
    testunit.addTest(Test("test_PerBuyer"))
    runner = HtmlTestRunner.HTMLTestRunner(output="order")

    runner.run(testunit)


    # unittest.main(testRunner = xmlrunner.XMLTestRunner(output="./jiddTest"))
