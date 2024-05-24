from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    NoSuchElementException, ElementNotInteractableException, JavascriptException,
    TimeoutException, ElementClickInterceptedException
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
import re
from datetime import datetime
from selenium.webdriver.edge.options import Options as EdgeOptions

class StockScraper:
    def __init__(self, stock):
        self.stock = stock
        self.url = f'https://invest.cnyes.com/usstock/detail/{stock}/news/englishnews#fixed'
        self.driver = self.initialize_driver()
        self.page = 1
        self.last_row_page = 0
        self.filename = f'{stock}_data.csv'
        self.last_row_title, self.last_row_page = self.read_last_row()

    def initialize_driver(self):
        user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')
        edge_options = EdgeOptions()
        edge_options.add_argument(f'user-agent={user_agent}')
        edge_options.add_argument('--headless')
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument('--window-size=1920,1080')
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Edge(options=edge_options)
        driver.get(self.url)
        return driver

    def save_csv(self, data):
        file_exists = os.path.exists(self.filename)
        with open(self.filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Date", "Title", "Content", "Page"])
            writer.writerow(data)

    def restart_driver(self):
        try:
            self.driver.close()
            self.driver = self.initialize_driver()
        except:
            print("Driver already closed last time")

    def get_articles(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'qmod-headline')]"))
        )
        return self.driver.find_elements(By.CLASS_NAME, 'qmod-headline')

    def close_ad(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, '_122qv')]"))
            )
            if element.is_displayed():
                element.click()
                print("Closed popup ad")
        except Exception as e:
            print("Nothing to close")

    def click_button(self, by_method, btn_name):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((by_method, btn_name))
            )
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by_method, btn_name))
            )
            if element.is_displayed():
                link = self.driver.find_element(by_method, btn_name)
                try:
                    link.click()
                except:
                    self.click_button(by_method, btn_name)
            else:
                print(f"Couldn't find button {btn_name}")
                js_code = "arguments[0].scrollIntoView();"
                self.driver.execute_script(js_code, link)
                link = self.driver.find_element(by_method, btn_name)
                ActionChains(self.driver).move_to_element(link).click(link).perform()
            return True    
        except TimeoutException:
            print(f"Timeout waiting for {btn_name} to be clickable")
            return False
        except ElementClickInterceptedException as e:
            print(f"ElementClickInterceptedException: {e}")
        except Exception as e:
            print("Error:", e)

    def split_text_at_ET(self, text):
        pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ET)'
        match = re.search(pattern, text)
        if match:
            split_pos = match.end()
            before_et = text[:split_pos]
            after_et = text[split_pos:].strip()
            after_et = re.sub(r'Summary\s*\n', '', after_et, 1)
            return after_et
        else:
            text = re.sub(r'Summary\s*\n', '', text, 1)
            return text

    def convert_date_form(self, date):
        try:
            date = datetime.strptime(date, "%B %d, %Y %I:%M %p")
            return date.strftime("%Y-%m-%d")
        except:
            print(f"Date format not matching since it's {str(date)}. Skipping.")
            return date

    def get_contents(self, articles, page):
        # contents = []
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        for article in articles:
            print("Article: ", article.text)
            self.click_button(By.PARTIAL_LINK_TEXT, article.text)
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[contains(@rv-html, 'modal.qmstory.qmtext')]"))
                )
            except TimeoutException:
                time.sleep(10)
                try:
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F5)
                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//*[contains(@rv-html, 'modal.qmstory.qmtext')]"))
                    )
                except TimeoutException:
                    print("Element is still not visible after additional wait.")
            date = self.driver.find_element(
                By.XPATH, "//*[contains(@rv-html, 'modal.qmstory.datetime')]").text
            date = self.convert_date_form(date)
            if date is not None:
                print(f'date: {str(date)}')
            else:
                print()
            cc = self.driver.find_element(
                By.XPATH, "//*[contains(@rv-html, 'modal.qmstory.qmtext')]").text
            cc = cc.split("Read the full article on Seeking Alpha")[0].split("Continue reading")[0].split("For further details see:")[0]
            cc = self.split_text_at_ET(cc)
            row = [date, article.text, cc, page]
            if len(str(cc)) > 10:
                self.save_csv(row)
                # contents.append(row)
                print(f'content appended: {cc[:50]}... \n')
            self.click_button(By.XPATH, "//*[contains(@rv-on-click, 'modal.close')]")
        # return contents

    def read_last_row(self):
        last_row = None
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    last_row = row
        if last_row:
            print(f"Found the row from the last scraping: {str(last_row[:2])} at page {str(last_row[-1])}")
            return last_row[1], int(last_row[3])
        return None, 0
    
    def try_next_page_again(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(@data-type, 'next')]"))
        )        

    def to_page(self, page_number):
        print(f"Processing to the last scraped page {page_number}")
        for _ in range(page_number - 1):
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@data-type, 'next')]"))
            )
            next_page = self.click_button(By.XPATH, "//*[contains(@data-type, 'next')]")
            
            while not next_page:
                print("Try reaching next page again")
                next_page = self.click_button(By.XPATH, "//*[contains(@data-type, 'next')]")         
                                       
            self.page += 1
            print(f"Now at page {self.page}")
        return page_number

    def start_from_last(self):
        self.page = self.to_page(self.last_row_page)
        print(f"Start scraping page {self.page}")
        articles = self.driver.find_elements(By.CLASS_NAME, 'qmod-headline')
        for index, article in enumerate(articles):
            if self.last_row_title == article.text:
                self.get_contents(articles[index + 1:], self.last_row_page)
                break

    def scrape(self, max_pages=1000):
        self.close_ad()
        if self.last_row_title:
            self.start_from_last()
        while self.page < max_pages:
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'qmod-headline')]"))
            )
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
            articles = self.get_articles()
            self.get_contents(articles, self.page)
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@data-type, 'next')]"))
            )
            self.click_button(By.XPATH, "//*[contains(@data-type, 'next')]")
            self.page += 1


if __name__ == "__main__":
    stock = "AAPL"
    scraper = StockScraper(stock)
    scraper.scrape()
