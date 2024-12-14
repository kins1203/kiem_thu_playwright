from playwright.sync_api import sync_playwright

def test_https_links():
    with sync_playwright() as p:
        print("Khởi động trình duyệt...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Truy cập trang https://demoqa.com/links...")
        page.goto("https://demoqa.com/links")

        links = page.query_selector_all("a")

        https_links = [link.get_attribute('href') for link in links if link.get_attribute('href') and link.get_attribute('href').startswith('https://')]

        print(f"Đang kiểm tra {len(https_links)} liên kết HTTPS...")

        for https_link in https_links:
            print(f"Kiểm tra liên kết HTTPS: {https_link}...")
            page.goto(https_link)

            response = page.goto(https_link)
            assert response.status == 200, f"Liên kết không hợp lệ: {https_link}, Mã trạng thái: {response.status}"

            print(f"Liên kết {https_link} hoạt động đúng.")

        page.close()
        browser.close()

        print("Hoàn thành kiểm thử HTTPS!")

if __name__ == "__main__":
    test_https_links()
