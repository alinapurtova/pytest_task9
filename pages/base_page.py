import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://automationexercise.com"

    def find(self, locator: str):
        return self.page.locator(locator)

    @allure.step("Navigate to: {path}")
    def open(self, path: str = "/"):
        self.page.goto(f"{self.base_url}{path}")

    def click(self, locator: str, name: str = "", index: int = None):
        with allure.step(f"Click on '{name}'"):
            element = self.find(locator)
            if index is not None:
                element = element.nth(index)
            expect(element).to_be_visible(timeout=5000)
            element.click()

    @allure.step("Fill '{name}' with '{text}'")
    def fill(self, locator: str, text: str, name: str = ""):
        element = self.find(locator)
        expect(element).to_be_visible(timeout=5000)
        element.fill(text)

    @allure.step("Check visibility of '{name}'")
    def is_visible(self, locator: str, name: str = "", timeout: int = 5000):
        element = self.find(locator)
        expect(element).to_be_visible(timeout=timeout)

    @allure.step("Check visibility of '{name}'")
    def is_locator_visible(self, locator, name: str = "", timeout: int = 5000):
        expect(locator).to_be_visible(timeout=timeout)

    @allure.step("Verify page title: '{title}'")
    def verify_title(self, title: str):
        expect(self.page).to_have_title(title, timeout=5000)

    def increase_quantity(self, locator: str, qty: int, name: str = "Quantity"):
        with allure.step(f"Set {name} to {qty}"):
            self.find(locator).fill(str(qty))
