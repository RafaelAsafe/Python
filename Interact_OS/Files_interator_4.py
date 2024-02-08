with open("spider.txt") as file:
    for line in file:
        print(line.upper().strip())

# file = open("spider.txt")
# lines = file.readlines()
# fiile.close()
# file.close()
# lines.sort()
# print(lines)

# o metódo readline de file, é útil para arquivos grandes como vão exigir muita memoria do pc 
# metodo open("file.txt") é útil para usar o arquivo no código inteiro, enquanto o with permite usar localmente em um bloco
# relembrando que abrior um arquivo com "w" apaga todo conteúdo anterior do arquivo