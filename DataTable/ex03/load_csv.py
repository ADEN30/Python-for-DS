from pandas import read_csv
from numpy import array


def load(path: str) -> array:
    """
    Charge un fichier CSV et le convertit en tableau NumPy.

    Cette fonction lit un fichier CSV sans en-tête, puis retourne les données
    sous forme de tableau NumPy. Elle affiche également les dimensions du jeu
    de données chargé.

    Parameters:
    ----------
    path : str
        Chemin vers le fichier CSV à charger.

    Returns:
    -------
    numpy.ndarray
        Tableau contenant les données du fichier CSV.

    Raises:
    ------
    Exception
        Affiche toute exception rencontrée lors de la lecture du fichier ou de la conversion.
    """
    try:
        file_list = read_csv(path, header=None).values
        file_array = array(file_list)
        print(f"Loading dataset of dimensions {file_array.shape}")
        return file_array
    except Exception as e:
        print(e)

