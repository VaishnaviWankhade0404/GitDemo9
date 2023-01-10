import time
import pytest
from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):
#   @pytest.fixture(params=[("vaishnavi", "vaishnavi@gmail.com", "Female"),("Suraj", "Wankhade", "Male")])
#   @pytest.fixture(params=[{"firstname":"vaishnavi","email": "vaishnavi@gmail.com", "gender":"Female"},{"firstname":"Suraj","email": "Wankhade","gender": "Male"}])
    @pytest.fixture(params = HomePageData.test_data_homepage)
    def getData(self, request):
        return request.param

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        log.info("firstname is "+getData["firstname"])
        # By name self.selectOptionByText(homePage.getDrpDown(), getData[2])
        homePage.getName().send_keys(getData["firstname"])

        log.info("email "+getData["email"])
        homePage.getEmail().send_keys(getData["email"])

        # handling dropdown
        self.selectOptionByText(homePage.getDrpDown(),getData['gender'])

        # click on submit button
        time.sleep(5)
        homePage.getSubmit().click()

        # assertion for success message
        message = homePage.getMessage().text
        # print(message)
        assert "Success" in message

        self.driver.refresh()





