import logging

class SeleniumDefense:
    @staticmethod
    def detect_automation(driver):
        """Detect if a browser is in headless mode."""
        try:
            capabilities = driver.capabilities
            is_headless = capabilities.get("headless", False)
            if is_headless:
                logging.warning("Headless browser detected! Possible automated attack.")
            else:
                logging.info("Browser is operating normally.")
        except Exception as e:
            logging.error(f"Error during automation detection: {str(e)}")
