from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
# Setup Selenium service
serv_obj = Service("/Users/spartan/Desktop/Automation/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

# Access the Audible search page
driver.get("https://www.audible.com/search")

# Collect product elements
products = driver.find_elements(By.XPATH, "//li[contains(@class,'productListItem')]")

# Lists to store product details
titles = []
authors = []
runtimes = []

# Loop through the products and extract the details
for product in products:
    titles.append(product.find_element(By.XPATH, ".//h3[contains(@class,'bc-heading')]").text)
    authors.append(product.find_element(By.XPATH, ".//li[contains(@class,'authorLabel')]").text)
    runtimes.append(product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]").text)

# Close the browser
driver.quit()

# Create a DataFrame from the extracted details
data = {
    'Title': titles,
    'Author': authors,
    'Runtime': runtimes
}

df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('audible_products.csv', index=False)

print("Data exported to 'audible_products.csv'")
