from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By

# Ruta al controlador de Chrome
PATH = "/ruta/a/chromedriver"

# Crear objeto Service
service = Service(PATH)

# Configuración del controlador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")

# Iniciar el controlador de Chrome
driver = webdriver.Chrome(service=service, options=options)

# Abrir Tinder
driver.get("https://tinder.com")

# Boton de aceptar
#input("pera")
sleep(2)
aceptar = driver.find_element(By.XPATH, '//div[contains(text(), "Acepto")]')
aceptar.click()

# Boton de log in
sleep(2)
LogIn = driver.find_element(By.XPATH,'//div[contains(text(), "Iniciar sesión")]')
LogIn.click()

sleep(2)
#input("Presione Enter para cerrar el navegador...")

# Dar Click en google
#input(print("espera..."))
facebook = driver.find_element(By.XPATH, '//div[contains(text(), "Iniciar sesión con Facebook")]')
facebook.click()

# save references to main and FB windows
sleep(2)
base_window = driver.window_handles[0]
fb_popup_window = driver.window_handles[1]
# switch to FB window
driver.switch_to.window(fb_popup_window)

try:
    cookies_accept_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Accept Cookies")]')))
    cookies_accept_button.click()
except:
    print('no cookies')
sleep(2)
email_field = driver.find_element(By.NAME, 'email')
pw_field = driver.find_element(By.NAME, 'pass')
login_button = driver.find_element(By.NAME, 'login')
email_field.send_keys('anedacos@fiec.espol.edu.ec')
pw_field.send_keys('GerEman0034')
login_button.click()
driver.switch_to.window(base_window)
try:
    allow_location_button_again = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Allow")]')))
    allow_location_button_again.click()
except:
    print('no location popup')
try:
    enable_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Enable")]')))
    enable_button.click()
except:
    print('no location enable')
