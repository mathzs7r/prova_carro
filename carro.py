class Carro:
    def __init__(self, marca, modelo, placa, valor_diaria):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria
        self.quilometragem = 0
        self.disponivel = True
    
    def exibir(self):
        print(" ---> CARRO <---  ")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Diária: R$ {self.valor_diaria}")
        print(f"Quilometragem: {self.quilometragem} km")
        print(f"Disponível: {self.disponivel}")
        print()
    
    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print("Sua máquina de drift foi alugado com sucesso!")
        else:
            print("Erro: Carro já está alugado!")
        print()
    
    def devolver(self, quilometragem_nova):
        if not self.disponivel:
            if quilometragem_nova > self.quilometragem:
                self.quilometragem = quilometragem_nova
                self.disponivel = True
                print("Carro devolvido com sucesso!")
            else:
                print("Erro: Quilometragem inválida!")
        else:
            print("Erro: Carro não está alugado!")
        print()
