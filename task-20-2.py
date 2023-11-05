# using python Testing_script visit https://labour.gov.in/ and do the following task given:
# go to the menu whose name is "Documents" and Download the monthly progress report
# goto the menu whose name is media where you will find sub menu whose name is photo gallery.your task is to download 10 photos from the webpage and store themin a folder .kindly create the folder useing python only


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException,MoveTargetOutOfBoundsException
import requests

class Labour:
    def __init__(self, weburl):
        self.url = weburl
        options = webdriver.ChromeOptions()
        # options.add_experimental_option('detach',True)
        options.add_experimental_option("prefs", {
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally":True
        })
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def navigate_browser(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
    def file_autosaving_testcase(self):
        try:
          actions = ActionChains(self.driver)
          actions.move_to_element(self.driver.find_element(by=By.XPATH, value='//ul[@class="menu"]/following::a[text()="Documents"]'))
          sleep(3)
          actions.perform()
          self.driver.find_element(by=By.XPATH, value='//a[text()="Monthly Progress Report"]').click()
          sleep(2)
          self.driver.find_element(by=By.XPATH, value='//a[text()="Download(475.77 KB)"]').click()
          self.driver.switch_to.alert.accept()
          sleep(10)
        except NoSuchElementException as error:
            print(error)
        except ElementNotInteractableException as error1:
            print(error1)
        except MoveTargetOutOfBoundsException as error2:
            print(error2)

    def images_auto_saving(self):
        try:
            # we_using link_text to find dropdown list media
            navbar_media = self.driver.find_element(by=By.LINK_TEXT, value='Media')
            navbar_media_pg = self.driver.find_element(by=By.XPATH, value='//a[text()="Photo Gallery"]')
            image = self.driver.find_elements(by=By.XPATH, value='//div[@class="field-content"]/img')
            # Action_chains are used to complete keyboard_actions and mouse_hover_actions
            actions = ActionChains(self.driver)
            # now, first we hover to media element so we_using move to element method
            actions.move_to_element(navbar_media)
            # and it shows dropdown list in media with respective photo gallery we click that one
            actions.click(navbar_media_pg)
            # without initialize perform() method actions_chains should not work
            actions.perform()
            sleep(3)
            # we want copy some images and put in folder so,we import os module and we use it
            folder_name = 'images'
            # now we create folder with name is images
            os.makedirs(folder_name, exist_ok=True)
            # we get an image using xpath
            image = self.driver.find_elements(by=By.XPATH, value='//div[@class="field-content"]/img[@typeof="foaf:Image"]')
            # instead we want download only first 10 images so  using conditional statement
            # requests module are faster than selenium
            for index, image_element in enumerate(image[:10]):
                image_url = image_element.get_attribute('src')
                # it collects all source of images
                if image_url:
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        folder_path = os.path.join(folder_name, f'image_{index}.jpg')
                        with open(folder_path, 'wb') as f:
                            f.write(response.content)
        except NoSuchElementException as error:
            print(error)
    def quit(self):
        self.driver.quit()


link = "https://labour.gov.in/"
data = Labour(link)
data.navigate_browser()
data.file_autosaving_testcase()
data.images_auto_saving()



