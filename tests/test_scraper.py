import pytest
from utils.scraper import WebScraper

def test_scrape():
    scraper = WebScraper()
    url = "https://www.geeksforgeeks.org/java-programming-examples/"
    content = scraper.scrape(url)
    assert content is not None
    assert "<html" in content.lower()
