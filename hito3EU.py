from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time, random, string
driver = webdriver.Chrome()


menu = 1
while(menu!=0):
    print("Ingrese su opcion: \n")
    print(" 1 - Registro automático \n")
    print(" 2 - Recuperar contraseña \n")
    print(" 3 - Bruteforce \n")
    print(" 4 - Cambiar contraseña con login \n")
    print(" 0 - Salir \n")
    if(menu == 1): #Registro
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
        inputmail.send_keys("tulitotrivinho@gmail.com")
        inputpass.send_keys("juaninteamo")
        inputToS.click()
        #driver.find_element(By.ID, "submit-login").click()
    elif(menu == 2): #Recuperar contraseña
        driver.get("https://www.aussar.es/recuperar-contrase%C3%B1a")
        inputmailr = driver.find_element(By.ID, "email")
        inputmailr.send_keys("tulitotrivinho@gmail.com")
        #inputmailr.send_keys(Keys.ENTER)
    elif(menu == 3): #Fuerza bruta
        driver.get("https://www.aussar.es/iniciar-sesion")