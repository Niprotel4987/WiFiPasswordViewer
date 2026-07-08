"""
wifi.py
----------------------------------------
Responsável por toda comunicação com o Windows
para obter informações das redes Wi-Fi.

Autor: Telmo Bittencourt
Projeto: WiFi Password Viewer
"""

import subprocess
import re


class WiFiManager:

    def executar_comando(self, comando):
        """
        Executa um comando do Windows.
        """

        try:

            resultado = subprocess.check_output(
                comando,
                shell=True,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )

            return resultado

        except subprocess.CalledProcessError:

            return ""


    def listar_redes_salvas(self):
        """
        Retorna todas as redes Wi-Fi salvas.
        """

        resultado = self.executar_comando(
            "netsh wlan show profiles"
        )

        redes = []

        for linha in resultado.splitlines():

            if "All User Profile" in linha:
                redes.append(
                    linha.split(":")[1].strip()
                )

            elif "Todos os Perfis de Usuário" in linha:
                redes.append(
                    linha.split(":")[1].strip()
                )

        return sorted(redes)


    def obter_detalhes_rede(self, nome):
        """
        Retorna senha e tipo de segurança.
        """

        resultado = self.executar_comando(
            f'netsh wlan show profile "{nome}" key=clear'
        )

        senha = ""
        seguranca = ""

        for linha in resultado.splitlines():

            if "Key Content" in linha:
                senha = linha.split(":")[1].strip()

            elif "Conteúdo da Chave" in linha:
                senha = linha.split(":")[1].strip()

            if "Authentication" in linha:
                seguranca = linha.split(":")[1].strip()

            elif "Autenticação" in linha:
                seguranca = linha.split(":")[1].strip()

        if senha == "":
            senha = "Sem senha"

        if seguranca == "":
            seguranca = "Desconhecida"

        return {
            "nome": nome,
            "senha": senha,
            "seguranca": seguranca
        }


    def listar_redes_disponiveis(self):
        """
        Lista redes disponíveis próximas ao computador.
        """

        resultado = self.executar_comando(
            "netsh wlan show networks mode=bssid"
        )

        redes = []

        nome = ""
        sinal = ""

        for linha in resultado.splitlines():

            linha = linha.strip()

            if linha.startswith("SSID"):

                partes = linha.split(":")

                if len(partes) > 1:
                    nome = partes[1].strip()

            elif linha.startswith("Signal"):

                partes = linha.split(":")

                if len(partes) > 1:
                    sinal = partes[1].strip()

                    redes.append({
                        "nome": nome,
                        "sinal": sinal
                    })

        return redes


    def obter_sinal(self, nome):
        """
        Retorna intensidade do sinal.
        """

        redes = self.listar_redes_disponiveis()

        for rede in redes:

            if rede["nome"] == nome:
                return rede["sinal"]

        return "--"


if __name__ == "__main__":

    wifi = WiFiManager()

    print("=" * 50)
    print("REDES SALVAS")
    print("=" * 50)

    redes = wifi.listar_redes_salvas()

    for rede in redes:

        info = wifi.obter_detalhes_rede(rede)

        print(f"""
Nome      : {info['nome']}
Segurança : {info['seguranca']}
Senha     : {info['senha']}
Sinal     : {wifi.obter_sinal(rede)}
""")
        