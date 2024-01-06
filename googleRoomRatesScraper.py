from logging.config import ConvertingTuple
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
from datetime import datetime
import calendar
from datetime import datetime, timedelta
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import StaleElementReferenceException , ElementNotInteractableException           

startDate = input('Start date : ')
date_obj1 = datetime.strptime(startDate, '%d/%m/%Y')
month_name = calendar.month_abbr[date_obj1.month]
day_name = calendar.day_abbr[date_obj1.weekday()]
startDate = f"{day_name}, {date_obj1.day} {month_name}"

endDate = input('End date : ')
date_obj2 = datetime.strptime(endDate, '%d/%m/%Y')
month_name = calendar.month_abbr[date_obj2.month]
day_name = calendar.day_abbr[date_obj2.weekday()]
endDate = f"{day_name}, {date_obj2.day} {month_name}"

fark = date_obj2 - date_obj1
fark = " ".split(str(fark))
fark = fark[0]

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                     'Chrome/85.0.4183.102 Safari/537.36'})
while True:
   try:
      driver.get("https://www.google.com/travel/hotels/four%20seasons%20nam%20hai%20vietnam/entity/CgsIlriB_sLHk536ARAB/prices?q=four%20seasons%20nam%20hai%20vietnam&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4597339%2C4757164%2C4814050%2C4850738%2C4864715%2C4874190%2C4886480%2C4893075%2C4920132%2C4924070%2C4936396%2C4955321%2C4965990%2C4968087%2C4972345%2C4977499%2C4989344%2C4990493%2C4992509%2C4995865%2C4995867&hl=en-SG&gl=sg&cs=1&ssta=1&rp=OAJAAEgBwAECmgICCAA&ictx=1&ved=0CAAQ5JsGahcKEwjo6ebv-aL-AhUAAAAAHQAAAAAQBA&ts=CAESCgoCCAMKAggDEAEaSQorEicyJTB4MzE0MjExZTQ4NzAwYmU4ZDoweGZhM2E0ZTNjMmZjMDVjMTYaABIaEhQKBwjnDxAEGAwSBwjnDxAEGA0YATICCAEqCQoFOgNTR0QaAA&ap=MAE")
      current_start_date = driver.find_element(By.XPATH , '/html/body/c-wiz[2]/div/div[2]/div[1]/div[2]/span[2]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div/div[2]/div[1]/div/input').get_attribute('value')
      time.sleep(1)
      driver.execute_script(f"""
      document.querySelector("#prices > c-wiz > c-wiz > div > div > div > div > div > div > div > section > div.LEPXne > div.w1RZXe.sgtnuf.abhqy.nIkIJf.WzEC0e > div > div.Ryi7tc.pI31md.hh3Grb > div:nth-child(2) > div > input").click()
      """)
      time.sleep(3)
      #click Reset button
      driver.find_element(By.XPATH , '/html/body/c-wiz[2]/div/div[2]/div[1]/div[2]/span[2]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/button[1]').click()
      time.sleep(0.5)
      #click Done button
      driver.find_element(By.XPATH , '/html/body/c-wiz[2]/div/div[2]/div[1]/div[2]/span[2]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/button[2]').click()
      time.sleep(1)
      driver.execute_script("""
      document.querySelector("#prices > div > c-wiz:nth-child(2) > footer > div.N1EQHd > c-wiz > button").click()
      """)
      break
   except:
      continue
time.sleep(2)
while True:
   try:
      driver.execute_script("""
      document.querySelector("#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.D5eS6.mF82qd.Up8vH.J9Nfi.iWO5td > span > div > div:nth-child(1) > span > div > label:nth-child(7) > div.zJKIV.k11Tnd.WEM9De.i9xfbb").click()
      """)
      driver.execute_script("""
      document.querySelector("#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.D5eS6.mF82qd.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > div:nth-child(2) > button > span").click()
      """)
      break
   except:
      continue
hotelNameList = []
roomTypeList = []
guestList = []
priceList = []
checkIn = []
chackOut = []
time.sleep(1)
sayac = 1

while True:
   if(driver.find_element(By.XPATH , '/html/body/c-wiz[2]/div/div[2]/div[1]/div[2]/span[2]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div/div[2]/div[1]/div/input').get_attribute('value') == startDate):
      break
   else:
      driver.find_element(By.XPATH , '/html/body/c-wiz[2]/div/div[2]/div[1]/div[2]/span[2]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/button').click()

while True:
   time.sleep(1)
   try:
      end = driver.find_element(By.XPATH , '/html/body/c-wiz[2]/div/div[2]/div[1]/div[2]/span[2]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input').get_attribute('value')
   except:
      continue
   if(end == endDate):
      break
   isClick = True
   while True:
      checkInDate = driver.find_element(By.XPATH ,   '/html/body/c-wiz[2]/div/div[2]/div[1]/div[2]/span[2]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div/div[2]/div[1]/div/input').get_attribute('value')
      time.sleep(1)
      checkOutDate = driver.find_element(By.XPATH ,   '/html/body/c-wiz[2]/div/div[2]/div[1]/div[2]/span[2]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div/div[2]/div[2]/div/input' ).get_attribute('value')
      if(checkInDate == endDate):
         break
      time.sleep(1)
      if(isClick):
         parent_element = driver.find_elements(By.CSS_SELECTOR, "div[class=\"vxYgIc fLiu5d\"]")[3]      
         list_elements = parent_element.find_elements(By.CSS_SELECTOR, "div[class=\"ADs2Tc\"]")
         more_options_button = list_elements[len(list_elements) - 1]
         more_options_button.click()
         for list_element in list_elements:
            try:
               name = list_element.find_element(By.CSS_SELECTOR, "span[class=\"NiGhzc\"]").text
               hotelNameList.append(name)
               price = list_element.find_element(By.CSS_SELECTOR, "span[class=\"iqYCVb\"]").text
               priceList.append(price)
               checkIn.append(checkInDate)
               chackOut.append(checkOutDate)
            except:
               pass
      try: 
         data = {
            'Hotel Name': hotelNameList,
            'checkInDate':checkIn,
            'checkOutDate':chackOut,
            'Price': priceList
         }
         df = pd.DataFrame(data)
         df.to_csv('sample.csv', index=False)
      except:
         None 
      # sayac += 1
      # try:
      #    if(sayac>int(fark)):
      #       break
      # except:
      #    None
      try:
         isClick = True
         wait = WebDriverWait(driver, 1)
         button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="prices"]/c-wiz/c-wiz/div/div/div/div/div/div/div/section/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button')))
         webdriver.ActionChains(driver).move_to_element(button).click(button ).perform()
         break
      except:
         try:
            isClick = True
            driver.execute_script(
               """
               document.querySelector("#ow482 > div > div.Wvne.hh3Grb > div:nth-child(2) > div > div.WViz0c.CKPWLe.U9gnhd.Xbfhhd > button > span.VfPpkd-kBDsod").click()
               """
            )
         except:
            isClick = False
            continue