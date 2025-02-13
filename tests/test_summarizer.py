from utils.summarizer import ContentSummarizer
def test_summarize():
    summarizer = ContentSummarizer()
    sample_text = "This is the first sentence. This is the second sentence. This is the third sentence."
    result = summarizer.summarize(sample_text)
    assert "This is the first sentence." in result
    assert len(result.split('.')) <= 5
