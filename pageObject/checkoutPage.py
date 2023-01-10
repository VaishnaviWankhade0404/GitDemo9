from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmPage
class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    #driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    #driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOutFooter = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    #driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    checkOutHeader = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCheckFooter(self):
        return self.driver.find_element(*CheckoutPage.checkOutFooter)

    def getCheckHeader(self):
        self.driver.find_element(*CheckoutPage.checkOutHeader).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage