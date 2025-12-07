import allure
from playwright.sync_api import expect

from utils.data_generator import random_name, random_email, random_text

product_name = "Blue Top"


@allure.feature("Products")
@allure.story("Test Case 8: Verify All Products and product detail page")
def test_products_and_details(page_objects):
    home = page_objects.home
    products = page_objects.products
    product_details = page_objects.product_details

    home.go_to_products()
    products.verify_products_page()
    products.view_first_product()
    product_details.verify_on_product_page(product_id=1)
    product_details.verify_product_details()
    expect(product_details.find(product_details.name)).to_be_visible()


@allure.feature("Products")
@allure.story("Test Case 9: Search Product")
def test_search_product(page_objects):
    home = page_objects.home
    products = page_objects.products

    home.go_to_products()
    products.verify_products_page()
    products.search_product(product_name)
    products.verify_searched_title_visible()
    products.verify_searched_products_visible()
    products.verify_searched_products_contains_keyword(product_name)
    expect(products.find(products.products_list).first).to_be_visible()


@allure.feature("Products")
@allure.story("Test Case 18: View Category Products")
def test_view_category_products(page_objects):
    home = page_objects.home
    products = page_objects.products

    home.go_to_products()
    products.verify_categories_visible()

    products.open_category(
        products.women_category,
        products.women_dress_subcategory,
        "Women - Dress", index=0)

    products.verify_category_title_contains(products.expected_women_title)
    expect(products.find(products.category_title)).to_be_visible()

    products.open_category(
        products.men_category,
        products.men_tshirts_subcategory,
        "Men - Tshirts", index=0
    )
    products.verify_category_title_contains(products.expected_men_title)


@allure.feature("Products")
@allure.story("Test Case 21: Add review on product")
def test_add_review(page_objects):
    home = page_objects.home
    products = page_objects.products
    product_details = page_objects.product_details

    home.go_to_products()
    products.verify_products_page()
    products.view_first_product()

    product_details.verify_review_section_visible()
    expect(product_details.find(product_details.write_review_title)).to_be_visible()

    name = random_name()
    email = random_email()
    review = random_text()

    product_details.fill_review_form(name, email, review)
    product_details.submit_review()
    product_details.verify_review_success_message()
