from .base_page import BasePage
import allure
from playwright.sync_api import expect


class LoginPage(BasePage):
    email_input = "input[data-qa='login-email']"
    password_input = "input[data-qa='login-password']"
    login_btn = "button[data-qa='login-button']"
    error_message = "#form p"
    login_title = ".login-form h2"

    def login(self, email: str, password: str):
        with allure.step(f"Enter login credentials and click Login"):
            self.fill(self.email_input, email, "Email")
            self.fill(self.password_input, password, "Password")
            self.click(self.login_btn, "Login button")

    def verify_error_message(self):
        with allure.step("Verify login error message is visible"):
            expect(self.page.locator(self.error_message)).to_be_visible()

    def verify_title_visible(self):
        with allure.step("Verify login title is visible"):
            expect(self.page.locator(self.login_title)).to_be_visible()
