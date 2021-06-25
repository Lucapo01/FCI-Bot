from mylib.func import _getDataM_, _loadParameters_,_writeExcel_,_getDataY_
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()


time = 8
url_date = "https://www.cafci.org.ar/ficha-fondo.html?q=41;41"

driver.get(url_date)
sleep(time/1.5)
driver.find_element_by_class_name("html").click()
sleep(time/1.5)
driver.switch_to.window(driver.window_handles[1])
sleep(time/1.5)
   
    
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, "html.parser")

datos_crudos = sel_soup.findAll("p")
datos_crudos = str(datos_crudos)

posStart = datos_crudos.find("""<p class="encuentreColortxt ng-binding">1822 Raices Valores Negociables<br/>Composición de Cartera al """)
tamañoStart = len("""<p class="encuentreColortxt ng-binding">1822 Raices Valores Negociables<br/>Composición de Cartera al""") 
posEnd = datos_crudos.find(""" </p>, <p class="destacado ng-binding">ARS 1000</p>, <p class="destacado ng-binding">48 hs. hábiles</p>""")
fecha = datos_crudos[posStart+tamañoStart:posEnd]

print(fecha)