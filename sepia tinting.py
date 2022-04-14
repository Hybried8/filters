import tkinter

def Sepia_tinting(image: Image) -> Image:
    """ Returns new image with sepia tint. 
    If pixel components are 62 or below, blue components must be multiplied 0.9 and red components by 1.1. 
    If pixel components are 63 to 191, blue components must be multiplied 0.85 and red components by 1.15. 
    If pixel components are 192 or greater, blue components must be multiplied 0.93 and red components by 1.08.
    """
    
    image_sepia_tinting= copy(image)
    red = 0
    green = 0
    blue = 0
    for x, y, (r,g,b) in image:
       
        if ((r,g,b) <= 62):
            b *= 0.9
            r *= 1.1
        elif (63 <= (r,g,b) <= 191):
            b *= 0.85
            r *= 1.15
            
        elif ((r,g,b) >= 192):
            b = 0.93
            r = 1.08  
                    
        new_image = create_colour(red, green, blue)
        set_colour(image_sepia_tinting, x, y, new_image)
        
    return image_sepia_tinting

choose_image = choose_file()
image = load_image(choose_image) 
show(image)
show(Sepia_tinting(image)) 