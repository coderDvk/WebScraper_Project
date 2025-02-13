#import libraries
from nltk.tokenize import sent_tokenize
class ContentSummarizer:
    def summarize(self, content):
        """Summarizes extracted content to the first 5 sentences."""
        try:
            sentences = sent_tokenize(content)
            return " ".join(sentences[:5])  # First 5 sentences
        except Exception as e:
            print(f"Error summarizing content: {e}")
            return None
