from playwright.sync_api import expect

from .base_page import BasePage
import allure


class ProductsPage(BasePage):
    products_list = ".features_items .product-image-wrapper"
    view_product_btn = ".features_items .product-image-wrapper:first-child a[href*='product_details']"
    search_input = "#search_product"
    search_btn = "#submit_search"
    searched_products_title = "//h2[text()='Searched Products']"
    products_name = "div.productinfo > p"
    all_products_title = "//h2[text()='All Products']"
    product_cards = ".features_items .product-image-wrapper"
    add_to_cart_btn = "a.add-to-cart"
    continue_shopping_btn = "button.close-modal"
    view_cart_btn = "div.modal-body a"
    quantity_input = "input#quantity"
    categories_block = "//div[@class='left-sidebar']"
    overlay_button = ".overlay-content a.add-to-cart"

    women_category = ".category-products h4 a"
    women_dress_subcategory = 'a[href="/category_products/1"]'
    men_category = "#accordian > div:nth-child(2) h4 a"
    men_tshirts_subcategory = 'a[href="/category_products/3"]'
    category_title = "//h2[contains(@class, 'title text-center')]"

    expected_women_title = "WOMEN"
    expected_men_title = "MEN"

    def open_category(self, main_cat_locator, sub_cat_locator, name, index=0):
        main_selector = f"{main_cat_locator} >> nth={index}"
        self.click(main_selector, f"Main category {name}")
        self.click(sub_cat_locator, f"Subcategory {name}")

    def verify_category_title_contains(self, expected):
        title = self.find(self.category_title).inner_text()
        assert expected in title.upper(), f"Expected title to contain '{expected}', got '{title}'"

    def verify_categories_visible(self):
        self.is_visible(self.categories_block, "Categories sidebar")

    def open_products(self):
        self.open("/products")
        self.is_visible(self.all_products_title, "'All Products' title")

    def hover_product(self, index: int):
        with allure.step(f"Hover over product #{index}"):
            self.find(self.product_cards).nth(index).hover()

    def add_to_cart(self, product_id: int):
        with allure.step(f"Add product #{product_id} to cart"):
            product = self.find(self.product_cards).nth(product_id-1)
            product.hover()
            product.locator(self.overlay_button).click()

    def click_continue_shopping(self):
        self.click(self.continue_shopping_btn, "Continue Shopping")

    def click_view_cart(self):
        self.click(self.view_cart_btn, "View Cart")

    def verify_products_page(self):
        expect(self.page).to_have_title("Automation Exercise - All Products")
        locator = self.page.locator(self.products_list)
        assert locator.count() > 0, "No products found"
        expect(locator.first).to_be_visible()

    def view_first_product(self):
        self.click(self.view_product_btn, "View first product", index=0)

    def search_product(self, product_name: str):
        self.fill(self.search_input, product_name, "Search input")
        self.click(self.search_btn, "Search button")

    def verify_searched_title_visible(self):
        self.is_visible(self.searched_products_title, "'Searched Products' title")

    def verify_searched_products_visible(self):
        products = self.find(self.products_list)
        for i in range(products.count()):
            self.is_locator_visible(products.nth(i), f"Product #{i}")

    def verify_searched_products_contains_keyword(self, search_query: str):
        products = self.find(self.products_name)
        for i in range(products.count()):
            product_text = products.nth(i).inner_text()
            assert search_query.lower() in product_text.lower(), f"Product '{product_text}' does not contain '{search_query}'"

    def increase_quantity(self, qty: int):
        self.increase_quantity(self.quantity_input, qty)
