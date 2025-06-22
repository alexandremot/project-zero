from classes.robot_hand import RobotVirtualHand
from classes.seeker import Seeker
from classes.appium_connector import AppiumConnector
from classes.screens_manager import ScreensManager

class Executor:

    def __init__(self):
        self.driver = AppiumConnector()
        self.clicker = RobotVirtualHand(self.driver.driver_initializer())
        self.seeker = Seeker()

    def get_image(self, image_reference):
        manager = ScreensManager()
        return manager.get_reference_image(image_reference)

    def acessa_tela(self, option):
        tela = self.get_image(option)
        element = self.seeker.get_buton(tela)
        self.clicker.click_at(element)

    def envia_texto(self, texto):
        self.clicker.send_text(texto)