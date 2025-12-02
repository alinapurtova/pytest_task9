import os
import allure
from pages.base_page import BasePage
from playwright.sync_api import expect


class ContactUsPage(BasePage):
    get_in_touch_title = ".bg h2.title.text-center"
    name_input = "input[data-qa='name']"
    email_input = "input[data-qa='email']"
    subject_input = "input[data-qa='subject']"
    message_input = "textarea[data-qa='message']"
    upload_input = "input[name='upload_file']"
    submit_btn = "input[data-qa='submit-button']"
    success_msg = "div.status.alert.alert-success"
    home_btn = "a.btn.btn-success"

    success_text = "Success! Your details have been submitted successfully."

    def verify_get_in_touch_visible(self):
        assert self.is_visible(self.get_in_touch_title, "'GET IN TOUCH' title")

    def fill_contact_form(self, name: str, email: str, subject: str, message: str):
        self.fill(self.name_input, name, "Name")
        self.fill(self.email_input, email, "Email")
        self.fill(self.subject_input, subject, "Subject")
        self.fill(self.message_input, message, "Message")

    def upload_file(self, filename: str):
        filepath = os.path.join(os.getcwd(), "files", filename)
        assert os.path.exists(filepath), f"File does not exist: {filepath}"
        locator = self.page.locator(self.upload_input)
        locator.scroll_into_view_if_needed()
        self.page.wait_for_selector(self.upload_input, state="visible", timeout=15000)
        locator.set_input_files(filepath)

    def submit_form(self):
        self.click(self.submit_btn, "Submit")
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.click(self.submit_btn, "Submit")

    def verify_success_message(self):
        with allure.step("Verify success message is visible"):
            msg = self.page.locator(self.success_msg)
            expect(msg).to_be_visible()
            assert self.success_text in msg.inner_text()

    def click_home_button(self):
        self.click(self.home_btn, "Home")
