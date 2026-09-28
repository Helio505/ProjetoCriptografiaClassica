"""
A criptografia de Cesar, é baseada em deslocamento. A chave
simplesmente determina o deslocamento da casas no alfabeto.

Exemplo:
- Alfabeto: A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z
- Letra codificada com chave 2: E
- Letra decodificada com chave 2: C
- Conclusão: Nós voltamos CHAVE casas para decodificar um caractere.

Exemplo se saida de espaço:
- Alfabeto: A-B-C-D
- Chave 2. Se eu tendo mover o caractere D, o index apontar para
uma posição que não existe. Pra resolver, voltamos novamente para o inicio do 
array e fazemos a conta lá.

Implementação:
- Para criptografar, simplesmente recebemos o texto e para cada carac
tere da string, substituimos por CHAVE casas a frente.
- Para descriptografar, fazemos o contrario.

Detalhes
- Temos que levar em conta espaços e caracteres especiais também. Esses,
nós não substituimos.
- No portugues, faz sentido incluirmos substituição de acentos também.
- Caso estivermos no final do alfabeto, o movimento sairia do nosso array.
Temos que checar isso.

Possiveis limitações:
- Se a chave for muito grande, podemos ter problemas.
- A testagem é manual, e não automatizada. Por isso, é possivel que erros passem despercebidos.
O correto seria implementar testes unitários, ex Pytest.

Autor: Helio
"""

# Nosso alfabeto que utilizamos para substituir caracteres
# OBS. Se não está aqui, é ignorado e continua no texto.
numeros = "0123456789"
simbolos = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
minusculas = "abcdefghijklmnopqrstuvwxyzàáâãäåèéêëìíîïòóôõöøùúûüçñ"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖØÙÚÛÜÇÑ"
alfabeto = f"{numeros}{simbolos}{minusculas}{maiusculas}"


def criptografar(texto_simples: str, chave: int) -> str:
    """
    Recebe o texto simples e retorna o texto criptografado.
    """
    # Iremos reconstruir a string nessa variavel
    array_texto_criptografado: list[str] = []
    for char in texto_simples:
        # Se encontrarmos no alfabeto, substituimos. Se não, não usamos o valor atual.
        if char in alfabeto:
            # Encontramos o index no array de alfabeto referente a essa letra
            index_char_atual = alfabeto.index(char)
            # Calculamos o index do novo caractere, deslocando CHAVE posições para FRENTE
            index_novo_char = index_char_atual+chave
            # Caso a o movimento index+chave faça sair do espaço do array, vamos para o inicio do array
            if len(alfabeto) < index_novo_char:
                index_novo_char -= len(alfabeto)
            # Avançamos CHAVE elementos para frente no index, e obtemos o elemento
            novo_elemento = alfabeto[index_novo_char]
            # Adicionamos no nosso array
            array_texto_criptografado.append(novo_elemento)
        else:
            array_texto_criptografado.append(char)

    # Converter de volta de array para string
    string_texto_criptografado = "".join(array_texto_criptografado)
    return string_texto_criptografado


def descriptografar(texto_criptografado: str, chave: int) -> str:
    """
    Recebemos o texto criptografado e retornamos o texto simples resultante da
    descriptografia.
    """

    # Iremos reconstruir a string nessa variavel
    array_texto_simples: list[str] = []
    for char in texto_criptografado:
        # Se encontrarmos no alfabeto, substituimos. Se não, não usamos o valor atual.
        if char in alfabeto:
            # Encontramos o index no array de alfabeto referente a essa letra
            index_char_atual = alfabeto.index(char)
            # Calculamos o index do novo caractere, deslocando CHAVE posições para TRÁS
            index_novo_char = index_char_atual-chave
            # Aqui, é desnecessário aquela logica que existe na criptografia. Pois o index negativo automaticamente faz o que queremos em Python já.
            # Avançamos CHAVE elementos para frente no index, e obtemos o elemento
            novo_elemento = alfabeto[index_novo_char]
            # Adicionamos no nosso array
            array_texto_simples.append(novo_elemento)
        else:
            array_texto_simples.append(char)

    # Converter de volta de array para string
    string_texto_simples = "".join(array_texto_simples)
    return string_texto_simples


def testes_locais():
    # Teste e resultados esperados
    print("CRIPTOGRAFAR")
    print(criptografar("A", 3)) # -> C
    print(criptografar("AB", 3)) # -> CD
    print(criptografar("BA", 3)) # -> DC
    print(criptografar("Olá Mundo!", 3)) # -> Qnã Owpfq!
    print(criptografar("Hello World", 3)) # -> Jgnnq Yqtnf
    print()

    print("DESCRIPTOGRAFAR")
    print(descriptografar("A", 3)) # -> Y
    print(descriptografar("C", 3)) # -> A
    print(descriptografar("CD", 3)) # -> AB
    print(descriptografar("DC", 3)) # -> BA
    print(descriptografar("Qnã Owpfq!", 3)) # -> Olá Mundo!
    print(descriptografar("Jgnnq Yqtnf", 3)) # -> Hello World
    print()

    # Testes onde criptografamos e depois descriptografamos, e esperamos o mesmo resultado.
    print("CRIPTOGRAFAR E DESCRIPTOGRAFAR")
    print(
        "Texto: A -",
        f"Passado: {descriptografar(criptografar("A", 3), 3)}"
    )
    print(
        "Texto: AB -",
        f"Passado: {descriptografar(criptografar("AB", 3), 3)}"
    )
    print(
        "Texto: BA -",
        f"Passado: {descriptografar(criptografar("BA", 3), 3)}"
    )
    print(
        "Texto: Olá Mundo! -",
        f"Passado: {descriptografar(criptografar("Olá Mundo!", 3), 3)}"
    )
    print(
        "Texto: Hello World -",
        f"Passado: {descriptografar(criptografar("Hello World", 3), 3)}"
    )
    print(
        "Texto: Olá Mundo! Hello World -",
        f"Passado: {descriptografar(criptografar("Olá Mundo! Hello World", 3), 3)}"
    )
    print(
        "Texto: Olá Mundo! Hello World 295 ç 42 <> @% -",
        f"Passado: {descriptografar(criptografar("Olá Mundo! Hello World 295 ç 42 <> @%", 3), 3)}"
    )
    print()

    # Textos grandes
    print("CRIPTOGRAFAR E DESCRIPTOGRAFAR - Textos grandes")
    # PTBR
    string_original_1 = "Capivara[3] ou carpincho[4] (nome científico: Hydrochoerus hydrochaeris) é uma espécie de mamífero roedor da família Caviidae e subfamília Hydrochoerinae. Alguns autores consideram que deva ser classificada em uma família própria. Está incluída no mesmo grupo de roedores ao qual se classificam as pacas, cutias, os preás e o porquinho-da-índia. Ocorre por toda a América do Sul ao leste dos Andes em habitats associados a rios, lagos e pântanos, do nível do mar até 1 300 m de altitude. Extremamente adaptável, pode ocorrer em ambientes altamente alterados pelo ser humano. É o maior roedor do mundo, pesando até 91 kg e medindo até 1,2 m de comprimento e 60 cm de altura. A pelagem é densa, de cor avermelhada a marrom escuro. É possível distinguir os machos por conta da presença de uma glândula proeminente no focinho apesar de o dimorfismo sexual não ser aparente. Existe uma série de adaptações no sistema digestório à herbivoria, principalmente no ceco. Alcança a maturidade sexual com cerca de 1,5 ano de idade, e as fêmeas dão à luz geralmente a quatro filhotes por vez, pesando até 1,5 kg e já nascem com pelos e dentição permanente. Em cativeiro, pode viver até 12 anos de idade."
    criptografado_1 = criptografar(string_original_1, 3)
    descriptografado_1 = descriptografar(criptografado_1, 3)
    if string_original_1 == descriptografado_1:
        print("PTBR - Teste PASSOU")
        print(f"Original:\n {string_original_1}\n")
        print(f"Criptografado:\n {criptografado_1}\n")
        print(f"Descriptografado:\n {descriptografado_1}\n")
    else:
        print("PTBR - Teste FALHOU")
        print(f"Original:\n {string_original_1}\n")
        print(f"Criptografado:\n {criptografado_1}\n")
        print(f"Descriptografado:\n {descriptografado_1}\n")

    print()

    # Inglês
    string_original_2 = "The capybara (/kæp.ɪˈbɑːr.ə, -băr′ə/ ⓘkap-uh-BAR-uh)[a] or greater capybara (Hydrochoerus hydrochaeris) is the largest living rodent,[2] native to all countries in South America except Chile. It is a semiaquatic herbivore that inhabits savannas and dense forests, living near and in bodies of freshwater and feeding mainly on grasses and aquatic plants. Together with the lesser capybara, it constitutes the genus Hydrochoerus. Its other close relatives include guinea pigs and rock cavies, and it is more distantly related to the agouti, the chinchilla, and the nutria. The capybara is a highly social species that usually lives in groups of 10–20 individuals, but can be found in groups as large as 100. It is hunted for its meat and hide and for grease from its thick fatty skin.[3]"
    criptografado_2 = criptografar(string_original_2, 3)
    descriptografado_2 = descriptografar(criptografado_2, 3)
    if string_original_2 == descriptografado_2:
        print("Ingles - Teste PASSOU")
        print(f"Original:\n {string_original_2}\n")
        print(f"Criptografado:\n {criptografado_2}\n")
        print(f"Descriptografado:\n {descriptografado_2}\n")
    else:
        print("Ingles - Teste FALHOU")
        print(f"Original:\n {string_original_2}\n")
        print(f"Criptografado:\n {criptografado_2}\n")
        print(f"Descriptografado:\n {descriptografado_2}\n")


if __name__ == "__main__":
    testes_locais()