# Tiki.github.io
locator chứa những Xpath em pull về từ trên web Tiki.
1. TikiHomePage
Mở trang chủ Tiki 
--> Đợi hiển thị Quảng Cáo khuyến mãi và bấm bỏ qua nó 
NẾU LỖI bắn ra dòng " Không tìm được nút bỏ qua quảng cáo ".
--> Click vào thanh ngang tìm kiếm và tra cứu về từ khoá "laptop" 
NẾU LỖI bắn ra dòng " Không thể tìm thấy thanh ngang hoặc không nhập được từ khoá 'laptop' "
--> Click vào nút tìm kiếm để di duyển đến trang sản phẩm 
NẾU LỖI bắn ra dòng " Không thấy nút TÌM KIẾM "
2. TikiProductPage.
--> Chọn một khoảng giá trong các mức giá trên web 
NẾU LỖI bắn ra dòng " Không chọn được khoảng giá nào ".
--> Sau khi chọn khoảng giá mua, đợi sản phẩm đầu tiên hiện ra và click chọn vô nó 
NẾU LỖI sẽ bắn ra dòng " Không có sản phầm nào phù hợp " 
// ở đây có 2 khả năng: 1 là lỗi nằm ở bên locator (tức Xpath bị sai) 
                        2 là không có sản phẩm của hãng đã chọn có mức giá như thế.
--> Đợi sản phẩm hiện ra và click vào nút chọn mua 
NẾU LỖI bắn ra dòng " Không tìm thấy nút CHỌN MUA"
3. TikiCartPage.
--> Sau khi bấm được nút chọn mua, Tiki sẽ yêu cầu ta đăng nhập tài khoản.
--> Đợi để nhập số điện thoại tài khoản Tiki
NẾU LỖI bắn ra dòng "Số điện thoại vừa nhập không hợp lệ hoặc không tìm thấy thanh nhập"
--> Bấm nút TIẾP TỤC 
NẾU LỖI bắn ra dòng " Không tìm thấy nút TIẾP TUC "
--> Đợi để nhập mật khẩu tài khoản Tiki
NẾU LỖI bắn ra dòng "Mật khẩu không hợp lệ hoặc không tìm thấy thanh nhập"
--> Bấm nút ĐĂNG NHẬP để hoàn thành việc đăng nhập tài khoản Tiki.
NẾU LỖI bắn ra " Không tìm thấy nút ĐĂNG NHẬP "
--> nhảy vào giỏ hàng
NẾU LỖI bắn ra dòng "Không tìm thấy nút vô giỏ hàng"
--> Click xác nhận tất cả đơn hàng
NẾU LỖI bắn ra "Không tìm được nút chọn toàn bộ đơn hàng"
--> Click vô nút mua hàng
NẾU LỖI bắn ra " Không tìm thấy nút mua hàng"

----> Hoàn tất việc test mua hàng trên Tiki còn bước cuối xác nhận đơn hàng thông qua 1 nút cuối nhưng em chỉ dám test đến đây vì lần trước em test đến tận bước chốt hàng, test nhiều quá gmail gửi về từ Tiki huỷ không kịp :((  
