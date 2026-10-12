from PIL import Image, ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")


main()
