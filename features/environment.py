from appium import webdriver
from app.application import Application


def before_scenario(context, scenario):
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities={'platformName': 'Android',
                                                            'platformVersion': '6.0',
                                                            'deviceName': 'Android 6.0 x86',
                                                            'automationName': 'UiAutomator2',
                                                            'app': '/Users/safo/Desktop/AppiumBDD/insta.apk',
                                                            'appPackage': 'com.instagram.android',
                                                            "appWaitActivity": 'com.instagram.nux.activity.SignedOutFragmentActivity'
                                                            })

    context.driver.implicitly_wait(30)

    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
