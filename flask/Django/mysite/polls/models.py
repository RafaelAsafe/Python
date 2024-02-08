from django.db import models

# Create your models here.
# usando esse código é possivel criar um esquema de banco de dados
# e também criar um apo de acesso ao banco de dados

class Question(models.Model): # classe definindo a tabela 
    question_text = models.CharField(max_length=200) # define o nome do campo e o tipo de dado armazenado
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE) # relaçãoi criado entre choice e question, usando ForeignKey
    choice_text = models.CharField(max_length=200) # um campo pode possuir valores obrigatórios como max_lenght
    votes = models.IntegerField(default=0 ) # ou valores opcionais