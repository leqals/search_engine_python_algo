from bs4 import BeautifulSoup
import pandas as pd
from .get_content import ScrapeWebsite


class WebScraper:
    def __init__(self, url_list):
        self.url_list = url_list
        self.website_data = self.collect_website_data()
        self.website_data = self.preprocess_data()

    # Define function to scrape website content
    def scrape_website(self, url):
        response = ScrapeWebsite(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text_content = soup.get_text()
        print(text_content)
        # text_content = ' '.join(text_content.split())
        return text_content

    # Define function to collect data from a website
    def collect_website_data(self):
        website_data = []
        for url in self.url_list:
            content = self.scrape_website(url)
            website_data.append({'url': url, 'content': content})
        website_data_df = pd.DataFrame(website_data)
        return website_data_df

    # Define function to preprocess data
    def preprocess_data(self):
        # Remove irrelevant or duplicate content
        # (This can be done using techniques like stemming, lemmatization, or stopword removal)
        print('processing data.../n')
        print(self.website_data)
        return self.website_data
    