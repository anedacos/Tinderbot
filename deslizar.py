from selenium.webdriver import Keys
from time import sleep
from loginFb import driver
def right_swipe():
    doc = driver.find_element('xpath', '//*[@id="Tinder"]/body')
    doc.send_keys(Keys.ARROW_RIGHT)

def auto_swipe():
    while True:
        sleep(1)
        try:
            right_swipe()
        except:
            close_match()

def close_match(self):
     match_popup = self.driver.find_element('xpath', '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
     match_popup.click()