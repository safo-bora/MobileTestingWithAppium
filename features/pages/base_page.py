class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        return self.driver.find_elements(by=locator[0],
                                         value=locator[1])

    def find_element(self, locator):
        return self.driver.find_element(by=locator[0],
                                        value=locator[1])

    def click_on_element(self, locator):
        element = self.driver.find_element(by=locator[0],
                                           value=locator[1])
        element.click()

    def input(self, text, locator):
        password_input = self.driver.find_element(by=locator[0],
                                                  value=locator[1])
        password_input.send_keys(text)

