from .base_page import BasePage
from playwright.sync_api import expect
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
    view_cart_btn = " div.modal-body a"
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

    def open_category(self, main_cat_locator, sub_cat_locator, name):
        with allure.step(f"Open category: {name}"):
            self.page.locator(main_cat_locator).first.click()
            self.page.locator(sub_cat_locator).first.click()

    def verify_category_title_contains(self, expected):
        with allure.step(f"Verify category title contains '{expected}'"):
            title = self.page.locator(self.category_title).first.inner_text()
            assert expected in title.upper(), \
                f"Expected title to contain '{expected}', got '{title}'"

    def verify_categories_visible(self):
        with allure.step("Verify categories block is visible"):
            assert self.page.locator(self.categories_block).is_visible(), \
                "Categories sidebar is not visible"

    def open_products(self):
        self.open("/products")
        expect(self.page.locator(self.all_products_title)).to_be_visible()

    def hover_product(self, index: int):
        with allure.step(f"Hover over product #{index}"):
            self.page.locator(self.product_cards).nth(index).hover()

    def add_to_cart(self, index: int):
        with allure.step(f"Add product #{index} to cart"):
            product = self.page.locator(self.product_cards).nth(index)
            product.hover()

            overlay_btn = product.locator(self.overlay_button)
            overlay_btn.click()

    def click_continue_shopping(self):
        with allure.step("Click 'Continue Shopping'"):
            self.page.locator(self.continue_shopping_btn).click()

    def click_view_cart(self):
        with allure.step("Click 'View Cart'"):
            self.page.locator(self.view_cart_btn).click()

    def verify_products_page(self):
        expect(self.page).to_have_title("Automation Exercise - All Products")
        locator = self.page.locator(self.products_list)
        assert locator.count() > 0, "No products found"
        expect(locator.first).to_be_visible()

    def view_first_product(self):
        # self.click(self.view_product_btn, "View first product")
        self.page.locator(self.view_product_btn).first.click()

    def search_product(self, product_name: str):
        with allure.step(f"Search for product: {product_name}"):
            self.page.fill(self.search_input, product_name)
            self.page.click(self.search_btn)

    def verify_searched_title_visible(self):
        with allure.step("Verify 'SEARCHED PRODUCTS' title is visible"):
            expect(self.page.locator(self.searched_products_title)).to_be_visible()

    def verify_searched_products_visible(self):
        with allure.step("Verify all searched products are visible"):
            products = self.page.locator(self.products_list)
            for i in range(products.count()):
                assert products.nth(i).is_visible()

    def verify_searched_products_contains_keyword(self, search_query: str):
        with allure.step(f"Verify all searched products contain '{search_query}' in their name"):
            products = self.page.locator(self.products_name)
            count = products.count()
            for i in range(count):
                product_text = products.nth(i).inner_text()
                assert search_query.lower() in product_text.lower(), f"Product '{product_text}' does not contain '{search_query}'"

    def increase_quantity(self, qty: int):
        with allure.step(f"Set quantity to {qty}"):
            self.page.locator(self.quantity_input).fill(str(qty))
