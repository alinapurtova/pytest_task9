from .base_page import BasePage
import allure


class HomePage(BasePage):
    signup_login_btn = "a[href='/login']"
    test_cases_btn = "a[href='/test_cases']"
    products_btn = "a[href='/products']"
    contact_btn = "a[href='/contact_us']"
    cart_btn = ".nav [href='/view_cart']"
    subscription_title = "//h2[text()='Subscription']"
    scroll_up_btn = "#scrollUp"
    main_heading_text = "div.item.active > div:nth-child(1) > h2"
    home_title = "Automation Exercise"

    def open_home(self):
        self.open("/")
        self.verify_title(self.home_title)

    def go_to_login(self):
        self.click(self.signup_login_btn, "Signup / Login")

    def go_to_cart(self):
        self.click(self.cart_btn, "Cart button")

    def verify_home_title(self):
        self.verify_title(self.home_title)

    def go_to_test_cases(self):
        self.click(self.test_cases_btn, "Test Cases")

    def go_to_products(self):
        self.click(self.products_btn, "Products")

    def go_to_contact_us(self):
        self.click(self.contact_btn, "Contact Us")

    def scroll_to_footer(self):
        with allure.step("Scroll to footer"):
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        self.click(self.scroll_up_btn, "Scroll Up Arrow")

    def verify_subscription_visible(self):
        assert self.is_visible(self.subscription_title, "Subscription title")

    def verify_main_heading_visible(self):
        assert self.is_visible(self.main_heading_text, "Main heading")
