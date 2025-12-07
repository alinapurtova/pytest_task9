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

    def open_cart(self):
        self.open("/view_cart")

    def get_product_info(self, product_id: int):
        row = self.find(self.cart_rows).nth(product_id-1)
        return {
            "name": row.locator(self.product_name).inner_text(),
            "price": row.locator(self.product_price).inner_text(),
            "quantity": int(row.locator(self.product_quantity).inner_text().strip()),
            "total": row.locator(self.product_total).inner_text()
        }

    def verify_number_of_products(self, expected: int):
        with allure.step(f"Verify {expected} products in cart"):
            expect(self.find(self.cart_rows)).to_have_count(expected)

    def scroll_to_footer(self):
        with allure.step("Scroll to footer"):
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def verify_subscription_title(self):
        self.is_visible(self.subscription_title, "SUBSCRIPTION title")

    def subscribe(self, email: str):
        self.fill(self.email_input, email, "Subscription email")
        self.click(self.submit_btn, "Submit subscription")

    def verify_subscription_success(self):
        self.is_visible(self.success_message, "Subscription success message")

    def verify_product_quantity(self, expected_qty: int):
        with allure.step(f"Verify product quantity is {expected_qty}"):
            quantity_locator = self.find(self.product_quantity)
            expect(quantity_locator).to_have_text(str(expected_qty))
