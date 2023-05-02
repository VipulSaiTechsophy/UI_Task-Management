# import logging
# import os
import time

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from Utilities.CustomLogger import customLogger
# import robot
# import pyperclip
# import pyautogui
# import subprocess

class ActionPage:
    log = customLogger()

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=(ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException))

    def getPageName(self):
        element = self.driver.title
        print(element)
        return element

    def click(self, locatorValue, locatorType):
        time.sleep(10)
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "NAME":
            self.driver.find_element(By.NAME, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "ID":
            self.driver.find_element(By.ID, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "CLASSNAME":
            self.driver.find_element(By.CLASS_NAME, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)

    def close_driver(self):
        self.driver.close()


    def sendKeys(self, locatorValue, locatorType, value):
        try:
            if str(locatorType) == "XPATH":
                self.driver.find_element(By.XPATH, locatorValue).send_keys(value)
                self.log.info("sent key as  ::  " + value)
            elif str(locatorType) == "NAME":
                self.driver.find_element(By.NAME, locatorValue).send_keys(value)
                self.log.info("sent key as  ::  " + value)
            elif str(locatorType) == "ID":
                self.driver.find_element(By.ID, locatorValue).send_keys(value)
                self.log.info("sent key as  ::  " + value)
        except Exception as e:
            self.log.info("got an exception as :: " + str(e))

    def selectByName(self, locatorValue, locatorType, selectionXpath):
        if locatorType == "XPATH":
            dropDOwn = self.driver.find_element(By.XPATH, locatorValue)
            Country_selected = Select(dropDOwn)
            Country_selected.select_by_visible_text(selectionXpath)
        elif locatorType == "CLASSNAME":
            dropDOwn = self.driver.find_element(By.CLASS_NAME, locatorValue)
            Country_selected = Select(dropDOwn)
            Country_selected.select_by_visible_text(selectionXpath)
        elif locatorType == "NAME":
            dropDOwn = self.driver.find_element(By.NAME, locatorValue)
            Country_selected = Select(dropDOwn)
            Country_selected.select_by_visible_text(selectionXpath)

    def selectByValue(self, locatorValue, locatorType, selectionXpath):
        if locatorType == "XPATH":
            dropDOwn = self.driver.find_element(By.XPATH, locatorValue)
            Country_selected = Select(dropDOwn)
            Country_selected.select_by_value(selectionXpath)
        elif locatorType == "CLASSNAME":
            dropDOwn = self.driver.find_element(By.CLASS_NAME, locatorValue)
            Country_selected = Select(dropDOwn)
            Country_selected.select_by_value(selectionXpath)
        elif locatorType == "NAME":
            dropDOwn = self.driver.find_element(By.NAME, locatorValue)
            Country_selected = Select(dropDOwn)
            Country_selected.select_by_value(selectionXpath)

    def clear_textfield(self, locatorValue, locatorType):
        if locatorType=='XPATH':
            self.driver.find_element(By.XPATH, locatorValue).clear()
        elif locatorType=='ID':
            self.driver.find_element(By.XPATH, locatorValue).clear()



    def is_Clickable(self,locatorValue, locatorType):
        try:
            element = None
            if str(locatorType) == "XPATH":
                element = self.driver.find_element(By.XPATH, locatorValue).isClickable()
            elif str(locatorType) == "NAME":
                self.driver.find_element(By.NAME, locatorValue).isClickable()
            elif str(locatorType) == "ID":
                self.driver.find_element(By.ID, locatorValue).isClickable()
            self.log.info("sent key as  ::  " + element)

        except Exception as e:
            self.log.info("got an exception as :: " + str(e))

    def get_textValue(self,locatorValue, locatorType):
        if str(locatorType) == "XPATH":
            element = self.driver.find_element(By.XPATH, locatorValue)
            gettext = element.text
            print(gettext)

    def get_Text(self, locatorValue, locatorType, exp_text):
        if str(locatorType) == "XPATH":
            element = self.driver.find_element(By.XPATH, locatorValue)
            gettext = element.text
            print(gettext)

            if gettext == exp_text:
                self.log.info(gettext+" is successful")
            else:
                self.log.info(gettext+" is failed")

    def tagname(self,locatorValue):
        self.driver.find_element(By.TAG_NAME, locatorValue).click()


    def exec_scr(self,locatorType,locatorValue,date):
        if str(locatorType) == "SCRIPT":
            self.driver.find_element(By.XPATH, locatorValue).click()
            date = 'yyyy-mm-dd'
            self.driver.execute_script(f"document.getElementById('id').value= '{date}'")

    def listofdrpdwn(self,locatorValue, locatorType):
        if str(locatorType) == 'XPATH':
            element = self.driver.find_elements(By.XPATH, locatorValue)
            data = [i.text for i in element]
            print(data)
            return data

    def useactionswithsendkeys(self, locatorValue,locatorValue2,value, locatorType):
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue).click()
            self.driver.find_element(By.XPATH, locatorValue2).send_keys(value)
            a = ActionChains(self.driver)
            a.send_keys(Keys.ARROW_DOWN).perform()
            a.send_keys(Keys.ENTER).perform()
    def filteruseactionswithsendkeys(self, locatorValue,value, locatorType):
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue).send_keys(value)
            a = ActionChains(self.driver)
            a.send_keys(Keys.ARROW_DOWN).perform()
            a.send_keys(Keys.ENTER).perform()

    def useactions(self, locatorValue, locatorType):
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue).click()
            a = ActionChains(self.driver)
            a.send_keys(Keys.ARROW_DOWN).perform()
            a.send_keys(Keys.ENTER).perform()


    def keysdown(self,locatorValue):
        sel = self.driver.find_element(By.XPATH, locatorValue).click()
        sel.send_keys(Keys.ARROW_DOWN,Keys.ENTER)

    # def uploadfile(self, locatorValue, locatorType, path):
    #
    #     if str(locatorType)=="XPATH":
    #         wait = WebDriverWait(self.driver, 10)
    #         uf = self.driver.find_element(By.XPATH, locatorValue)
    #         wait.until(EC.element_to_be_clickable(uf)).click()
    #         time.sleep(1)
    #         # pyperclip.copy(path)
    #         pyautogui.hotkey("tab")
    #         # time.sleep(5)
    #         pyautogui.hotkey("tab")
    #         # time.sleep(5)
    #         pyautogui.hotkey("tab")
    #         # time.sleep(5)
    #         pyautogui.press("enter")
    #         time.sleep(2)
    #         pyautogui.write(path)
    #         time.sleep(1)
    #         pyautogui.keyDown('down')
    #         pyautogui.keyUp('down')
    #         # subprocess.call(['xdotool', 'key', 'Down'])
    #         pyautogui.press("enter")
    #         time.sleep(10)
    #
########################################################

            # time.sleep(0.5)
            # # pyautogui.keyDown('down')
            # for i in range(1):
            #     pyautogui.keyUp('up')

            # pyautogui.keyDown('down')
            # time.sleep(2)
            # pyautogui.keyUp("up")
            # time.sleep(10)
            # pyautogui.press("down")


            # subprocess.run(["xdg-open", "/home/vipulsai/viewer.pdf"])
            # subprocess.run(["xdotool", "search", "--name", "File Upload", "type", "/home/vipulsai/viewer.pdf"])
            # subprocess.run(["xdotool", "key", "Return"])


            # # self.driver.find_element(By.XPATH, locatorValue).click().send_keys("/home/vipulsai/viewer.pdf")
            # file_Path = os.path.abspath("file:///home/vipulsai/viewer.pdf")
            # print(os.path.isfile(file_Path))
            # self.driver.execute_script("arguments[0].setAttribute('style', 'visibility: visible;'); arguments[0].style.display = 'block'; arguments[0].removeAttribute('disabled');",element)
            # element.send_keys(file_Path)
# file_input.send_keys(file_Path)
# self.driver.execute_script("var x=  document.createElement('INPUT');x.setAttribute('type', 'file'); x.setAttribute('onchange','this.form.submit()');x.setAttribute('hidden', 'true'); arguments[0].appendChild(x);",ele)
# self.driver.find_element(By.XPATH("//input[@type='file']")).send_keys("file:///home/vipulsai/viewer.pdf")

    def chkenabled(self, locatorValue, locatorType):
        if str(locatorType) == "XPATH":
            element = self.driver.find_element(By.XPATH, locatorValue)
            if element.is_enabled() == True:
                assert True
                self.log.info(locatorValue + " is enabled")
                # self.driver.find_element(By.XPATH, locatorValue).click()
                # self.log.info(" Clicked on field succesfully")
            else:
                self.log.info(locatorValue + " is not enabled")