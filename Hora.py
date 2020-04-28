class Hora:
    __hora = 0
    __min = 0
    __seg = 0

    def __init__(self, Hora = 0, Minuto = 0, Segundo = 0):
        if (Hora in range(24)):
            if (Minuto in range(60)):
                if (Segundo in range(60)):
                    self.__hora = Hora
                    self.__min = Minuto
                    self.__seg = Segundo
                else:
                    print('El rango de valores válidos es de 0 a 59.')
            else:
                print('El rango de valores válidos es de 0 a 59.')
        else:
            print('El rango de valores válidos es de 0 a 23.')

    def Mostrar(self):
        print('Hora:{} Minuto:{} Segundo:{}'.format(self.__hora,self.__min,self.__seg))

    def gHora (self):
        return self.__hora

    def gMin (self):
        return self.__min

    def gSeg (self):
        return self.__seg
