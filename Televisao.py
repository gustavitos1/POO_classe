class Eletronico:
    def __init__(self, marca, potencia, carga, preco, material):
        self.marca = marca
        self.potencia = potencia
        self.carga = carga
        self.preco = preco
        self.material = material

    def apresentar(self):
        print("Informações do Eletrônico:")
        print(f"Marca: {self.marca}")
        print(f"Potência: {self.potencia}W")
        print(f"Carga: {self.carga}mAh")
        print(f"Preço: {self.preco}")
        print(f"Material: {self.material}")


class Televisao(Eletronico):
    def __init__(self, marca, potencia, carga, preco, material, modelo, polegadas, resolucao):
        super().__init__(marca, potencia, carga, preco, material)
        self.modelo = modelo
        self.polegadas = polegadas
        self.resolucao = resolucao
        self.ligada = False
        self.canal = 1
        self.volume = 10

    def apresentar(self):
        print('Televisão')
        print('-' * 40)
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Polegadas: {self.polegadas}"')
        print(f'Resolução: {self.resolucao}')
        print(f'Preço: {self.preco}')

    def ligar(self):
        if not self.ligada:
            self.ligada = True
            print("A televisão foi ligada!")
        else:
            print("A televisão já está ligada!")

    def desligar(self):
        if self.ligada:
            self.ligada = False
            print("A televisão foi desligada!")
        else:
            print("A televisão já está desligada!")

    def mudar_canal(self, novo_canal):
        if self.ligada:
            if novo_canal > 0:
                self.canal = novo_canal
                print(f"Canal mudado para {novo_canal}.")
            else:
                print("Número de canal inválido. Escolha um canal maior que 0.")
        else:
            print("A televisão está desligada! Ligue primeiro.")

    def ajustar_volume(self, novo_volume):
        if self.ligada:
            if 0 <= novo_volume <= 100:
                self.volume = novo_volume
                print(f"Volume ajustado para {novo_volume}.")
            else:
                print("Volume fora do alcance permitido (0-100).")
        else:
            print("A televisão está desligada! Ligue primeiro.")



t1 = Televisao('LG', 150, 0, '1400$', 'Plástico', 'Smart TV 32"', 32, '4K')


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





