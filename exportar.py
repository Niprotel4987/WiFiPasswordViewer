"""
exportar.py
----------------------------------------
Responsável por exportar os dados das redes
Wi-Fi para arquivos TXT e CSV.

Autor: Telmo Bittencourt
Projeto: WiFi Password Viewer
"""

import csv
import os

from util import nome_arquivo


EXPORT_DIR = "exports"


def criar_pasta_exportacao():
    """
    Cria a pasta exports caso ela não exista.
    """

    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)


def exportar_txt(lista_redes):
    """
    Exporta informações das redes para TXT.
    """

    criar_pasta_exportacao()

    caminho = os.path.join(
        EXPORT_DIR,
        nome_arquivo("wifi", "txt")
    )

    with open(caminho, "w", encoding="utf-8") as arquivo:

        arquivo.write("WiFi Password Viewer\n")
        arquivo.write("=" * 50 + "\n\n")

        for rede in lista_redes:

            arquivo.write(f"Rede       : {rede['nome']}\n")
            arquivo.write(f"Segurança  : {rede['seguranca']}\n")
            arquivo.write(f"Senha      : {rede['senha']}\n")
            arquivo.write(f"Sinal      : {rede['sinal']}\n")
            arquivo.write("-" * 50 + "\n")

    return caminho


def exportar_csv(lista_redes):
    """
    Exporta informações das redes para CSV.
    """

    criar_pasta_exportacao()

    caminho = os.path.join(
        EXPORT_DIR,
        nome_arquivo("wifi", "csv")
    )

    with open(
        caminho,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(
            [
                "Rede",
                "Segurança",
                "Senha",
                "Sinal"
            ]
        )

        for rede in lista_redes:

            escritor.writerow(
                [
                    rede["nome"],
                    rede["seguranca"],
                    rede["senha"],
                    rede["sinal"]
                ]
            )

    return caminho