from features.credentials import EMAIL, PASSWORD
from features.pages.base_page import Page

from selenium.webdriver.common.by import By


class LoginPage(Page):
    EMAIL_INPUT = (By.ID, "com.instagram.android:id/login_username")
    PASSWORD_INPUT = (By.ID, "com.instagram.android:id/password")
    SUBMIT_BUTTON = (By.ID, "com.instagram.android:id/button_text")
    TRY_AGAIN_BUTTON = (By.ID, "com.instagram.android:id/negative_button")

    def login_with_email_and_password(self):

        if not EMAIL or not PASSWORD:
            raise Exception("Please add credentials to configuration file!")

        self.input(EMAIL, self.EMAIL_INPUT)
        self.input(PASSWORD, self.PASSWORD_INPUT)

        self.click_on_element(self.SUBMIT_BUTTON)

        # TODO Validate that we use correct credentials (There is no button "Retry again")
