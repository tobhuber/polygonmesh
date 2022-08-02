# Gradientmesh
Python Script to generate colorful triangle mesh

## Usage
### Installation
Clone this repository and make sure all requirements are fulfilled.
These are: 

- NumPy
- argparse
- random
- PIL
- svgwrite

### How to use it
run `python triangle_generator.py --help` to view all available parameter.
Example command: 
```
 python triangle_generator.py --width 2000 --heigh 600 --grid 40 --variance 0.2 --color-variance 0.01 --outline-intensity 1 --out "png" --color-list "#004192" "#0d82cc" "#0f95fc" "#28cce8" "#e7f4ff" "#d60600"
```

![Fade from #0049e6 to #018506](https://github.com/tobhuber/polygonmesh/blob/main/triangles.png)
