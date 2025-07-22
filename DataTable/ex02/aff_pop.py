from matplotlib.pyplot import subplots, show
import matplotlib.ticker as ticker

from load_csv import load
from numpy import array, where


def parse_number(s):
    """
    Convertit une chaîne avec suffixe K, M, B en un nombre.

    Exemples :
    - '56.3K' -> 56300
    - '20M'-> 20000000
    - '1.5K'-> 1500
    - '500'-> 500 
    """
    multipliers = {'K': 1e3, 'M': 1e6, 'B': 1e9}
    s = str(s).upper().replace(',', '')
    return float(s[:-1]) * multipliers[s[-1]] if s[-1] in multipliers else float(s)


def format_number(num, pos):
    """
    Convertit un nombre en chaîne avec suffixe K, M, B.

    Exemples :
    - 56300     -> '56.3K'
    - 20000000  -> '20M'
    - 1500      -> '1.5K'
    - 500       -> '500'
    """
    abs_num = abs(num)
    if abs_num >= 1e9:
        formatted = f"{num / 1e9:.1f}B"
    elif abs_num >= 1e6:
        formatted = f"{num / 1e6:.1f}M"
    elif abs_num >= 1e3:
        formatted = f"{num / 1e3:.1f}K"
    else:
        return str(num)
    
    # Supprimer le .0 final si présent (ex: 20.0M -> 20M)
    if formatted.endswith('.0B') or formatted.endswith('.0M') or formatted.endswith('.0K'):
        formatted = formatted[:-3] + formatted[-1]
    
    return formatted


def position_of_country_in_array_column(tab:array, treasure) -> int:
    """
    Trouve l'index de la colonne de la première occurrence exacte d'une valeur dans un tableau NumPy 2D.

    Parameters
    ----------
    tab : numpy.array
        Tableau 2D dans lequel effectuer la recherche.
    treasure : str or int or float
        Valeur exacte à rechercher.

    Returns
    -------
    int
        Index de la colonne où la première occurrence de `treasure` est trouvée.

    Raises
    ------
    ValueError
        Si la valeur n'est pas trouvée dans le tableau.
    """
    # Trouver exactement "France"
    result = where(tab == treasure)

    # Convertir les résultats en (ligne, colonne)
    positions = list(zip(result[0], result[1]))
    if not positions:
        raise ValueError(f"'{treasure}' n'a pas été trouvé dans le tableau.")
    return((positions[0][0]))


def draw_graph(data: array, x_label: str, y_label: str, title: str, item1, item2):
    """
    Affiche deux courbes représentant l'évolution de deux pays à partir d'un tableau NumPy 2D.

    Cette fonction trace deux courbes :
    - Les abscisses (x) sont les valeurs de la première ligne du tableau (généralement les années).
    - Les ordonnées (y) sont les valeurs associées à deux pays différents, spécifiés par `item1` et `item2`.
    - Les valeurs textuelles comme "56.3M" sont converties en nombres pour être affichées correctement.

    Les courbes sont affichées sur le même graphique avec une légende placée en bas à droite du graphique.
    L'axe des ordonnées commence à 0 et affiche les valeurs en millions avec le suffixe "M".

    Parameters
    ----------
    data : numpy.array
        Tableau 2D contenant les données, incluant la ligne des années et les lignes des pays.
    x_label : str
        Titre de l'axe des abscisses.
    y_label : str
        Titre de l'axe des ordonnées.
    title : str
        Titre principal du graphique.
    item1 : str
        Nom exact du premier pays à afficher.
    item2 : str
        Nom exact du second pays à afficher.

    Returns
    -------
    None
        La fonction affiche le graphique à l'écran.
    """
    fig, ax = subplots()
    try:
        item1_position = position_of_country_in_array_column(data, item1)
        item2_position = position_of_country_in_array_column(data, item2)
    except Exception as e:
        print(e)
    x = data[0 , 1:250]
    y1 = data[item1_position , 1:250]
    y2 = data[item2_position , 1:250]
    y1_clean = [parse_number(val) for val in y1]
    y2_clean = [parse_number(val) for val in y2]
    ax.plot(x, y1_clean, color='green', label=item1)
    ax.plot(x, y2_clean, color='blue', label=item2)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    
    ax.set_ylim(bottom=0)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    # Pas de 20 millions sur l'axe des y
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20_000_000))
    # Formatter pour afficher 20M, 40M, ...
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_number))
    ax.legend(loc='lower right', frameon=True)
    show()


def main():
    data = load("population_total.csv")
    draw_graph(data, "Year", "Population", "Population Projections", "France", "Belgium")


if __name__ == "__main__":
    main()