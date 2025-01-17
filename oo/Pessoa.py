class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá{id(self)}"


if __name__ == '__main__':
    Tiago = Pessoa(nome="Tiago")
    Luciano = Pessoa(Tiago, nome="Luciano")
    print(Pessoa.cumprimentar(Luciano))
    print(id(Luciano))
    print(Luciano.cumprimentar())
    print(Luciano.nome)
    print(Luciano.idade)
    for filhos in Luciano.filhos:
        print(filhos.nome)
    Luciano.sobrenome = "Ramalho"
    del Luciano.filhos
    Luciano.olhos = 1
    del Luciano.olhos
    print(Luciano.__dict__)
    print(Tiago.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Luciano.olhos)
    print(Tiago.olhos)
    print(id(Pessoa.olhos)), id(Luciano.olhos), id(Tiago.olhos)
