import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service


def scrape_website(website: str):
    """
    This method is scraping the website
    """
    print("Launching chrome driver")
