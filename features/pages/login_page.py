from selenium.webdriver.common.by import By

from features.pages.base_page import Page


class LoginPage(Page):
    EMAIL_INPUT = (By.ID, "com.instagram.android:id/login_username")
    PASSWORD_INPUT = (By.ID, "com.instagram.android:id/password")
    SUBMIT_BUTTON = (By.ID, "com.instagram.android:id/button_text")

    def login_with_email_and_password(self, email, password):
        self.input(email, self.EMAIL_INPUT)
        self.input(password, self.PASSWORD_INPUT)
        self.click_on_element(self.SUBMIT_BUTTON)
