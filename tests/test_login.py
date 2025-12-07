import allure
from playwright.sync_api import expect

from utils.data_generator import random_email, random_password


@allure.feature("Login")
@allure.story("Test Case 3: Login User with incorrect email and password")
def test_login_incorrect(page_objects):
    home = page_objects.home
    login = page_objects.login

    home.go_to_login()
    login.verify_title_visible()

    email = random_email()
    password = random_password()

    login.login(email, password)
    expect(login.find(login.error_message)).to_be_visible()
    login.verify_error_message()
