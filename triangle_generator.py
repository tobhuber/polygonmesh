import argparse
from PIL import Image, ImageDraw, ImageColor
import random
import numpy as np

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result

parser = argparse.ArgumentParser()
parser.add_argument("--width", help="width of the picture in pixel", type=int)
parser.add_argument("--height", help="height of the picture in pixel", type=int)
parser.add_argument("--grid", default=28, help="grid size", type=int)
parser.add_argument("--variance", default=1, help="how uniform the triangles are [0,0.5)", type=float)
parser.add_argument("--color-variance", default=0, help="how funky the colors get [0,1]", type=float)
parser.add_argument("--gradient-from", help="start color for gradient in hex")
parser.add_argument("--gradient-to", help="stop color for gradient in hex")
parser.add_argument("--outline-intensity", help="intensity of the polygon outline [0,1]", type=float)
args = parser.parse_args()

width = args.width
height = args.height
grid_width = args.grid
variance = args.variance
colorvariance = args.color_variance
start_color = ImageColor.getcolor(args.gradient_from, "RGB")
end_color = ImageColor.getcolor(args.gradient_to, "RGB")
outline_intensity = args.outline_intensity

array = get_gradient_3d(width, height, start_color, end_color, (False, True, True))
gradient = Image.fromarray(np.uint8(array))
image = Image.new("RGBA", (width, height), (255, 255, 255, 255))        # create new white image to draw on
draw = ImageDraw.Draw(image)

# calculate grid
random = random.Random()
random.seed()
ratio = height / width 
grid_height = int (ratio * grid_width)
box_width = int (width / grid_width)
box_height = int (height / grid_height)
print(f"Ratio: {ratio}")
print(f"grid_width: {grid_width}")
print(f"grid_height: {grid_height}")
grid = [
    [
        (
            random.randrange(
                x * box_width + int(variance * box_width), 
                (x+1) * box_width - int(variance * box_width)
            ), 
            random.randrange(
                y * box_height + int(variance * box_height), 
                (y+1) * box_height - int(variance * box_height)
            )
        ) 
        for x in range(grid_width)] 
    for y in range(grid_height)]

# draw triangles
polygons = []

# core polygons
for x in range(grid_width - 1):
    for y in range(grid_height -1):
        polygons.append([grid[y][x], grid[y][x+1], grid[y+1][x+1]])
        polygons.append([grid[y][x], grid[y+1][x], grid[y+1][x+1]])
# left edge
for y in range(grid_height - 1):
    polygons.append([
        (0, y * box_height),
        (0, (y + 1) * box_height),
        grid[y][0]
    ])
    polygons.append([
        (0, (y + 1) * box_height),
        grid[y][0],
        grid[y + 1][0]
    ])
polygons.append([
    (0, (grid_height - 1) * box_height),
    (0, height),
    grid[grid_height - 1][0]
])
# top edge
for x in range(grid_width - 1):
    polygons.append([
        (x * box_width, 0),
        ((x + 1) * box_width, 0),
        grid[0][x]
    ])
    polygons.append([
        grid[0][x],
        grid[0][x + 1],
        ((x + 1) * box_width, 0)
    ])
polygons.append([
    ((grid_width - 1) * box_width, 0),
    (width, 0),
    grid[0][grid_width - 1]
])
# right edge
for y in range(grid_height - 1):
    polygons.append([
        (width, y * box_height),
        (width, (y + 1) * box_height),
        grid[y][grid_width - 1]
    ])
    polygons.append([
        (width, (y + 1) * box_height),
        grid[y][grid_width - 1],
        grid[y + 1][grid_width - 1]
    ])
polygons.append([
    (width, (grid_height - 1) * box_height),
    (width, height),
    grid[grid_height - 1][grid_width - 1]
])
# bottom edge
for x in range(grid_width - 1):
    polygons.append([
        (x * box_width, height),
        ((x + 1) * box_width, height),
        grid[grid_height - 1][x]
    ])
    polygons.append([
        grid[grid_height - 1][x],
        grid[grid_height - 1][x + 1],
        ((x + 1) * box_width, height)
    ])
polygons.append([
    ((grid_width - 1) * box_width, height),
    (width, height),
    grid[grid_height - 1][grid_width - 1]
])

# calculate triangle colors

for polygon in polygons:
    a, b, c = polygon
    center = (int((a[0] + b[0] + c[0]) / 3), int((a[1] + b[1] + c[1]) / 3))
    r = int(gradient.getpixel(center)[0] + colorvariance * random.randrange(-255,255))
    g = int(gradient.getpixel(center)[1] + colorvariance * random.randrange(-255,255))
    b = int(gradient.getpixel(center)[2] + colorvariance * random.randrange(-255,255))
    outline = gradient.getpixel((int(width/2), int(height/2)))
    draw.polygon(polygon, fill=(r, g, b), outline=(outline + (int(outline_intensity * 255),)))

image.save("triangles.png")
