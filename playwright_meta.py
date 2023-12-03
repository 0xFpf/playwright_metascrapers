from playwright.sync_api import sync_playwright
import time

# A meta script to automatically pull cookies and make a data request for json file using playwright,
# Requires a bit of trial and error finding the right request to get the data you want and get the right cookie

url='https://www.asos.com/asos-design/'
cookie_location=3
accept_cookies_name="That's ok"

def get_cookie_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        time.sleep(5)
        page.locator("'"+accept_cookies_name+"'").click()
        # page.click("button.L2AGLb")
        # pprint(context.cookies())
        cookie_value = context.cookies()[cookie_location]['value']
        cookie_key= context.cookies()[cookie_location]['name']
        print("Key of cookie: "+cookie_key)
        print("Value of cookie: "+cookie_value)
        browser.close()
    return cookie_key, cookie_value