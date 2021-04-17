class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    andre = Pessoa(nome='André')
    sabrina= Pessoa(andre, nome='Sabrina')
    print(Pessoa.cumprimentar(sabrina))
    print(id(sabrina))
    print(sabrina.cumprimentar())
    print(sabrina.nome)
    print(sabrina.idade)
    for filho in sabrina.filhos:
        print(filho.nome)
    print(sabrina.filhos)

