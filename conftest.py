import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):  # встроенная функция
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help="Choose language")

@pytest.fixture(scope="function")  # фикстура для обработки данных из командной строки
def browser(request):
    browser_name = request.config.getoption("browser_name")  # встроенная фикстура request
    language_name = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()  # или =webdriver.ChromeOptions() тогда без импорта from selenium.webdriver.chrome.options import Options
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #убираем USB: usb_device_handle_win.cc:1049 Failed...
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(2)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language_name)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
