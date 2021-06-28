import unittest
import TikiHomePage
import TikiProductPage
import TikiCartPage

from selenium import webdriver


class TikiTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../chromessssss/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://tiki.vn/")

    def test_Tiki(self):
        # Vào trang chủ Tiki, nhấn nút quả qua quảng cáo và tra cứu sản phẩm.
        home_page = TikiHomePage.HomePage(self.driver)
        home_page.is_advertise_appear()
        home_page.search_information()
        # Vào trang sản phẩm, chọn mức giá, chọn sản phẩm đầu tiên hiện ra và chọn vào giỏ hàng.
        product_page = TikiProductPage.ProductPage(self.driver)
        product_page.choose_price()
        product_page.choose_first_item_appear()
        product_page.check_product_price()
        product_page.click_on_shopping_button()
        # Đăng nhập tài khoản, nhảy vào giỏ hàng, chọn tất cả đơn hàng, chọn mua hàng.
        cart_page = TikiCartPage.CartPage(self.driver)
        cart_page.log_in_account()
        cart_page.click_on_shopping_cart()
        cart_page.click_on_checkbox_fake()
        cart_page.click_on_buying_button()

    def tearDown(self):
        # Close the browser.
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
