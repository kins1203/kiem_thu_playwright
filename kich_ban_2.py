from playwright.sync_api import sync_playwright


def test_api_links():
    with sync_playwright() as p:
        print("Khởi động trình duyệt...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Truy cập trang https://demoqa.com/links...")
        page.goto("https://demoqa.com/links")

        api_links = {
            "a#created": 201,
            "a#no-content": 204,
            "a#moved": 301,
            "a#bad-request": 400,
            "a#unauthorized": 401,
            "a#forbidden": 403,
            "a#invalid-url": 404
        }

        for link_selector, expected_status in api_links.items():
            print(f"Kiểm tra liên kết: {link_selector}...")

            with page.expect_response(lambda response: response.status == expected_status) as response_info:
                page.click(link_selector)
            response = response_info.value

            actual_status = response.status
            print(f"Mã trạng thái nhận được: {actual_status}, Mong đợi: {expected_status}")
            assert actual_status == expected_status, f"Lỗi: Mã trạng thái không khớp! Nhận được: {actual_status}, Mong đợi: {expected_status}"

        page.close()
        browser.close()
        print("Hoàn thành kiểm thử API links!")


# Chạy kiểm thử
if __name__ == "__main__":
    test_api_links()
