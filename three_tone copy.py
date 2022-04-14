def three_tone(input_image: Image, colourset: str) -> Image:
    """
    This function changes image into three colors based on the pixel brightness.

    >>> three_tone(original_image, black, gray, white)
    >>> Color(red=0, green=0, blue=0)
    """
   
    if colourset == '1':
        colour1 = name_value("black")
        colour2 = name_value("gray")
        colour3 = name_value("white")
    elif colourset == '2':
        colour1 = name_value("blue")
        colour2 = name_value("green")
        colour3 = name_value("blood")
    elif colourset == '3':
        colour1 = name_value("magenta")
        colour2 = name_value("cyan")
        colour3 = name_value("lemon")        
 
    output_image = copy(input_image)        
 
    for pixel in output_image:        
        x, y, (r, g, b) = pixel
        brightness = (r + g + b) / 3
       
        if brightness <= 84:                       
            set_color(output_image, x, y, colour1)    
       
        elif 84 < brightness < 170:                
            set_color(output_image, x, y, colour2)    
       
        else:                                             
            set_color(output_image, x, y, colour3)    
   
    return output_image     
