from pages.base_page import BasePage


class TestCasesPage(BasePage):
    header = "#form h2"

    def verify_test_cases_page(self):
        self.is_visible(self.header, "Test Cases Page Header")
