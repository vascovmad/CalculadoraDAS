print("Calculadora")

numero1 = float(input("\n1º número: "))
conta = input("Operador: ")
numero2 = float(input("2º número: "))

if conta == "+":
    print(numero1 + numero2)
elif conta == "*":
    print(numero1 * numero2)
elif conta == "/":
    print(numero1 / numero2)
elif conta == "-":
    print(numero1 - numero2)
else:
    print("Operador Inválido!")