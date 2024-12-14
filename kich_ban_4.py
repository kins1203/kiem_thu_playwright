from playwright.sync_api import sync_playwright

def test_external_link():
    with sync_playwright() as p:
        print("Khởi động trình duyệt...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Truy cập trang https://demoqa.com/links...")
        page.goto("https://demoqa.com/links")

        print("Click vào liên kết 'External Link'...")

        with context.expect_page() as new_page_info:
            page.click("a#simpleLink")

        new_page = new_page_info.value

        actual_url = new_page.url
        expected_url = "https://www.google.com"

        print(f"URL thực tế: {actual_url}, URL mong đợi: {expected_url}")

        assert actual_url.startswith(expected_url), f"URL không khớp! Thực tế: {actual_url}, Mong đợi: {expected_url}"

        new_page.close()
        page.close()
        browser.close()

        print("Hoàn thành kiểm thử liên kết bên ngoài!")

if __name__ == "__main__":
    test_external_link()
