import svgwrite
from random import Random

class SVGService():

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.draw = svgwrite.Drawing("triangles.svg")

    def generate_img(self, polygons, gradient, colorvariance, outline_intensity):
        random = Random()
        random.seed()
        for polygon in polygons:
            a, b, c = polygon
            points = [[a[0], a[1]], [b[0], b[1]], [c[0], c[1]]]
            poly = svgwrite.shapes.Polygon(points=points)
            center = (int((a[0] + b[0] + c[0]) / 3), int((a[1] + b[1] + c[1]) / 3))
            r = int(gradient.getpixel(center)[0] + colorvariance * random.randrange(-255,255))
            g = int(gradient.getpixel(center)[1] + colorvariance * random.randrange(-255,255))
            b = int(gradient.getpixel(center)[2] + colorvariance * random.randrange(-255,255))
            outline = gradient.getpixel((int(self.w/2), int(self.h/2)))
            poly.fill(f"rgb({r}, {g}, {b})").stroke(f"rgb({outline[0]}, {outline[1]}, {outline[2]})")
            self.draw.add(poly)
            self.draw.saveas("src/output/triangles.svg")