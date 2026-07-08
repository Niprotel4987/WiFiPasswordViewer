"""
interface.py
----------------------------------------
Interface gráfica do WiFi Password Viewer

Autor: Telmo Bittencourt
Projeto desenvolvido para estudos em Python
"""

import tkinter as tk
from tkinter import ttk, messagebox

from wifi import WiFiManager
from exportar import exportar_txt, exportar_csv
from util import copiar_para_area_transferencia, filtrar_redes


class WiFiViewer:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("WiFi Password Viewer")

        self.root.geometry("1000x600")

        self.root.minsize(900, 550)

        self.root.configure(bg="#ECECEC")

        self.wifi = WiFiManager()

        self.redes = []

        self.redes_filtradas = []

        self.criar_interface()

        self.carregar_redes()

    # --------------------------------------------------

    def criar_interface(self):

        titulo = tk.Label(
            self.root,
            text="WiFi Password Viewer",
            font=("Segoe UI", 22, "bold"),
            bg="#ECECEC"
        )

        titulo.pack(pady=15)

        # ---------------- Pesquisa ----------------

        pesquisa_frame = tk.Frame(
            self.root,
            bg="#ECECEC"
        )

        pesquisa_frame.pack(fill="x", padx=20)

        tk.Label(
            pesquisa_frame,
            text="Pesquisar:",
            bg="#ECECEC",
            font=("Segoe UI", 11)
        ).pack(side="left")

        self.pesquisa = tk.Entry(
            pesquisa_frame,
            font=("Segoe UI", 11),
            width=40
        )

        self.pesquisa.pack(
            side="left",
            padx=10
        )

        self.pesquisa.bind(
            "<KeyRelease>",
            self.pesquisar
        )

        # ---------------- Tabela ----------------

        colunas = (
            "Rede",
            "Segurança",
            "Senha",
            "Sinal"
        )

        self.tabela = ttk.Treeview(
            self.root,
            columns=colunas,
            show="headings",
            height=18
        )

        for coluna in colunas:

            self.tabela.heading(
                coluna,
                text=coluna
            )

            self.tabela.column(
                coluna,
                width=200,
                anchor="center"
            )

        self.tabela.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ---------------- Botões ----------------

        botoes = tk.Frame(
            self.root,
            bg="#ECECEC"
        )

        botoes.pack(pady=10)

        tk.Button(
            botoes,
            text="Atualizar Redes",
            width=18,
            command=self.carregar_redes
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            botoes,
            text="Copiar Senha",
            width=18,
            command=self.copiar_senha
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            botoes,
            text="Exportar TXT",
            width=18,
            command=self.exportar_para_txt
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            botoes,
            text="Exportar CSV",
            width=18,
            command=self.exportar_para_csv
        ).grid(row=0, column=3, padx=5)

        # ---------------- Barra de Status ----------------

        self.status = tk.Label(
            self.root,
            text="Sistema iniciado.",
            anchor="w",
            bg="#D9D9D9",
            relief="sunken"
        )

        self.status.pack(
            side="bottom",
            fill="x"
        )

    # --------------------------------------------------

    def carregar_redes(self):

        self.redes.clear()

        nomes = self.wifi.listar_redes_salvas()

        if not nomes:

            self.status.config(
                text="Nenhuma rede Wi-Fi encontrada."
            )

            self.atualizar_tabela()

            return

        for nome in nomes:

            info = self.wifi.obter_detalhes_rede(nome)

            info["sinal"] = self.wifi.obter_sinal(nome)

            self.redes.append(info)

        self.redes_filtradas = self.redes.copy()

        self.atualizar_tabela()

        self.status.config(
            text=f"{len(self.redes)} rede(s) carregada(s)."
        )

    # --------------------------------------------------

    def atualizar_tabela(self):

        self.tabela.delete(*self.tabela.get_children())

        for rede in self.redes_filtradas:

            self.tabela.insert(
                "",
                tk.END,
                values=(
                    rede["nome"],
                    rede["seguranca"],
                    rede["senha"],
                    rede["sinal"]
                )
            )

    # --------------------------------------------------

    def pesquisar(self, event=None):

        texto = self.pesquisa.get()

        nomes = filtrar_redes(
            [r["nome"] for r in self.redes],
            texto
        )

        self.redes_filtradas = [
            r
            for r in self.redes
            if r["nome"] in nomes
        ]

        self.atualizar_tabela()

    # --------------------------------------------------

    def copiar_senha(self):

        selecionado = self.tabela.focus()

        if not selecionado:

            messagebox.showwarning(
                "Aviso",
                "Selecione uma rede."
            )

            return

        valores = self.tabela.item(
            selecionado,
            "values"
        )

        copiar_para_area_transferencia(
            self.root,
            valores[2]
        )

        messagebox.showinfo(
            "Sucesso",
            "Senha copiada."
        )

    # --------------------------------------------------

    def exportar_para_txt(self):

        if not self.redes:

            messagebox.showwarning(
                "Aviso",
                "Nenhuma rede para exportar."
            )

            return

        caminho = exportar_txt(self.redes)

        messagebox.showinfo(
            "Exportação",
            f"Arquivo salvo em:\n\n{caminho}"
        )

    # --------------------------------------------------

    def exportar_para_csv(self):

        if not self.redes:

            messagebox.showwarning(
                "Aviso",
                "Nenhuma rede para exportar."
            )

            return

        caminho = exportar_csv(self.redes)

        messagebox.showinfo(
            "Exportação",
            f"Arquivo salvo em:\n\n{caminho}"
        )

    # --------------------------------------------------

    def executar(self):

        self.root.mainloop()