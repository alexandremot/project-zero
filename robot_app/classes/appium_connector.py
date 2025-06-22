from appium import webdriver
from appium.options.android import UiAutomator2Options

class AppiumConnector:

    def driver_initializer(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "ZF524DM7Q2"
        options.automation_name = "UiAutomator2"
        options.app_package = "com.itau"
        options.app_activity = "br.com.itau.pf.modules.features.appUse.appStart.splash.view.SplashActivity"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
        return driver
