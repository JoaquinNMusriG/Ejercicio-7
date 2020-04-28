from math import ceil
from Hora import Hora

class FechaHora:
    __Dia = 0
    __Mes = 0
    __Anio = 0
    __Hora = 0
    __Minuto = 0
    __Segundo = 0

    def __init__(self, dia = 1, mes = 1, anio = 2020, hora = 0, minuto = 0, segundo = 0):
        if (anio > 0):
            if (mes in range(1,13)):
                if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
                    if (dia in range(1,31)):
                        if (hora in range(24)):
                            if (minuto in range(60)):
                                if (segundo in range(60)):
                                    self.__Anio = anio
                                    self.__Mes = mes                    #genera el objeto si es un mes de 30 dias
                                    self.__Dia = dia                    #y los datos ingresados son correctos
                                    self.__Hora = hora
                                    self.__Minuto = minuto
                                    self.__Segundo = segundo
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 59.')
                        else:
                            print('El rango de valores válidos es de 0 a 23.')
                    else:
                        print('El mes ' + str(mes) + ' solo tiene 30 días.')
                elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
                    if (dia in range(1,32)):
                        if (hora in range(24)):
                            if (minuto in range(60)):
                                if (segundo in range(60)):
                                    self.__Anio = anio
                                    self.__Mes = mes                    #genera el objeto si es un mes de 31 dias
                                    self.__Dia = dia                    #y los datos ingresados son correctos
                                    self.__Hora = hora
                                    self.__Minuto = minuto
                                    self.__Segundo = segundo
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 59.')
                        else:
                            print('El rango de valores válidos es de 0 a 23.')
                    else:
                        print('El mes ' + str(mes) + ' solo tiene 31 días.')
                else:
                    if ((anio%4 == 0) & (anio%100 != 0)) or (anio%400 == 0):
                        if (dia in range(1,30)):
                            if (hora in range(24)):
                                if (minuto in range(60)):
                                    if (segundo in range(60)):
                                        self.__Anio = anio              #genera el objeto si es que es un año bisiesto,
                                        self.__Mes = mes                #es el mes de febrero y los datos ingresados son correctos
                                        self.__Dia = dia
                                        self.__Hora = hora
                                        self.__Minuto = minuto
                                        self.__Segundo = segundo
                                    else:
                                        print('El rango de valores válidos es de 0 a 59.')
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 23.')
                        else:
                            print('El mes ' + str(mes) + ' solo tiene 29 días por ser año bisiesto.')
                    else:
                        if (dia in range(1,29)):
                            if (hora in range(24)):
                                if (minuto in range(60)):
                                    if (segundo in range(60)):
                                        self.__Anio = anio
                                        self.__Mes = mes                #genera el objeto si es que no es un año bisiesto,
                                        self.__Dia = dia                #es el mes de febrero y los datos ingresados son correctos
                                        self.__Hora = hora
                                        self.__Minuto = minuto
                                        self.__Segundo = segundo
                                    else:
                                        print('El rango de valores válidos es de 0 a 59.')
                                else:
                                    print('El rango de valores válidos es de 0 a 59.')
                            else:
                                print('El rango de valores válidos es de 0 a 23.')
                        else:
                            print('El mes ' + str(mes) + ' solo tiene 28 días.')
            else:
                print('Los años solo tienen 12 meses.')
        else:
            print('Año inválido.')

    def Mostrar(self):
        print('Año:{} Mes:{} Día:{} Hora:{} Minuto:{} Segundo:{}'.format(self.__Anio,self.__Mes,self.__Dia,self.__Hora,self.__Minuto,self.__Segundo))

    def getDia (self):
        return self.__Dia

    def getMes (self):
        return self.__Mes

    def getAnio (self):
        return self.__Anio

    def getHora (self):
        return self.__Hora

    def getMinuto (self):
        return self.__Minuto

    def getSegundo (self):
        return self.__Segundo

    def verificarSuma (self, d, mes, a, h, m, s):
        #Verificar Minutos
        if (s >= 60):
            m += 1
            s = s - 60
        #Verificar Hora
        if (m >= 60):
            h += 1
            m = m - 60
        #Verificar Dia
        if(h >= 24):
            d += 1
            h = h - 24
        #Verificar Mes
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if (d > 30):
                mes += 1
                d = d - 30
        elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if (d > 31):
                mes += 1
                d = d - 31
        else:
            if ((a%4 == 0) & (a%100 != 0)) or (a%400 == 0): #Mes de febrero en año Bisiesto
                if (d > 29):
                    mes += 1
                    d = d - 29
            elif (d > 28):
                mes += 1
                d = d - 28
        #Verificar Año
        if (mes > 12):
            a += mes // 12
            mes = mes - ((mes // 12)* 12)

        return FechaHora(d,mes,a,h, m, s)

    def verificarSumaInt(self, d,mes,a,h, m, s):
        #Verificar Mes
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if (d > 30):
                mes += d // 30
                d = d - ((d // 30)* 30)
        elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if (d > 31):
                mes += d // 31
                d = d - ((d // 31)* 31)
        else:
            if ((a%4 == 0) & (a%100 != 0)) or (a%400 == 0): #Mes de febrero en año Bisiesto
                if (d > 29):
                    mes += d // 29
                    d = d - ((d // 29)* 29)
            elif (d > 28):
                mes += d // 28
                d = d - ((d // 28)* 28)
        if (d == 0):
            d = 1
        #Verificar Año
        if (mes > 12):
            a += mes // 12
            mes = mes - ((mes // 12)* 12)

        if ((a%4 == 0) & (a%100 != 0)) or (a%400 == 0) & (mes == 2):
            if (d > 29):
                mes += d // 29
                d = d - ((d // 29)* 29)
        elif (d > 28):
            mes += d // 28
            d = d - ((d // 28)* 28)

        return FechaHora(d,mes,a,h, m, s)

    def __add__ (self, unHoI):
        if (str(unHoI).isdigit()):
            d = self.getDia() + unHoI
            mes = self.getMes()
            a = self.getAnio()
            h = self.getHora()
            m = self.getMinuto()
            s = self.getSegundo()

            return self.verificarSumaInt(d,mes,a,h, m, s)
        else:
            d = self.getDia()
            mes = self.getMes()
            a = self.getAnio()
            h = self.getHora() + unHoI.gHora()
            m = self.getMinuto() + unHoI.gMin()
            s = self.getSegundo() + unHoI.gSeg()

            return self.verificarSuma(d,mes,a,h, m, s)

    def __radd__ (self, unHoI):
        if (str(unHoI).isdigit()):
            d = self.getDia() + unHoI
            mes = self.getMes()
            a = self.getAnio()
            h = self.getHora()
            m = self.getMinuto()
            s = self.getSegundo()

            return self.verificarSumaInt(d,mes,a,h, m, s)
        else:
            d = self.getDia()
            mes = self.getMes()
            a = self.getAnio()
            h = self.getHora() + unHoI.gHora()
            m = self.getMinuto() + unHoI.gMin()
            s = self.getSegundo() + unHoI.gSeg()

            return self.verificarSuma(d,mes,a,h, m, s)

    def verificarResta(self, d, mes, a, h, m, s):
        #Verificar Mes
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if (d < 0):
                mes -= ceil((-d)/30)
                d = d + (ceil((-d)/30) * 30)
            elif (d == 0):                                         #Cuando se resta 1 y se está en el primer dia de los meses
                mes -= 1
                d = 31
        elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if (d < 0):
                mes -= ceil((-d)/31)
                d = d + (ceil((-d)/31) * 31)
            elif (d == 0):                                         #Cuando se resta 1 y se está en el primer dia de los meses
                if (mes != 1) & (mes != 8) & (mes != 3):
                    mes -= 1
                    d = 30
                elif (mes == 8):
                    mes = 7
                    d = 31
                elif (mes == 1):
                    mes = 12
                    d = 31
                elif (mes == 3):
                    if ((a%4 == 0) & (a%100 != 0)) or (a%400 == 0):
                        mes = 2
                        d = 29
                    else:
                        mes = 2
                        d = 28
        elif (mes == 2) & (d == 0):                                #Cuando se resta 1 y se está en el primer dia de febrero 
            mes = 1
            d = 31
        else:
            if ((a%4 == 0) & (a%100 != 0)) or (a%400 == 0): #Mes de febrero en año Bisiesto
                if (d < 0):
                    mes -= ceil((-d)/29)
                    d = d + (ceil((-d)/29) * 29)
            else:
                if (d < 0):
                    mes -= ceil((-d)/28)
                    d = d + (ceil((-d)/28) * 28)
        if (d == 0):
            d = 1
        #Verificar Año
        if (mes < 0):
            a -= ceil((-mes)/12)
            mes = mes + (ceil((-mes)/12) * 12)
        elif (mes == 0):
            a -= 1
            mes = 12

        return FechaHora(d,mes,a,h, m, s)

    def __sub__(self, unInt):
        d = self.getDia() - unInt
        mes = self.getMes()
        a = self.getAnio()
        h = self.getHora()
        m = self.getMinuto()
        s = self.getSegundo()

        return self.verificarResta(d,mes,a,h, m, s)
