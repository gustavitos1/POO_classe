class Pessoa:
    def __init__(self, nome, codigo, data_nascimento, estudando, trabalhando):
        self.nome = nome
        self.codigo = codigo
        self.data_nascimento = data_nascimento
        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = 100


    def apresentar(self):
        print(f'Olá sou {self.nome} \nmeu aniversario é dia: {self.data_nascimento}')
        print(f'Estudante: {'Sim' if self.estudando else 'Não'}')
        print(f"Trabalhando: {'Sim' if self.trabalhando else 'Não'}")
        print("-" * 40)

    def trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario += 100
            print(f"{self.nome} Começou a trabalhar!")
        else:
            print(f"{self.nome} ja esta Trabalhando!")

    def estudar(self):
        if not self.estudando:
            self.estudando = True
            print(f"{self.nome} Começou a estudar")
        elif self.estudando and self.trabalhando:
            self.salario += 1000
            print(f"{self.nome} "
                  f"começou a estudar e aumentou seu salario para "
                  f"R${self.salario:.2f}"
            )
        else:
            print(f"{self.nome} ja esta Estudando!")

    def mostrar(self):
        print(f"O Salario de {self.nome} é {self.salario}")
        print("-" * 40)

p1 = Pessoa('Pedro', "aghds", "23/09/1990", estudando=True, trabalhando=True)
p1.apresentar()
p1.mostrar()

class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento, codigo, estudando=False, trabalhando=False):
        super().__init__(nome, data_nascimento, codigo, estudando, trabalhando)
        self.chorando = True
        self.fome = True
        self.dormindo = False

    def estado(self):
        estado_fome = "Tem Fome" if self.fome == True else "Não tem Fome"
        estado_chorando = "Esta Chorando" if self.chorando == True else "Não esta Chorando"
        estado_dormindo = "Esta Dormindo" if self.dormindo == True else "Não esta Dormindo"
        print(f"{self.nome} {estado_fome}, {estado_chorando} e {estado_dormindo}")

    def mamar(self):
      if self.fome:
          self.fome = False
          self.chorando = False
          print(f"{self.nome} Mamou e gostou muito")
      else:
          print(f"{self.nome} ja nao esta com fome")


    def chorar(self):
        if self.fome:
            self.chorando = True
            print(f"{self.nome} esta Chorando e com fome")
        else:
            print(f"{self.nome} ja nao esta Chorando e sem fome")

    def dormir(self):
        if self.fome:
            print(f"{self.nome} esta com fome e não pode dormir")
        else:
            print(f"{self.nome} esta dormindo")

    def acordar(self):
        if self.fome:
            self.fome = True
            self.dormindo = False
            print(f"{self.nome} acordou e esta com fome")
        else:
            print(f"{self.nome} ainda esta dormindo")

b1 = Bebe('Lucas', "23/09/2024", "kid1", estudando=False, trabalhando=False)

p1.apresentar()
p1.mostrar()
b1.estado()
b1.chorar()
b1.mamar()
b1.dormir()
b1.acordar()