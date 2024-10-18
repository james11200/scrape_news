import os
import pandas as pd
import yfinance as yf
from datetime import timedelta, datetime
from tqdm import tqdm

class StockPriceProcessor:
    def __init__(self, stock, file_path):
        self.stock = stock
        self.file_path = file_path
        self.df = None
        self.stock_data = None
        self.available_dates = None

    def load_data(self):
        self.df = pd.read_csv(f'{self.stock}/{self.file_path}.csv')
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def filter_data(self):
        print(f"Rows before filtering: {len(self.df)}")
        self.df['Content'] = self.df['Content'].apply(lambda x: str(x).split('Read more »')[0])
        self.df['Content_Word_Count'] = self.df['Content'].apply(lambda x: len(str(x).split()))
        self.df = self.df[self.df['Content_Word_Count'] >= 200]
        self.df = self.df.drop(columns=['Content_Word_Count'])
        print(f"Rows remaining after filtering: {len(self.df)}")

    def fetch_stock_data(self):
        start_date = self.df['Date'].min() - timedelta(days=100)
        end_date = self.df['Date'].max() + timedelta(days=100)

        print(f"Fetching historical stock prices for {self.stock} from {start_date} to {end_date}...")
        self.stock_data = yf.download(self.stock, start=start_date, end=end_date)
        self.stock_data.reset_index(inplace=True)
        self.available_dates = set(self.stock_data['Date'])
        print("Stock prices fetched.")

    @staticmethod
    def next_trading_day(date, available_dates):
        date = pd.Timestamp(date)
        while date not in available_dates:
            date += timedelta(days=1)
            if date > max(available_dates) or date > datetime.today():
                return None
        return date

    @staticmethod
    def previous_trading_day(date, available_dates):
        date = pd.Timestamp(date)
        while date not in available_dates:
            date -= timedelta(days=1)
            if date < min(available_dates):
                return None
        return date

    def process_news_data(self, prediction_days):
        self.df[f'{prediction_days}-Day Value Change'] = None
        self.df[f'{prediction_days}-Day Price Change (%)'] = None
        self.df['Transaction Volume'] = None
        self.df['Transaction Value'] = None
        
        today = datetime.today().date()
        
        print("Processing each news entry...")
        
        for idx, row in tqdm(self.df.iterrows(), total=len(self.df)):
            if pd.notna(row['Date']):
                news_date = row['Date'].date()
            else:
                if idx > 0:
                    news_date = self.df.loc[idx-1, 'Date'].date()
                else:
                    continue

            days_diff = (today - news_date).days
            
            if news_date == today or days_diff <= prediction_days:
                continue

            prediction_days_after = news_date + timedelta(days=prediction_days)

            prev_trading_date = self.previous_trading_day(news_date, self.available_dates)
            next_trading_date = self.next_trading_day(prediction_days_after, self.available_dates)

            if prev_trading_date is None or next_trading_date is None:
                continue

            prev_price = self.stock_data.loc[self.stock_data['Date'] == prev_trading_date, 'Adj Close'].values[0]
            next_price = self.stock_data.loc[self.stock_data['Date'] == next_trading_date, 'Adj Close'].values[0]

            if prev_price == 0 or next_price == 0:
                continue

            value_change = next_price - prev_price
            price_change_percentage = ((next_price - prev_price) / prev_price) * 100

            volume = self.stock_data.loc[self.stock_data['Date'] == prev_trading_date, 'Volume'].values[0]
            closing_price_on_news_date = self.stock_data.loc[self.stock_data['Date'] == prev_trading_date, 'Adj Close'].values[0]
            transaction_value = volume * closing_price_on_news_date

            self.df.at[idx, f'{prediction_days}-Day Value Change'] = value_change
            self.df.at[idx, f'{prediction_days}-Day Price Change (%)'] = price_change_percentage
            self.df.at[idx, 'Transaction Volume'] = volume
            self.df.at[idx, 'Transaction Value'] = transaction_value

    def save_data(self, prediction_days):
        directory = f"{self.stock}/labeled_data"
        os.makedirs(directory, exist_ok=True)        
        output_file_path = f'{self.file_path}_labeled_stock_price_{prediction_days}_days.csv'
        file_path = os.path.join(directory, output_file_path)
        self.df.to_csv(file_path, index=False)
        print(f"Updated CSV file with stock prices and changes saved to {output_file_path}")

        # directory = "aapl/labeled_data"
        # os.makedirs(directory, exist_ok=True)
        # file_path = os.path.join(directory, "aapl_50.csv")
        # df.to_csv(file_path, index=False)

    def run(self, prediction_days):
        self.load_data()
        self.filter_data()
        self.fetch_stock_data()
        self.process_news_data(prediction_days)
        self.save_data(prediction_days)


if __name__ == "__main__":
    stocks = ["META"]  # "TSLA","NVDA""AMZN", "AAPL", "GOOG", "MSFT"
    short_term = [i for i in range(1, 16)]
    mid_term = [15,30]
    long_term=[60,90,180]

    dates = short_term + mid_term+long_term
    print("Updating dates: ",dates)
    for stock in stocks:
        file_path = stock + '_data'
        for prediction_days in dates:
            processor = StockPriceProcessor(stock, file_path)
            processor.run(prediction_days)
