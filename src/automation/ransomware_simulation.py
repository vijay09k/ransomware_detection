import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time

# Configure logging
logging.basicConfig(
    filename="simulation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RansomwareSimulator:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def simulate_attack(self, url):
        """Simulate a ransomware-like attack scenario."""
        service = Service(self.driver_path)
        driver = webdriver.Chrome(service=service)

        try:
            logging.info(f"Simulation started for URL: {url}")
            driver.get(url)
            logging.info("Page loaded successfully.")

            # Dynamically locate and interact with links
            links = driver.find_elements(By.TAG_NAME, "a")
            logging.info(f"Found {len(links)} links on the page.")

            for idx in range(min(5, len(links))):  # Limit to 5 links
                try:
                    # Re-locate links dynamically to avoid stale references
                    links = driver.find_elements(By.TAG_NAME, "a")
                    link = links[idx]
                    href = link.get_attribute("href")
                    logging.info(f"Clicking link {idx + 1}: {href}")

                    # Wait for the element to be clickable
                    wait = WebDriverWait(driver, 10)
                    clickable_element = wait.until(
                        EC.element_to_be_clickable((By.XPATH, f"(//a)[{idx + 1}]"))
                    )
                    clickable_element.click()

                    # Short delay to let the DOM stabilize
                    time.sleep(2)
                except (StaleElementReferenceException, TimeoutException) as e:
                    logging.warning(f"Failed to click link {idx + 1}: {str(e)}")
                except Exception as e:
                    logging.error(f"Unexpected error for link {idx + 1}: {str(e)}")

            logging.info("Simulation activity completed.")
        except Exception as e:
            logging.error(f"Simulation failed: {str(e)}")
        finally:
            driver.quit()
            logging.info("Browser session ended.")
