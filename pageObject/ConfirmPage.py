from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    #driver.find_element(By.ID, "country").send_keys("ind")
    Country = (By.ID, "country")

    #driver.find_element(By.LINK_TEXT, "India").click()
    dropoption = (By.LINK_TEXT, "India")

    #driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
    check = (By.CSS_SELECTOR, ".checkbox")

    #driver.find_element(By.XPATH, "//input[@type='submit']").click()
    sub = (By.XPATH, "//input[@type='submit']")

    #driver.find_element(By.CSS_SELECTOR, ".alert").text
    SuccMsg = (By.CSS_SELECTOR, ".alert")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.Country)
    def getDrpopt(self):
        return self.driver.find_element(*ConfirmPage.dropoption)
    def getCheck(self):
        return self.driver.find_element(*ConfirmPage.check)
    def getSub(self):
        return self.driver.find_element(*ConfirmPage.sub)
    def getSuccMsg(self):
        return self.driver.find_element(*ConfirmPage.SuccMsg)

