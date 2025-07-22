from numpy import array as np_array

def ft_invert(lst):
    """
    Inverse les couleurs d'une image représentée par une liste.

    Cette fonction prend une liste représentant une image et retourne
    un nouveau tableau où chaque valeur de pixel est inversée par rapport à 255.

    Parameters:
    lst (list): Une liste qui represente l'image.

    Returns:
    numpy.ndarray: Un tableau NumPy avec les couleurs inversées.
    """
    lst = np_array(lst)
    inverted_array = 255 - lst
    return inverted_array

def ft_red(lst):
    """
    Conserve uniquement le canal rouge d'une image représentée par une liste.

    Cette fonction prend une liste représentant une image et retourne
    un nouveau tableau où seuls les canaux rouges sont conservés, les autres étant mis à 0.

    Parameters:
    lst (list): Une liste qui represente l'image.

    Returns:
    numpy.ndarray: Un tableau NumPy avec uniquement le canal rouge.
    """
    red_array = np_array(lst)
    red_array[:, :, 1] = 0
    red_array[:, :, 2] = 0
    return red_array

def ft_green(lst):
    """
    Conserve uniquement le canal vert d'une image représentée par une liste.

    Cette fonction prend une liste représentant une image et retourne
    un nouveau tableau où seuls les canaux verts sont conservés, les autres étant inversés.

    Parameters:
    lst (list): Une liste qui represente l'image.

    Returns:
    numpy.ndarray: Un tableau NumPy avec uniquement le canal vert.
    """
    green_array = np_array(lst)
    green_array[:, :, 0] = 255 - green_array[:, :, 0]
    green_array[:, :, 2] = 255 - green_array[:, :, 2]
    return green_array

def ft_blue(lst):
    """
    Conserve uniquement le canal bleu d'une image représentée par une liste.

    Cette fonction prend une liste représentant une image et retourne
    un nouveau tableau où seuls les canaux bleus sont conservés, les autres étant mis à 0.

    Parameters:
    lst (list): Une liste qui represente l'image.

    Returns:
    numpy.ndarray: Un tableau NumPy avec uniquement le canal bleu.
    """
    blue_array = np_array(lst)
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    return blue_array

def ft_grey(lst):
    """
    Convertit une image en niveaux de gris.

    Cette fonction prend une liste représentant une image et retourne
    un nouveau tableau où chaque pixel est converti en niveaux de gris en calculant
    la moyenne des valeurs des canaux RVB.

    Parameters:
    lst (list): Une liste qui represente l'image.

    Returns:
    numpy.ndarray: Un tableau NumPy représentant l'image en niveaux de gris.
    """
    grey_array = np_array(lst)
    grey_values = (grey_array[:, :, 0] + grey_array[:, :, 1] + grey_array[:, :, 2]) // 3
    grey_array[:, :, 0] = grey_values
    grey_array[:, :, 1] = grey_values
    grey_array[:, :, 2] = grey_values
    return grey_array