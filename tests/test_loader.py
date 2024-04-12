# tests/test_loader.py

import unittest
import pandas as pd
import nltk
nltk.download('stopwords')  # Download stopwords corpus
nltk.download('punkt')

from src.loader import NewsDataLoader

class TestNewsDataLoader(unittest.TestCase):
    def setUp(self):
        # Initialize NewsDataLoader with sample data directory
        self.data_directory = "../data"
        self.loader = NewsDataLoader(self.data_directory)

    def test_load_data(self):
        # Test loading data method
        data = self.loader.load_data()
        self.assertIsNotNone(data)  

    def test_analyze_data(self):
        # Test analyze data method
        # Create sample data for testing
        sample_data = pd.DataFrame({
            'title_sentiment': [0.5, -0.2, 0.8],
            'GlobalRank': [1000, 2000, 1500]
        })
        analysis_result = self.loader.analyze_data(sample_data)
        # Assert expected results based on sample data
        self.assertIn('descriptive_statistics', analysis_result)
        self.assertAlmostEqual(analysis_result['mean_sentiment'], 0.36666666666666664)  # expected mean sentiment value
        self.assertAlmostEqual(analysis_result['median_sentiment'], 0.5)  # expected median sentiment value
        self.assertEqual(analysis_result['max_views'], 2000)  # expected max views value

    def test_preprocess_text(self):
        # Test preprocess text method
        # Create sample data for testing
        sample_description = pd.Series(['This is a test description.', 'Another test description.'])
        preprocessed_text = self.loader.preprocess_text(sample_description)

        expected_output = ['test descript', 'anoth test descript']
        self.assertEqual(preprocessed_text.tolist(), expected_output)

if __name__ == "__main__":
    unittest.main()
