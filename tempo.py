tempo = input("Esta fazendo sol?")

if (tempo == "sim"):
    dinheiro = input("Você tem dinheiro?")
    if (dinheiro == "sim"):
        print("Vamos à praia.")
    else:
        print("Vá ligar o ventilador")
else:
    print("Vamos assistir Netflix.")