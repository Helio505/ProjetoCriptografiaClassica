"""
Cifra de Transposição - Rail Fence (Cerca de Linhas).

A criptografia Rail Fence não substitui as letras, ela apenas muda a posição
delas (transposição). A chave é um número inteiro que representa a quantidade 
de linhas.

Exemplo de Criptografia:
- Texto: MENSAGEM SECRETA
- Chave: 3 (3 linhas)

Escrevemos em zigue-zague:
Linha 1: M . . . A . . .  . . . C . . . T .
Linha 2: . E . S . G . M . S . C . R . E . A
Linha 3: . . N . . . E . . . E . . . E . .

Lendo linha por linha, o texto criptografado fica:
"MA CTESGMSCREANEEE"

Implementação:
- Criptografia: Simulamos as linhas criando um array de strings. Iteramos 
  pelo texto e vamos descendo e subindo as linhas, adicionando a letra na linha atual.
- Descriptografia: Precisamos reconstruir o "esqueleto" do zigue-zague para 
  saber onde cada letra deve cair, preencher esse esqueleto linha por linha com 
  o texto criptografado, e depois ler o texto final percorrendo o zigue-zague 
  novamente.

Autor: Gabriel
"""

def criptografar(texto_simples: str, chave: int) -> str:

    # recebe texto e chave, retorna texto criptografado.
    if chave <= 1 or chave >= len(texto_simples):
        return texto_simples
    # lista de string vazia p cada linha
    linha = [''] * chave

    # inicializa variavel para ver em qual linha estamos, e se estamos descendo ou subindo
    linha_atual = 0
    descendo = False

    # loop para guardar cada letra na linha correta
    for char in texto_simples:
        # pega o que tem na linha atual e concatena o char no final
        linha[linha_atual] += char

        # se estamos na primeira ou ultima linha, invertemos a direção
        if linha_atual == 0 or linha_atual == chave - 1:
            descendo = not descendo
        
        # verifica se descendo é True e soma 1 na linha atual, se não subtrai 1
        if descendo:
            linha_atual += 1
        else:
            linha_atual -= 1
        
    # retorna a junção de todas as linhas
    return ''.join(linha)

def descriptografar(texto_criptografado: str, chave: int) -> str:
    # recebe texto criptografado e chave, retorna texto descriptografado.
    if chave <= 1 or chave >= len(texto_criptografado):
        return texto_criptografado
    # cria uma matriz com o tamanho da chave e do texto criptografado, preenchida com "\n"
    matriz = [["\n"] * len(texto_criptografado) for _ in range(chave)]

    linha_atual = 0
    descendo = False
    # varrer a matriz e colocar "*" nos lugares onde as letras vão ficar
    for i in range(len(texto_criptografado)):
        matriz[linha_atual][i] = '*'
        if linha_atual == 0 or linha_atual == chave - 1:
            descendo = not descendo
        if descendo:
            linha_atual += 1
        else:
            linha_atual -= 1

    contador_letras = 0
    for linha in range(chave):
        for coluna in range(len(texto_criptografado)):
            if matriz[linha][coluna] == '*' and contador_letras < len(texto_criptografado):
                matriz[linha][coluna] = texto_criptografado[contador_letras]
                contador_letras += 1
    
    # ler a matriz em zig-zag e colocar as letras na lista resultado
    resultado = []
    linha_atual = 0
    descendo = False

    for i in range(len(texto_criptografado)):
        resultado.append(matriz[linha_atual][i])
        if linha_atual == 0 or linha_atual == chave - 1:
            descendo = not descendo
        if descendo:
            linha_atual += 1
        else:
            linha_atual -= 1
    # retorna resultado junto
    return ''.join(resultado)

def testes_locais():

    print("CRIPTOGRAFAR")

    texto_simples = "MENSAGEM SECRETA"
    chave = 3

    criptografado = criptografar(texto_simples, chave)

    print(f"Original: '{texto_simples}' | Chave: {chave}")
    print(f"Criptografado: '{criptografado}'\n")

    print("DESCRIPTOGRAFAR")

    descriptografado = descriptografar(criptografado, chave)

    print(f"Criptografado: '{criptografado}' | Chave: {chave}")
    print(f"Descriptografado: '{descriptografado}'\n")

    print("CRIPTOGRAFAR E DESCRIPTOGRAFAR - Testes Rápidos")
    
    textos = ["CASA", "SEGURANCA DA INFORMACAO", "Gabriel 123 !@#", "A"]
    chave_teste = 4
    
    for t in textos:
        c = criptografar(t, chave_teste)
        d = descriptografar(c, chave_teste)
        if t == d:
            print(f"PASSOU - Texto: '{t}' -> Cripto: '{c}'")
        else:
            print(f"FALHOU - Texto: '{t}' -> Desc: '{d}'")

if __name__ == "__main__":
    testes_locais()




        



    


