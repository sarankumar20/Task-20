from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from Data import data
from Locators import locator

class Cowin:
    def __init__(self):
        # Create a new WebDriver instance
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def navigating(self):
        try:
            # Open the Cowin website
            self.driver.get(data.Webdata().url)
            print(self.driver.title)
            print(self.driver.current_url)
            self.driver.implicitly_wait(10)
            # Find the "FAQ" and "Partners" anchor tags and click them to open new windows
            faq_menu = self.driver.find_element(by=By.LINK_TEXT, value=locator.Webelements().faq_menu)
            faq_menu.click()
            sleep(3)
            partners_menu = self.driver.find_element(by=By.XPATH, value= locator.Webelements().partner_menu)
            partners_menu.click()
            sleep(3)
        except NoSuchElementException as error1:
            print(error1)
    def close_all_windows(self):
        # Get the handles of the currently open windows (main window and the two new windows)
        window_handles = self.driver.window_handles
        # Close the two new windows
        self.driver.switch_to.window(window_handles[2])
        print(self.driver.current_url)
        self.driver.close()
        sleep(3)
        self.driver.switch_to.window(window_handles[1])
        print(self.driver.current_url)
        self.driver.close()
        sleep(3)
        # Switch back to the main window
        self.driver.switch_to.window(window_handles[0])
        self.driver.close()

driver = Cowin()
driver.navigating()
driver.close_all_windows()
