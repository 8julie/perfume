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
        if (os.path.exists("index.json")):
            os.remove("index.json")

        self.s.makeIndex()

        # soup = self.s.scrape()
        fn = self.s.makeIndex()
        self.assertTrue(os.path.exists(fn))

    # @unittest.skip("Don't need to rebuild every time")
    def test_scrape_index(self):
        """Tests if index is correct"""

        if (os.path.exists("/ingredients") == False):
            self.s.scrapeIndex()

        self.assertTrue(os.path.exists("/ingredients/172.json"))
    
    def test_scrape_profiles(self):
        # self.s.saveProfiles()


if __name__ == '__main__':
    unittest.main()
