'''
Question-4
Automate Product Search on Myntra Using Class Name Locator
Description
Open the Myntra website using Selenium WebDriver.
Locate the search input field on the homepage using the class name locator.
Enter the text "shoes" into the search field using Selenium’s send_keys() method.
Ensure that the correct locator is used to identify the search box before entering the text.
Expected Outcome
The browser launches successfully.
The Myntra homepage loads.
The search field is located using the class name locator.
The word "shoes" appears in the search box.
The script executes without errors.
'''

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
import time

driver.get("https://www.myntra.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"desktop-searchBar").send_keys("shoes")
time.sleep(3)
driver.quit()

