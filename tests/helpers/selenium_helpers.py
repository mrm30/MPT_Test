# helpers/selenium_helpers.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_elements(driver, xpath, timeout=1):
    """Find elements by XPath with a specified timeout."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )


def assert_elements_present(elements, message):
    """Assert that elements are present."""
    assert len(elements) > 0, message
