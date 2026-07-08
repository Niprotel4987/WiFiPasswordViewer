from typing import Self

from CTkTable import CTkTable
import customtkinter as ctk

from constantes import *


class WiFiViewer(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(APP_NOME)
        self.geometry(f"{LARGURA}x{ALTURA}")

        self.criar_interface()

    def criar_interface(self):

        # Layout principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==========================
        # MENU LATERAL
        # ==========================

        self.menu = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.menu.grid(row=0, column=0, sticky="ns")

        titulo = ctk.CTkLabel(
            self.menu,
            text="📶 WiFi Viewer",
            font=(FONTE, 22, "bold")
        )

        titulo.pack(pady=(30, 20))

        self.btn_inicio = ctk.CTkButton(
            self.menu,
            text="🏠 Início"
        )

        self.btn_inicio.pack(fill="x", padx=15, pady=8)

        self.btn_atualizar = ctk.CTkButton(
            self.menu,
            text="🔄 Atualizar"
        )

        self.btn_atualizar.pack(fill="x", padx=15, pady=8)

        self.btn_txt = ctk.CTkButton(
            self.menu,
            text="📄 Exportar TXT"
        )

        self.btn_txt.pack(fill="x", padx=15, pady=8)

        self.btn_csv = ctk.CTkButton(
            self.menu,
            text="📊 Exportar CSV"
        )

        self.btn_csv.pack(fill="x", padx=15, pady=8)

        self.btn_sobre = ctk.CTkButton(
            self.menu,
            text="⚙ Sobre"
        )

        self.btn_sobre.pack(fill="x", padx=15, pady=8)

        # ==========================
        # ÁREA PRINCIPAL
        # ==========================

        self.principal = ctk.CTkFrame(self)

        self.principal.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        self.principal.grid_columnconfigure(0, weight=1)

        # Pesquisa

        self.pesquisa = ctk.CTkEntry(
            self.principal,
            placeholder_text="Pesquisar rede..."
        )

        self.pesquisa.pack(
            fill="x",
            padx=20,
            pady=20
        )

        # Área onde futuramente ficará a tabela

        dados = [
            ["Rede", "Segurança", "Senha", "Sinal"],
            ["Carregando...", "-", "-", "-"]
        ]

        self.tabela = CTkTable(
            master=self.principal,
            values=dados,
            corner_radius=8
        )

        self.tabela.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # Barra inferior

        self.status = ctk.CTkLabel(
            self,
            text="Status: Pronto",
            anchor="w"
        )

        self.status.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=5
        )