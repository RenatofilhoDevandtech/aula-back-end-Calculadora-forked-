print("Bem-vindo à Calculadora Python!")
print("Vamos realizar algumas operações matemáticas.")

operaçao = input("Por favor, digite a operação desejada (+, -, *, / ou %): ")

a = float(input("Agora, digite o primeiro número: "))
b = float(input("E digite o segundo número: "))

if operaçao == '+':
    resultado = a + b
    print(f"O resultado de {a} + {b} é: {resultado}")
elif operaçao == '-':
    resultado = a - b
    print(f"O resultado de {a} - {b} é: {resultado}")
elif operaçao == '*':
    resultado = a * b
    print(f"O resultado de {a} * {b} é: {resultado}")
elif operaçao == '/':
    if b != 0:
        resultado = a / b
        print(f"O resultado de {a} / {b} é: {resultado}")
    else:
        print("Desculpe, a divisão por zero não é permitida.")
elif operaçao == '%':
    resultado = a + b/100
    print(f"O resultado de {a} % {b} é: {resultado}")
else:
    print("Desculpe, essa operação não existe. Tente novamente.")

print("Obrigado por usar a Calculadora Python!")
