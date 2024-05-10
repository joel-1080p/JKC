from selenium.webdriver.common.by import By
from datetime import date
import sys
from selenium import webdriver


# URL for ShopRite KETTLE BRAND Jalapeno, Potato Chips, 7.5 Ounce
url = "https://www.shoprite.com/sm/pickup/rsid/3000/product/kettle-brand-jalapeo-potato-chips-75-oz-00084114902047"

# Web driver.
browser = webdriver.Chrome()

# Requests information from the URL.
browser.get(url)

# Gets the span that holds the price.
price_element = browser.find_elements(By.XPATH, "//span[@data-testid='pdpMainPrice-div-testId']")

# Removes $ from the returned string.
price = price_element[0].text.replace('$','')

# Gets the span that holds the price.
deal_elements = browser.find_elements(By.XPATH, "//span[@data-testid='promotionBagdgeWrapper-testId']")

# Get's today's date.
today = date.today()

# Assigns the current price to the final price.
final_price = f"{today.strftime('%m/%d/%Y')},{price},{deal_elements[0].text}\n"

# Opens the file in the Documents folder and appends new data to it.
# First if writes non-sale price, while second if statement writes '2 for 1' special.
with open('C:/Users/joel/Documents/Freelance/Clients/ChrisLenk/Kettle2.0/source_code/data.csv', 'a') as f:
    f.write(final_price)

# Closes chrome driver and browser.
browser.close()
browser.quit()

sys.exit()
