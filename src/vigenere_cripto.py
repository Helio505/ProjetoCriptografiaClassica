"""
A criptografia de Vigenère é parecida com a de César, também é baseada em
deslocamento. A diferença é que a chave agora é uma PALAVRA, e não um número.
Cada letra da chave diz quantas casas vamos deslocar cada letra do texto.

Exemplo (usando um alfabeto simples só para entender a ideia):
- Alfabeto: A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z
- Posições: A=0, B=1, C=2, D=3, ...
- Texto: CASA
- Chave: BD (B=1, D=3)
- A chave é repetida até ficar do tamanho do texto: BDBD
- C + B(1) = D
- A + D(3) = D
- S + B(1) = T
- A + D(3) = D
- Resultado: DDTD
- Para descriptografar, fazemos o contrario: voltamos as casas ao invés de avançar.

Implementação:
- Usamos o mesmo alfabeto da cifra de César.
- O deslocamento de cada letra é a posição (index) da letra da chave no alfabeto.
- Usamos uma variável para saber em qual letra da chave estamos. Quando ela
chega no final da chave, voltamos para o inicio.

Detalhes
- Caracteres que não estão no alfabeto não são substituidos e continuam no texto.
Nesse caso, também não avançamos na chave.
- Caso estivermos no final do alfabeto, o movimento sairia do nosso array.
Para resolver isso usamos o operador % (resto da divisão), que faz o index
"dar a volta" e começar do inicio do alfabeto de novo.

Possiveis limitações:
- A chave não pode ser vazia, e todas as letras dela precisam estar no alfabeto.
- A testagem é manual, e não automatizada. Por isso, é possivel que erros passem despercebidos.

Autor: Luiz
"""

# Nosso alfabeto que utilizamos para substituir caracteres (o mesmo da cifra de César)
# OBS. Se não está aqui, é ignorado e continua no texto.
numeros = "0123456789"
simbolos = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
minusculas = "abcdefghijklmnopqrstuvwxyzàáâãäåèéêëìíîïòóôõöøùúûüçñ"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖØÙÚÛÜÇÑ"
alfabeto = f"{numeros}{simbolos}{minusculas}{maiusculas}"


def criptografar(texto_simples: str, chave: str) -> str:
    """
    Recebe o texto simples e a chave (palavra), e retorna o texto criptografado.
    """
    # Iremos reconstruir a string nessa variavel
    array_texto_criptografado: list[str] = []
    # Guarda em qual letra da chave nós estamos
    posicao_chave = 0

    for char in texto_simples:
        # Se encontrarmos no alfabeto, substituimos. Se não, não usamos o valor atual.
        if char in alfabeto:
            # Pegamos a letra da chave que vamos usar agora
            letra_chave = chave[posicao_chave]
            # O deslocamento é a posição da letra da chave no alfabeto
            deslocamento = alfabeto.index(letra_chave)
            # Encontramos o index no array de alfabeto referente a essa letra
            index_char_atual = alfabeto.index(char)
            # Calculamos o index do novo caractere, deslocando para FRENTE.
            # O % faz voltar para o inicio do alfabeto caso passe do final.
            index_novo_char = (index_char_atual + deslocamento) % len(alfabeto)
            # Obtemos o novo elemento e adicionamos no nosso array
            novo_elemento = alfabeto[index_novo_char]
            array_texto_criptografado.append(novo_elemento)

            # Avançamos para a proxima letra da chave
            posicao_chave += 1
            # Se chegamos no final da chave, voltamos para a primeira letra
            if posicao_chave == len(chave):
                posicao_chave = 0
        else:
            array_texto_criptografado.append(char)

    # Converter de volta de array para string
    string_texto_criptografado = "".join(array_texto_criptografado)
    return string_texto_criptografado


def descriptografar(texto_criptografado: str, chave: str) -> str:
    """
    Recebemos o texto criptografado e a chave (palavra), e retornamos o texto
    simples resultante da descriptografia.
    """
    # Iremos reconstruir a string nessa variavel
    array_texto_simples: list[str] = []
    # Guarda em qual letra da chave nós estamos
    posicao_chave = 0

    for char in texto_criptografado:
        # Se encontrarmos no alfabeto, substituimos. Se não, não usamos o valor atual.
        if char in alfabeto:
            # Pegamos a letra da chave que vamos usar agora
            letra_chave = chave[posicao_chave]
            # O deslocamento é a posição da letra da chave no alfabeto
            deslocamento = alfabeto.index(letra_chave)
            # Encontramos o index no array de alfabeto referente a essa letra
            index_char_atual = alfabeto.index(char)
            # Calculamos o index do novo caractere, deslocando para TRÁS.
            # O % faz voltar para o final do alfabeto caso passe do inicio.
            index_novo_char = (index_char_atual - deslocamento) % len(alfabeto)
            # Obtemos o novo elemento e adicionamos no nosso array
            novo_elemento = alfabeto[index_novo_char]
            array_texto_simples.append(novo_elemento)

            # Avançamos para a proxima letra da chave
            posicao_chave += 1
            # Se chegamos no final da chave, voltamos para a primeira letra
            if posicao_chave == len(chave):
                posicao_chave = 0
        else:
            array_texto_simples.append(char)

    # Converter de volta de array para string
    string_texto_simples = "".join(array_texto_simples)
    return string_texto_simples


def testes_locais():
    # Teste e resultados esperados
    print("CRIPTOGRAFAR")
    print(criptografar("CASA", "0"))  # -> CASA (a chave "0" desloca 0 casas)
    # -> DBTB (a chave "1" desloca 1 casa, igual César com chave 1)
    print(criptografar("CASA", "1"))
    # -> DDTD (a chave "13" representa "1" e "3", então desloca 1 casa na primeira letra, 3 casas na segunda, 1 na terceira e 3 na quarta)
    print(criptografar("CASA", "13"))
    print(criptografar("Olá Mundo!", "limao"))
    print(criptografar("Hello World", "limao"))
    print()

    print("DESCRIPTOGRAFAR")
    print(descriptografar("CASA", "0"))  # -> CASA
    print(descriptografar("DBTB", "1"))  # -> CASA
    print(descriptografar("DDTD", "13"))  # -> CASA
    print()

    # Testes onde criptografamos e depois descriptografamos, e esperamos o mesmo resultado.
    print("CRIPTOGRAFAR E DESCRIPTOGRAFAR")
    textos = [
        "A",
        "AB",
        "Olá Mundo!",
        "Hello World",
        "Olá Mundo! Hello World 295 ç 42 <> @%",
    ]
    chave = "limao"
    for texto in textos:
        criptografado = criptografar(texto, chave)
        descriptografado = descriptografar(criptografado, chave)
        if texto == descriptografado:
            print("PASSOU -", "Texto:", texto,
                  "- Criptografado:", criptografado)
        else:
            print("FALHOU -", "Texto:", texto,
                  "- Descriptografado:", descriptografado)
    print()

    # Texto grande
    print("CRIPTOGRAFAR E DESCRIPTOGRAFAR - Texto grande")
    string_original = "Capivara[3] ou carpincho[4] (nome científico: Hydrochoerus hydrochaeris) é uma espécie de mamífero roedor da família Caviidae e subfamília Hydrochoerinae. É o maior roedor do mundo, pesando até 91 kg e medindo até 1,2 m de comprimento e 60 cm de altura."
    chave = "Capivara"
    criptografado = criptografar(string_original, chave)
    descriptografado = descriptografar(criptografado, chave)
    if string_original == descriptografado:
        print("PTBR - Teste PASSOU")
    else:
        print("PTBR - Teste FALHOU")
    print(f"Original:\n {string_original}\n")
    print(f"Criptografado:\n {criptografado}\n")
    print(f"Descriptografado:\n {descriptografado}\n")


if __name__ == "__main__":
    testes_locais()
