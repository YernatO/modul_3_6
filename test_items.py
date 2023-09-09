from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket(browser):
    browser.maximize_window()
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button.is_displayed()
    button.click()

