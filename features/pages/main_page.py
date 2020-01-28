from selenium.webdriver.common.by import By

from features.pages.base_page import Page


def compare_data_with_expected(expected, real):
    assert expected == real, "Expected '{}', but got '{}'".format(expected, real)


class MainPage(Page):
    USER_ICON_LIST = (By.ID, "com.instagram.android:id/username")
    TAB_BAR = (By.ID, "com.instagram.android:id/tab_bar")
    LINER_BAR = (By.CLASS_NAME, "android.widget.FrameLayout")

    def verify_main_page_is_open(self):
        user_icon_list = self.find_elements(self.USER_ICON_LIST)

        compare_data_with_expected(expected=5, real=len(user_icon_list))
        compare_data_with_expected(expected="Your Story", real=user_icon_list[0].text)

        tab_bar = self.find_element(self.TAB_BAR)
        liner_tab = tab_bar.find_elements(self.LINER_BAR[0], self.LINER_BAR[1])

        compare_data_with_expected(expected=5, real=len(liner_tab))

        compare_data_with_expected(expected="Home", real=liner_tab[0].get_attribute("content-desc"))
        compare_data_with_expected(expected="Search and Explore", real=liner_tab[1].get_attribute("content-desc"))
        compare_data_with_expected(expected="Camera", real=liner_tab[2].get_attribute("content-desc"))
        compare_data_with_expected(expected="Activity", real=liner_tab[3].get_attribute("content-desc"))
        compare_data_with_expected(expected="Profile", real=liner_tab[4].get_attribute("content-desc"))
