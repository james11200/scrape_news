
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

| Date       | Title                                               | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Page | 5-Day Value Change | 5-Day Price Change (%) |
|------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|---------------------|------------------------|
| 2024-05-24 | Amazon: Ranking 'The Magnificent 7' (Midyear Update) | We provide an update to our January rankings of the Magnificent 7 stocks, with a special focus on Amazon. After reviewing Amazon's business, four big growth drivers, valuation and risks, we rank each "Mag-7" stock with special consideration for market conditions and the group's maturation, dividends, AI and more. We conclude with our strong opinion on investing in Amazon (and each of the Magnificent 7 stocks) for the remainder of this year (and beyond). Data as of 5/23/24 (StockRover) ... | 1    | 0.31                | 0.16                   |
| 2024-05-24 | Best Stocks To Buy Right Now? 2 Tech Stocks To Know | The tech industry is a dynamic and rapidly evolving sector of the stock market, characterized by innovation and rapid growth. Investing in tech stocks offers significant advantages, including the potential for high returns. ... [Read More] 2 Consumer Discretionary Stocks To Watch In Mid-May 2024. NVIDIA Corporation (NVDA) reported earnings of $6.12 per share, with revenue of $26.04 billion for the quarter. ... Salesforce (CRM) announced innovations to its Einstein 1 Marketing and Commerce platforms. | 1    | 0.31                | 0.16                   |
| 2024-05-23 | The Time Traveler's Portfolio: 3 Stocks to Buy Now for Massive Returns by 2034 | Imagine you could go back in time to find last decade’s long-term stocks to buy. Nvidia (NASDAQ: NVDA) returned nearly 20,000% growth since 2014. ... Mind Medicine (MNMD), Desktop Metal (DM), and Tesla (TSLA) are highlighted as potential long-term investments. Each stock presents unique opportunities in the evolving market landscape. | 1    | 3.11                | 1.66                   |

