#  Challenge 1: Create a script that searches for all gaming headsets on sale on Amazon that also offer Prime delivery.
#  Additionally, export the names, dates, prices, and reviews to an Excel spreadsheet.

from datetime import datetime
from time import sleep

import numpy as np
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Variables
amazon = 'https://www.amazon.com.br/'
product = input('Digite o produto desejado:')
date = datetime.today().date()

# Access the Amazon
driver = webdriver.Chrome()
driver.get(amazon)
sleep(10)

# Search for gaming headsets
search = driver.find_element(By.XPATH, '//input[@name="field-keywords"]')
search.send_keys(product)
search.send_keys(Keys.RETURN)
sleep(2)

# Filter - Prime Delievery
prime = driver.find_element(By.XPATH, '//li[@id="p_n_free_shipping_eligible/19171733011"]/span/a/div/label/i')
prime.click()
sleep(2)

# Product Names and Prices
names = []  # names list
prices = []  # prices list

# Get all product containers
containers = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")  

# Responsible for being the first path
for container in containers:
    try:
        name = container.find_element(By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']").text
        names.append(name)
    except:
        names.append(np.NaN)

    try:
        price = container.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        prices.append(price)
    except:
        prices.append(np.NaN)

# Close the browser
driver.quit()

# Create a DataFrame and save to Excel
df = pd.DataFrame({
    'Product Name': names,
    'Price': prices,
    'Date': [date] * len(names)
})

df.to_excel('Challenge #1 - Data.xlsx', index=False)
open('Challenge #1 - Data.xlsx')
sleep(5)