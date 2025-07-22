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
    width, height = cropped_img.size
    zoom_width = 1
    zoom_height = 1
    zoom_img = cropped_img.resize((int(width * zoom_width), int(height * zoom_height)), Image.LANCZOS)
    zoom_img = zoom_img.rotate(angle=90, expand=True)
    img_print(array(zoom_img, dtype=uint8))
    imshow(zoom_img, cmap='gray')
    show()
    

def main():
    pixel_array = ft_load('./animal.jpeg')
    
    zoom(pixel_array)
    
if __name__ == "__main__":
    main()