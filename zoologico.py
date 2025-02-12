class Zoo:
    def __init__(self):
        
        self.animal=[]
        self.abertura=False
        self.nome=""
        self.localizacao=""
        
    def listaanimais(self):
        
        for i in range(10):
            
            print(f"Digite o nome do animal: ")
            animal=input()
            self.animal.append(f" Nome do animal {i+1}: {animal} ")
            
            print(f"Digite a espécie do animal: ")
            especie=input()
            self.animal.append(f" Espécie do animal {i+1}: {especie} ")
            
            print(f"Adicionar mais animais? Sim ou Não")
            resposta= input()
            
            if resposta=="Não":
                break
            elif resposta=="Sim":
                i-=1
            else:
                print(f"Apenas Sim ou Não")
                break
            
            
            
    def mostralistaanimais(self):
        
        print(f"Lista de animais: {self.animal} ")
        
        
    def consultarabertura(self):
        
        for i in range(0,10):
         print(f"Consultar abertura? Sim ou Não")
        
         resposta2= input()
         if resposta2=="Sim":
             
            if self.abertura==True:
                
             print(f"Zoológico: Aberto")
             
             break
             
            else:
             print(f"Zoológico: Fechado")
             
             break
            
         elif resposta2=="Não":
            print(f"Ok, obrigado")
            break
        
         else:
            print(f"Apenas Sim ou Não")
            i-=1
            
    def aberturazoo(self):
        
        for i in range(0,10): 
            
         print(f"Abrir zoológico? Sim ou Não")
        
         resposta3=input()
         
         if resposta3=="Sim":
            self.abertura=True
            break
         elif resposta3=="Não":
            self.abertura=False
            break
         else:
             print(f"Apenas Sim ou Não")
             i-=1   
             
    def nome1(self):
        
        print(f"Digite o nome do zoológico: ")
        
        self.nome=input()
        
        print(f"Nome do Zoológico: {self.nome}")  
    
    def localizacao1(self):
        
        print(f"Digite a localização do zoológico: ")  
        
        self.localizacao=input()
        
        print(f"Localização do Zoológico: {self.localizacao}") 
        

zoologico=Zoo()

print(zoologico.listaanimais())
print(zoologico.mostralistaanimais())
print(zoologico.consultarabertura())
print(zoologico.aberturazoo())
print(zoologico.consultarabertura())
print(zoologico.nome1())
print(zoologico.localizacao1())

        
     
     
             
        
            
            
            
             
             
                