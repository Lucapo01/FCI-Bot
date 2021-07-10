from mylib.func import FCI_Bot
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

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
    ["Allaria Acciones", "https://www.cafci.org.ar/ficha-fondo.html?q=441;835", -1,-1,-1],
    ["Premier Renta Variable", "https://www.cafci.org.ar/ficha-fondo.html?q=227;227", -1,-1,-1],

]

#load parameters

start_time = 15
errores = [0,]

FCI_Bot = FCI_Bot(fondos,start_time)
FCI_Bot._loadParameters_(fondos[0][1])

#Scrapping Websites

if FCI_Bot.choice == 1:
    for fondo in FCI_Bot.fondos:
        fondo[2],fondo[3] = FCI_Bot._getDataM_(fondo[1])

elif FCI_Bot.choice == 2:
    for fondo in FCI_Bot.fondos:
        fondo[2],fondo[3] = FCI_Bot._getDataY_(fondo[1])

elif FCI_Bot.choice == 3:
    for fondo in FCI_Bot.fondos:
        fondo[2],fondo[3] = FCI_Bot._getDataV_(fondo[1])

else:
    print("Error en choice")
    exit()

FCI_Bot.driver.close()
 
# Data Math

for fondo in FCI_Bot.fondos:

    if fondo[3] > 0:
        fondo[4] = int(((fondo[3]/100)*fondo[2]) / FCI_Bot.COT)
    else:
        fondo[4] = -1


FCI_Bot._writeExcel_()

#error manager
for fondo in FCI_Bot.fondos:
    if fondo[3] < 0:
        errores[0] = errores[0] + 1
        errores.append(fondo[0])

log_file = open("log.txt","w")
if errores[0] == 0:
    log_file.write("Sin errores")

else:
    log_file.write("Hay " + str(errores[0])+ " errores en los siguientes fondos: ")
    errores.pop(0)
    log_file.writelines(errores)
    