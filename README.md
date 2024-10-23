
# Stock Financial News Scraper and Price Labeller

This program is a tool for scraping stock news articles from https://invest.cnyes.com/ using the Selenium library and labeling them with historical stock prices.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [scrape_news.py](#scrape_newspy)
  - [label_price.py](#label_pricepy)

## Overview

1. `scrape_news.py`: This script scrapes stock financial news articles from a web source, specifically targeting US stock news.
2. `label_price.py`: This script labels each scraped news article with stock price data using historical price changes, leveraging Yahoo Finance.

## Requirements

The following Python libraries are required:
- `selenium`
- `pandas`
- `yfinance`
- `tqdm`

Make sure you have [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) installed and accessible via PATH for web scraping using Selenium.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/james11200/scrape_news.git
   ```

2. Install the required dependencies:
   ```
   pip install selenium pandas yfinance tqdm
   ```

3. Download and place Edge WebDriver executable in your PATH.

## Usage

### `scrape_news.py`

This script scrapes news articles from a stock's webpage on https://invest.cnyes.com/ using Selenium.

**Steps to use:**
1. Run the script:
   ```
   python scrape_news.py
   ```

2. Enter the stock symbol you want to scrape news for (e.g., AAPL for Apple, NVDA for Nvidia).

  The output will include the following columns:

  * Date: The date the news article was published.
  * Title: The title of the news article.
  * Content: The body text of the news article.
  * Page: The page number from the website.

3. The scraped data will be saved as a CSV file named `<stock>_data.csv`.


### `label_price.py`

This script processes the scraped news articles and labels them with the corresponding stock price changes, using data fetched from Yahoo Finance.


**Steps to use:**
1. Run the script:
   ```
   python label_price.py
   ```

2. The script will fetch the closing prices on the publication date of each article and add new columns to the CSV file.

   The processed CSV will be saved with additional columns for:

  * Closing Price: The stock's closing price on the article's publication date.
  * Price Changes: Stock price movements following the publication.
  * Transaction Details: Relevant information about price changes over time.

### Example of CSV Output

Here’s an example of how the output CSV file will look like:

| Date       | Title                                                                                          | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |   Page | 5-Day Value Change | 5-Day Price Change (%)|
|:-----------|:-----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------:|-----------:|-----------------------:|
| 2024-05-22 | 3 Inexpensive Stocks That Could Deliver Jaw-Dropping Returns                                     | InvestorPlace - Stock Market News, Stock Advice & Trading Tips
Everything looks expensive right now.
From groceries to travel and fuel, we’ve seen massive price hikes across all industries. And unless inflation cools, we must deal with it. However, investors can make the most of the impact of inflation on the stocks. Several stocks have seen a drop in value despite reporting impressive quarterly results.
So, could this be your chance to pounce? A few inexpensive high-potential stocks can deliver jaw-dropping returns, and they have already reported strong fundamentals.
Each stock trades below $200 and present as a long-term buy and hold. As some of the best companies in their respective industries, these stocks have the strength to survive the market turmoil and rise higher. Let’s take a look at them.
Airbnb (ABNB)
Source: sdx15 / Shutterstock.com
Beaten-down Airbnb (NASDAQ: ABNB ) stock is trading at $143 today and has lost 8% value in the past month. The company has been under pressure after the first-quarter results since investors weren’t happy with the guidance.
Airbnb had the best Q1 ever with 133 million nights and experiences booked. It reported an 18% year-over-year ( YOY ) jump in revenue to hit $2.1 billion. The net income came in at $264 million, which is also its most profitable first quarter.
However, the market only paid attention to the guideline for the second quarter which shadowed the impressive numbers. The management is aiming for a 9% revenue growth in Q2 to hit $2.7 billion, lower than the growth achieved in the first quarter and below estimates. Since Airbnb operates an asset-light model, it has the potential to gain financial strength with each profitable quarter.
I believe Airbnb is a solid long-term play and am impressed at the company’s bounce-back post pandemic. The summer travel could lead to better-than-expected results for the company.
ABNB gives strong competition to hotels and is using technology to enhance user experience. I think the market reaction is overdone, and the recent dip in the stock is a chance to accumulate.
Apple (AAPL)
Source: sylv1rob1 / Shutterstock.com                                       |      1 | -0.90998840|  -0.4766833066604257  |
| 2024-05-23 | Opera: Best Of Both Worlds? Low PEG Ratio And High Dividend Yield                              | Opera Limited is a smaller technology company developing a better web browser for the world, especially gamers, with 300+ million active users. The European Union's promotion of competition in the browser space is boosting Opera's long-term outlook and driving strong business growth. OPRA's low valuation, high-growth rate, and extraordinary 6% dividend yield make it an appealing investment option. Opera Limited ( OPRA ) is a smaller technology company out of Norway, with 600 employees and an equity market cap of $1.15 billion at $13 per share. Each OPRA American Depository Share represents 2 ordinary shares , with the company acting as a subsidiary of Kunlun Tech Limited (with the latter holding more than 50% voting control). The outfit has developed its own web browsers and online software to compete with the big boys of Microsoft ( MSFT ) Edge/Explorer, Alphabet/Google ( GOOGL ) ( GOOG ) Chrome , Apple ( AAPL ) Safari , and not-for-profit Mozilla Firefox . Opera recently renewed its search agreement with Google , in place since 2001.... |      1 |
| 2024-05-23 | Apple foldable MacBooks could ship 1M units in 2026: analyst                                   | More on Apple Apple's Stock Is A Steal At This Price Apple Q2: Smartphone Sales Decline As Global Smartphone Market Grows Apple: Here's My Price Target And WWDC Strategy Humane explores sale after rocky launch of AI wearable device: Bloomberg Apple notches seven straight sessions of gains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |      1 |
| 2024-05-23 | Google plans to invest billions of dollars to make Pixel phones in India's Tamil Nadu - report | More on Alphabet Alphabet: Still A Hold Google: A Leader In AI Worth Investing In Google: An Undeniable Leader In AI For better or for worse: AI is changing content licensing and writing Google plans to bring ads in search AI Overviews                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |      1 |
| 2024-05-23 | 3 Blue Chip Stocks That You Can Buy and Hold for Years                                         | There are many stocks that you can invest in for the long haul and effectively forget about. These are businesses with robust financials, strong growth prospects, and a lot of stability for investors. They are what you would consider to be blue chip stocks. Three of the best blue chip stocks to buy, whether you're a seasoned investor or new to Wall Street, are Walmart (NYSE: WMT) , Apple (NASDAQ: AAPL) , and Eli Lilly (NYSE: LLY) . Here's a closer look at these stocks to see why they can make for solid investments in the long run. It's hard to imagine a scenario where big-box retailer Walmart isn't a huge force in the future. The company recently released its first-quarter earnings for fiscal 2025, with consolidated revenue of $161.5 billion (for the period ending April 30) rising by 6% year over year.                                                                                                                                                                                                                                                  |      1 |
| 2024-05-23 | 1 Stock Warren Buffett Is Selling Hand Over Fist                                               | Apple (NASDAQ: AAPL) is still Warren Buffett's biggest stock holding within Berkshire Hathaway (NYSE: BRK.A) (NYSE: BRK.B) , but the stake just got a lot smaller. Buffett is selling over 1 million shares per day on average, and Travis Hoium dug into why that might be in the video below. *Stock prices used were end-of-day prices of May 22, 2024. The video was published on May 22, 2024.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |      1 |
| 2024-05-23 | Could This Bull Market Buy Help You Become a Millionaire?                                      | Apple (NASDAQ: AAPL) has helped many investors become millionaires or at least generate a significant amount of wealth over the years. The maker of the iPhone, Mac, and other popular products has grown earnings over time, and that's prompted share-price performance. For example, Apple, including dividend payments, has climbed more than 900% over the past decade. In recent times, though, declining demand from China has weighed on earnings growth, and investors have seen Apple as slower than other tech companies to invest in the high-growth area of artificial intelligence (AI). As a result, the tech giant's shares have lagged behind; this year, they've hardly changed so far. Still, Apple over time has proven it's a growth company you can count on, and a top buy during bull markets and beyond. So could this bull market buy help you become a millionaire in the coming years as it's done for others in the past? Let's find out.                                                                                                                         |      1 |
| 2024-05-23 | Taiwan Semiconductor expects semiconductor industry's annual growth to reach 10% - report      | More on Taiwan Semiconductor TSMC: Derisking China Invasion Threats Taiwan Semiconductor: Breaking Major Upside Levels (Technical Analysis) Taiwan Semiconductor: Tracking A Trailing-Edge Semiconductor Slowdown TSMC, ASML could remotely shut down Taiwan chip machines if China invades: report Apple COO visits Taiwan Semiconductor to secure advanced tech for AI chips: report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |      1 |
