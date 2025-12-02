import allure
from utils.data_generator import random_email
import re


@allure.feature("Cart")
@allure.story("Test Case 11: Verify Subscription in Cart page")
def test_subscription_in_cart(page_objects):
    home = page_objects.home
    cart = page_objects.cart

    home.go_to_cart()
    cart.scroll_to_footer()
    cart.verify_subscription_title()

    email = random_email()
    cart.subscribe(email)
    cart.verify_subscription_success()


@allure.feature("Cart")
@allure.story("Test Case 12: Add Products in Cart")
def test_add_products_to_cart(page_objects):
    home = page_objects.home
    products = page_objects.products
    cart = page_objects.cart

    home.go_to_products()
    products.add_to_cart(0)
    products.click_continue_shopping()
    products.add_to_cart(1)
    products.click_view_cart()
    cart.verify_number_of_products(2)
    product1 = cart.get_product_info(0)
    product2 = cart.get_product_info(1)

    with allure.step("Verify product details"):
        assert product1["quantity"] == 1
        assert product2["quantity"] == 1

        price1 = int(re.sub(r"[^\d]", "", product1["price"]))
        price2 = int(re.sub(r"[^\d]", "", product2["price"]))
        total1 = int(re.sub(r"[^\d]", "", product1["total"]))
        total2 = int(re.sub(r"[^\d]", "", product2["total"]))

        assert total1 == price1
        assert total2 == price2


@allure.feature("Cart")
@allure.story("Test Case 13: Verify Product quantity in Cart")
def test_product_quantity_in_cart(page_objects):
    home = page_objects.home
    product_details = page_objects.product_details
    products = page_objects.products
    cart = page_objects.cart

    home.go_to_products()
    products.verify_products_page()
    products.view_first_product()
    product_details.verify_on_product_page(1)
    product_details.verify_product_details()
    product_details.increase_quantity(4)
    product_details.add_to_cart()
    product_details.click_view_cart()
    cart.verify_product_quantity(4)
