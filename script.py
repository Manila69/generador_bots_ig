import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyperclip
from mimesis import Generic
import random
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Configuración inicial
gen = Generic()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://maildrop.cc/")
time.sleep(5)

# Genera un nuevo correo electrónico
boton_mail = driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/section[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]')
boton_mail.click()
time.sleep(2)

# Copia la nueva dirección de correo electrónico generada al portapapeles
mail = pyperclip.paste()
print(mail)

# Accede al buzón del nuevo correo
al_buzon = driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/section[1]/div/div[2]/div[2]/div/div[2]/div[2]/button')
al_buzon.click()

# Obtiene el nombre de usuario generado
userName_input = driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div[3]/form/div/input')
userN = userName_input.get_attribute('value')
time.sleep(2)

# Abre una nueva pestaña
driver.execute_script("window.open('', '_blank');")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)

# Accede a la página de registro de Instagram
driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(5)

# Completa el formulario de registro
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

# Clic en el botón de registro
pyautogui.moveTo(504, 712, duration=1)  # Ajustar según la ubicación del botón en tu pantalla
time.sleep(3)
pyautogui.click()

# Selecciona la fecha de nacimiento
time.sleep(3)
select_element = driver.find_element(By.XPATH, '//select[@title="Año:"]')
select_element.click()
time.sleep(2)
selec = driver.find_element(By.XPATH, '//option[@title="2003"]')
selec.click()
time.sleep(1)
select_element.click()
time.sleep(1)
pyautogui.moveTo(504, 494, duration=1)  # Ajustar según la ubicación del botón en tu pantalla
time.sleep(3)
pyautogui.click()

# Espera para la verificación del correo
time.sleep(15)
driver.switch_to.window(driver.window_handles[0])
time.sleep(60)

# Actualiza el buzón de correo y obtiene el código de verificación
actualizar = driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/main/div/div[1]/div/div/div[1]/div[2]/button')
actualizar.click()
time.sleep(5)
elemento_td = driver.find_element(By.XPATH, '//*[@id="email_content"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]')
numero = elemento_td.text
time.sleep(5)

# Cambia a la pestaña de Instagram y completa el código de verificación
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
input_code = driver.find_element(By.XPATH, '//*[@id="mount_0_0_/k"]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')
input_code.click()
time.sleep(1)
input_code.send_keys(numero)
time.sleep(1)
pyautogui.moveTo(953, 590, duration=1)  # Ajustar según la ubicación del botón en tu pantalla
time.sleep(3)
pyautogui.click()
