#Modifica o comportamento de uma função sem alterar seu código 
class uppercase(object):
    """recebe função e retorna os argumentos 0 e 1 em maiúsculo"""
    def __init__(self,f):
        self.f = f
    def __call__(self,*args):
        self.f(args[0].upper(),args[1].upper())
        

@uppercase
def pessoa(nome,nacionalidade):
    print(f"Nome: {nome}, Nacionalidade: {nacionalidade}")

pessoa('Carlos','Haitiano')
