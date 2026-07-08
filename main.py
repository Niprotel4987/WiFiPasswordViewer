"""
main.py
----------------------------------------
Arquivo principal do projeto.

Autor: Telmo Bittencourt
Projeto: WiFi Password Viewer
"""

from wifi import WiFiManager


def main():

    wifi = WiFiManager()

    redes = wifi.listar_redes_salvas()

    if not redes:
        print("Nenhuma rede Wi-Fi salva foi encontrada.")
        return

    print("=" * 70)
    print("               WiFi Password Viewer")
    print("=" * 70)

    for indice, nome in enumerate(redes, start=1):

        info = wifi.obter_detalhes_rede(nome)
        sinal = wifi.obter_sinal(nome)

        print(f"""
[{indice}] {info['nome']}

Segurança : {info['seguranca']}
Senha     : {info['senha']}
Sinal     : {sinal}

{'-' * 70}
""")


if __name__ == "__main__":
    main()
    