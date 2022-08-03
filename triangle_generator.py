import argparse
from PIL import Image, ImageColor
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
parser.add_argument("--outline-intensity", help="intensity of the polygon outline [0,1] (only supported for .png files)", type=float)
parser.add_argument("--out", default="svg", help="defines the output type [png,svg]", type=str)
parser.add_argument("--print-outline", default=False, help="whether to print polygone outline or not", type=bool)
parser.add_argument("--color-list", default=[], nargs='+', help="list of colors to generate a picture for each possible tuple")
parser.add_argument("--input", default=None, help="use input picture instead of generating gradient, colors will be ignored", type=str)
args = parser.parse_args()

width = args.width
height = args.height
grid_width = args.grid
variance = args.variance
colorvariance = args.color_variance
outline_intensity = args.outline_intensity
output_type = args.out
outline = args.print_outline
input = args.input
color_list = [(ImageColor.getcolor(a, "RGB"), ImageColor.getcolor(b, "RGB")) for a in args.color_list for b in args.color_list if a != b]
if input:
    color_list = [("", ""), ("", "")]
print(f"Printing {len(color_list)} pictures")
count = 0
for tuple in color_list:
    start, stop = tuple   
    grid = Grid(width=width, height=height, grid_width=grid_width, variance=variance)
    if not input:
        background = Gradient().generate_gradient(width=width, height=height, start=start, stop=stop)
    else: 
        background = Image.open(input)
        width = background.width
        height = background.height
        start = "None"
        stop = "None"
    polygons = PolygonService().generate_polygons(grid, width, height)

    if output_type == "png":
        PNGService(
            width=width, 
            height=height
        ).generate_img(
            polygons=polygons,
            gradient=background,
            colorvariance=colorvariance,
            print_outline=outline,
            outline_intensity=outline_intensity,
            name=f"src/output/rgb{start}_to_rgb{stop}.png"
            )
    if output_type == "svg":
        SVGService(
            width=width, 
            height=height
        ).generate_img(
            polygons=polygons, 
            gradient=background, 
            colorvariance=colorvariance, 
            print_outline=outline,
            name=f"src/output/rgb{start}_to_rgb{stop}.svg"
        )
    count += 1
    print(f"{count}/{len(color_list)}")
