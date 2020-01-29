from selenium import webdriver
from time import sleep

from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(10)

        fb_button = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_button.click()

        # switch to login window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input.send_keys(username)
        pass_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_input.send_keys(password)
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(1)

        self.driver.switch_to_window(base_window)

        sleep(1)

        allow_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_btn.click()

        sleep(1)

        enable_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.8)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    continue
    
    def close_popup(self):
        popup_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_btn.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()
