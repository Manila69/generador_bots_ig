import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyperclip
from mimesis import Generic
import random
import pyautogui

gen = Generic()

driver = webdriver.Chrome()
driver.maximize_window()
# Abre el sitio web
driver.get("https://maildrop.cc/")

# Espera hasta que la página esté completamente cargada
time.sleep(5)

# Encuentra y hace clic en el botón "Generar nuevo correo electrónico"
boton_mail = driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/section[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]')
boton_mail.click()

# Espera para asegurarse de que el nuevo correo electrónico se haya generado
time.sleep(2)

# Copia la nueva dirección de correo electrónico generada al portapapeles
mail = pyperclip.paste()
print(mail)
# Encuentra y hace clic en el enlace "Ir al buzón"
al_buzon = driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/section[1]/div/div[2]/div[2]/div/div[2]/div[2]/button')
al_buzon.click()

userName_input = driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div[3]/form/div/input')
userN = userName_input.get_attribute('value')
# Espera para asegurarse de que la nueva pestaña se haya abierto
time.sleep(2)

driver.execute_script("window.open('', '_blank');")
time.sleep(2)
# Cambia al controlador de la nueva pestaña
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
# Abre la segunda página en la nueva pestaña
driver.get("https://www.instagram.com/accounts/emailsignup/")

# Espera para asegurarse de que la página de registro de Instagram se haya cargado
time.sleep(5)

# Encuentra el campo de correo electrónico y lo completa con la dirección generada
mailOcel = driver.find_element(By.NAME, 'emailOrPhone')
mailOcel.send_keys(mail)

nombre = driver.find_element(By.NAME, 'fullName')
nombre.click()
time.sleep(1)
name = gen.person.full_name()
nombre.send_keys(name)
time.sleep(3)

username = driver.find_element(By.NAME, 'username')
username.click()

time.sleep(2)
username.send_keys(userN)
time.sleep(2)

passw = driver.find_element(By.NAME, 'password')
password = gen.person.password(length=9)
time.sleep(1)
passw.send_keys(password)

time.sleep(4)

# Ya rellene todo el formulario..
# Posición actual del mouse: Point(x=504, y=712)
pyautogui.moveTo(504, 712, duration=1)
send = driver.find_element(By.XPATH, '//button[@class="_acan _acap _acas _aj1- _ap30" and @type="submit"]')
time.sleep(4)
pyautogui.click()
time.sleep(1)
send.click()

# cumpleanios
time.sleep(3)
select_element = driver.find_element(By.XPATH, '//select[@title="Año:"]')
select_element.click()

time.sleep(2)

selec = driver.find_element(By.XPATH, '//option[@title="2003"]')
selec.click()

time.sleep(1)

select_element.click()

time.sleep(1)

enter = driver.find_element(By.XPATH, '//button[@type="button"]')
enter.click()

time.sleep(3)

cross = driver.find_element(By.CSS_SELECTOR, 'button._abl-')
time.sleep(1)
cross.click()

time.sleep(5)
#Posición actual del mouse: Point(x=504, y=494)
pyautogui.moveTo(504, 494, duration=1)

# Hacer clic en la ubicación actual del mouse
pyautogui.click()

time.sleep(2)
#enter = driver.find_element(By.XPATH, '//button[@type="button"]')
#enter.click()
