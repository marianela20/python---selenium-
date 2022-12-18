import time 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="C:/Users/Marianela/OneDrive/PIL ISPC/selenium/chromedriver.exe", options=options)

driver.maximize_window()
driver.get("https://www.grimoldi.com/")

time.sleep(2)
iconoUsuario = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/section[5]/div[2]/div/a")
iconoUsuario.click()

iniciarSesion = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/section[5]/div[2]/div/ul[1]/li[1]/a")
iniciarSesion.click()
time.sleep(2)

linkRegistrarme = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/section/form/div/p[4]/a[1]")
linkRegistrarme.click()
time.sleep(1)

requirement = () 
labelObtained = () 

def compareLabels():
    if requirement in labelObtained: 
        print("Pass")
    else:
        print("Fail")

labelNombre = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[1]/label")
labelCampoNombre = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[1]/label").text 
labelObtained = labelCampoNombre 
print(labelObtained)
requirement = "Nombre"
compareLabels()

labelApellido = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[2]/label[1]")
labelCampoApellido = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[2]/label[1]").text 
labelObtained = labelCampoApellido
print(labelObtained)
requirement = "Apellido"
compareLabels()

labelEmail = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[3]/label")
labelCampoEmail = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[3]/label").text 
labelObtained = labelCampoEmail
print(labelObtained)
requirement = "Email"
compareLabels()

labelFechaNacimiento = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[5]/label")
labelCampoFechaNacimiento = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[5]/label").text 
labelObtained = labelCampoFechaNacimiento 
print(labelObtained)
requirement = "Fecha de Nacimiento"
compareLabels()

labelContraseña = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[7]/label")
labelCampoContraseña = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[7]/label").text 
labelObtained = labelCampoContraseña
print(labelObtained)
requirement = "Contraseña"
compareLabels()

labelRepiteContraseña = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[7]/span")
labelCampoRepiteContraseña = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[7]/span").text 
labelObtained = labelCampoRepiteContraseña
print(labelObtained)
requirement = "Repita su contraseña"
compareLabels()

labelSexo = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[4]/label")
labelCampoSexo = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[4]/label").text 
labelObtained = labelCampoSexo
print(labelObtained)
requirement = "Sexo"
compareLabels()

labelMasculino = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[4]/span[1]")
labelCampoMasculino = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[4]/span[1]").text 
labelObtained = labelCampoMasculino
print(labelObtained)
requirement = "Masculino"
compareLabels()

labelFemenino = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[4]/span[2]")
labelCampoFemenino = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[4]/span[2]").text 
labelObtained = labelCampoFemenino
print(labelObtained)
requirement = "Femenino"
compareLabels()

labelProvincia = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[6]/label")
labelCampoProvincia = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[6]/label").text 
labelObtained = labelCampoProvincia
print(labelObtained)
requirement = "Provincia"
compareLabels()

driver.close()

