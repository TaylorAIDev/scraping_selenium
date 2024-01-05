from lib2to3.pgen2 import driver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select
import csv  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/travel/hotels/four%20seasons%20nam%20hai%20vietnam/entity/CgsIlriB_sLHk536ARAB/prices?q=four%20seasons%20nam%20hai%20vietnam&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4597339%2C4757164%2C4814050%2C4850738%2C4864715%2C4874190%2C4886480%2C4893075%2C4920132%2C4924070%2C4936396%2C4955321%2C4965990%2C4968087%2C4972345%2C4977499%2C4989344%2C4990493%2C4992509%2C4995865%2C4995867&hl=en-SG&gl=sg&cs=1&ssta=1&rp=OAJAAEgBwAECmgICCAA&ictx=1&ved=0CAAQ5JsGahcKEwiovbGB_8SDAxUAAAAAHQAAAAAQBA&ts=CAESCgoCCAMKAggDEAEaSQorEicyJTB4MzE0MjExZTQ4NzAwYmU4ZDoweGZhM2E0ZTNjMmZjMDVjMTYaABIaEhQKBwjoDxABGAgSBwjoDxABGAkYATICCAEqCQoFOgNTR0QaAA&ap=MAE&utm_campaign=sharing&utm_medium=link&utm_source=htls")

parent_element = driver.find_elements(By.CSS_SELECTOR, "div[class=\"vxYgIc fLiu5d\"]")[3]

list_elements = parent_element.find_elements(By.CSS_SELECTOR, "div[class=\"ADs2Tc\"]")
button = list_elements[len(list_elements) - 1]
button.click()
print(len(list_elements))
for list_element in list_elements:
    try:
        name = list_element.find_element(By.CSS_SELECTOR, "span[class=\"NiGhzc\"]").text
        price = list_element.find_element(By.CSS_SELECTOR, "span[class=\"iqYCVb\"]").text
        print(name,price)
    except:
        pass

sleep(1000)