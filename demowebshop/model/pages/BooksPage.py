import os
from selene import browser
from selene import have


BASE_URL = os.getenv('BASE_URL')

class BooksPage:

    def open(self):
        browser.open('/books')
        return self

    def go_to_product_page(self, *, book_title: str):
        browser.all('.product-title').element_by(have.exact_text(book_title)).click()
        return self

    def add_book_to_cart(self):
        browser.element('.add-to-cart-button').click()
        return self

    def go_to_cart(self):
        browser.element('.cart-label').click()
        return self

    def sort_books_by_name_z_to_a(self):
        browser.element('[value$="orderby=6"]').click()
        return self

    def should_be_sorted_by_name_z_to_a(self, first_in_sorting):
        browser.all('.product-title').first.should(have.exact_text(first_in_sorting))
        return self

