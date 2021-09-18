from PIL import Image, ImageColor


def generate():
    # Get base image type input
    icontype = input("Select Image Type [METALLIC, SHINY, DULL]: ")

    if icontype.casefold() == "METALLIC".casefold() or icontype.casefold() == "M".casefold():
        picture = Image.open("resources/base/metallic.png")
    elif icontype.casefold() == "SHINY".casefold() or icontype.casefold() == "S".casefold():
        picture = Image.open("resources/base/shiny.png")
    elif icontype.casefold() == "DULL".casefold() or icontype.casefold() == "D".casefold():
        picture = Image.open("resources/base/dull.png")
    else:
        picture = Image.open("resources/base/metallic.png")

    # Setup output image
    out = picture

    # Size of the image
    width, height = picture.size

    # Get color input
    c = input("Select Color (format 0xB4B478 OR #B4B478): ")
    if "0x" in c:
        c = "#" + c[2:].upper()
    elif "#" in c:
        c.upper()
    else:
        print("WRONG DATA FORMAT! Use '0x' or '#'!")
        return

    new_color = ImageColor.getcolor(c, "RGB")

    # Modify pixels
    for x in range(0, width):
        for y in range(0, height):
            # Get Current Pixel Color
            current_color = picture.getpixel((x, y))

            # Photoshop Overlay Algorithm
            average = int((current_color[0] + current_color[1] + current_color[2]) / 3)
            if average < 128:
                r = int((2 * current_color[0] * new_color[0]) / 255)
                g = int((2 * current_color[1] * new_color[1]) / 255)
                b = int((2 * current_color[2] * new_color[2]) / 255)

                loc = (r, g, b)
            else:
                r = int((1 - (2 * (1 - current_color[0]) * (1 - new_color[0]))) / 255) * -1
                g = int((1 - (2 * (1 - current_color[1]) * (1 - new_color[1]))) / 255) * -1
                b = int((1 - (2 * (1 - current_color[2]) * (1 - new_color[2]))) / 255) * -1

                loc = (r, g, b)

            out.putpixel((x, y), loc)

    # Write File
    out.save("output/" + icontype + "_" + c + ".png")
    return


run = 1
while True:
    generate()
    run = input("Run again? 0 to quit. ")
    if run != 0:
        break
