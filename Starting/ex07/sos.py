import sys


def encode_to_morse(input_string):
    """
    Encode une chaîne de caractères en code Morse.

    Cette fonction prend une chaîne de caractères en entrée et la convertit en code Morse
    en utilisant un dictionnaire de correspondance. Les caractères alphanumériques sont
    pris en charge, ainsi que les espaces.

    Args:
        input_string (str): La chaîne de caractères à encoder en code Morse.

    Returns:
        str: La chaîne encodée en code Morse, où chaque caractère Morse est séparé par un espace,
             et les mots sont séparés par un slash.

    Raises:
        ValueError: Si un caractère non pris en charge est trouvé dans la chaîne d'entrée.
    """
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }

    input_string = input_string.upper()
    morse_code = []

    for char in input_string:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            raise ValueError(f"Le caractère '{char}' n'est pas pris en charge.")

    return ' '.join(morse_code)


def test_args():
    """
    Vérifie que les arguments fournis au programme sont corrects.

    Cette fonction vérifie que le programme a reçu exactement un argument en plus du nom du script,
    et que cet argument est une chaîne de caractères.

    Raises:
        AssertionError: Si le nombre d'arguments est incorrect ou si l'argument n'est pas une chaîne.
    """
    import sys
    if len(sys.argv) != 2:
        raise AssertionError("he arguments are bad")

    if not isinstance(sys.argv[1], str):
        raise AssertionError("he arguments are bad")


def main():
    """
    Fonction principale du programme qui encode une chaîne de caractères en code Morse.

    Cette fonction gère les arguments de la ligne de commande, vérifie leur validité,
    et encode la chaîne fournie en code Morse. Les erreurs sont capturées et affichées.
    """
    try:
        test_args()
        input_string = sys.argv[1]
        morse_result = encode_to_morse(input_string)
        print(morse_result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print(f"Erreur: {e}")
    except Exception as e:
        print(f"Erreur inattendue: {e}")


if __name__ == "__main__":
    main()