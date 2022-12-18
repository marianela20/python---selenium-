import time # modulo para agregar un tiempo entre accion y accion
from selenium import webdriver # lo necesario para poder simular el browser o navegador
from selenium.webdriver.common.keys import Keys # nos permite simular el ingreso de teclado o presion de una tecla
from selenium.webdriver.common.by import By # para poder buscar un elemento dentro de la pagina

driver = webdriver.Chrome(executable_path="C:/Users/Marianela/OneDrive/PIL ISPC/selenium/chromedriver.exe")
driver.get("https://www.anses.gob.ar/")
buscadorAnses = driver.find_element(By.NAME, "search_api_fulltext")
buscadorAnses.send_keys("Refuerzo Alimentario")
time.sleep(2)
buscadorAnses.send_keys(Keys.ENTER)
Link = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/div/span/a")
Link.click()
time.sleep(2)
driver.close()