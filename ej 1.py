import time # modulo para agregar un tiempo entre accion y accion
from selenium import webdriver # lo necesario para poder simular el browser o navegador
from selenium.webdriver.common.keys import Keys # nos permite simular el ingreso de teclado o presion de una tecla
from selenium.webdriver.common.by import By # para poder buscar un elemento dentro de la pagina

# de esta forma le decimos que el browser que va a simular es Chrome
# y le declaramos la ruta en donde esta nuestro chromedriver.exe
driver = webdriver.Chrome(executable_path="C:\Users\Marianela\OneDrive\PIL ISPC\selenium\chromedriver.exe")
# mediante una request get accedemos a la pagina a automatizar
driver.get("https://www.google.com/")
# ubicamos el buscador en la pagina web mediante su atributo "name" y lo guardamos en una variable
buscador = driver.find_element(By.NAME, "q")
# agregamos un delay para poder observar como escribe en el buscador 
time.sleep(2)
# enviamos al buscador la frase "selenium con python"
buscador.send_keys("Selenium con Python")
# agregamos otro delay para visualizar cuando se presiona enter
time.sleep(2)
# simulamos en el buscador que se ha presionado la tecla "enter"
buscador.send_keys(Keys.ENTER)
# agregamos un ultimo delay para que la ejecucion no se cierre automaticamente
time.sleep(5)
# de esta forma cerramos la automatizacion para que no permanezca en ejecucion 
driver.close()
