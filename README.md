# JKC (Jalapeño Kettle Chips) Web Scraper

![IMG_1526](https://github.com/joel-1080p/JKC/assets/156847809/f0dd82fb-ed1f-4cc0-aca5-3f480cb0d7a0)

### RUNNING JKC
- Shange path on both `get_JKC_price.py` and `JKC.py` to whatever directory you stored the `data.csv` in.
- Run `get_JKC_price.py` to get the latest price from https://www.shoprite.com/sm/pickup/rsid/3000/product/kettle-brand-jalapeo-potato-chips-75-oz-00084114902047
- The script will get the current JKC price and store it in `data.csv`.
- To view historical data, run `JKC.py`.
- If you hover over the date on the price line, it will show either the raw price or sale price.

![Screenshot 2024-03-08 at 9 30 46 AM](https://github.com/joel-1080p/JKC/assets/156847809/a52284c7-2d4b-43c9-8876-cb7f7d351038)
![Screenshot 2024-03-08 at 9 31 14 AM](https://github.com/joel-1080p/JKC/assets/156847809/f2cc39e3-c654-4690-8105-ab8aa24515b6)


### HOW IT WORKS
- `get_JKC_price.py` goes to the URL looks for today's price.
- It also scans for sale prices like '3 for $7' and stores this infomation as well.
- Either raw price or sale price are stored in `data.csv`.
- When you run, `JKC.py`, it pulls the data from `data.csv`.
- It checks for sale price first, then it looks at the raw price.

### HOW I USE IT
- Currently using pyinstaller to create a get_JKC_price.exe and JKC.exe
- All files were moved to Program Files (x86)
- I use Task Scheduler (or crontab on Linux) to automate the pull at 5AM every day.
- Next step is to create a full installer.

### KNOWN ISSUES
- When creating the exe, it has issues pulling the data.
- I believe this issue is caused with the chrome driver.

### Requirements

-   [Python](https://www.python.org) \>= 2.7, 3.4+
-   [Selenium](https://www.selenium.dev/) \>= 4.8

### P.S.

Please drop me a note with any feedback you have.

**Joel**
