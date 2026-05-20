from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

# Defining Classes
class WebAutomation:
    def __init__(self):
        # Define driver, options, and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option("prefs", prefs)

        service = Service('chromedriver-mac-arm64/chromedriver')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Load login page
        self.driver.get('https://demoqa.com/login')
        # Locate username, password and login button
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userName'))
        )
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'password'))
        )
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in credentials and login
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the form elements
        self.driver.get("https://demoqa.com/text-box")

        self.driver.execute_script("""
               let ads = document.querySelectorAll('iframe');
               ads.forEach(ad => ad.remove());
           """)

        fullname_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userName'))
        )
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'userEmail'))
        )
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress'))
        )
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress'))
        )
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)

        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Go directly to the text-box page
        self.driver.get("https://demoqa.com/upload-download")

        # Remove ads on the new page
        self.driver.execute_script("""
            let ads = document.querySelectorAll('iframe');
            ads.forEach(ad => ad.remove());
        """)

        download_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'downloadButton'))
        )
        download_button.click()

        # FIX: wait for the download to start before close() quits the browser
        time.sleep(3)


    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    bot = WebAutomation()
    bot.login('Python_learning', '@Python1977')
    bot.fill_form("Python_learning", "@Python1977", "Random street 1", "Random street 1")
    bot.download()
    bot.close()

    # Finished for now 20/05/2026