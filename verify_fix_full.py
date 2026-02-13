from playwright.sync_api import sync_playwright
import os

def test_full_journey():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        path = "file://" + os.path.abspath("index.html")
        page.goto(path)

        total_stages = 6
        for i in range(1, total_stages):
            # Check current stage is visible and active
            stage = page.locator(f'.stage[data-stage="{i}"]')
            assert stage.is_visible()
            assert "active" in stage.get_attribute("class")

            # Check next stage is hidden
            if i + 1 <= total_stages:
                next_stage = page.locator(f'.stage[data-stage="{i+1}"]')
                assert not next_stage.is_visible()

            # Click unlock
            print(f"Unlocking stage {i} -> {i+1}")
            page.locator(f'.stage[data-stage="{i}"] .unlock-btn').click()
            page.wait_for_timeout(500)

        # Check final stage
        final_stage = page.locator(f'.stage[data-stage="{total_stages}"]')
        assert final_stage.is_visible()
        assert "active" in final_stage.get_attribute("class")
        print("Successfully reached the final stage!")

        # Verify surprise reveal
        print("Clicking surprise box...")
        page.locator(".surprise-box").click()
        page.wait_for_timeout(1000)
        assert page.locator("#surpriseContent").is_visible()
        print("Surprise content revealed!")

        browser.close()

if __name__ == "__main__":
    test_full_journey()
