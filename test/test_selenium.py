#https://selenium-python.readthedocs.io/navigating.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest


def test_uzletek_oldal():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/uzletek")
    assert driver.title == 'Üzletek'
    driver.close()

def test_uj_uzlet_letrehozas():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/uzlet_uj")
    print(driver.title)

    # új üzlet rögzítése
    element = driver.find_element(By.NAME, "uzlet_nev")
    element.send_keys("Test_Selenium")
    element_button = driver.find_element(By.NAME, "uzlet_nev_mentes")
    element_button.click()

    # driver.get("http://127.0.0.1:8000/uzletek")
    #element_link = driver.find_element(By.NAME, "test_selenium_modosit")
    assert driver.find_element(By.NAME, "test_selenium_modosit")
    assert driver.find_element(By.NAME, "test_selenium_torol")
    driver.close()

def test_nemletezo_uzlet():
        
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/uzletek")

    with pytest.raises(NoSuchElementException) as exc_info:
        driver.find_element(By.NAME, "test_selenium_nemletezik")
    #print(exc_info.value.msg)    
    assert 'Unable to locate element' in str(exc_info.value.msg)

    # try: 
    #     driver.find_element(By.NAME, "test_selenium_nemletezik")
    # except NoSuchElementException as exc:
    #     assert 1 == 1, "should have thrown an exception"  
    driver.close()


def test_uzlet_modosit():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/uzletek")
    element_link = driver.find_element(By.NAME, "test_selenium_modosit")
    element_link.click()

    element = driver.find_element(By.NAME, "uzlet_nev")
    element.clear()
    element.send_keys("Test_Selenium_Test")
    element_button = driver.find_element(By.NAME, "uzlet_nev_modosit")
    element_button.click()

    driver.get("http://127.0.0.1:8000/uzletek")
    assert driver.find_element(By.NAME, "test_selenium_test_modosit")
    driver.close()


def test_uzlet_torol():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/uzletek")
    assert driver.find_element(By.NAME, "test_selenium_test_torol")
    element_link = driver.find_element(By.NAME, "test_selenium_test_torol")
    element_link.click()

    with pytest.raises(NoSuchElementException) as exc_info:
        driver.find_element(By.NAME, "test_selenium_test_torol")
    assert 'Unable to locate element' in str(exc_info.value.msg)
    driver.close()

# pytest -s .\test\test_selenium.py::test_nemletezo_uzlet
# pytest -v -m .\test\test_selenium.py
# pytest -vs -m .\test\test_selenium.py


# pytest .\test\test_selenium.py::test_nemletezo_uzlet

# def test_search_in_python_org():
#     driver = webdriver.Chrome()
#     driver.get("http://www.python.org")

#     assert driver.title == 'Welcome to Python.org'

#     # elem = driver.find_element(By.NAME, "q")
#     # elem.send_keys("pycon")
#     # elem.send_keys(Keys.RETURN)
    
#     # assert driver.page_source != 'pycon'

#     driver.close()





    # elem = driver.find_element(By.NAME, "q")
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    
    # assert driver.page_source != 'pycon'
