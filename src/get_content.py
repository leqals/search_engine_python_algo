from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

class ScrapeWebsite:
    def __init__(self, url):
        self.url = url
        self.content = None
        self.scrape()

    def scrape(self):
        options = Options()
        options.headless = True
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        try:
            driver = Firefox(executable_path="/geckodriver.exe", options=options)
            print("Scraping url...")
            driver.get(self.url)
            self.content = driver.page_source
            print("Scraping done.../n closing driver")
            driver.quit()
        except Exception as e:
            print("An error occurred while scraping the website:", e)
            