shop_link =  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_should_see_add_to_basket(browser):
    browser.implicitly_wait(5)
    browser.get(shop_link)
    count_button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert count_button > 0, 'add to basket button is not found'
