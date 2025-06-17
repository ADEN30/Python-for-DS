import sys

from ft_filter import ft_filter

def main():
    # Vérification du nombre d'arguments
    try:
        test_args()
        S = sys.argv[1]
        N = int(sys.argv[2])
        result = ft_filter(lambda word: len(word) > N, S.split())
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


def test_args():
    """_summary_
        Just check if args is != 3
    Args:
        agrs (_type_): lists of args
    throw AssertionError if args length != 3
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    
        # Récupération des arguments
    try:
        int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

if __name__ == "__main__":
    # Exécution du programme principal
    main()