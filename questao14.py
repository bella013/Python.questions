multaSP = 4
pesobom = 50
peso = float(input("Insira o peso da pesca em kg: "))
if(peso>pesobom):
    excesso = peso-pesobom
    multa = excesso*multaSP
    print("Há um excesso de: ", excesso, "kg.", " A multa custará: R$", multa)
else:
    print("O peso está dentro do regulamento")