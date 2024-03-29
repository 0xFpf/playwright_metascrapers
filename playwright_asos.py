from playwright.sync_api import sync_playwright
import requests
import time
import playwright_meta
import self_email
# Template for websites using playwright_meta
subject = 'Test Email'
body = 'This is a test email sent from a Python script. Item is in stock!'
sender_email = input('your_email@gmail.com ')
sender_password = input('your_generated_app_gmail_password ')
countdown=60*15 # 60 seconds*15= 15 minutes, this script checks stock every 15 minutes.

url2='https://www.asos.com/api/product/catalogue/v4/stockprice?productIds=205495961&store=COM&currency=GBP&keyStoreDataversion=h7g0xmn-38&country=GB'
COOKIE_KEY = None
COOKIE_VALUE = None

def get_cookies():
    cookie_key, cookie_value = playwright_meta.get_cookie_playwright()
    return cookie_key, cookie_value

def req_with_cookie(cookie_key, cookie_value):
    global COOKIE_KEY, COOKIE_VALUE
    cookies = dict(
        Cookie=f'notice_preferences=2:; notice_gdpr_prefs=0,1,2::implied,eu; {cookie_key}={cookie_value};')
    try:
        r = requests.get(url2, cookies=cookies)
        return r.json()
    except requests.RequestException as e:
        COOKIE_KEY = None
        COOKIE_VALUE = None
        print(f"Error during request: {e}")
        print("RESETTING COOKIES")


def check_stock():
    while True:
        global COOKIE_KEY, COOKIE_VALUE
        if COOKIE_KEY is None or COOKIE_VALUE is None:
            COOKIE_KEY, COOKIE_VALUE=get_cookies()
        else:
            data = req_with_cookie(COOKIE_KEY, COOKIE_VALUE)
            # print(data) # use this if you want to see where the variable you need to find is located
            isInStock=str(data[0]['variants'][0]['isInStock']) # change this to select and parse the data/variable you need
            print("isInStock "+isInStock)
            if isInStock == 'True':
                self_email.send_email(subject, body, sender_email, sender_password)
            else:
                pass
            time.sleep(countdown)

if __name__ == '__main__':
    check_stock()