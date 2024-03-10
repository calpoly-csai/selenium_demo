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
    """
    
    """
    # Fill in Form: 700 Statement of Economic Interests
    formtypefield = driver.find_element(By.ID, "CLASS_SRCH_WRK2_INSTITUTION$31$")
    formtypefield.click()

    calpoly = "Cal Poly"
    formtypefield.send_keys(calpoly)
    print("Enter")
    

def filter_prefix(driver, prefix):
    """
    This function filters out by course prefix. 
    Ex. CSC, MATH, etc.
    """

    formtypefield = driver.find_element(By.ID, "SSR_CLSRCH_WRK_SUBJECT_SRCH$0")
    formtypefield.click()
    # for _ in range(course_prefixes.index(prefix)):
    #     formtypefield.send_keys(Keys.ARROW_DOWN)
    # formtypefield.send_keys(Keys.ENTER)
    formtypefield.send_keys(prefix)


def include_closed_classes(driver):
    """
    This function includes closed classes in the search.
    """
    # Write your code here
    
    checkbox = driver.find_element(By.ID, "SSR_CLSRCH_WRK_SSR_OPEN_ONLY_LBL$3")
    checkbox.click()



def fill_course_number(driver, course_number):
    """
    This function fills in the course number.
    """
    course_number_field = driver.find_element(By.ID, "SSR_CLSRCH_WRK_CATALOG_NBR$1")
    course_number_field.click()
    course_number_field.send_keys(course_number)


def scrape_results(driver):
    """
    This function scrapes the results of the search.
    """
    # Write your code here
    
    print("Scraping Results")


    # Here we find the main table in the class search results

    table = driver.find_element(By.ID, "ACE_SSR_CLSRSLT_WRK_GROUPBOX2$0")
    print('table found')

    # Find all row elements in the table (tr tags)
    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        # Find all cell elements in this row (td tags)
        cells = row.find_elements(By.TAG_NAME, "td")
        
        # Extract text from each cell
        for cell in cells:
            print(cell.text)


def main():
    """
    The main function that executes the automation task.
    """
    # Setup Firefox WebDriver
    # service = Service(GeckoDriverManager().install())
    service = Service("./geckodriver")
    driver = webdriver.Firefox(service=service)

    # Navigate to the website
    url = "https://cmsweb.pscs.calpoly.edu/psc/CSLOPRD/EMPLOYEE/SA/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL"
    driver.get(url)

    # Wait for a moment to ensure the page has loaded
    # Adjust time as necessary for your network speed and page complexity
    # driver.implicitly_wait(10)  # For our demo, we will use a simple sleep to allow us to see whats goind on


    time.sleep(2)
    filter_institution(driver)
    time.sleep(2)
    filter_prefix(driver, "CSC")
    time.sleep(2)
    fill_course_number(driver, "101")
    time.sleep(2)
    include_closed_classes(driver)

    submit = driver.find_element(By.ID, "CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH")
    submit.click()

    time.sleep(3)

    scrape_results(driver)

    # Remember to close the browser once your automation task is done
    driver.quit()

    # If you need to perform more complex interactions, you will have to identify the
    # specific elements using methods like find_element_by_id, find_element_by_name, etc.,
    # and then use methods like click() or send_keys() to interact with those elements.


if __name__ == '__main__':
    print("Hello, World!")
    main()

