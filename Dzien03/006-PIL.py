from PIL import Image, ImageDraw, ImageFont, ImageFilter

image = Image.open("../extras/pasek.jpg")
font = ImageFont.truetype("../extras/trebuc.ttf", 44)

text = "Python jest SUPER!"
draw = ImageDraw.Draw(image)
draw.text( (200,500), text, font=font, fill="white" )

image.save("wynik.jpg")

blurred = image.filter(ImageFilter.BLUR)
blurred.save("blur.jpg")

# #https://pillow.readthedocs.io/en/4.2.x/handbook/concepts.html#concept-modes
grayed = image.convert("L")

grayed = grayed.rotate(40)
#grayed.show()

# miniaturki
import glob, os
files = glob.glob("../Dzien02/images/**/*.jpg", recursive=True)
for file in files:
    file_name, ext = os.path.splitext(file)
    print(file_name,ext)

    with Image.open(file) as im:
        im.thumbnail( (400,200) )
        im.save(file+"-thumbnail"+ext)

