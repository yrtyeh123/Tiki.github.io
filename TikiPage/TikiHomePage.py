import time

from Unity import BasePage
from Unity.locator import HomepageLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(BasePage):

    def search_information(self):
        try:
            search_taskbar = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, HomepageLocator.search_taskbar))
            )
            search_taskbar.send_keys("ngo ngot")
            print("Hiển thi thanh ngang tìm kiếm và tra cứu về từ khoá ///ngo ngot///.")
        except:
            print("Không hiển thị thanh ngang tìm kiếm hoặc không nhập được từ khoá tra cứu.")
        time.sleep(10)

        try:
            search_button = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, HomepageLocator.search_button))
            )
            search_button.click()
            print("Tìm thấy nút tìm kiếm và bấm thành công vào nó.")
        except:
            print("Không tìm thấy nút tìm kiếm.")
        time.sleep(10)
