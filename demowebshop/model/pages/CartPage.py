import os
from selene import browser, be
from selene import have



class CartPage:

    def open(self):
        browser.open('/cart')
        return self


    def should_have_product(self, product_name: str):
        browser.all('.product-name').element_by(have.exact_text(product_name)).should(be.visible)
        return self