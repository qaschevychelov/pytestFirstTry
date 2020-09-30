from ..pages.YandexPages import SearchHelper
from ..beforeTest.conftest import browser


def test_yandex_search(browser):
    ya_main_page = SearchHelper(browser)
    ya_main_page.go_to_site()
    ya_main_page.enter_word("Привет")
    ya_main_page.click_on_the_search_button()
    elements = ya_main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements