import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path to the ChromeDriver)


CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH", r"C:\Users\vijay\projects\chromedriver-win64\chromedriver.exe")