import unittest
import os
from automation.selenium_defense import SeleniumDefense
from automation.ransomware_simulation import RansomwareSimulator
from selenium import webdriver

class TestRansomwareSimulation(unittest.TestCase):
    def test_simulation_logging(self):
        simulator = RansomwareSimulator(driver_path="path/to/chromedriver")
        test_url = "https://example.com"
        
        simulator.simulate_attack(test_url)
        self.assertTrue(os.path.exists("simulation.log"))

        with open("simulation.log", "r") as log_file:
            log_content = log_file.read()
            self.assertIn("Simulation started for URL", log_content)
            self.assertIn("Simulation activity completed", log_content)

    def test_detect_automation(self):
        driver = webdriver.Chrome()
        try:
            result = SeleniumDefense.detect_automation(driver)
            self.assertIsNone(result)
        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()
