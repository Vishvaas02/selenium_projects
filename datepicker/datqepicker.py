from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Chrome driver service object
serv_obj = Service("/Users/spartan/Desktop/Automation/chromedriver-mac-arm64/chromedriver")

# Set up Chrome options with only headless mode
ops = Options()
ops.add_argument("--headless=new")  # Use --headless=new for modern Chrome versions

# Initialize WebDriver
driver = webdriver.Chrome(service=serv_obj, options=ops)

# Navigate to the website
driver.get("https://jqueryui.com/")
driver.find_element(By.XPATH, "//a[text()='Datepicker']").click()

# Switch to the iframe
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

# Open the date picker
driver.find_element(By.XPATH, "//input[@class='hasDatepicker']").click()

month = "September"
year = "2025"
date = "17"

# Loop through months and years until the desired one is found
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if yr == year and mon == month:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

# Find and select the desired date
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        ele.click()
        break

time.sleep(5)
driver.quit()  # Close the browser after the operation
