import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    global webdriver
    browserName = request.config.getoption("browser_name")
    if browserName == "chrome":
         service_obj = Service(r"C:\Users\pcpoint\Downloads\chromedriver_win32 (1)\chromedriver.exe")
         driver = webdriver.Chrome(service=service_obj)
    elif browserName =="firefox":
        service_obj = Service(r"C:\Users\pcpoint\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browserName == "IE":
        print("Running on IE")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
#    yield
#    driver.close()

