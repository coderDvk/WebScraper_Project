#import all required libraries
from utils.scraper import WebScraper
from utils.extractor import DataExtractor
from utils.summarizer import ContentSummarizer

class WebScraperApp:
    def __init__(self, url):
        self.url = url
        self.scraper = WebScraper()
        self.extractor = DataExtractor()
        self.summarizer = ContentSummarizer()

    def run(self):
        #Step1:- Scrape the content
        html_content = self.scraper.scrape(self.url)
        if not html_content:
            print("Failed to scrape content from the URL.")
            return

        #Step2:- Extract data
        extracted_data = self.extractor.extract(html_content)

        #Step3:- Summarize data
        summary = self.summarizer.summarize(extracted_data)

        #results
        print("\nExtracted Information:")
        print(extracted_data)
        print("\nSummary:")
        print(summary)

if __name__ == "__main__":
    url = input("Enter a URL to scrape: ")
    app = WebScraperApp(url)
    app.run()
