from utils.data_generator import random_name, random_email, random_word, random_text
import allure


@allure.feature("Contact Us")
@allure.story("Test Case 6: Contact Us Form")
def test_contact_us_form(page_objects):
    home = page_objects.home
    contact = page_objects.contact

    home.go_to_contact_us()
    contact.verify_get_in_touch_visible()

    name = random_name()
    email = random_email()
    subject = random_word()
    message = random_text()

    contact.fill_contact_form(name, email, subject, message)
    contact.upload_file("test_file.txt")
    contact.submit_form()
    contact.verify_success_message()
    contact.click_home_button()
    home.verify_home_title()
