from playwright.sync_api import sync_playwright

BASE_URL = "https://resume.auo.com/"

def test_register_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.click("a.btn-info[href='/Account/Agreement']")
        page.wait_for_url("**/Account/Agreement")
        assert "/Account/Agreement" in page.url
        browser.close()

def test_login_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.click("a.btn-primary[href='/Account/Login']")
        page.wait_for_url("**/Account/Login")
        assert "/Account/Login" in page.url
        browser.close()

def test_forgot_password_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.click("a.btn-primary[href='/Account/ForgetPassword']")
        page.wait_for_url("**/Account/ForgetPassword")
        assert "/Account/ForgetPassword" in page.url
        browser.close()

if __name__ == "__main__":
    test_register_button()
    test_login_button()
    test_forgot_password_button()
    print("All tests passed!")
