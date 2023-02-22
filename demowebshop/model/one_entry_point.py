from demowebshop.model.pages.MainPage import MainPage
from demowebshop.model.pages.BooksPage import BooksPage
from demowebshop.model.pages.CartPage import CartPage
from demowebshop.model.pages.AccountPage import AccountPage






class Application:
    main = MainPage()
    books = BooksPage()
    cart = CartPage()
    account = AccountPage()