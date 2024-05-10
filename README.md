# JKC (Jalapeño Kettle Chips) Web Scraper 2.0

![IMG_1526](https://github.com/joel-1080p/JKC/assets/156847809/f0dd82fb-ed1f-4cc0-aca5-3f480cb0d7a0)

## RUNNING JKC
- Change path on both `get_JKC_price.py` and `JKC.py` to whatever directory you stored the `data.csv` in.
- Run `get_JKC_price.py` to get the latest price from https://www.shoprite.com/sm/pickup/rsid/3000/product/kettle-brand-jalapeo-potato-chips-75-oz-00084114902047
- The script will get the current JKC price and store it in `data.csv`.
- To view historical data, go to local ip 127.0.0.1
- When you hover over the date on the price line, it will show you the price.
- If you tap or click on the price, it will show you if it's a sale price.
  
![Screenshot 2024-05-10 at 7 53 50 AM](https://github.com/joel-1080p/JKC/assets/156847809/ff603c75-5cce-4553-9314-afd3478abfce)
![Screenshot 2024-05-10 at 7 54 02 AM](https://github.com/joel-1080p/JKC/assets/156847809/e0be64b0-2597-4ca4-a163-090b909bd840)

## HOW IT WORKS
- `get_JKC_price.py` goes to the URL looks for today's price.
- It also scans for sale prices like '3 for $7' and stores this infomation as well.
- Either base price or sale price are stored in `data.csv`.
- When you run, the flask app, it pulls the data from `data.csv`.
- It checks for sale price first, then it looks at the base price.

## HOW I USE IT
- I opened port 5000 on my router and set the Flask app to broadcast on that port.
- I then can run it from from my mobile device wherever I am.

## KNOWN ISSUES
- When you click on a sale price and then try to click on a base price, it will disapear. You'd then have to click on it twice.

## Requirements

-   [Python](https://www.python.org) \>= 2.7, 3.4+
-   [Selenium](https://www.selenium.dev/) \>= 4.8
-   [Flask](https://flask.palletsprojects.com/en/3.0.x/) \>= 3.0.3

### P.S.

Please drop me a note with any feedback you have.

**Joel**
