from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time, random, string
driver = webdriver.Chrome()

driver.get("https://bycatchproject.co.uk/register.php")

#Registro
inputusuario = driver.find_element(By.ID,"username")
inputpassword = driver.find_element(By.ID,"password")
inputemail = driver.find_element(By.ID, "email")
inputname = driver.find_element(By.ID, "name")
inputorganisation = driver.find_element(By.ID, "organisation")
input18 = driver.find_element(By.ID, "18")
inputprepared = driver.find_element(By.ID, "prepared")
inputTandC = driver.find_element(By.ID, "TandC")
selectcountry = Select(driver.find_element(By.ID,"country"))
selectage = Select(driver.find_element(By.NAME,"age"))
selectareyoua = Select(driver.find_element(By.NAME,"occupation"))
selectexperience = Select(driver.find_element(By.NAME, "experience"))


#selectcountry.select_by_value("Chile")
#selectage.select_by_value("18-25")
#selectareyoua.select_by_value("Other")
#selectexperience.select_by_value("No")