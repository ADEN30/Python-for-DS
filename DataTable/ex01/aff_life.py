from matplotlib.pyplot import subplots, show
from load_csv import load
from numpy import array


def draw_graph(data: array, x_label: str, y_label: str, title: str):
    """
    Affiche une courbe à partir d'un tableau NumPy 2D.

    Cette fonction trace une courbe en utilisant :
    - la première ligne (`data[0, 1:]`) comme valeurs pour l'axe x,
    - la ligne 59 (`data[59, 1:]`) comme valeurs pour l'axe y.

    Elle ajoute les labels et le titre au graphique, puis l'affiche.

    Parameters
    ----------
    data : numpy.array
        Tableau 2D contenant les données. Les colonnes 1 à N sont utilisées pour le tracé.
    x_label : str
        Texte pour l'axe des abscisses.
    y_label : str
        Texte pour l'axe des ordonnées.
    title : str
        Titre du graphique.

    Returns
    -------
    None
    """
    fig, ax = subplots()
    ax.plot(data[0 , 1:], data[59 , 1:])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    show()
    

def main():
    data = load("life_expectancy_years.csv")
    draw_graph(data, "Year", "Life expectancy", "France Life expectancy Projections")



if __name__ == "__main__":
    main()