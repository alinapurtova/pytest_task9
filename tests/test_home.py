import allure
from playwright.sync_api import expect


@allure.feature("Scroll")
@allure.story("Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality")
def test_scroll_up_and_down(page_objects):
    home = page_objects.home

    home.scroll_to_footer()
    expect(home.find(home.footer)).to_be_visible()
    home.verify_subscription_visible()
    home.scroll_up()
    home.verify_main_heading_visible()
