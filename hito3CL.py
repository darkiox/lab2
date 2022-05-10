from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, random, string
from random import seed
from random import randint
seed(27381)
driver = webdriver.Chrome()
passposible = ['contraContra1!','contraContra2!','contraContra3!','contraNueva1!']
passelegida = passposible[2]

#Obtención de un correo temporal
driver.get("https://correotemporal.org/")
correo = driver.current_window_handle #Guardar ventana de correo

#Abrir Trulustore en nueva pestaña
driver.execute_script("window.open('https://trulustore.cl/mi-cuenta/','trulu');")
time.sleep(5)

#Obtener el correo temporal generado en correotemporal.org
temp_email = driver.find_element(By.ID, "emailtemporal").get_attribute("value")

#Cambiar a pestaña trulustore
driver.switch_to.window("trulu")

#Ingresar correo y contraseña
inputcorreo = driver.find_element(By.ID, "reg_email")
inputcorreo.send_keys(temp_email)
#print("Correo utilizado: "+temp_email)
inputpass = driver.find_element(By.ID, "reg_password")
print("Contraseña utilizada: " + passelegida)
inputpass.send_keys(passelegida)
inputpass.send_keys(Keys.ENTER)
time.sleep(5)

#Sección de cambio de contraseña con login
driver.find_element(By.PARTIAL_LINK_TEXT,"Detalles de la cue").click()
time.sleep(1)
inpname = driver.find_element(By.ID, "account_first_name")
inpname.send_keys("Tulio")
inplname = driver.find_element(By.ID, "account_last_name")
inplname.send_keys("Trivinho")
inppasscurrent = driver.find_element(By.ID, "password_current")
inppasscurrent.send_keys(passelegida)
inppassnew1 = driver.find_element(By.ID, "password_1")
inppassnew1.send_keys(passposible[3])
inppassnew2 = driver.find_element(By.ID, "password_2")
inppassnew2.send_keys(passposible[3])
inppassnew2.send_keys(Keys.ENTER)
time.sleep(10)

#Cerrar sesión
driver.find_element_by_partial_link_text("Cerrar sesi").click()

#Sección de reestablecimiento de contraseña con correo
driver.find_element(By.PARTIAL_LINK_TEXT,"Olvidaste la contra").click()
olvidaste = driver.find_element(By.ID,"user_login")
olvidaste.send_keys(temp_email)
olvidaste.send_keys(Keys.ENTER)
time.sleep(10)
driver.switch_to.window(correo)
time.sleep(10)
driver.switch_to.window("trulu")

#driver.quit()
