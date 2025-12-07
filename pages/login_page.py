from .base_page import BasePage
import allure


class LoginPage(BasePage):
    email_input = "input[data-qa='login-email']"
    password_input = "input[data-qa='login-password']"
    login_btn = "button[data-qa='login-button']"
    error_message = "#form p"
    login_title = ".login-form h2"

    def login(self, email: str, password: str):
        with allure.step("Enter login credentials and click Login"):
            self.fill(self.email_input, email, "Email")
            self.fill(self.password_input, password, "Password")
            self.click(self.login_btn, "Login button")

    def verify_error_message(self):
        self.is_visible(self.error_message, "Login error message")

    def verify_title_visible(self):
        self.is_visible(self.login_title, "Login page title")
