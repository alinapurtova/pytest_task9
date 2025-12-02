import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://automationexercise.com"

    @allure.step("Navigate to: {path}")
    def open(self, path: str = "/"):
        self.page.goto(f"{self.base_url}{path}")

    @allure.step("Click on '{name}'")
    def click(self, locator: str, name: str = ""):
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=5000)
        element.click()

    @allure.step("Fill '{name}' with '{text}'")
    def fill(self, locator: str, text: str, name: str = ""):
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=5000)
        element.fill(text)

    @allure.step("Check visibility of '{name}'")
    def is_visible(self, locator: str, name: str = "") -> bool:
        element = self.page.locator(locator)
        return element.is_visible()

    @allure.step("Verify page title: '{title}'")
    def verify_title(self, title: str):
        expect(self.page).to_have_title(title, timeout=5000)

    def increase_quantity(self, locator: str, qty: int, name: str = "Quantity"):
        with allure.step(f"Set {name} to {qty}"):
            self.page.locator(locator).fill(str(qty))

    def click_element(self, locator: str, name: str = ""):
        with allure.step(f"Click '{name}'"):
            self.page.locator(locator).click()
