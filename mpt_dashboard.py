from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dashboard():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")  # Optional: particularly for Linux environments and running as root (not recommended for production)

    # Create a new Chrome WebDriver instance with headless options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Navigate to the React program URL
        driver.get("http://host.docker.internal:3000/react_program")

        # Wait for the 'custom-swim-ctnr-button' elements to be present
        custom_swim_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'custom-swim-ctnr')]"))
        )

        # Check if any 'custom-swim-ctnr-button' elements are found
        assert len(custom_swim_buttons) > 0, "No 'custom-swim-ctnr-button' elements found"

        # Click the first 'custom-swim-ctnr-button' element
        custom_swim_buttons[0].click()

        # Wait for the 'Custom Swim Session' text to be present
        custom_swim_session_text = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Custom Swim Session')]"))
        )

        # Check if the 'Custom Swim Session' text is found
        assert len(custom_swim_session_text) > 0, "'Custom Swim Session' text not found"

        # Add any additional assertions or actions as needed

    finally:
        # Quit the WebDriver
        driver.quit()

if __name__ == "__main__":
    test_dashboard()
