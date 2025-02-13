Web Scraper Project

This project is a Python-based web scraper that extracts content (headings and paragraphs) from a given URL, processes the data, and provides a concise summary.

Features

Scrapes HTML content from any provided URL.
Extracts meaningful information such as headings and paragraphs.
Summarizes extracted content to the most relevant points (first 5 sentences).
Modular class-based design for scalability and maintainability.

Setup Instructions

Clone the repository:
git clone https://github.com/Manishsingh89716/Zocket_Task_
cd Zocket_Task_

Install dependencies:
pip install -r requirements.txt

Run the program:
python main.py
Enter a URL when prompted (e.g., https://www.geeksforgeeks.org/java-programming-examples/).

Usage
Input a valid URL to scrape.

The program will:
Scrape the content.
Extract headings and paragraphs.
Summarize the content into a concise overview.
Results will be displayed directly in the terminal.

Testing
To run unit tests, use:
pytest tests/

Future Enhancements
Handle pagination for multi-page scraping.
Export extracted content to a file (e.g., CSV or JSON).
Add support for dynamic websites using Selenium or Playwright.
