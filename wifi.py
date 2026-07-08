import subprocess
import re


class WiFiManager:

    def listar_redes_salvas(self):
        """
        Retorna todas as redes Wi-Fi salvas.
        """

        try:

            resultado = subprocess.check_output(
                "netsh wlan show profiles",
                shell=True,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )

        except:

            return []

        redes = []

        for linha in resultado.splitlines():

            if "Todos os Perfis de Usuário" in linha or "All User Profile" in linha:

                nome = linha.split(":")[1].strip()

                info = self.obter_informacoes(nome)

                redes.append(info)

        return redes

    def obter_informacoes(self, nome):

        try:

            resultado = subprocess.check_output(
                f'netsh wlan show profile name="{nome}" key=clear',
                shell=True,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )

        except:

            return {
                "nome": nome,
                "seguranca": "-",
                "senha": "-",
                "sinal": "-"
            }

        senha = "-"

        tipo = "-"

        chave = re.search(r"Conteúdo da Chave\s*:\s*(.*)", resultado)

        if chave:

            senha = chave.group(1)

        autenticacao = re.search(r"Autenticação\s*:\s*(.*)", resultado)

        if autenticacao:

            tipo = autenticacao.group(1)

        return {

            "nome": nome,

            "seguranca": tipo,

            "senha": senha,

            "sinal": "-"

        }