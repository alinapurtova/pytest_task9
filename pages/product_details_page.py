from .base_page import BasePage
import allure
from playwright.sync_api import expect


class ProductDetailsPage(BasePage):
    name = "div.product-information h2"
    category = "div.product-information p:nth-of-type(1)"
    price = "div.product-information span span"
    availability = "div.product-information p:nth-of-type(2)"
    condition = "div.product-information p:nth-of-type(3)"
    brand = "div.product-information p:nth-of-type(4)"
    quantity_input = "input#quantity"
    add_to_cart_btn = "button.btn.btn-default.cart"
    view_cart_btn = "div.modal-body a"

    write_review_title = "a[href='#reviews']"
    name_input = "#name"
    email_input = "#email"
    review_input = "#review"
    submit_review_btn = "#button-review"
    success_message = "//span[text()='Thank you for your review.']"

    def verify_product_details(self):
        for locator in [self.name, self.category, self.price, self.availability, self.condition, self.brand]:
            assert self.is_visible(locator, "Product detail")

    def increase_quantity(self, qty: int):
        super().increase_quantity(self.quantity_input, qty)

    def add_to_cart(self):
        self.click(self.add_to_cart_btn, "Add to Cart")

    def click_view_cart(self):
        super().click_element(self.view_cart_btn, "View Cart")

    def verify_review_section_visible(self):
        expect(self.page.locator(self.write_review_title)).to_be_visible()

    def fill_review_form(self, name: str, email: str, review: str):
        self.fill(self.name_input, name, "Review Name")
        self.fill(self.email_input, email, "Review Email")
        self.fill(self.review_input, review, "Review Text")

    def submit_review(self):
        self.click(self.submit_review_btn, "Submit Review")

    def verify_review_success_message(self):
        expect(self.page.locator(self.success_message)).to_be_visible()

    def verify_on_product_page(self, product_id: int = 1):
        expected_url = f"{self.base_url}/product_details/{product_id}"
        with allure.step(f"Verify current URL is '{expected_url}'"):
            assert self.page.url == expected_url, f"Expected URL: {expected_url}, but got: {self.page.url}"
