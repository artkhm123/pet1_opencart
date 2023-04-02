import datetime
import os
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import logging
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "ff", "firefox", "yandex", "ya", "MicrosoftEdge"])
    parser.addoption("--drivers", action="store",
                     default=os.path.expanduser("~\\khomiakov_a\\Downloads\\drivers\\"))
    parser.addoption("--url", action="store", default="http://192.168.31.28:8081")
    parser.addoption("--headless", action="store_true", default=True)
    parser.addoption("--log_level", action="store", default="INFO",
                     choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    parser.addoption("--executor", action="store", default="192.168.31.28")
    # parser.addoption("--executor", action="store", default="local")
    parser.addoption("--api_url", default="https://jsonplaceholder.typicode.com/")


@pytest.fixture
def jsonplaceholder_url(request):
    return request.config.getoption("--api_url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    drivers_path = request.config.getoption("--drivers")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    driver = None

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.originalname}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    if executor == "local":
        if _browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.headless = headless
            service = ChromeService(executable_path=drivers_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
        elif _browser == "ff" or _browser == "firefox":
            ff_options = FFOptions()
            ff_options.headless = headless
            service = FFService(executable_path=drivers_path)
            driver = webdriver.Firefox(service=service, options=ff_options)
        elif _browser == "yandex" or _browser == "ya":
            ya_options = ChromeOptions()
            ya_options.headless = headless
            service = ChromeService(executable_path=drivers_path)
            driver = webdriver.Chrome(service=service, options=ya_options)
        elif _browser == "MicrosoftEdge":
            edge_options = EdgeOptions()
            edge_options.headless = headless
            service = EdgeService(executable_path=drivers_path)
            driver = webdriver.Edge(service=service, options=edge_options)
    else:
        driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            desired_capabilities={"browserName": _browser,
                                  "selenoid:options": {
                                      "name": "Artem",
                                      "screenResolution": "1280x1024x24",
                                      "enableLog": True
                                  }
                                  }
        )

    driver.get(url)
    driver.url = url
    driver.maximize_window()
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.originalname
    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def finalizer():
        if request.node.status != 'passed':
            allure.attach(body=driver.get_screenshot_as_png(), name=f"{request.node.name}_screenshot_image",
                          attachment_type=AttachmentType.PNG)
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(finalizer)
    return driver
