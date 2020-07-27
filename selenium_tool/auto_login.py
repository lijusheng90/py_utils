from secret_token.otp import generate_secret, generate_verify_code
from selenium import webdriver
import time


def generate_one_time_secret(our_permanent_secret, raw_secret):
    secret = generate_secret(raw_secret)
    verify_code = our_permanent_secret + generate_verify_code(secret)
    return verify_code


def auto_login(url, our_permanent_secret, raw_secret, user_name):
    pass_word = generate_one_time_secret(our_permanent_secret, raw_secret)
    browser = webdriver.Chrome(executable_path="chromedriver")
    browser.get(url)
    time.sleep(2)
    user_name_input = browser.find_element_by_id("username")
    user_pw_input = browser.find_element_by_id("password")
    user_login = browser.find_element_by_id("loginSubmit")

    user_name_input.send_keys(user_name)
    user_pw_input.send_keys(pass_word)
    # time.sleep(0.1)
    user_login.click()
    time.sleep(5)
    # browser.quit()


if __name__ == "__main__":
    our_permanent_secret = "xxxxxx"
    raw_secret = "xxxxxxxxxxx"
    url = "https://xxxxx.xxxxxx.xxxx/"
    user_name = "xxxxxx.xx"

    auto_login(url, our_permanent_secret, raw_secret, user_name)
