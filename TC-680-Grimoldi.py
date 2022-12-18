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
iconoUsuario = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/section[5]/div[2]/div/a")
iconoUsuario.click()

iniciarSesion = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/section[5]/div[2]/div/ul[1]/li[1]/a")
iniciarSesion.click()
time.sleep(2)

linkRegistrarme = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/section/form/div/p[4]/a[1]")
linkRegistrarme.click()
time.sleep(1)

campoEmailInvalido = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[3]/input")
campoEmailInvalido.send_keys("45654545454544")
campoEmailInvalido.send_keys(Keys.ENTER)

requirement = () 
labelObtained = () 

def compareLabels():
    if requirement in labelObtained: 
        print("Pass")
    else:
        print("Fail")

emailInvalido = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[3]/label[2]")
labelEmailInvalido = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/form/div[3]/label[2]").text
labelObtained = labelEmailInvalido 
print(labelObtained) 
requirement = "Por favor ingrese un email válido"
compareLabels()
time.sleep(2)