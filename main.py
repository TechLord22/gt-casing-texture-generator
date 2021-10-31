from PIL import Image, ImageColor


def generate():
    # Get base image type input
    material_icon_type = input('Select Material Icon Set [METALLIC, SHINY, DULL]: ')

    if material_icon_type == 'M'.casefold():
        material_icon_type = 'METALLIC'
    elif material_icon_type == 'S'.casefold():
        material_icon_type = 'SHINY'
    elif material_icon_type == 'D'.casefold():
        material_icon_type = 'DULL'

    if material_icon_type.casefold() == 'METALLIC'.casefold():
        picture = Image.open('resources/base/metallic.png')
    elif material_icon_type.casefold() == "SHINY".casefold():
        picture = Image.open('resources/base/shiny.png')
    elif material_icon_type.casefold() == "DULL".casefold():
        picture = Image.open('resources/base/dull.png')
    else:
        print(f'Invalid Material Icon Set: {material_icon_type}')
        return 0

    # Setup output image
    output = picture

    # Size of the image
    width, height = picture.size

    # Get color input
    color = input('Select Color (format 0xB4B478 OR #B4B478): ')
    if '0x' in color[:2]:
        color = '#' + color[2:].upper()
    elif '#' == color[0]:
        color.upper()
    else:
        print("WRONG DATA FORMAT! Use '0x' or '#'!")
        return 0

    file_name = str(color)
    color = ImageColor.getcolor(color, 'RGB')

    # Modify pixels
    for x in range(width):
        for y in range(height):
            # Get Current Pixel Color
            current_color = picture.getpixel((x, y))

            # Photoshop Overlay Algorithm
            average = int((current_color[0] + current_color[1] + current_color[2]) / 3)
            if average < 128:
                r = int((2 * current_color[0] * color[0]) / 255)
                g = int((2 * current_color[1] * color[1]) / 255)
                b = int((2 * current_color[2] * color[2]) / 255)
                loc = (r, g, b)
            else:
                r = int((1 - (2 * (1 - current_color[0]) * (1 - color[0]))) / 255) * -1
                g = int((1 - (2 * (1 - current_color[1]) * (1 - color[1]))) / 255) * -1
                b = int((1 - (2 * (1 - current_color[2]) * (1 - color[2]))) / 255) * -1
                loc = (r, g, b)

            output.putpixel((x, y), loc)

    # Write File
    output.save('output/' + material_icon_type + '_' + file_name + '.png')

    # Increment amount files written counter
    return 1


run = 1
totalWritten = 0
while True:
    totalWritten += generate()
    run = int(input('Run again? 0 to quit. '))
    if run == 0:
        break

print(f'Complete! Written {totalWritten} files to output')
