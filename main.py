import pyautogui as pg
import pygetwindow
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = r"D:\Games\chromedriver-win64\chromedriver.exe"
address = "https://elgoog.im/dinosaur-game/"


class Bot:
    def __init__(self):
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(address)

    def auth(self):
        time.sleep(15)
        try:
            agree_btn = self.driver.find_element(By.CLASS_NAME, "css-47sehv")
            agree_btn.click()
        except:
            print("error")

    def screen(self):
        game_window = pygetwindow.getActiveWindow()
        game_window.maximize()
        time.sleep(1)
        pg.press("space")
        time.sleep(3)
        game_play = pg.screenshot(region=(200, 700, 270, 300))
        game_play = game_play.convert('RGB')
        game = True
        while game:
            time.sleep(0.01)
            game_play = pg.screenshot(region=(210, 650, 260, 300))
            game_play = game_play.convert('RGB')
            for i in range(240, 260):
                r, g, b = game_play.getpixel((i, 250))
                p, q, r = game_play.getpixel((i, 135))
                brightness = (r + g + b) / 3
                brightness2 = (p + q + r) / 3
                if brightness < 210 or brightness2 < 210:
                    pg.press("space")
                    break


my_bot = Bot()
my_bot.auth()
my_bot.screen()
