from PIL import Image
from numpy import array

def ft_load(path: str) -> list:
    try:
        with Image.open(path) as img:
            print(img.format)
            img_array = array(img, copy=True)
            print(type(img_array))
            print(img_array.shape)
            print(img_array) 
    except Exception as e:
        print(e)