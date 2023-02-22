from selene import browser, have, be


class MainPage:

    def open(self):
        browser.open('')
        return self

    def go_to_account_settings(self):
        browser.element('.account').click()
        return self

    def search_a_product(self, product_name: str):
        browser.element('[name=q]').type(product_name)
        browser.element('[type=submit]').click()
        return self

    def should_have_product(self, product_name: str):
        browser.all('.product-title').element_by(have.exact_text(product_name)).should(be.visible)
        return self

    def log_out(self):
        browser.element('.ico-logout').click()
        return self

    def should_not_be_logged(self):
        browser.element('.ico-login').should(have.exact_text('Log in'))
        return self





