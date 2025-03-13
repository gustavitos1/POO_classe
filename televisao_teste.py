class Eletronico:
    def __init__(self, marca, potencia, carga, preco, material):
        self._marca = marca
        self.__potencia = potencia
        self.__carga = carga
        self.__preco = preco
        self.__material = material

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, potencia):
        self.__potencia = potencia

    def get_carga(self):
        return self.__carga

    def set_carga(self, carga):
        self.__carga = carga

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def apresentar(self):
        print("Informações do Eletrônico:")
        print('-' * 40)
        print(f"Marca: {self.get_marca()}")
        print(f"Potência: {self.get_potencia()}W")
        print(f"Carga: {self.get_carga()}mAh")
        print(f"Preço: {self.get_preco()}")
        print(f"Material: {self.get_material()}")
        print("\n")


class Televisao(Eletronico):
    def __init__(self, marca, potencia, carga, preco, material, modelo, polegadas, resolucao):
        super().__init__(marca, potencia, carga, preco, material)
        self.__modelo = modelo
        self.__polegadas = polegadas
        self.__resolucao = resolucao
        self.__ligada = False
        self.__canal = 1
        self.__volume = 10

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_polegadas(self):
        return self.__polegadas

    def set_polegadas(self, polegadas):
        self.__polegadas = polegadas

    def get_resolucao(self):
        return self.__resolucao

    def set_resolucao(self, resolucao):
        self.__resolucao = resolucao

    def get_ligada(self):
        return self.__ligada

    def apresentar(self):
        print('Televisão')
        print('-' * 40)
        print(f'Marca: {self.get_marca()}')
        print(f'Modelo: {self.__modelo}')
        print(f'Polegadas: {self.__polegadas}"')
        print(f'Resolução: {self.__resolucao}')
        print(f'Preço: {self.get_preco()}')

    def ligar(self):
        if not self.__ligada:
            self.__ligada = True
            print("A televisão foi ligada!")
        else:
            print("A televisão já está ligada!")

    def desligar(self):
        if self.__ligada:
            self.__ligada = False
            print("A televisão foi desligada!")
        else:
            print("A televisão já está desligada!")

    def mudar_canal(self, novo_canal):
        if self.__ligada:
            if novo_canal > 0:
                self.__canal = novo_canal
                print(f"Canal mudado para {novo_canal}.")
            else:
                print("Número de canal inválido. Escolha um canal maior que 0.")
        else:
            print("A televisão está desligada! Ligue primeiro.")

    def ajustar_volume(self, novo_volume):
        if self.__ligada:
            if 0 <= novo_volume <= 100:
                self.__volume = novo_volume
                print(f"Volume ajustado para {novo_volume}.")
            else:
                print("Volume fora do alcance permitido (0-100).")
        else:
            print("A televisão está desligada! Ligue primeiro.")

e1 = Eletronico('Eletrolux', 150, 0, 7000, 'alumínio')
t1 = Televisao('LG', 150, 0, '1400$', 'Plástico', 'Smart TV 32"', 32, '4K')

e1.apresentar()
t1.apresentar()
print()

t1.ligar()
t1.mudar_canal(5)
t1.ajustar_volume(25)
t1.desligar()
t1.mudar_canal(7)
t1.ligar()
t1.ajustar_volume(110)
t1.ajustar_volume(45)
