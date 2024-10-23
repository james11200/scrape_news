
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
| Date       | Title                                               | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Page | 5-Day Value Change | 5-Day Price Change (%) | Transaction Volume | Transaction Value           |
|------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|---------------------|------------------------|--------------------|------------------------------|
| 2024-05-24 | Amazon: Ranking 'The Magnificent 7' (Midyear Update) | We provide an update to our January rankings of the Magnificent 7 stocks, with a special focus on Amazon. After reviewing Amazon's business, four big growth drivers, valuation and risks, we rank each "Mag-7" stock with special consideration for market conditions and the group's maturation, dividends, AI and more. We conclude with our strong opinion on investing in Amazon (and each of the Magnificent 7 stocks) for the remainder of this year (and beyond). Data as of 5/23/24 (StockRover) ... | 1    | 0.31                | 0.16                   | 36,294,600         | $6,895,247,952.93          |
| 2024-05-24 | Best Stocks To Buy Right Now? 2 Tech Stocks To Know | The tech industry is a dynamic and rapidly evolving sector of the stock market, characterized by innovation and rapid growth. Investing in tech stocks offers significant advantages, including the potential for high returns. ... [Read More] 2 Consumer Discretionary Stocks To Watch In Mid-May 2024. NVIDIA Corporation (NVDA) reported earnings of $6.12 per share, with revenue of $26.04 billion for the quarter. ... Salesforce (CRM) announced innovations to its Einstein 1 Marketing and Commerce platforms. | 1    | 0.31                | 0.16                   | 36,294,600         | $6,895,247,952.93          |
| 2024-05-23 | The Time Traveler's Portfolio: 3 Stocks to Buy Now for Massive Returns by 2034 | Imagine you could go back in time to find last decade’s long-term stocks to buy. Nvidia (NASDAQ: NVDA) returned nearly 20,000% growth since 2014. ... Mind Medicine (MNMD), Desktop Metal (DM), and Tesla (TSLA) are highlighted as potential long-term investments. Each stock presents unique opportunities in the evolving market landscape. | 1    | 3.11                | 1.66                   | 51,005,900         | $9,531,982,841.05          |



| Date       | Title                                                                                          | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |   Page |
|:-----------|:-----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------:|
| 2024-05-23 | Outperform Recommendation Issued On AAPL By Wedbush                                            | Wedbush analyst issues OUTPERFORM recommendation for AAPL on May 23, 2024 06:15PM ET. The previous analyst recommendation was Outperform. AAPL was trading at $186.88 at issue of the analyst recommendation. The overall analyst consensus : BUY. Current analyst recommendations are : 24 - Buy, 10 - Hold, 2 - Sell recommendations . Historical Analyst Recommendations Latest 10 recommenda ... Full story available on KlickAnalytics.com                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |      1 |
| 2024-05-23 | Opera: Best Of Both Worlds? Low PEG Ratio And High Dividend Yield                              | Opera Limited is a smaller technology company developing a better web browser for the world, especially gamers, with 300+ million active users. The European Union's promotion of competition in the browser space is boosting Opera's long-term outlook and driving strong business growth. OPRA's low valuation, high-growth rate, and extraordinary 6% dividend yield make it an appealing investment option. Opera Limited ( OPRA ) is a smaller technology company out of Norway, with 600 employees and an equity market cap of $1.15 billion at $13 per share. Each OPRA American Depository Share represents 2 ordinary shares , with the company acting as a subsidiary of Kunlun Tech Limited (with the latter holding more than 50% voting control). The outfit has developed its own web browsers and online software to compete with the big boys of Microsoft ( MSFT ) Edge/Explorer, Alphabet/Google ( GOOGL ) ( GOOG ) Chrome , Apple ( AAPL ) Safari , and not-for-profit Mozilla Firefox . Opera recently renewed its search agreement with Google , in place since 2001.... |      1 |
| 2024-05-23 | Apple foldable MacBooks could ship 1M units in 2026: analyst                                   | More on Apple Apple's Stock Is A Steal At This Price Apple Q2: Smartphone Sales Decline As Global Smartphone Market Grows Apple: Here's My Price Target And WWDC Strategy Humane explores sale after rocky launch of AI wearable device: Bloomberg Apple notches seven straight sessions of gains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |      1 |
| 2024-05-23 | Google plans to invest billions of dollars to make Pixel phones in India's Tamil Nadu - report | More on Alphabet Alphabet: Still A Hold Google: A Leader In AI Worth Investing In Google: An Undeniable Leader In AI For better or for worse: AI is changing content licensing and writing Google plans to bring ads in search AI Overviews                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |      1 |
| 2024-05-23 | 3 Blue Chip Stocks That You Can Buy and Hold for Years                                         | There are many stocks that you can invest in for the long haul and effectively forget about. These are businesses with robust financials, strong growth prospects, and a lot of stability for investors. They are what you would consider to be blue chip stocks. Three of the best blue chip stocks to buy, whether you're a seasoned investor or new to Wall Street, are Walmart (NYSE: WMT) , Apple (NASDAQ: AAPL) , and Eli Lilly (NYSE: LLY) . Here's a closer look at these stocks to see why they can make for solid investments in the long run. It's hard to imagine a scenario where big-box retailer Walmart isn't a huge force in the future. The company recently released its first-quarter earnings for fiscal 2025, with consolidated revenue of $161.5 billion (for the period ending April 30) rising by 6% year over year.                                                                                                                                                                                                                                                  |      1 |
| 2024-05-23 | 1 Stock Warren Buffett Is Selling Hand Over Fist                                               | Apple (NASDAQ: AAPL) is still Warren Buffett's biggest stock holding within Berkshire Hathaway (NYSE: BRK.A) (NYSE: BRK.B) , but the stake just got a lot smaller. Buffett is selling over 1 million shares per day on average, and Travis Hoium dug into why that might be in the video below. *Stock prices used were end-of-day prices of May 22, 2024. The video was published on May 22, 2024.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |      1 |
| 2024-05-23 | Could This Bull Market Buy Help You Become a Millionaire?                                      | Apple (NASDAQ: AAPL) has helped many investors become millionaires or at least generate a significant amount of wealth over the years. The maker of the iPhone, Mac, and other popular products has grown earnings over time, and that's prompted share-price performance. For example, Apple, including dividend payments, has climbed more than 900% over the past decade. In recent times, though, declining demand from China has weighed on earnings growth, and investors have seen Apple as slower than other tech companies to invest in the high-growth area of artificial intelligence (AI). As a result, the tech giant's shares have lagged behind; this year, they've hardly changed so far. Still, Apple over time has proven it's a growth company you can count on, and a top buy during bull markets and beyond. So could this bull market buy help you become a millionaire in the coming years as it's done for others in the past? Let's find out.                                                                                                                         |      1 |
| 2024-05-23 | Taiwan Semiconductor expects semiconductor industry's annual growth to reach 10% - report      | More on Taiwan Semiconductor TSMC: Derisking China Invasion Threats Taiwan Semiconductor: Breaking Major Upside Levels (Technical Analysis) Taiwan Semiconductor: Tracking A Trailing-Edge Semiconductor Slowdown TSMC, ASML could remotely shut down Taiwan chip machines if China invades: report Apple COO visits Taiwan Semiconductor to secure advanced tech for AI chips: report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |      1 |
