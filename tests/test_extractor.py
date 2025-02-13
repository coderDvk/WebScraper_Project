from utils.extractor import DataExtractor
def test_extract():
    extractor = DataExtractor()
    sample_html = """
    <html>
        <body>
            <h1>Sample Heading</h1>
            <p>Sample paragraph content.</p>
        </body>
    </html>
    """
    result = extractor.extract(sample_html)
    assert "Sample Heading" in result
    assert "Sample paragraph content." in result
