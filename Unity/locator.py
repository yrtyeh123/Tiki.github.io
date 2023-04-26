import random


class HomepageLocator(object):
    # Nút bỏ qua quảng cáo.
    # slidedown_button = '//*[@id="onesignal-slidedown-cancel-button"]'

    # Thanh ngang tìm kiếm sản phầm.
    search_taskbar = '//*[@id="main-header"]//input'

    # Nút tìm kiếm sản phẩm.
    search_button = '//*[@id="main-header"]//button'


class ProductLocator(object):
    # Chọn khoảng giá mua.
    number_price = random.randint(1, 4)
    choose_price = '//*[@class="fast-price-filter"]/div[' + str(number_price) + ']/span'

    # CHọn hãng sản xuất.
    number_trademark = random.randint(1, 14)
    print(number_trademark)
    choose_trademark = '//*[@data-view-label = "Thương hiệu"]/div/label[' + str(number_trademark) + ']//img[2]'

    # Chọn sản phẩm đầu tiên hiện ra.
    first_product = '//a [@class= "product-item" and @data-view-index="0"]'

    # Giá thực tế.
    # real_price = '//*[@id="__next"]/div[1]/main/div[4]/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/span[1]'

    # Giá ban đầu.
    # original_price = '//*[@id="__next"]/div[1]/main/div[4]/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/span[2]'

    # Phần trăm chiết khấu.
    # discount_rate = '//*[@id="__next"]/div[1]/main/div[4]/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/span[3]'

    # Nút chọn hàng.
    shopping_button = '//*[@class="btn btn-add-to-cart"]'


class CartPageLocator(object):
    # Thanh nhập thông tin tài khoản.
    # account_information_taskbar = '//*[@class = "input "]'
    account_phone_taskbar = '//input [@type = "tel"]'
    account_pass_taskbar = '//input [@type = "password"]'

    # Nút "Tiếp tục".
    jog_on_button = '//*[@class = "styles__StyledLoginWithPhone-sc-si1ros-0 jdahxv"]/form/button'

    # Nút hoàn tất đăng nhập.
    completed_button = '//*[@class = "styles__StyledLoginWithPass-sc-1p7u8we-0 AFbbS"]/form/button'

    # Nút nhảy vào giỏ hàng.
    shopping_cart = '//*[@class="btn-view-cart"]'

    # Nút chọn tất cả sản phẩm trong gian hàng.
    checkbox_fake = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/div/div[1]/label/span'

    # Nút mua hàng.
    buying_button = '//*[@id="__next"]/div[1]/main/div/div/div[2]/div[2]/div/button'
