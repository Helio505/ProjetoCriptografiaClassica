"""
Ponto de entrada da aplicação.
"""

import sys

from src.cesar_cripto import criptografar as cesar_ecript
from src.cesar_cripto import descriptografar as cesar_dcript


def menu_option_cesar():
    print("- Você escolheu a Cifra de César -")
    print("Escolha a operação:")
    print("1 - Criptografa")
    print("2 - Descriptografa")
    print("0 - Voltar ao menu principal")
    operacao = input("Digite o número da operação desejada: ")
    if operacao == "1":
        print("- Criptografia -")
        texto_simples = input("Digite o texto simples: ")
        chave = int(input("Digite a chave (número inteiro): "))
        texto_criptografado = cesar_ecript(texto_simples, chave)
        print(f"Texto criptografado: {texto_criptografado}")
    elif operacao == "2":
        print("- Descriptografia -")
        texto_criptografado = input("Digite o texto criptografado: ")
        chave = int(input("Digite a chave (número inteiro): "))
        texto_simples = cesar_dcript(texto_criptografado, chave)
        print(f"Texto simples: {texto_simples}")
    elif operacao == "0":
        print("Voltando ao menu principal...")
    else:
        print("Opção inválida. Tente novamente.")

def menu_option_vigenere():
    print("- Você escolheu a Cifra de Vigenère -")
    print("Escolha a operação:")
    print("1 - Criptografa")
    print("2 - Descriptografa")
    print("0 - Voltar ao menu principal")
    operacao = input("Digite o número da operação desejada: ")
    if operacao == "1":
        print("- Criptografia -")
        pass
    elif operacao == "2":
        print("- Descriptografia -")
        pass
    elif operacao == "0":
        print("Voltando ao menu principal...")
    else:
        print("Opção inválida. Tente novamente.")


def menu_option_substituicao():
    print("- Você escolheu a Cifra de Substituição Monoalfabética -")
    print("Escolha a operação:")
    print("1 - Criptografa")
    print("2 - Descriptografa")
    print("0 - Voltar ao menu principal")
    operacao = input("Digite o número da operação desejada: ")
    if operacao == "1":
        print("- Criptografia -")
        pass
    elif operacao == "2":
        print("- Descriptografia -")
        pass
    elif operacao == "0":
        print("Voltando ao menu principal...")
    else:
        print("Opção inválida. Tente novamente.")

def menu_option_transposicao():
    print("- Você escolheu a Cifra de Transposição (Columnar ou Rail Fence) -")
    print("Escolha a operação:")
    print("1 - Criptografa")
    print("2 - Descriptografa")
    print("0 - Voltar ao menu principal")
    operacao = input("Digite o número da operação desejada: ")
    if operacao == "1":
        print("- Criptografia -")
        pass
    elif operacao == "2":
        print("- Descriptografia -")
        pass
    elif operacao == "0":
        print("Voltando ao menu principal...")
    else:
        print("Opção inválida. Tente novamente.")

def main():
    print("=== Projeto de Criptografia Clássica ===")

    # Menu infinito, que só sai se acionarmo "0" ou Ctrl+C
    while True:
        print()
        print("Escolha a estratégia de criptografia:")
        print("1 - Cifra de César")
        print("2 - Cifra de Vigenère")
        print("3 - Cifra de Substituição Monoalfabética")
        print("4 - Cifra de Transposição (Columnar ou Rail Fence)")
        print("0 - Sair")
        escolha = input("Digite o número da estratégia desejada: ")

        if escolha == "1":
            menu_option_cesar()
        elif escolha == "2":
            menu_option_vigenere()
        elif escolha == "3":
            menu_option_substituicao()
        elif escolha == "4":
            menu_option_transposicao()
        elif escolha == "0":
            print("Saindo...")
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
