import os
from dotenv import load_dotenv
import pytest
from selene.support.shared import browser
from data.users import User
from data.products import Product
from utils.base_session import BaseSession

BASE_URL = os.getenv('BASE_URL')
API_URL = os.getenv('BASE_URL')

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def given_browser_management():
    browser.config.base_url = BASE_URL

    yield

    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def demoshop():
    api_url = os.getenv('BASE_URL')
    return BaseSession(api_url)


@pytest.fixture(scope='function', autouse=False)
def given_customer(demoshop):
    customer = User(name='Aleksei',
                    email=LOGIN,
                    password=PASSWORD)

    response = demoshop.post('/login', json={'Email': customer.email, 'Password': customer.password},
                             allow_redirects=False)
    auth_cookie = response.cookies.get('NOPCOMMERCE.AUTH')

    browser.open(f'{API_URL}/Themes/DefaultClean/Content/images/logo.png')

    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_cookie})
    browser.open('')


@pytest.fixture(scope='function', autouse=False)
def given_books():
    computing_and_internet = Product(name='Computing and Internet',
                                     description='More Than 100 tips about computing and internet.',
                                     price='10.00')

    fiction = Product(name='Fiction',
                      description='Bestselling fiction',
                      price='24.00')

    science = Product(name='Science',
                      description='A guide to elementary science',
                      price='51.00')

    return {
        'computing_and_internet': computing_and_internet,
        'fiction': fiction,
        'science': science
    }


@pytest.fixture(scope='function', autouse=False)
def given_electronics():
    camera = Product(name='1MP 60GB Hard Drive Handycam Camcorder',
                     description='Capture video to hard disk drive; 60 GB storage',
                     price='349.00')

    return {
        'camera': camera
    }
