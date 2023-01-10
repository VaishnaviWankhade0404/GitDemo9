from selenium.webdriver.common.by import By
from pageObject.checkoutPage import CheckoutPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    #driver.find_element(By.XPATH,"//a[contains(@href, 'shop')]
    shop = (By.XPATH,"//a[contains(@href, 'shop')]")

    #driver.find_element(By.NAME, "name").send_keys("vaishnavi")
    name = (By.NAME, "name")

    #driver.find_element(By.NAME, "email").send_keys("vaishnaviwankhde@cogniwize.com")
    email = (By.NAME, "email")

    #(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))

    drpdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")

    #driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    submit = (By.XPATH, "//input[@value='Submit']")

    #driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div").text
    message = (By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getDrpDown(self):
        return self.driver.find_element(*HomePage.drpdown)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)