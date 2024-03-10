"""
Filename: demo.py
Original Author: David Hernandez
Modified By: <INSERT NAME HERE>

Description: This script demonstrates the usage of Selenium WebDriver to automate web interactions.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def filer_form_type(driver, opt=None):
    """
    This skeleton function filters the form type based on the given option.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        opt (str, optional): The option to filter the form type. Defaults to None.
    """
    # Write your code here


def filter_institution(driver):

    dropdown = driver.find_element(By.ID, "CLASS_SRCH_WRK2_INSTITUTION$31$")
    dropdown.click()

    calpoly = "Cal Poly"
    dropdown.send_keys(calpoly) 
    

def filter_prefix(driver, prefix):
    """
    This function filters out by course prefix. 
    Ex. CSC, MATH, etc.
    """

    dropdown = driver.find_element(By.ID, "SSR_CLSRCH_WRK_SUBJECT_SRCH$0")
    dropdown.click()
    dropdown.send_keys(prefix)


def filter_course_number(driver, course_number):
    """
    This function filters out by course number. 
    Ex. 101, 102, etc.
    """

    dropdown = driver.find_element(By.ID, "SSR_CLSRCH_WRK_CATALOG_NBR$1")
    dropdown.click()
    dropdown.send_keys(str(course_number))


def include_closed_classes(driver):
    """
    This function includes closed classes in the search.
    """
    checkbox = driver.find_element(By.ID, "SSR_CLSRCH_WRK_SSR_OPEN_ONLY_LBL$3")
    checkbox.click()


def submit_search(driver):
    """
    This function submits the search.
    """
    # submit_button = driver.find_element(By.ID, "CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH")
    # # submit_button.click()
    # submit_button.send_keys(Keys.ENTER)

    submit = driver.find_element(By.ID, "CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH")
    submit.click()

def scrape_results(driver):
    table = driver.find_element(By.ID, "ACE_SSR_CLSRSLT_WRK_GROUPBOX2$0")

    rows = table.find_elements(By.TAG_NAME, "tr") 

    for row in rows:
        
        cells = row.find_elements(By.TAG_NAME, "td")
     
        if len(cells) > 5:
            print(cells[4].text)
            print(cells[2].text)
            print(cells[1].text)



def main():

    # Setup Firefox WebDriver
    # service = Service(GeckoDriverManager().install())
    service = Service("./geckodriver")  #./geckodriver.exe On Windows
    driver = webdriver.Firefox(service=service)

    # Navigate to the website
    url = "https://cmsweb.pscs.calpoly.edu/psc/CSLOPRD/EMPLOYEE/SA/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL"
    driver.get(url)
    time.sleep(1)
    
    filter_institution(driver)
    time.sleep(1)
    filter_prefix(driver, "CSC")
    time.sleep(1)
    filter_course_number(driver, 101)
    time.sleep(1)
    include_closed_classes(driver)
    time.sleep(1)
    submit_search(driver)
    time.sleep(4)


    scrape_results(driver)

    driver.quit()


if __name__ == '__main__':
    print("Hello, World!")
    main()

