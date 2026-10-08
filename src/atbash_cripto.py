"""
A criptografia de Atbash é uma criptografia de simples substituição. Ela
consiste na substituição da primeira letra pela ultima, segunda pela pe
nultima e assim por diante (olhando no alfabeto)

Exemplo:
- Alfabeto: A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z
- Letras originais e resultantes:
    - A -> Z
    - C -> X
- Conclusão: Simplesmente usamos a letra equivalente na posição inversa.

Implementação:
- Usei um alfabeto original e um inverso. Para criptografar,
nós procuramos o elemento no original, encontramos seu index e
usamos esse index para acessar o inverso.
- Para descriptografar, fazemos o contrario. Utilizamos o inverso
como original.

Possiveis limitações:
- Mantive o alfabeto classico para simplicidade. Caracteres especiais, pt-br e numeros
não são substituidos.

Recursos:
- https://pt.wikipedia.org/wiki/Atbash

Autor: Helio
"""

# Nosso alfabeto que utilizamos para substituir caracteres
# OBS. Se não está aqui, é ignorado e continua no texto.
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_reversed = "zyxwvutsrqponmlkjihgfedcba"
# alfabeto_reversed = "".join(reversed(alfabeto)) # O reversed sozinho não resolve, pois retorna um iterador. Então estamos transformando lista em string com join.


def criptografar(texto_simples: str) -> str:
    """
    Recebe o texto simples e retorna o texto criptografado.
    """
    # Iremos reconstruir a string nessa variavel
    string_texto_criptografado: str = ""
    # Para cada caractere, nós procuramos o de mesmo index no array invertido
    for char in texto_simples:
        # Se encontrarmos no alfabeto, substituimos. Se não, deixamos o mesmo valor atual
        if char in alfabeto and char in alfabeto_reversed:
            # Encontramos o index no array de alfabeto referente a essa letra
            index_char_atual = alfabeto.index(char)
            novo_elemento = alfabeto_reversed[index_char_atual]
            # Adicionamos no nosso array
            string_texto_criptografado += novo_elemento
        else:
            string_texto_criptografado += char
    return string_texto_criptografado


def descriptografar(texto_criptografado: str) -> str:
    """
    Recebemos o texto criptografado e retornamos o texto simples resultante da
    descriptografia.
    """
    # Iremos reconstruir a string nessa variavel
    string_texto_descriptografado: str = ""
    # Para cada caractere, nós procuramos o de mesmo index no array invertido
    for char in texto_criptografado:
        # Se encontrarmos no alfabeto, substituimos. Se não, deixamos o mesmo valor atual
        if char in alfabeto and char in alfabeto_reversed:
            # MARK: É o inverso da criptografia, então usamos o array reversed como original
            # Encontramos o index no array de alfabeto referente a essa letra
            index_char_atual = alfabeto_reversed.index(char)
            novo_elemento = alfabeto[index_char_atual]
            # Adicionamos no nosso array
            string_texto_descriptografado += novo_elemento
        else:
            string_texto_descriptografado += char
    return string_texto_descriptografado


def testes_locais():
    # Teste e resultados esperados
    print("CRIPTOGRAFAR")
    print(criptografar("a"))  # -> z
    print(criptografar("ab"))  # -> zy
    print(criptografar("c"))  # -> x
    print(criptografar("ola mundo!"))  # -> loz nfmwl!
    print(criptografar("hello world!"))  # -> svool dliow!
    print(criptografar("python"))  # -> kbgslm
    print(criptografar("eu EU 123 !@#"))  # -> fv FV 123 !@#
    print()

    print("DESCRIPTOGRAFAR")
    print(descriptografar("z"))  # -> a
    print(descriptografar("zy"))  # -> ab
    print(descriptografar("x"))  # -> c
    print(descriptografar("loz nfmwl!"))  # -> ola mundo!
    print(descriptografar("svool dliow!"))  # -> hello world!
    print(descriptografar("kbgslm"))  # -> python
    print(descriptografar("fv FV 123 !@#"))  # -> eu EU 123 !@#
    print()

    # Testes onde criptografamos e depois descriptografamos, e esperamos o mesmo resultado.
    print("CRIPTOGRAFAR E DESCRIPTOGRAFAR")
    data = [
        "a",
        "ab",
        "c",
        "ba",
        "ola mundo!",
        "hello world!",
        "python",
        "eu EU 123 !@#",
    ]
    for item in data:
        criptografado = criptografar(item)
        descriptografado = descriptografar(criptografado)
        print(f"Original: {item}")
        print(f"Criptografado: {criptografado}")
        print(f"Descriptografado: {descriptografado}")
        print(f"Correto: {item == descriptografado}")
        print()

    print()


if __name__ == "__main__":
    testes_locais()
