from demowebshop.model.one_entry_point import Application as app


def test_add_a_product_to_cart(

    given_browser_management,
    given_customer,
    given_books):


    (
        app
        .books
        .open()
        .go_to_product_page(
            book_title=given_books['fiction'].name)
        .add_book_to_cart()
        .go_to_cart()
    )


    (
        app
        .cart
        .should_have_product(given_books['fiction'].name)
    )


def test_search_a_product(

    given_browser_management,
    given_customer,
    given_electronics):


    (
        app
        .main
        .search_a_product(given_electronics['camera'].name)


        .should_have_product(given_electronics['camera'].name)
    )


def test_rename_user(

    given_browser_management,
    given_customer):
    given_new_name = 'Vasya'


    (
        app
        .account.go_to_account_settings()
        .rename(name=given_new_name)
        .save_info()
        .back_to_main_page()
        .go_to_account_settings()


        .first_name_should_have_value(given_new_name)
    )



def test_sort_products_by_name_z_to_a(

    given_browser_management,
    given_customer,
    given_books):


    (
        app
        .books
        .open()
        .sort_books_by_name_z_to_a()


        .should_be_sorted_by_name_z_to_a(
            first_in_sorting=given_books['science'].name
        )
    )


def test_log_out(

    given_browser_management,
    given_customer):


    (
        app
        .main
        .log_out()


        .should_not_be_logged()
    )
