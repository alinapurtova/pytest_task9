from pages.base_page import BasePage
from playwright.sync_api import expect


class TestCasesPage(BasePage):
    header = "#form h2"

    def verify_test_cases_page(self):
        expect(self.page.locator(self.header)).to_be_visible()