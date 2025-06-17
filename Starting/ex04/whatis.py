import sys


def test_input_conversion(input_value):
    try:
        # Essayer de convertir l'entrée en un entier
        integer_value = int(input_value)
        print(f"Conversion réussie : {integer_value}")
    except ValueError:
        # Lever une AssertionError si la conversion échoue
        raise AssertionError("argument is not an integer")
    
def test_length_input():
    assert (sys.argv.__len__() < 2), "more than one argument is provided"


try:
    test_length_input()
    test_input_conversion(sys.argv[1])
    number = int(sys.argv[1]), 
    if (number):
        if (number % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
 
 
 