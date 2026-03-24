import unittest
import os

from scraper import Scraper

class TestScraper(unittest.TestCase):
    url = "https://www.thegoodscentscompany.com/peb-az.html"
    s = Scraper(url)

    # def test(self):
    #     # Must be false
    #     self.assertTrue(3 == 4)

    def test_scrape(self):
        """
        Test that it scrapes
        """

        # Deletes pre-existing files
        os.remove("index.json")

        soup = self.s.scrape()
        fn = self.s.saveIndex(soup)
        self.assertTrue(os.path.exists(fn))


if __name__ == '__main__':
    unittest.main()
