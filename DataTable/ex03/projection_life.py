from load_csv import load
from matplotlib.pyplot import subplots, show, xscale
from numpy import array, where
from matplotlib.ticker import MultipleLocator, FuncFormatter

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

def filter_year(data: array, year: int):
    result = where(data == year)
    position = list(zip(result[0], result[1]))
    column = position[0][1]
    result = data[:, column]
    print(result)
    return (data[:, column])

def main():
    inflation_numpy = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    inflation_1900 = filter_year(inflation_numpy, 1900)

    life_numpy = load("life_expectancy_years.csv")
    life_1900 = filter_year(life_numpy, 1900)

    fig, ax = subplots()
    ax.scatter(inflation_1900, life_1900)

    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.set_ylim(top=55, bottom=18)
    ticks = [20, 25, 30, 35, 40, 45, 50, 55]
    ax.set_yticks(ticks)



    xscale('log')

    ax.set_xlim(right=10000, left=300)

    # Forcer les ticks à inclure 300
    ticks = [300, 1000, 10000]
    ax.set_xticks(ticks)
    ax.xaxis.set_major_formatter(FuncFormatter(format_number))

    show()


if __name__ == "__main__":
    main()