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

linkRegistrarme = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/section/form/div/p[4]/a[1]")
linkRegistrarme.click()
time.sleep(1)
 
campoNombre = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[1]/input")
campoNombre.send_keys("Ana")
time.sleep(2)

campoApellido = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[2]/input")
campoApellido.send_keys("rodriguez")
time.sleep(2)

campoEmail = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[3]/input")
campoEmail.send_keys("anarodriguez55556@gmail.com")
time.sleep(2)

campoFechaNacimiento = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[5]/input")
campoFechaNacimiento.send_keys("21/11/2002")
time.sleep(2)

campoContraseña = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[7]/input[1]")
campoContraseña.send_keys("anita100")
time.sleep(2)
campoRepiteContraseña = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[7]/input[2]")
campoRepiteContraseña.send_keys("anita100")
time.sleep(2)
campoSexo = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[4]/input[2]")
campoSexo.click()
time.sleep(2)
campoProvincia = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[6]/select")
campoProvincia.click()
provincia = campoProvincia.send_keys("Córdoba")
time.sleep(2)
provincia = campoProvincia.send_keys(Keys.ENTER)
time.sleep(2)

enviar = driver.find_element(By.ID,'formSubmit')
enviar.click()
time.sleep(2)

requirement = () 
labelObtained = () 

def compareLabels():
    if requirement in labelObtained: 
        print("Pass")
    else:
        print("Fail")

registro = driver.find_element(By.ID,'successDialog')
labelRegistro = driver.find_element(By.ID,'successDialog').text
labelObtained = labelRegistro 
print(labelObtained) 
requirement = "Se ha registrado correctamente."
compareLabels()
time.sleep(2)

driver.close()