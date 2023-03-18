from src.scrape import WebScraper
from src.search_engine import TFIDF

url_list = ['https://leqals.github.io/']
web_scraper = WebScraper(url_list)
website_data = web_scraper.website_data

# define some sample documents
docs = website_data
tfidf = TFIDF(docs)

query = "cat"
sorted_indexes = tfidf.search(query)
print(sorted_indexes)
print(docs)
# for i in sorted_indexes:
    # print(docs[i])
