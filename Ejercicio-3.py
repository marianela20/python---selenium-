import time # modulo para agregar un tiempo entre accion y accion
from selenium import webdriver # lo necesario para poder simular el browser o navegador
from selenium.webdriver.common.keys import Keys # nos permite simular el ingreso de teclado o presion de una tecla
from selenium.webdriver.common.by import By # para poder buscar un elemento dentro de la pagina
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="C:/Users/Marianela/OneDrive/PIL ISPC/selenium/chromedriver.exe", options=options)
driver.maximize_window()
driver.get("https://www.grimoldi.com/")

#ingreso a la seccion mujer
mujer = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/section[2]/div/ul[1]/li[2]/a")
mujer.click()
time.sleep(1)

# selecciono el producto
producto = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[3]/section[2]/div[1]/ul/li[2]/a[1]/div/div[2]/div/img[4]")
producto.click()
time.sleep(1)

#visualizo las opciones del talle
listaTalle = driver.find_element(By.ID, 'idMedidaSeleccionada')
listaTalle.click()
time.sleep(1)

# seleciono un talle
talleSelecionado = listaTalle.send_keys("EUR 37.0")
time.sleep(1)
talleSelecionado = listaTalle.send_keys(Keys.ENTER)
time.sleep(1)

##visualizo las opciones del cantidad
listaCantidad = driver.find_element(By.ID, 'cantidadSeleccionada')
listaCantidad.click()
time.sleep(1)

# seleciono una cantidad
cantidadSelecionado = listaCantidad.send_keys("2")
time.sleep(1)
cantidadSelecionado = listaCantidad.send_keys(Keys.ENTER)
time.sleep(1)

#hago click en comprar 
linkComprar = driver.find_element(By.ID, 'comprar')
linkComprar.click()
time.sleep(2)

driver.close()