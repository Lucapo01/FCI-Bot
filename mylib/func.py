import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

class FCI_Bot:

    def __init__(self,url,time,fondos):

        driver = webdriver.Firefox()
        sleep(3)

        self.url = url
        self.driver = driver
        self.time = time
        self.fondos = fondos
        self.choice = 0
        self.fecha = "NaN"    

    def _getDataM_ (self):



        self.driver.get(url)
        sleep(self.time/1.5)
        self.driver.find_element_by_class_name("html").click()
        sleep(self.time/1.5)
        self.driver.switch_to.window(driver.window_handles[1])
        sleep(self.time/1.5)
    
        
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
        self.driver.switch_to.window(driver.window_handles[0])
        return (Patrimonio,Mirg)
            
    def _getDataY_ (self):



        self.driver.get(url)
        sleep(self.time/1.5)
        self.driver.find_element_by_class_name("html").click()
        sleep(self.time/1.5)
        self.driver.switch_to.window(driver.window_handles[1])
        sleep(self.time/1.5)
    
        
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
            print("Error conversion a float getMirg")
            YPF = -1

        self.driver.close()
        self.driver.switch_to.window(driver.window_handles[0])
        return (Patrimonio,YPF)

    def _loadParameters_(self,url):

        self.driver.get(url)
        sleep(self.time*2)
        self.driver.find_element_by_class_name("html").click()
        sleep(self.time*2)
        self.driver.switch_to.window(driver.window_handles[1])
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
        self.driver.switch_to.window(driver.window_handles[0])
        self.driver.close()

        print("La fecha a analizar es: ",self.fecha)

        while True:
            

            try:
                self.choice = int(input("Ingrese\n 1 --> MIRG\n 2 --> YPF\n Su eleccion: "))
                self.COT = float(input("Ingrese la cotizacion del Activo en el periodo a analizar (999.99): "))
                self.time = float(input("Ingrese la velocidad de funcionamiento, recomendable 8.0 (sg.ms): "))
                break
            except:
                print("Revise los formatos de lo que ingreso")
        
    
        return (COT,time,choice,fecha)

    def _writeExcel_(self):
        import xlsxwriter
    
        if self.choice == 1:
            outWorkbook = xlsxwriter.Workbook("outMirg.xlsx")
            outSheet = outWorkbook.add_worksheet()

            outSheet.write("A2", "Fondos")
            outSheet.write("C2", "Cant. Mirg")
            outSheet.write("B1", self.fecha)

            for item in range(len(self.fondos)):
                outSheet.write(item+2, 0, self.fondos[item][0])
                outSheet.write(item+2, 2, self.fondos[item][4])
        

        elif choice == 2:
            outWorkbook = xlsxwriter.Workbook("outYPF.xlsx")
            outSheet = outWorkbook.add_worksheet()

            outSheet.write("A2", "Fondos")
            outSheet.write("C2", "Cant. YPF")
            outSheet.write("B1", self.fecha)

            for item in range(len(self.fondos)):
                outSheet.write(item+2, 0, self.fondos[item][0])
                outSheet.write(item+2, 2, self.fondos[item][4])
        
        else:
            print("Error en choice")
            exit()


        outWorkbook.close()
        