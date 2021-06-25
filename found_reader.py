from mylib.func import _getDataM_, _loadParameters_,_writeExcel_,_getDataY_
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


COT , time, choice, fecha = _loadParameters_()
driver = webdriver.Firefox()
sleep(3)


# formato: "fondo", "url", $patrimonio, %mirg, $mirg
fondos = [

    ["1822 Raices Valores Negociables", "https://www.cafci.org.ar/ficha-fondo.html?q=41;41", -1,-1,-1],
    ["Alpha Acciones", "https://www.cafci.org.ar/ficha-fondo.html?q=35;35", -1,-1,-1 ],
    ["Alpha Mega", "https://www.cafci.org.ar/ficha-fondo.html?q=36;381", -1,-1,-1],
    ["Balanz", "https://www.cafci.org.ar/ficha-fondo.html?q=669;1400", -1,-1,-1],
    ["Bull Market", "https://www.cafci.org.ar/ficha-fondo.html?q=847;2408", -1,-1,-1],
    ["Consultatio Acciones Argentina", "https://www.cafci.org.ar/ficha-fondo.html?q=216;1208", -1,-1,-1],
    ["Consultatio Renta Variable", "https://www.cafci.org.ar/ficha-fondo.html?q=514;1037", -1,-1,-1],
    ["Fima Acciones", "https://www.cafci.org.ar/ficha-fondo.html?q=21;21", -1,-1,-1],
    ["Fima PB Acciones", "https://www.cafci.org.ar/ficha-fondo.html?q=22;22", -1,-1,-1],
    ["HF Acciones Argentinas", "https://www.cafci.org.ar/ficha-fondo.html?q=164;164", -1,-1,-1],
    ["HF Acciones Lideres", "https://www.cafci.org.ar/ficha-fondo.html?q=29;29", -1,-1,-1],
    ["Quinquela Acciones", "https://www.cafci.org.ar/ficha-fondo.html?q=378;1214", -1,-1,-1],
    ["SBS Acciones Argentina", "https://www.cafci.org.ar/ficha-fondo.html?q=436;820", -1,-1,-1],
    ["Rofex 20 Renta Variable", "https://www.cafci.org.ar/ficha-fondo.html?q=599;1216", -1,-1,-1],
    ["FBA Acciones Argentinas", "https://www.cafci.org.ar/ficha-fondo.html?q=433;814", -1,-1,-1],
    ["FBA Calificado", "https://www.cafci.org.ar/ficha-fondo.html?q=200;200", -1,-1,-1],
    ["Pellegrini Acciones", "https://www.cafci.org.ar/ficha-fondo.html?q=118;118", -1,-1,-1],
    ["Pionero Acciones", "https://www.cafci.org.ar/ficha-fondo.html?q=39;39", -1,-1,-1],
    ["Toronto Trust Multimercado", "https://www.cafci.org.ar/ficha-fondo.html?q=561;1135", -1,-1,-1],
    ["IAM Renta Variable", "https://www.cafci.org.ar/ficha-fondo.html?q=430;803", -1,-1,-1],
]

if choice == 1:
    for fondo in fondos:
        fondo[2],fondo[3] = _getDataM_(fondo[1],driver,time)

elif choice == 2:
    for fondo in fondos:
        fondo[2],fondo[3] = _getDataY_(fondo[1],driver,time)

else:
    print("Error en choice")
    exit()



driver.close()

for fondo in fondos:
    fondo[4] = int(((fondo[3]/100)*fondo[2]) / COT)

print(fondos)


_writeExcel_(fondos, choice, fecha)