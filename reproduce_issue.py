from playwright.sync_api import sync_playwright

def test_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Use absolute path for the file
        import os
        path = "file://" + os.path.abspath("index.html")
        page.goto(path)

        # Check if Stage 1 is active and visible
        stage1 = page.locator('.stage[data-stage="1"]')
        print(f"Stage 1 active: {'active' in stage1.get_attribute('class')}")
        print(f"Stage 1 visible: {stage1.is_visible()}")

        # Check Stage 2
        stage2 = page.locator('.stage[data-stage="2"]')
        print(f"Stage 2 active: {'active' in stage2.get_attribute('class')}")
        print(f"Stage 2 visible: {stage2.is_visible()}")

        # Click unlock button in Stage 1
        page.locator('.stage[data-stage="1"] .unlock-btn').click()

        # Give it a moment for transitions
        page.wait_for_timeout(500)

        print("After click:")
        print(f"Stage 1 active: {'active' in stage1.get_attribute('class')}")
        print(f"Stage 1 visible: {stage1.is_visible()}")
        print(f"Stage 2 active: {'active' in stage2.get_attribute('class')}")
        print(f"Stage 2 visible: {stage2.is_visible()}")

        browser.close()

if __name__ == "__main__":
    test_navigation()
