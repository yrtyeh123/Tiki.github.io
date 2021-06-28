import time

from locator import CartPageLocator
from __init__ import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage(BasePage):
    def log_in_account(self):
        try:
            account_phone_taskbar = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, CartPageLocator.account_information_taskbar))
            )
            account_phone_taskbar.send_keys("0837556473")
            print("Nhập thành công số điện thoại")
        except:
            print("Số điện thoại không hợp lệ hoặc không tìm thấy thanh nhập.")
        time.sleep(5)
        try:
            jog_on_button = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, CartPageLocator.jog_on_button))
            )
            jog_on_button.click()
            print("Ấn thành công nút ///tiếp tục///.")
        except:
            print("Không tìm được nút ///tiếp tục///.")
        time.sleep(5)
        try:
            account_password_taskbar = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, CartPageLocator.account_information_taskbar))
            )
            account_password_taskbar.send_keys("Dino2001d")
            print("Nhập thành công mật khẩu.")
        except:
            print("Mật khẩu không hợp lệ hoặc không tìm thấy thanh nhập.")
        time.sleep(10)
        try:
            completed_button = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, CartPageLocator.completed_button))
            )
            completed_button.click()
            print("Thành công hoàn tất việc đăng nhập tài khoản.")
        except:
            print("Không tìm thấy nút hoàn tất đăng nhập tài khoản.")
        time.sleep(10)

    def click_on_shopping_cart(self):
        try:
            shopping_cart = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, CartPageLocator.shopping_cart))
            )
            shopping_cart.click()
            print("Nhảy thành công vào giỏ hàng.")
        except:
            print("Không bấm được vào giỏ hàng.")
        time.sleep(10)

    def click_on_checkbox_fake(self):
        try:
            checkbox_fake = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, CartPageLocator.checkbox_fake))
            )
            checkbox_fake.click()
            print("Bấm chọn toàn bộ đơn hàng.")
        except:
            print("Không tìm được nút chọn toàn bộ đơn hàng.")
        time.sleep(10)

    def click_on_buying_button(self):
        try:
            buying_button = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, CartPageLocator.buying_button))
            )
            buying_button.click()
            print("Bấm thành công mua hàng.")
        except:
            print("Không tìm thấy nút mua hàng.")