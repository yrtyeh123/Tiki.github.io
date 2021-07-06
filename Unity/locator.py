import random


class HomepageLocator(object):
    # Nút bỏ qua quảng cáo.
    slidedown_button = '//*[@id="onesignal-slidedown-cancel-button"]'

    # Thanh ngang tìm kiếm sản phầm.
    search_taskbar = '//*[@id="__next"]/div[1]/header/div[1]/div/div[1]/div[2]/div/input'

    # Nút tìm kiếm sản phẩm.
    search_button = '//*[@id="__next"]/div[1]/header/div[1]/div/div[1]/div[2]/div/button'


class ProductLocator(object):
    # Chọn khoảng giá mua.
    number_price = random.randint(1, 4)
    choose_price = '//*[@id="__next"]/div[1]/main/div[2]/div/div[1]/div[4]/div[1]/div[' + str(number_price) + ']/span'

    # CHọn hãng sản xuất.
    number_trademark = random.randint(1, 5)
    choose_trademark = '//*[@id="__next"]/div[1]/main/div[2]/div/div[1]/div[5]/div/label[' + str(
        number_trademark) + ']/label/span/img[2]'

    # Chọn sản phẩm đầu tiên hiện ra.
    if number_price == 1:
        first_product = '//*[@id="__next"]//div[1]/a/span/div/div[1]/img'
    elif number_price == 3:
        first_product = '//*[@id="__next"]//div[1]/a/span/div/div[1]/img[2]'
    else:
        first_product = '//*[@id="__next"]//a[1]/span/div/div[1]/img[2]'

    # Giá thực tế.
    real_price = '//*[@id="__next"]/div[1]/main/div[4]/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/span[1]'

    # Giá ban đầu.
    original_price = '//*[@id="__next"]/div[1]/main/div[4]/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/span[2]'

    # Phần trăm chiết khấu.
    discount_rate = '//*[@id="__next"]/div[1]/main/div[4]/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/span[3]'

    # Nút chọn hàng.
    shopping_button = '//*[@class="btn btn-add-to-cart"]'


class CartPageLocator(object):
    # Thanh nhập thông tin tài khoản.
    account_information_taskbar = '/html/body/div[10]/div/div/div/div[1]/div/form/div/input'

    # Nút "Tiếp tục".
    jog_on_button = '/html/body/div[10]/div/div/div/div[1]/div/form/button'

    # Nút hoàn tất đăng nhập.
    completed_button = '/html/body/div[10]/div/div/div/div[1]/div/form/button'

    # Nút nhảy vào giỏ hàng.
    shopping_cart = '//*[@class="btn-view-cart"]'

    # Nút chọn tất cả sản phẩm trong gian hàng.
    checkbox_fake = '//*[@id="__next"]/div[1]/main/div/div/div/div[3]/div[1]/div/div[1]/div/div[1]/label/span[1]'

    # Nút mua hàng.
    buying_button = '//*[@id="__next"]/div[1]/main/div/div/div/div[3]/div[2]/div/button'
