import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import xlsxwriter

class FCI_Bot:

    def __init__(self,fondos,time):

        self.driver = webdriver.Firefox()
        sleep(3)

        
        
        self.time = time
        self.fondos = fondos
        self.choice = 0
        self.fecha = "NaN"    

    def _getDataM_ (self,url):



        self.driver.get(url)
        sleep(self.time)
        self.driver.find_element_by_class_name("html").click()
        sleep(self.time)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(self.time)
    
        
        html = self.driver.execute_script("return document.documentElement.outerHTML")
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

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        return (Patrimonio,Mirg)
            
    def _getDataY_ (self,url):



        self.driver.get(url)
        sleep(self.time)
        self.driver.find_element_by_class_name("html").click()
        sleep(self.time)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(self.time)
    
        
        html = self.driver.execute_script("return document.documentElement.outerHTML")
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
            print("Error conversion a float getYPF")
            YPF = -1

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return (Patrimonio,YPF)

    def _getDataV_(self,url):
        self.driver.get(url)
        sleep(self.time)
        self.driver.find_element_by_class_name("html").click()
        sleep(self.time)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(self.time)
    
        
        html = self.driver.execute_script("return document.documentElement.outerHTML")
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
            
        posStart = datos_crudos.find("Cedear Vista Oil Gas")
        VIS = datos_crudos[posStart+155:]

        posEnd = VIS.find("<")
        VIS = VIS[:posEnd]

        try:
            VIS = float(VIS)
        except:
            print("Error conversion a float getVis")
            VIS = -1

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return (Patrimonio,VIS)

    def _loadParameters_(self,url):

        self.driver.get(url)
        sleep(self.time*2)
        self.driver.find_element_by_class_name("html").click()
        sleep(self.time*2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(self.time*2)
        
            
        html = self.driver.execute_script("return document.documentElement.outerHTML")
        sel_soup = BeautifulSoup(html, "html.parser")

        datos_crudos = sel_soup.findAll("p")
        datos_crudos = str(datos_crudos)

        posStart = datos_crudos.find("""<p class="encuentreColortxt ng-binding">1822 Raices Valores Negociables<br/>Composición de Cartera al """)
        tamañoStart = len("""<p class="encuentreColortxt ng-binding">1822 Raices Valores Negociables<br/>Composición de Cartera al""") 
        posEnd = datos_crudos.find(""" </p>, <p class="destacado ng-binding">ARS 1000</p>, <p class="destacado ng-binding">48 hs. hábiles</p>""")
        self.fecha = datos_crudos[posStart+tamañoStart:posEnd]

        self.driver.close()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        

        print("La fecha a analizar es: ",self.fecha)

        while True:
            

            try:
                self.choice = int(input("Ingrese\n 1 --> MIRG\n 2 --> YPF\n 3 --> VIST\n Su eleccion: "))
                self.COT = float(input("Ingrese la cotizacion del Activo en el periodo a analizar (999.99): "))
                self.time = float(input("Ingrese la velocidad de funcionamiento, recomendable 8.0 (sg.ms): "))
                break
            except:
                print("Revise los formatos de lo que ingreso")
        
    def _writeExcel_(self):
    
        if self.choice == 1:
            outWorkbook = xlsxwriter.Workbook("outMirg.xlsx")
            outSheet = outWorkbook.add_worksheet()

            outSheet.write("A2", "Fondos")
            outSheet.write("C2", "Cant. Mirg")
            outSheet.write("B1", self.fecha)

            for item in range(len(self.fondos)):
                outSheet.write(item+2, 0, self.fondos[item][0])
                outSheet.write(item+2, 2, self.fondos[item][4])
    
        elif self.choice == 2:
            outWorkbook = xlsxwriter.Workbook("outYPF.xlsx")
            outSheet = outWorkbook.add_worksheet()

            outSheet.write("A2", "Fondos")
            outSheet.write("C2", "Cant. YPF")
            outSheet.write("B1", self.fecha)

            for item in range(len(self.fondos)):
                outSheet.write(item+2, 0, self.fondos[item][0])
                outSheet.write(item+2, 2, self.fondos[item][4])
        
        elif self.choice == 3:
            outWorkbook = xlsxwriter.Workbook("outVist.xlsx")
            outSheet = outWorkbook.add_worksheet()

            outSheet.write("A2", "Fondos")
            outSheet.write("C2", "Cant. Vist")
            outSheet.write("B1", self.fecha)

            for item in range(len(self.fondos)):
                outSheet.write(item+2, 0, self.fondos[item][0])
                outSheet.write(item+2, 2, self.fondos[item][4])
        
        else:
            print("Error en choice")
            exit()


        outWorkbook.close()
        