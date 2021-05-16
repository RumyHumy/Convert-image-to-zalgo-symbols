from PIL import Image
import clipboard
while 1:
    image_path = input("Input a path to your image: ")
    image = Image.open(image_path)
    width = min(image.size[0], 100)
    height = min(image.size[1], 100)
    palette = [chr(781), chr(782)]
    pixels = image.load()
    text = '.'+'&#10;\n'*round(width/6)
    for x in range(width):
        for y in reversed(range(height)):
           col = pixels[x, y]
           mid = (col[0]+col[1]+col[2])/255/3*2
           text += palette[round(max(min(mid,1),0)*(len(palette)-1))]
        text += '.'
    clipboard.copy(text)
    print("Copied!\n")
