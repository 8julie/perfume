import unittest
import os

from scraper import Scraper

class TestScraper(unittest.TestCase):
    url = "https://www.thegoodscentscompany.com/peb-az.html"
    s = Scraper(url)

    # def test(self):
    #     # Must be false
    #     self.assertTrue(3 == 4)

    @unittest.skip("Don't need to rebuild every time")
    def test_index(self):
        """
        Test that it scrapes for the index
        """

        # Deletes pre-existing files
        os.remove("index.json")

        self.s.makeIndex()

        # soup = self.s.scrape()
        fn = self.s.makeIndex()
        self.assertTrue(os.path.exists(fn))

    def test_scrape_index(self):
        self.s.scrapeIndex()

if __name__ == '__main__':
    unittest.main()
