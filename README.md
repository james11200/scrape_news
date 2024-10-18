#Stock News Scraper and Price Labeler

This program is a tool for scrapping stock news data from https://invest.cnyes.com/ using the selenium library.

You can run the program and type the stock you want to scrape. Ex. AAPL, NVDA.

The output columns include [Date, Title, Content, and Page.]

After scraping the target stock news, run the label_price.py program to label the data with the stock price from yfinance corresponding to the date of the closing price.
