# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json
from pathlib import Path
import sys
from os.path import dirname, abspath

# Add the project root directory to the sys.path
# sys.path.insert(0, dirname(dirname(abspath(__file__))))

project_path = Path(r'/mnt/c/Users/miles/OneDrive/MPT_Test')


@pytest.fixture(scope="session")
def driver():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(
        "--no-sandbox")  # Optional: particularly for Linux environments and running as root (not recommended for production)

    # Create a new Chrome WebDriver instance with headless options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()



@pytest.fixture(scope="function", autouse=True)
def reset_state(driver):
    reset_state_script = """
    window.store.dispatch({ type: 'RESET_STATE', payload: JSON.parse(arguments[0]) })
    """
    with open(project_path / Path('tests/fixtures/data/mockStore.json'), 'r') as f:
        mock_store = json.load(f)
    driver.execute_script(reset_state_script, json.dumps(mock_store))
