import time

from Unity import BasePage
from Unity.locator import ProductLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage(BasePage):
    def choose_price(self):
        try:
            choose_price = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, ProductLocator.choose_price))
            )
            choose_price.click()
            print("Chọn thành công một khoảng giá.")
        except:
            print("Không chọn được khoảng giá nào.")
        time.sleep(5)

    def choose_trademark(self):
        try:
            choose_trademark = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, ProductLocator.choose_trademark))
            )
            choose_trademark.click()
            print("Chọn thành công hãng sản xuất.")
        except:
            print("Không chọn được nhà sản xuất nào.")
        time.sleep(5)

    def choose_first_item_appear(self):
        try:
            choose_first_item_appear = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, ProductLocator.first_product))
            )
            choose_first_item_appear.click()
            print("Lựa chọn sản phẩm đầu tiên hiện ra thành công.")
        except:
            print("Không có sản phẩm nào phù hợp.")
        time.sleep(5)

    def check_product_price(self):
        try:
            original_price = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, ProductLocator.original_price))
            )
            print("Giá ban đầu của sản phẩm là: ", original_price.text)
        except:
            print("Không lấy được giá bán ban đầu.")
        time.sleep(3)
        try:
            real_price = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, ProductLocator.real_price))
            )
            print("Giá thực tế của sản phần là: ", real_price.text)
        except:
            print("Không lấy được giá bán thực tế.")
        time.sleep(3)
        try:
            discount_rate = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, ProductLocator.discount_rate))
            )
            print("Phần trăm chiết khấu là: ", discount_rate.text)
        except:
            print("Không lấy được giá trị chiết khấu.")
        time.sleep(3)

    def click_on_shopping_button(self):
        try:
            shopping_button = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, ProductLocator.shopping_button))
            )
            shopping_button.click()
            print("Bấm thành công nút chọn hàng.")
        except:
            print("Không bấm được nút chọn hàng.")
        time.sleep(5)
