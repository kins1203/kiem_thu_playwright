from playwright.sync_api import sync_playwright

def test_link_not_responding():
    with sync_playwright() as p:
        print("Khởi động trình duyệt...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Truy cập trang https://demoqa.com/links...")
        page.goto("https://demoqa.com/links")

        def block_request(route, request):
            print(f"Đang chặn yêu cầu: {request.url}")
            route.abort()

        page.on("route", block_request)

        print("Click vào liên kết 'Created'...")
        page.click("a#created")

        try:
            page.wait_for_selector("text=ERR_CONNECTION_REFUSED", timeout=5000)
            print("Thông báo lỗi kết nối hiển thị!")
        except Exception as e:
            print("Không tìm thấy thông báo lỗi kết nối, hoặc trang không bị treo!")

        page.close()
        browser.close()
        print("Hoàn thành kiểm thử liên kết không phản hồi!")

if __name__ == "__main__":
    test_link_not_responding()
