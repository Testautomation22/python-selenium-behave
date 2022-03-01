from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
b_stack_username = 'doml_LPu2fw'
b_stack_key='yqgxSysUCcpFTMxoAucs'


#Browser Initialization
def browser_init(context):

    browser_name = ""
    if browser_name == "chrome":
        # Chrome Headless Mode
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    elif browser_name == "firefox":
        #Firefox browser
        options = webdriver.FirefoxOptions()
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    else:
        #Default option: Execute with Browserstack
        desired_cap = {
            "os": "Windows",
            "os_version": "11",
            "browser": "Firefox",
            "browser_version": "latest",
            "project": "Gettop",
            "build": "Build 1.0",
            "name": "Shopping Cart",
            "browserstack.local": "false",
            "browserstack.selenium_version": "3.10.0",
            "acceptSslCerts": "true"



        }
        url = f'https://{b_stack_username}:{b_stack_key}@hub-cloud.browserstack.com/wd/hub'
        context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(15)
    context.driver.wait = WebDriverWait(context.driver, 20)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
