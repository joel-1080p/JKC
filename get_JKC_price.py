from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from datetime import date
import sys

# URL for ShopRite KETTLE BRAND Jalapeno, Potato Chips, 7.5 Ounce
url = "https://www.shoprite.com/sm/pickup/rsid/3000/product/kettle-brand-jalapeo-potato-chips-75-oz-00084114902047"

# Root folder.
root_folder = "C:\\Program Files (x86)\\JKC\\"

# Used to download current chrome driver.
s = Service(ChromeDriverManager().install())

# Creates undetected chrome driver with options.
# Sets the process to run in the background.
browser = uc.Chrome(use_subprocess = True,driver_executable_path = s.path)

# Requests information from the URL.
browser.get(url)

# Gets the HTML output in text format (one lone string).
html_output = browser.find_element(By.XPATH, "/html/body").text

# Splits the strings by new line.
html_output = html_output.split("\n")

# Get's today's date.
today = date.today()

# Parses the HTML output looking for strings that have'$' in it.
# Once it finds it, it knows that the price is the 2nd string.
for row in html_output:

    # Looks for $ in row.
    if '$' in row:

        # Looks for '2 for 6' type of price.
        # Gets the final price as a string.
        if '2 for' in row or '3 for' in row:

            # Splits input string.
            # Example - 2 for $5
            price_unsplit = row.split(' ')

            # Gets only the price.
            # Example - x[0] = '2', x[1] =, 'for' x[2] = '$5'
            price_str = price_unsplit[2].split('$')

            # Sets full price as the overall price.
            full_price = row

            # Gets the number price and casts it as float.
            # Example - y[0] = '$', y[1] = '5'
            price_float = float(price_str[1])

            # Splits the price to the price per unit.
            # Outputs as string.
            final_price = str(round(price_float/int(price_unsplit[0]),2))
            break

        # Gets the standard price for non-sale.
        elif 'was' in row:
 
                # Gets only the price.
                price_str = row.split('was')
                price_str = price_str[0].split('$')

                # If the price is greater than 0.
                if float(price_str[1]) > 0:

                    # Gets only the number price.
                    # Example - x[0] = '$', x[1] = '3'
                    final_price = price_str[1]

                    # Sets full price as empty string.
                    full_price = ' '
                    break

        # Gets the standard price.
        else:

            # Gets only the price.
            price_str = row.split('$')

            # If the price is greater than 0.
            if float(price_str[1]) > 0:

                # Gets the price without '$'
                final_price = price_str[1]

                # Sets full_price as blank.
                full_price = ' '
                break
    

# Opens the file in the Documents folder and appends new data to it.
# First if writes non-sale price, while sencond if statement writes '2 for 1' special.
with open(root_folder + 'data.csv', 'a') as f:
    if full_price == ' ':
        f.write(f"{today.strftime('%m/%d/%Y')},{str(final_price)},{full_price}\n")
    else:
        f.write(f"{today.strftime('%m/%d/%Y')},{str(final_price)},{full_price}\n")

# Closes chromedriver and browser.
browser.close()
browser.quit()

sys.exit()