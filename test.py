from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Optional: if you want to run headless
options.add_argument("--disable-gpu")  # Optional: on some systems, this can be required
options.add_argument("--no-sandbox")  # Optional: particularly for Linux environments and running as root (not recommended for production)

# Set up the service with ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Now pass the service and options when creating the Chrome WebDriver instance
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://host.docker.internal:3000/react_program")
    print(driver.title)  # Outputs the title of the page
finally:
    driver.quit()
