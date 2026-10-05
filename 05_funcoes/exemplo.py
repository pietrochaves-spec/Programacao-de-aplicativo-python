#O que é uma função:

# Uma função é um bloco de código criado para realizar uma determinada tarefa.
#
# Ela permite organizar e reutilizar o código.

#1. Criando uma função-

#Ultilizar a palavra 'def' para criar uma função

def saudacao():
    print("Olá, seja bem vindo.")


#para executar a função, chamamos seu nome. Ex: saudacao()
saudacao()

#2. Função com parâmetro
def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("Ana")
saudacao("Carlos")

#3. Mais de um parâmetro
def apresentar(nome , idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria", 17)

#4. Função com cálculo
def somar(numero1 , numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar(10, 5)

#5. Retornando um valor
#O return devolde o valor para o local onde a função foi chamada.

def somar(numero1 , numero2):
    return numero1 + numero2

resultado = somar(10, 20)
print(resultado)


#6. Função com condição --> verificação de idade ex.
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

resultado = verificarIdade(20)
print(resultado)

#7. Parâmetro com valor padrão
#Podemos definir um valor padrão para um parâmetro.


def saudacao(nome="Aluno"):
    print(f"Olá, {nome}")

saudacao()
saudacao("João")

#8. Vários Parâmetros
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) /3
    return media

print(calcularMedia(8, 7, 9))


#9. Funções para organizar um programa
def cadastrarProduto():
    nome = input("Digite o nome do Produto: ")
    preco = float(input("Digite o preco(em reais): "))
    return nome, preco

def exibirProduto(nome , preco):
    print("\n ==== PRODUTO ====")
    print(f"nome: {nome}")
    print(f"preço: {preco} reais")

nome, preco = cadastrarProduto()
exibirProduto(nome, preco)