from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time, random, string
driver = webdriver.Chrome()
passposible = ['contraContra1!','contraContra2!','contraContra3!','contraNueva1!']
passelegida = passposible[2]

#Obtención de un correo temporal
driver.get("https://correotemporal.org/")
correo = driver.current_window_handle #Guardar ventana de correo

#Abrir Aussar en nueva pestaña
driver.execute_script("window.open('https://www.aussar.es/iniciar-sesion?create_account=1','aussar');")
time.sleep(5)

#Obtener el correo temporal generado en correotemporal.org
temp_email = driver.find_element(By.ID, "emailtemporal").get_attribute("value")

#Cambiar a pestaña Aussar
driver.switch_to.window("aussar")

#Registro
driver.get("https://www.aussar.es/iniciar-sesion?create_account=1")
inputgender = driver.find_element(By.ID, "field-id_gender-1") #Click
inputname = driver.find_element(By.ID, "field-firstname")
inputlname = driver.find_element(By.ID, "field-lastname")
inputmail = driver.find_element(By.ID, "field-email")
inputpass = driver.find_element(By.ID, "field-password")
inputToS = driver.find_element(By.ID, "acceptLopd") #Click
inputgender.click()
inputname.send_keys("Tulio")
inputlname.send_keys("Trivinho")
inputmail.send_keys(temp_email)
inputpass.send_keys(passelegida)
inputToS.click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="customer-form"]/footer/button').click()
time.sleep(10)


#Cambiar contraseña con login
driver.find_element(By.XPATH,'//*[@id="header"]/nav/div[1]/div/div/div/div/div[2]/div/ul/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="identity-link"]/span').click()
inpoldpass = driver.find_element(By.ID, "field-password")
inpoldpass.send_keys(passelegida)
inpnewpass = driver.find_element(By.ID, "field-new_password")
inpnewpass.send_keys(passposible[3])
time.sleep(2)
inputToS2 = driver.find_element(By.ID, "acceptLopd") #Click
inputToS2.click()
time.sleep(2)
submit = driver.find_element(By.XPATH, '//*[@id="customer-form"]/footer/button')
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/nav/ol/li[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="main"]/footer/div/a').click()

#Recuperar contraseña
driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[3]/a').click()
inputmailr = driver.find_element(By.ID, "email")
inputmailr.send_keys(temp_email)
inputmailr.send_keys(Keys.ENTER)
time.sleep(10)
#Fuerza bruta
driver.find_element(By.XPATH, '//*[@id="back-to-login"]').click()
for x in passposible:
    loginmail = driver.find_element(By.ID, "field-email")
    loginmail.send_keys(temp_email)
    loginpass = driver.find_element(By.ID, "field-password")
    loginpass.send_keys(passposible[0])
    loginpass.send_keys(Keys.ENTER)
    if "mi-cuenta" in driver.current_url:
        break
    time.sleep(5)