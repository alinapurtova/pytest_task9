import pytest
import allure
from playwright.sync_api import Playwright, Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.contact_us_page import ContactUsPage
from pages.cart_page import CartPage


@pytest.fixture(scope="function")
def new_page(playwright: Playwright, request) -> Page:
    browser_name = request.config.getoption('--browser_name')
    headed = request.config.getoption('--headed')

    if browser_name not in ["chromium", "firefox", "webkit"]:
        raise ValueError(f"Unsupported browser: {browser_name}")

    browser = getattr(playwright, browser_name).launch(headless=not headed)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.set_default_timeout(10000)
    try:
        yield page
    finally:
        context.close()
        browser.close()


class PageObjects:
    def __init__(self, page):
        self.home = HomePage(page)
        self.login = LoginPage(page)
        self.products = ProductsPage(page)
        self.product_details = ProductDetailsPage(page)
        self.cart = CartPage(page)
        self.contact = ContactUsPage(page)


@pytest.fixture()
def page_objects(new_page):
    return PageObjects(new_page)


@pytest.fixture(autouse=True)
def open_home_before_test(page_objects):
    with allure.step("Open Home Page"):
        page_objects.home.open_home()
        page_objects.home.verify_home_title()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chromium', help="Browser: chromium, firefox, webkit")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()
    if result.failed and "new_page" in item.funcargs:
        page = item.funcargs["new_page"]
        allure.attach(
            page.screenshot(full_page=True),
            name=f"{item.nodeid.replace('::', '_')}.png",
            attachment_type=allure.attachment_type.PNG
        )
