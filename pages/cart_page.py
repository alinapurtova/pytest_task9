import allure
from playwright.sync_api import expect
from .base_page import BasePage


class CartPage(BasePage):
    subscription_title = "div.single-widget > h2"
    email_input = "#susbscribe_email"
    submit_btn = "#subscribe"
    success_message = "//div[text()='You have been successfully subscribed!']"
    cart_rows = "tbody tr"
    product_name = "td.cart_description h4 a"
    product_price = "td.cart_price p"
    product_quantity = "td.cart_quantity button"
    product_total = "td.cart_total p"
    cart_product_qty = 'td.cart_quantity button'

    def open_cart(self):
        self.open("/view_cart")

    def get_product_info(self, index: int):
        row = self.page.locator(self.cart_rows).nth(index)
        return {
            "name": row.locator(self.product_name).inner_text(),
            "price": row.locator(self.product_price).inner_text(),
            "quantity": int(row.locator(self.product_quantity).inner_text().strip()),
            "total": row.locator(self.product_total).inner_text()
        }

    def verify_number_of_products(self, expected: int):
        with allure.step(f"Verify {expected} products in cart"):
            expect(self.page.locator(self.cart_rows)).to_have_count(expected)

    def scroll_to_footer(self):
        with allure.step("Scroll to footer"):
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def verify_subscription_title(self):
        assert self.is_visible(self.subscription_title, "SUBSCRIPTION title")

    def subscribe(self, email: str):
        self.fill(self.email_input, email, "Subscription email")
        self.click(self.submit_btn, "Submit subscription")

    def verify_subscription_success(self):
        assert self.is_visible(self.success_message, "Subscription success message")

    def verify_product_quantity(self, expected_qty: int):
        quantity_text = self.page.locator(self.cart_product_qty).inner_text()
        quantity = int(quantity_text.strip())
        assert quantity == expected_qty, f"Expected {expected_qty}, got {quantity}"