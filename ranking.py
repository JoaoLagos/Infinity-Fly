from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import operator

''' Salva o NOME e a PONTUAÇÃO do jogador no RANKING, já organizando em ORDEM DECRESCENTE dos pontos '''


def savePoints(name, pontos):

    ### Abre o arquivo em modo LEITURA, para pegar os dados das linhas.
    arquivoRanking = open("txt_files/ranking.txt", "r")
    lista = arquivoRanking.readlines()
    arquivoRanking.close()

    ### Cria uma lista organizada (sem os "\n", strings) e organiza em ordem decrescente. POIS o lista = arquivoRanking.readlines() vem desorganizado. Adicionando o novo dado.
    listaNova = []
    for linha in lista:
        linhaAppend = linha.split("#")
        linhaAppend[1] = int(linhaAppend[1])
        listaNova.append(linhaAppend)
    listaNova.append([name, int(pontos)])
    listaNova.sort(key=operator.itemgetter(1),
                   reverse=True)  # Coloca em ordem pela pontuação, para isso use como referência o listaNova[1], ou seja, operator.itemgetter(1).

    ### Abre o arquivo em modo ESCRITA para reinserir os dados em ordem crescente, com a adição do novo dado.
    arquivoRanking = open("txt_files/ranking.txt", "w")
    for dados in listaNova:
        arquivoRanking.writelines([dados[0], "#", str(dados[1]), "\n"])
    arquivoRanking.close()


''' Inicializar essa Janela '''


def start():
    # JANELA
    janela_width = 1280
    janela_height = 720
    janela = Window(janela_width, janela_height)
    background = GameImage("components/background/bg2_colinas.jpg")
    background.draw()

    listRank = Sprite("components/ranking/listRank4.png")
    listRank.x = janela.width / 2 - listRank.width / 2
    listRank.draw()

    medalha1 = "components/ranking/medalha1.png"
    medalha2 = "components/ranking/medalha2.png"
    medalha3 = "components/ranking/medalha3.png"
    medalha4 = "components/ranking/medalha4.png"
    medalha5 = "components/ranking/medalha5.png"
    medalhas = [medalha1, medalha2, medalha3, medalha4, medalha5]
    jogadores = []
    ordenado = []
    maior = "0#0"

    teclado = Window.get_keyboard()

    rank_archive = open("txt_files/ranking.txt", "r")
    linha = rank_archive.readline().strip("\n")
    while linha != "":
        jogadores.append(linha)
        linha = rank_archive.readline().strip("\n")
    rank_archive.close()
    while len(jogadores) > 0:
        for j in jogadores:
            mai = maior.split("#")
            nm, pts = j.split("#")
            if int(pts) >= int(mai[1]):
                maior = j
        ordenado.append(maior)
        jogadores.remove(maior)
        maior = "0#0"

    arquivoRanking = open("txt_files/ranking.txt", "w")
    for i in range(len(ordenado)):
        arquivoRanking.write(ordenado[i]+"\n")
    arquivoRanking.close()
    #lista = rank_archive.readlines()

    posicao = 0
    while True:
        if teclado.key_pressed("ESC"):
            break

        for rank_ID in ordenado:
            if posicao < 5 and posicao < len(ordenado):
                ### Desenha medalhas
                medalha = Sprite(medalhas[posicao])
                medalha.x = listRank.x + 30
                medalha.y = 200 - 6 + posicao * 60
                medalha.draw()

                ### Coloca o Rank
                rank_ID = rank_ID.split("#")
                janela.draw_text(f"{posicao + 1}. LUGAR: {rank_ID[0]} - {rank_ID[1]} pontos", x=listRank.x + 80,
                                 y=200 + posicao * 60, bold=True, size=18)
                posicao += 1

        janela.update()
