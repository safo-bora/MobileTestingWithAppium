from selenium.webdriver.common.by import By

from features.pages.base_page import Page


class LaunchPage(Page):
    BUTTON_LOGIN = (By.ID, "com.instagram.android:id/log_in_button")
    BUTTON_CREATE_ACCOUNT = (By.ID, "com.instagram.android:id/sign_up_with_email_or_phone")

    def login_with_existing_account(self):
        self.click_on_element(self.BUTTON_LOGIN)

    def create_new_account(self):
        self.click_on_element(self.BUTTON_CREATE_ACCOUNT)