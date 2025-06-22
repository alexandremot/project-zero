from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains

class RobotVirtualHand:
    def __init__(self, driver):
        self.driver = driver

    def click_at(self, coordinates):
        x, y = coordinates
        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()

    def send_text(self, texto):
        self.driver.switch_to.active_element.send_keys(texto)
