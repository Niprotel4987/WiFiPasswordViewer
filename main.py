from config import configurar_aplicacao
from interface import WiFiViewer


def main():

    configurar_aplicacao()

    app = WiFiViewer()

    app.mainloop()


if __name__ == "__main__":
    main()
    