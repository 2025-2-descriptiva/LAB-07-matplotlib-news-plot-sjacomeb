"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    # Leer el archivo CSV
    df = pd.read_csv("files/input/news.csv", index_col=0)

    plt.figure()

    #Define colores de las lineas
    colors = {
        "Newspaper": "grey",
        "Television": "dimgray",
        "Radio": "Lightgrey",
        "Internet": "tab:blue",
    }

    #Define orden de las lineas
    zorder = {
        "Newspaper": 1,
        "Television": 1,
        "Radio": 1,
        "Internet": 2,
    }

    #Define grosor de las lineas
    linewidths = {
        "Newspaper": 2,
        "Television": 2,
        "Radio": 2,
        "Internet": 3,
    }

    for col in df.columns:
        plt.plot(
            df[col], 
            color = colors[col],
            label=col,
            zorder = zorder[col],
            linewidth = linewidths[col],
        )

        first_year = df.index[0]
        plt.scatter(
            x = first_year, 
            y = df[col][first_year],
            color = colors[col],
            zorder = zorder[col],
        )

        plt.text(
            first_year - 0.2, 
            df[col][first_year],    
            col + " "+ str(df[col][first_year]) + "%",
            color = colors[col],
            va = "center", #alineacion vertical
            ha = "right", #alineacion horizontal
        )
            
        last_year = df.index[-1]
        plt.scatter(
            x = last_year, 
            y = df[col][last_year],
            color = colors[col],
            zorder = zorder[col],
        )

        plt.text(
            last_year + 0.2, 
            df[col][last_year],    
            str(df[col][last_year]) + "%",
            color = colors[col],
            va = "center",
            ha = "left",
        )
    
    plt.xticks(
        ticks=df.index,
        labels = df.index,
        ha = "center",
    )

    plt.title("How people get their news", fontsize = 16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)    
    plt.gca().spines['left'].set_visible(False) 
    plt.gca().axes.get_yaxis().set_visible(False)   
    #plt.show()

     #Creo la carpeta plots si no existe
    os.makedirs("files/plots", exist_ok=True)
    # guardo el grafico en el archivo indicado
    plt.savefig("files/plots/news.png")
    plt.close()


if __name__ == "__main__":
    pregunta_01()