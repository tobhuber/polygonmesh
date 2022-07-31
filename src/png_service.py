from PIL import Image, ImageDraw
from random import Random

class PNGService():
    
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.image = Image.new("RGBA", (width, height), (255, 255, 255, 255))        # create new white image to draw on
        self.draw = ImageDraw.Draw(self.image)
    
    def generate_img(self, polygons, gradient, colorvariance, outline_intensity):
        random = Random()
        random.seed()
        for polygon in polygons:
            a, b, c = polygon
            center = (int((a[0] + b[0] + c[0]) / 3), int((a[1] + b[1] + c[1]) / 3))
            r = int(gradient.getpixel(center)[0] + colorvariance * random.randrange(-255,255))
            g = int(gradient.getpixel(center)[1] + colorvariance * random.randrange(-255,255))
            b = int(gradient.getpixel(center)[2] + colorvariance * random.randrange(-255,255))
            outline = gradient.getpixel((int(self.w/2), int(self.h/2)))
            self.draw.polygon(polygon, fill=(r, g, b), outline=(outline + (int(outline_intensity * 255),)))

        self.image.save("src/output/triangles.png")