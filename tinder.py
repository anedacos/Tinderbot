from threading import Timer
from time import sleep
import loginFb
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import envio_msj_noLeidos


import deslizar
import envioMsjMatches

from selenium.webdriver.common.action_chains import ActionChains
#mensajes = loginFb.driver.find_element('xpath', 'q-1411276781"]')
#mensajes.click()
#input("Da enter para continuar...")


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 500)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_secs -= 1
    return num_of_secs
#loginFb.driver.implicitly_wait(10)
#actions = ActionChains(loginFb.driver)
#actions.move_to_element(element).perform()

def prueba():
    mensajes = loginFb.driver.find_element('xpath', '//*[@id="t595584048"]')
    mensajes.click()
    element = loginFb.driver.find_element(By.XPATH,'//*[@id="t-1582500781"]/div[4]')
    contador=0
    while contador<50:
        actions = ActionChains(loginFb.driver)
        actions.move_to_element(element).perform()
        contador += 1


#deslizar.auto_swipe()

#envioMsjMatches.send_messages_to_matches()
#input("Enter...")
#prueba()
envio_msj_noLeidos.send_messages_nuevos()


#input("Da enter para salir...")

loginFb.driver.quit()