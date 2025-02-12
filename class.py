class pessoa:
    def __init__(self, nome, idade, nacionalidade):
        self.nome= nome
        self.idade= idade
        self.nacionalidade= nacionalidade
        
    def apresentacao(self):
        print(f"Olá, eu sou o {self.nome} e eu tenho {self.idade} anos, e eu sou {self.nacionalidade}")
    
p1= pessoa("João", " ", "Brasileiro")

print(p1.apresentacao())

