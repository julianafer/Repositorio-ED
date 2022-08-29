class Data:
    def __init__(self, dia:int, mes:int, ano:int):
        self.__dia = dia
        self.__mes = None
        self.__ano = ano
        self.__limite = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


    @property
    def dia(self)->int:
        return self.__dia

    @property
    def mes(self)->int:
        return self.__mes

    @property
    def ano(self)->int:
        return self.__ano

    @dia.setter
    def dia(self, dia):
        assert dia <= self.__limite[self.__mes], f'Dia inválido'
        self.__dia = dia

    @mes.setter
    def mes(self, mes):
        assert mes > 0 and mes < 13, f'Mês {mes} é inválido'
        self.__mes = mes

    @ano.setter
    def ano(self, ano:int):
        assert ano > 0, f'{ano} é um ano inválido'
        self.__ano = ano

    def __str__(self):
        return f'{self.__dia:02}/{self.__mes:02}/{self.__ano}'
