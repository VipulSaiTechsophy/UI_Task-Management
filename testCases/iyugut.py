# def func1(s:str) -> bool:
#     dict1 = {'(': ')', '{': '}', '[': ']'}
#     list1 = []
#     for i in s:
#         if i in dict1.keys():
#             list1.append(i)
#         else:
#             if list1 == []:
#                 return False
#             a = list1.pop()
#             if i != dict1[a]:
#                 return False
#     return list1 == []
#
# print(func1("{[]}"))
import time

# from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://dev.taskmanagement.techsophy.com/")
driver.find_element(By.ID, "username").send_keys("bhavya")
driver.find_element(By.ID, "password").send_keys("test")
driver.find_element(By.ID, "kc-login").click()
time.sleep(2)
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[3]/button[2]").click()
time.sleep(3)
# driver.find_element(By.XPATH, "//input[@id='end-Date']").click()
# driver.find_element(By.XPATH, "//input[@id='end-Date']").send_keys("20/03/2022, 11:50")
# ac = ActionChains(driver)
# ed = driver.find_element(By.XPATH, "//input[@id='end-Date']")
# ac.double_click(ed).perform()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#end-Date").click()
