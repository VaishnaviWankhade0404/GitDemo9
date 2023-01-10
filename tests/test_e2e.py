from selenium.webdriver.common.by import By
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        #click on shop link
        #self.driver.find_element(By.XPATH,"//a[contains(@href, 'shop')]").click()
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Getting all product titles")

        #collect all item in a list
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        #checkoutPage = checkoutPage.getCardTitles()
        products = checkoutPage.getCardTitles()
        for product in products:
            if  product.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                break

        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        checkoutPage.getCheckFooter().click()

        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        confirmPage = checkoutPage.getCheckHeader()
        log.info("Entering country name as ind")

        #self.driver.find_element(By.ID, "country").send_keys("ind")
        confirmPage.getCountry().send_keys("ind")

        #expicit wait
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifylinkpresence("India")

        confirmPage.getDrpopt().click()

        #self.driver.find_element(By.LINK_TEXT, "India").click()

        #self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
        confirmPage.getCheck().click()

        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirmPage.getSub().click()

        #SuccessMsg = self.driver.find_element(By.CSS_SELECTOR, ".alert").text
        SuccessMsg = confirmPage.getSuccMsg().text
        assert "Success! Thank you!" in SuccessMsg
        #self.driver.close()

        print("Accents name")









