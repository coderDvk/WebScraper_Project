#import libraries
from bs4 import BeautifulSoup
class DataExtractor:
    def extract(self, html):
        """Extracts headings and paragraph content from HTML."""
        try:
            soup = BeautifulSoup(html, "html.parser")
            headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3'])]
            paragraphs = [para.text.strip() for para in soup.find_all('p')]

            #combine extracted data
            extracted_data = "Headings:\n" + "\n".join(headings) + "\n\nParagraphs:\n" + "\n".join(paragraphs)
            return extracted_data
        except Exception as e:
            print(f"Error extracting data: {e}")
            return None
