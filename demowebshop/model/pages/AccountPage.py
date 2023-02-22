from selene.support.shared import browser
from selene import have


class AccountPage:

    def open(self):
        browser.open('/customer/info')
        return self

    def go_to_account_settings(self):
        browser.element('.account').click()
        return self

    def rename(self, name):
        browser.element('#FirstName').set_value(name)
        return self

    def save_info(self):
        browser.element('.save-customer-info-button').click()
        return self

    def back_to_main_page(self):
        browser.element('.header-logo').click()
        return self

    def first_name_should_have_value(self, new_value):
        browser.element('#FirstName').should(have.value(new_value))
        return self
