#Conceito de classes

class MinhaClasse:
    def __init__(self):
        self.x=10
        self.y=20
    
#criar um objeto

objeto=MinhaClasse()

#Acessar a propriedade x do objeto

print(objeto.x)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
    def apresentar(self):
        print(f'Olá, eu sou {self.nome} e tenho {self.idade} anos.')
        
p1= Pessoa("João", 30)
p2= Pessoa("Maria", 25)

print(p1.nome)

print(p2.apresentar())






