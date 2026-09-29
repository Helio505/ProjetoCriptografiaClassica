"""
Cifra de Substituição Monoalfabética.

A chave é uma palavra utilizada para montar um alfabeto de substituição.

Exemplo:

Alfabeto original:
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Chave:
LIMAO

Alfabeto de substituição:
LIMAOBCDEFGHJKNPQRSTUVWXYZ

Cada letra do texto original é substituída pela letra que está
na mesma posição do alfabeto de substituição.

A mesma letra sempre terá a mesma substituição.

Autor: Pedro
"""


numeros = "0123456789"
simbolos = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
minusculas = "abcdefghijklmnopqrstuvwxyzàáâãäåèéêëìíîïòóôõöøùúûüçñ"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖØÙÚÛÜÇÑ"

alfabeto = f"{numeros}{simbolos}{minusculas}{maiusculas}"


def criar_alfabeto_substituicao(chave: str) -> str:
    """
    Cria o alfabeto de substituição utilizando a chave.

    Os caracteres da chave aparecem primeiro.
    Depois são adicionados os caracteres do alfabeto
    que ainda não apareceram.
    """

    if not chave:
        raise ValueError("A chave não pode ser vazia.")

    alfabeto_substituicao = []

    # Adiciona os caracteres da chave sem repetir.
    for char in chave:
        if char not in alfabeto:
            raise ValueError(
                f"O caractere '{char}' não pertence ao alfabeto."
            )

        if char not in alfabeto_substituicao:
            alfabeto_substituicao.append(char)

    # Completa o restante do alfabeto.
    for char in alfabeto:
        if char not in alfabeto_substituicao:
            alfabeto_substituicao.append(char)

    return "".join(alfabeto_substituicao)


def criptografar(texto_simples: str, chave: str) -> str:
    """
    Criptografa o texto utilizando substituição monoalfabética.
    """

    alfabeto_substituicao = criar_alfabeto_substituicao(chave)

    texto_criptografado = []

    for char in texto_simples:

        if char in alfabeto:
            posicao = alfabeto.index(char)

            novo_char = alfabeto_substituicao[posicao]

            texto_criptografado.append(novo_char)

        else:
            texto_criptografado.append(char)

    return "".join(texto_criptografado)


def descriptografar(texto_criptografado: str, chave: str) -> str:
    """
    Descriptografa o texto utilizando a mesma chave.
    """

    alfabeto_substituicao = criar_alfabeto_substituicao(chave)

    texto_simples = []

    for char in texto_criptografado:

        if char in alfabeto_substituicao:
            posicao = alfabeto_substituicao.index(char)

            novo_char = alfabeto[posicao]

            texto_simples.append(novo_char)

        else:
            texto_simples.append(char)

    return "".join(texto_simples)


def testes_locais():
    print("CRIPTOGRAFAR")

    texto = "CASA"
    chave = "limao"

    criptografado = criptografar(texto, chave)

    print("Texto:", texto)
    print("Chave:", chave)
    print("Criptografado:", criptografado)

    print()

    print("DESCRIPTOGRAFAR")

    descriptografado = descriptografar(criptografado, chave)

    print("Criptografado:", criptografado)
    print("Chave:", chave)
    print("Descriptografado:", descriptografado)

    print()

    if texto == descriptografado:
        print("TESTE PASSOU")
    else:
        print("TESTE FALHOU")


if __name__ == "__main__":
    testes_locais()
