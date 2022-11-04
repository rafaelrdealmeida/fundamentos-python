
# funções build-in python - print(), type(), input()

# tipo de dado basico string

# simbolo de igual é um atribuidor de variavel
caracteres = "Visando promover e previnir a saúde mental da comunidade unespiana, durante o cenário do isolamento da pandemia da COVID-19, a Unesp em parceria  com a Famesp, está disponibilizando atendimento psicológico."
# tipo de dado basico numerico

num_01 = 10
num_02 = 20

print(caracteres)
print(type(caracteres))

print("#####")

print(num_01, type(num_01))

print("#####")

soma = num_01 + num_02

print(soma)

print("#####")

num_03 = input("Insira um valor: ")
num_04 = input("Insira outro valor: ")

soma = int(num_03) + int(num_04)

## f-string (combinar string com variavel)
print(f"A soma dos valores inseridos é: {soma}")


