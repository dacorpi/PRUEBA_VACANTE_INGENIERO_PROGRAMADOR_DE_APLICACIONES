from selenium import webdriver
from selenium.webdriver.common.by import By 

clave="PORTATILES LENOVO GAMER"
driver = webdriver.Chrome(executable_path="driver\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.mercadolibre.com.co/")

aceptarCookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]')
aceptarCookies.click()

busqueda = driver.find_element(By.XPATH, '//input[@class="nav-search-input"]')
busqueda.click()
busqueda.send_keys(clave)

buscar = driver.find_element(By.XPATH, '/html/body/header/div/form/button')
buscar.click()

items = driver.find_elements(By.XPATH, '//li[@class="ui-search-layout__item"]')

print("\n")
print("LISTA DE PRODUCTOS PARA " + clave + "\n")
for producto in items:
    descripcion = producto.find_element(By.XPATH, './/h2[@class="ui-search-item__title"]').text
    precio = producto.find_element(By.XPATH, './/span[@class="price-tag-fraction"]').text
    print("Producto: " + descripcion)
    print("Precio: $ " + precio + "\n")

driver.quit()