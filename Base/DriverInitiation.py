# from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.configReader import readConfig
# from selenium.webdriver.chrome.options import Options

class Driver:

    def getDriverMethod(self):
        # opt = Options()
        # opt.add_argument("--headless")
        # opt.add_argument("--disable-gpu")
        # opt.add_argument("--window-size=1280,800")
        # opt.add_argument("--allow-insecure-localhost")
        # opt.add_argument('--no-sandbox')
        # driver = webdriver.Chrome(options=opt)
        # driver.maximize_window()
        # driver.implicitly_wait(20)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(readConfig("url", "webUrl"))
        driver.implicitly_wait(15)
        return driver
