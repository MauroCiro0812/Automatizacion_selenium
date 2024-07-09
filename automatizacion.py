import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

excel_credenciales = r"C:\Users\Mauro\Downloads\prueba_automatizacion.xlsx"

df = pandas.read_excel(excel_credenciales)

user = df['usuario'][0]
psw = df['contraseña'][0]

print(user)
print(psw)

url1 = "https://www.linkedin.com/"

# Selectores:

boton_inicio_sesion = '/html/body/nav/div/a[2]'
# otra_cuenta = '/html/body/div/main/div/div[3]/div/button'
selector_usuario = '/html/body/div/main/div[2]/div[1]/form/div[1]/input'
selector_contraseña = '/html/body/div/main/div[2]/div[1]/form/div[2]/input'
boton_login = '/html/body/div/main/div[2]/div[1]/form/div[3]/button'

# Abrir navegador
driver = webdriver.Chrome()
# Maximizar pantalla
driver.maximize_window()

wait = WebDriverWait(driver, 10)

window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])

driver.get(url1)

# Acciones en la pagina

#driver.find_element_By_ID(boton_inicio_sesion).click()

#driver.find_element_By_ID(otra_cuenta).click()

#driver.find_element(selector_usuario).send_keys(user)

#driver.find_element(selector_contraseña).send_keys(psw)

#driver.find_element(boton_login).click()

botonInicio = driver.find_element(by=By.XPATH, value=boton_inicio_sesion)
botonInicio.click()

print("Boton inicio de sesion")

time.sleep(10)
# Esperamos hasta que el botón de exportar datos sea clickeable y luego hacemos clic en éls

print("Elegir otra cuenta")


selectorUsuario = driver.find_element(by=By.XPATH, value= selector_usuario)
selectorUsuario.send_keys(user)

print("trae el usuario del excel")


selectorContraseña = driver.find_element(by=By.XPATH, value=selector_contraseña)
selectorContraseña.send_keys(psw)

print("trae la contraseña del excel")


botonLogin = driver.find_element(by=By.XPATH, value=boton_login)
botonLogin.click()

print(" selecciona el login")


print ("Proceso terminado con exito")


# Mas acciones dentro de la pagina
time.sleep(7)

# cerrar
driver.quit()

