from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, random, string
from random import seed
from random import randint
seed(27381)
driver = webdriver.Chrome()
passposible = ['contraContra1!','contraContra2!','contraContra3!']
passelegida = passposible[2]

#Obtención de un correo temporal
#driver.get("https://correotemporal.org/")
driver.get("https://www.google.com") #En pruebas
correo = driver.current_window_handle
#----------------
correotest = "jada50v_z156s@hxsni.com"
clavetest = "ContraSuperSegura"
#----------------
#Abrir Trulustore en nueva pestaña
driver.execute_script("window.open('https://trulustore.cl/mi-cuenta/','trulu');")
time.sleep(5)
#Obtener el correo temporal generado en correotemporal.org
#temp_email = driver.find_element(By.ID, "emailtemporal").get_attribute("value")

#Cambiar a pestaña trulustore
driver.switch_to.window("trulu")

#Ingresar correo y contraseña
#Por ahora se testea con un login
inputcorreo = driver.find_element(By.ID,"username")#driver.find_element(By.ID, "reg_email")
inputcorreo.send_keys(correotest)
#print("Correo utilizado: "+temp_email)
inputpass = driver.find_element(By.ID, "password")#driver.find_element(By.ID, "reg_password")
print("Contraseña utilizada: " + passelegida)
inputpass.send_keys(clavetest)
inputpass.send_keys(Keys.ENTER)
time.sleep(5)

#Cerrar sesión
driver.find_element_by_partial_link_text("Cerrar sesi").click()

#Fuerza bruta para inicio de sesión
inputcorreo = driver.find_element(By.ID,"username")
inputcorreo.send_keys(correotest)
inputbrute = driver.find_element(By.ID,"password")
for x in passposible:
    inputbrute.send_keys(x)
    #inputbrute.send_keys(Keys.ENTER)
    time.sleep(30)

#Sección de reestablecimiento de contraseña

#driver.find_element(By.PARTIAL_LINK_TEXT,"Olvidaste la contra").click()
#olvidaste = driver.find_element(By.ID,"user_login")
#olvidaste.send_keys(correotest)
#olvidaste.send_keys(Keys.ENTER)

#driver.quit()
