'''
Question-3
Automate Text Field Entry Using ID Locator
Description
Open the Naukri.com website using Selenium WebDriver.
Navigate to the registration page and identify the text input fields such as Name, Email, and Password.
Use the ID locator strategy to locate these elements and enter appropriate sample data into each field using Selenium commands.
Students should ensure that the browser opens successfully, elements are identified correctly, and the values are entered into the fields.
Expected Outcome
The browser launches successfully.
The Naukri registration page opens.
Text is entered into the Name, Email, and Password fields using By.ID.
'''

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
import time

driver.get("https://www.naukri.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(3)
driver.find_element(By.ID, "name").send_keys("Nehal agarwal")
time.sleep(3)
driver.find_element(By.ID, "email").send_keys("nehala1801@gmail.com")
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("nehal@1234")
time.sleep(5)
driver.quit()
