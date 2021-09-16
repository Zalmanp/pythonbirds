class Pessoa:
    def cumprimentar(self):
        return f"Olá{id(self)}"


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "tiago"
    print(p.nome)
    print(p.idade)