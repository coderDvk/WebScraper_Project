#import libraies
import requests
class WebScraper:
    def scrape(self, url):
        """Fetches HTML content from a URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error scraping URL: {e}")
            return None
