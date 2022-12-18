import time # modulo para agregar un tiempo entre accion y accion
from selenium import webdriver # lo necesario para poder simular el browser o navegador
from selenium.webdriver.common.keys import Keys # nos permite simular el ingreso de teclado o presion de una tecla
from selenium.webdriver.common.by import By # para poder buscar un elemento dentro de la pagina

driver = webdriver.Chrome(executable_path="C:\Users\Marianela\OneDrive\PIL ISPC\selenium\chromedriver.exe")
driver.get("https://www.musimundo.com/")
elemento = driver.find_element(By.CLASS_NAME, "mus-product-box js-bind-ga-carousel-item")
driver.click()
time.sleep(3)

driver.close()