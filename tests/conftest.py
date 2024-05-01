import pytest

from playwright.sync_api import Page
from pages.home_pages import HomePage


@pytest.fixture
def fill_form(page: Page) -> HomePage:
    return HomePage(page)
