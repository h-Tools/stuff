from PIL import Image
image = []
dot = 0
line = 0
colour = 0
dot2 = 0
sizeX = int(input('Length of image (X)? '))
sizeY = int(input('Height of image (Y)? '))
for y in range(sizeY):
    line += 1
    colour = line*-1
    dot = line*-3
    for x in range(sizeX):
        dot += 1
        colour += 1
        rgb = (255,255,255)
        for j in range (-1, 2): # Goes through the various adjecent tiles
            for i in range (-1, 2):
                dot2 = dot + 4*i + j
                colour2 = colour + 3*i + j
                if (j == 0 and (i == -1 or i == 1)) == False: # Makes sure the tile is not above or below a H's center
                    if dot2 % 7 == 0: # Checks if the tile is the center of a H
                        if colour2 % 4 == 0:
                            rgb = (255,153,170)
                        elif colour2 % 4 == 1:
                            rgb = (81,233,244)
                        elif colour2 % 4 == 2:
                            rgb = (126,237,86)
                        elif colour2 % 4 == 3:
                            rgb = (255,214,53)
                        break
        image.extend(rgb)
image=bytes(image)
img = Image.frombytes('RGB', (sizeX,sizeY), image)
img.save('h.png')
img.show()

