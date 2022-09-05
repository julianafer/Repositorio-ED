class Celular: #essa classe não tem um construtor definido(__init__), e a ausência de um construtor não impede que você possa criar propriedades de instância
    def trocarBateria(self, novaBateria):
        self.bateria = novaBateria

    def showBateria(self):
        print('Batria:', self.bateria)

cel = Celular()
cel.showBateria() #se tentar usar o showBateria antes do trocarBateria vai dar erro porque como não existe um construtor os atributos foram passados pelo trocarBateria
cel.trocarBateria('3.000mA')
