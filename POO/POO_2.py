#definindo uma nova classe 
class Apple: # define uma nova clase
    color = ""
    flavor = ""

GreenApple = Apple() # define uma instacia para classe Apple
GreenApple.color = "green" #preenche os atributos da classe Apple
GreenApple.flavor = "bitter"
print(GreenApple.color) #exibe o atributo da classe
print(GreenApple.flavor)
print(GreenApple.flavor.upper()) # a partir do Dot notation da para acessar métodos e atribuitos das classes 

RedApple = Apple # outra instancia,possui os mesmos tipos atributos mas são diferentes
RedApple.color = "red"
RedApple.flavor = "sweet"
print(RedApple.color)
print(RedApple.flavor)