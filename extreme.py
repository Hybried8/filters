

from tkinter import *

def extreme_contrast(image: Image) -> Image:
    """Returns a copy of an image with extreme contrast. If the components value is between 0
    and 127, the components value is changed to 0. If the value is between 128 and 255, the 
    value is changed to 255.
       """
    
    new_image = copy(image)
    red = 0
    green = 0
    blue = 0
    for x, y, (r,g,b) in image:
        
        if r >= 0 and r <= 127:
            red = 0
        else:
            red = 255        
        
        if g >= 0 and g <= 127:
            green = 0
        else:
            green = 255
        
        if b >= 0 and b <= 127:
            blue = 0
        else:
            blue = 255
      
        contrast_image = create_color(red, green, blue)
        set_color(new_image, x, y, contrast_image)
       
    return new_image


selection = choose_file()
image = load_image(selection)
show(extreme_contrast(image))

    
 
