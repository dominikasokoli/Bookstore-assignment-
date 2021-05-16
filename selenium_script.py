import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import unittest

#Preliminatory conditions
class EmpikBookSearching(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Firefox()
        driver.get("http://www.empik.com")
        driver.implicity_wait(60)

#Test steps
    def testInvalidEmail(self):
        driver = self.driver
        search_input = driver.find_element_by_xpath('//*[@id="bq"]')
        search_input.send_keys('Harry Potter')
        close_button = driver.find_element_by_xpath('/html/body/main/footer/div[5]/div[2]/div[1]/button')
        close_button.click()
        search_category = driver.find_element_by_xpath('//*[@id="searchSet"]/div[2]/button')
        search_category.click()
        search_category_book = driver.find_element_by_xpath('//*[@id="searchSet"]/div[2]/div/label[14]')
        search_category_book.click()
        search_btn = driver.find_element_by_xpath('//*[@id="searchSet"]/button')
        search_btn.click()

    def tearDown(self):
        #finish test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
