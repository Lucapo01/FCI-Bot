import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


def _getDataM_ (url,driver,time):



    driver.get(url)
    sleep(time/1.5)
    driver.find_element_by_class_name("html").click()
    sleep(time/1.5)
    driver.switch_to.window(driver.window_handles[1])
    sleep(time/1.5)
   
    
    html = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup = BeautifulSoup(html, "html.parser")

    datos_crudos = sel_soup.findAll("tr")
    datos_crudos = str(datos_crudos)


    posStart = datos_crudos.find("""<!-- ngIf: row.tipo == 'pie' --><td class="ng-scope" ng-if="row.tipo == 'pie'"><strong class="ng-binding">""")
    tamañoStart = len("""<!-- ngIf: row.tipo == 'pie' --><td class="ng-scope" ng-if="row.tipo == 'pie'"><strong class="ng-binding">""") 
    posEnd = datos_crudos.find("""</strong></td><!-- end ngIf: row.tipo == 'pie'""")
    Patrimonio = datos_crudos[posStart+tamañoStart:posEnd]
    Patrimonio = Patrimonio.replace(",","")


    if Patrimonio == "":
        print("Error en string (getPatrimonio)")
        return -1
    
    try:
        Patrimonio = float(Patrimonio)

    except:
        print("Error en conversion a float (getPatrimonio)")
        Patrimonio = -1
        
    posStart = datos_crudos.find("Mirgor")
    Mirg = datos_crudos[posStart+141:]

    posEnd = Mirg.find("<")
    Mirg = Mirg[:posEnd]

    try:
        Mirg = float(Mirg)
    except:
        print("Error conversion a float getMirg")
        Mirg = -1

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return (Patrimonio,Mirg)
        
def _getDataY_ (url,driver,time):



    driver.get(url)
    sleep(time/1.5)
    driver.find_element_by_class_name("html").click()
    sleep(time/2)
    driver.switch_to.window(driver.window_handles[1])
    sleep(time/1.5)
   
    
    html = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup = BeautifulSoup(html, "html.parser")

    datos_crudos = sel_soup.findAll("tr")
    datos_crudos = str(datos_crudos)


    posStart = datos_crudos.find("""<!-- ngIf: row.tipo == 'pie' --><td class="ng-scope" ng-if="row.tipo == 'pie'"><strong class="ng-binding">""")
    tamañoStart = len("""<!-- ngIf: row.tipo == 'pie' --><td class="ng-scope" ng-if="row.tipo == 'pie'"><strong class="ng-binding">""") 
    posEnd = datos_crudos.find("""</strong></td><!-- end ngIf: row.tipo == 'pie'""")
    Patrimonio = datos_crudos[posStart+tamañoStart:posEnd]
    Patrimonio = Patrimonio.replace(",","")


    if Patrimonio == "":
        print("Error en string (getPatrimonio)")
        return -1
    
    try:
        Patrimonio = float(Patrimonio)

    except:
        print("Error en conversion a float (getPatrimonio)")
        Patrimonio = -1
        
    posStart = datos_crudos.find("YPF - D")
    YPF = datos_crudos[posStart+142:]

    posEnd = YPF.find("<")
    YPF = YPF[:posEnd]

    try:
        YPF = float(YPF)
    except:
        print("Error conversion a float getMirg")
        YPF = -1

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return (Patrimonio,YPF)

def _loadParameters_():

    

    while True:
        

        try:
            choice = int(input("Ingrese\n 1 --> MIRG\n 2 --> YPF\n Su eleccion: "))
            COT = float(input("Ingrese la cotizacion del Activo en el periodo a analizar (999.99): "))
            time = float(input("Ingrese la velocidad de funcionamiento, recomendable 8.0 (sg.ms): "))
            fecha = input("Ingrese fecha a analizar: ")
            break
        except:
            print("Revise los formatos de lo que ingreso")
    
   
    return (COT,time,choice,fecha)

def _writeExcel_(fondos,choice,fecha):
    import xlsxwriter
    
    if choice == 1:
        outWorkbook = xlsxwriter.Workbook("outMirg.xlsx")
        outSheet = outWorkbook.add_worksheet()

        outSheet.write("A2", "Fondos")
        outSheet.write("C2", "Cant. Mirg")
        outSheet.write("B1", fecha)

        for item in range(len(fondos)):
            outSheet.write(item+2, 0, fondos[item][0])
            outSheet.write(item+2, 2, fondos[item][4])
    

    elif choice == 2:
        outWorkbook = xlsxwriter.Workbook("outYPF.xlsx")
        outSheet = outWorkbook.add_worksheet()

        outSheet.write("A2", "Fondos")
        outSheet.write("C2", "Cant. YPF")
        outSheet.write("B1", fecha)

        for item in range(len(fondos)):
            outSheet.write(item+2, 0, fondos[item][0])
            outSheet.write(item+2, 2, fondos[item][4])
    
    else:
        print("Error en choice")
        exit()


    outWorkbook.close()
    import xlsxwriter
    
    if choice == 1:
        outWorkbook = xlsxwriter.Workbook("outMirg.xlsx")
        outSheet = outWorkbook.add_worksheet()

        outSheet.write("A2", "Fondos")
        outSheet.write("C2", "Cant. Mirg")
        outSheet.write("B1", fecha)

        for item in range(len(fondos)):
            outSheet.write(item+2, 0, fondos[item][0])
            outSheet.write(item+2, 2, fondos[item][4])
    

    elif choice == 2:
        outWorkbook = xlsxwriter.Workbook("outYPF.xlsx")
        outSheet = outWorkbook.add_worksheet()

        outSheet.write("A2", "Fondos")
        outSheet.write("C2", "Cant. YPF")
        outSheet.write("B1", fecha)

        for item in range(len(fondos)):
            outSheet.write(item+2, 0, fondos[item][0])
            outSheet.write(item+2, 2, fondos[item][4])
    
    else:
        print("Error en choice")
        exit()


    outWorkbook.close()