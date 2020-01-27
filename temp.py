from appium import webdriver
from selenium.webdriver.common.by import By
from config import configuration

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                          desired_capabilities={'platformName': 'Android',
                                                'platformVersion': '6.0',
                                                'deviceName': 'Android 6.0 x86',
                                                'automationName': 'UiAutomator2',
                                                'app': '/Users/safo/Desktop/AppiumBDD/insta.apk',
                                                'appPackage': 'com.instagram.android',
                                                "appWaitActivity": 'com.instagram.nux.activity.SignedOutFragmentActivity'
                                                })


#driver.install_app('/Users/safo/Desktop/AppiumBDD/insta.apk')

#driver.launch_app('com.android.instagram')

driver.implicitly_wait(10)

login_button = driver.find_element(By.ID, "com.instagram.android:id/log_in_button")
login_button.click()

# ------------------
# Login page
login_input = driver.find_element(By.ID, "com.instagram.android:id/login_username")
login_input.send_keys(configuration["email"])

password_input = driver.find_element(By.ID, "com.instagram.android:id/password")
password_input.send_keys(configuration["password"])

submit_button = driver.find_element(By.ID, "com.instagram.android:id/button_text")
submit_button.click()

# ----------------------
# Main page
user_icon_list= driver.find_elements(By.ID, "com.instagram.android:id/username")

assert len(user_icon_list) == 5
assert user_icon_list[0].text == "Your Story"

# ------------
# Tab bar
tab_bar= driver.find_element(By.ID, "com.instagram.android:id/tab_bar")
liner_tab = tab_bar.find_elements(By.CLASS_NAME, "android.widget.FrameLayout")

for i, elem in enumerate(liner_tab):
    print("Debug = ", elem.get_attribute("content-desc") )
    if i == 0 :
        assert elem.get_attribute("content-desc") == "Home"
    elif i == 1:
        assert elem.get_attribute("content-desc") == "Search and Explore"
    elif i == 2:
        assert elem.get_attribute("content-desc") == "Camera"
    elif i == 3:
        assert elem.get_attribute("content-desc") == "Activity"
    elif i == 4:
        assert elem.get_attribute("content-desc") == "Profile"
    else:
        raise Exception("Wrong result for = %s" % liner_tab)

driver.quit()

