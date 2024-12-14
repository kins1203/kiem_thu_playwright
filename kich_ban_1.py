from playwright.sync_api import sync_playwright

def test_open_link_in_new_tab():
    with sync_playwright() as p:
        print("Khởi động trình duyệt...")
        browser = p.chromium.launch(headless=False) #Cái này mo trinh duyen k chay an
        context = browser.new_context()
        page = context.new_page()

        print("Truy cập vào trang https://demoqa.com/links...")
        page.goto("https://demoqa.com/links")

        print("Click vào Home...")




        #Bat su kien click mơ trang moi

        with context.expect_page() as new_page_info:
            page.click("a#simpleLink") #Dang click vao nut home
        new_page = new_page_info.value

        print("Chờ load...")
        new_page.wait_for_load_state("load")

        print("Đang kiểm tra URL của tab mới...")
        actual_url = new_page.url.rstrip('/')
        expected_url = "https://demoqa.com"

        print(f"URL thực tế: {actual_url}, URL mong đợi: {expected_url}")
        # Kiểm tra URL của tab mới
        assert actual_url == expected_url, f"URL không khớp! Thực tế: {actual_url}, Mong đợi: {expected_url}"

        print("Đóng tab mới và quay lại tab gốc...")
        new_page.close()
        page.close()
        browser.close()
        print("Hoàn thành kiểm thử!")

if __name__ == "__main__":
    test_open_link_in_new_tab()
