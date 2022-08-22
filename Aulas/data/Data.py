class Data:
    def __init__(self, dia:int, mes:int, ano:int):
        self.__dia = dia
        self.__mes = None
        self.__ano = ano
        self.__validaMes(mes)


    def __validaMes(self, mes):
        if self.__mes>=1 and self.__mes<=12:
            self.__mes = mes


    @property
    def dia(self)->int:
        return self.__dia

    @dia.setter
    def dia(self, novoDia):
        self.__dia = novoDia

    @property
    def mes(self)->int:
        if self.__mes>=1 and self.__mes<=12:
            return self.__mes

    @mes.setter
    def mes(self, novoMes):
        if novoMes>=1 and novoMes<=12:
            self.__mes = novoMes

    @property
    def ano(self)->int:
        return self.__ano

    @ano.setter
    def ano(self, novoAno):
        self.__ano = novoAno

    def __str__(self):
        return f'{self.__dia:02}/{self.__mes:02}/{self.__ano}'

    
