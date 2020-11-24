import time
import random

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

from config import (
    CONF,
    eastern_tz
)
from constants import USER_AGENT_DATA_PATH


class WalmartCheckoutBot:

    def __init__(self, is_dry_run=False):
        self.is_dry_run = is_dry_run
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            f'--user-data-dir={CONF["chrome_profile_dir"]}'
        )

        self.driver_path = ChromeDriverManager().install()
        self.driver = None

    @staticmethod
    def get_random_user_agent():
        with open(USER_AGENT_DATA_PATH, 'r') as _file:
            agents = _file.readlines()
            idx = random.randint(0, len(agents))
        return agents[idx]

    def execute(self):
        self.wait_for_launch()

        self.driver = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

        self.driver.maximize_window()

        # add items to cart
        for url in CONF['item_urls']:
            self.driver.get(url)

            add_to_cart_class_name = 'button.spin-button.prod-ProductCTA--primary.button--primary'
            self.wait(By.CLASS_NAME, add_to_cart_class_name)
            add_to_cart_btn = self.driver.find_element_by_class_name(
                add_to_cart_class_name
            )
            add_to_cart_btn.click()

        # click checkout button
        check_out_class_name = 'button.ios-primary-btn-touch-fix.hide-content-max-m.checkoutBtn.button--primary'
        self.wait(By.CLASS_NAME, check_out_class_name)
        checkout_btn = self.driver.find_element_by_class_name(
            check_out_class_name
        )
        checkout_btn.click()

        # click continue button
        continue_class_name = 'button.cxo-continue-btn.button--primary'
        self.wait(By.CLASS_NAME, continue_class_name)
        continue_btn = self.driver.find_element_by_class_name(
            continue_class_name
        )
        continue_btn.click()

        continue_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button'
        self.wait(By.XPATH, continue_xpath)
        continue_btn = self.driver.find_element_by_xpath(
            continue_xpath
        )
        continue_btn.click()

        cvv_id_val = 'cvv-confirm'
        self.wait(By.ID, cvv_id_val)
        cvv_input_box = self.driver.find_element_by_id(
            cvv_id_val
        )
        cvv_input_box.clear()
        cvv_input_box.send_keys(CONF['cvv'])

        review_class_name = 'button.btn-block-max-s.pull-right.margin-top.fulfillment-opts-continue.button--primary'
        self.wait(By.CLASS_NAME, review_class_name)
        review_btn = self.driver.find_element_by_class_name(
            review_class_name
        )
        review_btn.click()

        if not self.is_dry_run:
            place_order_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button'
            self.wait(By.XPATH, place_order_xpath)
            place_order_btn = self.driver.find_element_by_xpath(
                place_order_xpath
            )
            place_order_btn.click()

    def wait(self, by, value, timeout=10000000000000):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            expected_conditions.visibility_of_element_located(
                (
                    by,
                    value
                )
            )
        )

    @staticmethod
    def wait_for_launch():
        launch_time = CONF['launch_time']
        now = datetime.now(tz=eastern_tz)
        while now < launch_time:
            time.sleep(.1)
            now = datetime.now(tz=eastern_tz)

    def stop(self):
        self.driver.quit()


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        '--dry',
        action='store_true'
    )

    args = vars(parser.parse_args())

    bot = WalmartCheckoutBot(is_dry_run=args['dry'])
    bot.execute()
