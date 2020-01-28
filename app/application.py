from features.pages.launch_page import LaunchPage
from features.pages.login_page import LoginPage
from features.pages.main_page import MainPage


class Application:
    def __init__(self, driver):
        self.launch_page = LaunchPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
