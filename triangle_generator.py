import argparse
from PIL import ImageColor
from src.gradient import Gradient
from src.grid import Grid
from src.png_service import PNGService
from src.svg_service import SVGService
from src.gradient import Gradient
from src.polygon_service import PolygonService

parser = argparse.ArgumentParser()
parser.add_argument("--width", help="width of the picture in pixel", type=int)
parser.add_argument("--height", help="height of the picture in pixel", type=int)
parser.add_argument("--grid", default=28, help="grid size", type=int)
parser.add_argument("--variance", default=0.2, help="how uniform the triangles are [0,0.5)", type=float)
parser.add_argument("--color-variance", default=0, help="how funky the colors get [0,1]", type=float)
parser.add_argument("--gradient-from", help="start color for gradient in hex", type=str)
parser.add_argument("--gradient-to", help="stop color for gradient in hex", type=str)
parser.add_argument("--outline-intensity", help="intensity of the polygon outline [0,1] (only supported for .png files)", type=float)
parser.add_argument("--out", default="svg", help="defines the output type [png,svg]", type=str)
args = parser.parse_args()

width = args.width
height = args.height
grid_width = args.grid
variance = args.variance
colorvariance = args.color_variance
start_color = ImageColor.getcolor(args.gradient_from, "RGB")
end_color = ImageColor.getcolor(args.gradient_to, "RGB")
outline_intensity = args.outline_intensity
output_type = args.out

grid = Grid(width=width, height=height, grid_width=grid_width, variance=variance)
gradient = Gradient().generate_gradient(width=width, height=height, start=start_color, stop=end_color)
polygons = PolygonService().generate_polygons(grid, width, height)

if output_type == "png":
    PNGService(width=width, height=height).generate_img(polygons=polygons, gradient=gradient, colorvariance=colorvariance, outline_intensity=outline_intensity)
if output_type == "svg":
    SVGService(width=width, height=height).generate_img(polygons=polygons, gradient=gradient, colorvariance=colorvariance, outline_intensity=outline_intensity)
