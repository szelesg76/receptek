#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# PATH = "C:\Users\gabor.szeles\Desktop\python_tanfolyam\receptek\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/uzlet_uj")
# assert "Python" in driver.title
print(driver.title)

# új üzlet rögzítése
element = driver.find_element(By.NAME, "uzlet_nev")
element.send_keys("Test_Selenium")
element_button = driver.find_element(By.NAME, "uzlet_nev_mentes")
element_button.click()

time.sleep(2)


# üzlet módosítása
# driver = webdriver.Chrome()

#driver.get("http://127.0.0.1:8000/uzletek")
element_link = driver.find_element(By.NAME, "test_selenium_modosit")
element_link.click()
time.sleep(2)

element = driver.find_element(By.NAME, "uzlet_nev")
element.clear()
element.send_keys("Test_Selenium_Test")
element_button = driver.find_element(By.NAME, "uzlet_nev_modosit")
element_button.click()
time.sleep(2)

#üzlet törlése
element_link = driver.find_element(By.NAME, "test_selenium_test_torol")
element_link.click()
time.sleep(2)


driver.close()





# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
