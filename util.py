"""
util.py
----------------------------------------
Funções auxiliares do projeto.

Autor: Telmo Bittencourt
Projeto: WiFi Password Viewer
"""

from datetime import datetime


def copiar_para_area_transferencia(janela, texto):
    """
    Copia um texto para a área de transferência.
    """

    janela.clipboard_clear()
    janela.clipboard_append(texto)
    janela.update()


def filtrar_redes(lista_redes, pesquisa):
    """
    Filtra redes pelo nome.
    """

    pesquisa = pesquisa.lower().strip()

    if pesquisa == "":
        return lista_redes

    return [
        rede
        for rede in lista_redes
        if pesquisa in rede.lower()
    ]


def barras_sinal(valor):
    """
    Converte porcentagem do sinal em barras.
    """

    if valor == "--":
        return "-----"

    try:

        valor = int(valor.replace("%", ""))

    except:

        return "-----"

    if valor >= 80:
        return "█████"

    elif valor >= 60:
        return "████░"

    elif valor >= 40:
        return "███░░"

    elif valor >= 20:
        return "██░░░"

    return "█░░░░"


def data_hora():
    """
    Retorna data e hora atuais.
    """

    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def nome_arquivo(prefixo, extensao):
    """
    Gera nome para exportação.
    """

    data = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{prefixo}_{data}.{extensao}"