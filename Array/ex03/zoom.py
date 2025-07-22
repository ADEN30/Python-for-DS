from load_image import ft_load
from PIL import Image
from numpy import array, uint8
from matplotlib.pyplot import imshow, show


def img_print(img):
    print(img.shape)
    print(img)

def zoom(pixel_array: list):
    pixel_numpy = array(pixel_array, dtype=uint8)
    img_print(pixel_numpy)
    
    img = Image.fromarray(pixel_numpy)
    greyscale_img = img.convert('L')
    
    cropped_img = greyscale_img.crop((450, 100, 850, 500 ))
    img_print(array(cropped_img, dtype=uint8))
    imshow(cropped_img, cmap='gray')
    show()
    

def main():
    pixel_array = ft_load('./animal.jpeg')
    
    zoom(pixel_array)
    
if __name__ == "__main__":
    main()