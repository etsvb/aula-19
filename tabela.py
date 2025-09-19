altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite quantos kg você tem: "))

imc = peso / altura**2

print("Seu IMC é %.4f" % imc)

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade grau 1")
elif imc < 40:
    print("Obesidadde grau 2")
else:
    print("Obesidade grau 3(Morbida)")