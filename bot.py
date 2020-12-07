
import selenium
from selenium import webdriver
import os






class Bot:

    def __init__(self):
        self.username = None
        self.password = None

        self.options = webdriver.ChromeOptions()
        self.options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        #self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"), chrome_options=self.options)
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def signin(self, username, password):
        self.driver.get("https://www.google.cl")
        print(username)
        print(password)

    def close(self):
        self.driver.close()



if __name__ == "__main__":
    bot = Bot()
    bot.signin("pytesting01", "456852jj")
    bot.close()

