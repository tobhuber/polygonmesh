from random import Random

class Grid():
    def __init__(self, width, height, grid_width, variance):
        random = Random()
        random.seed()
        ratio = height / width 
        self.h = int (ratio * grid_width)
        self.w = grid_width
        self.box_w = int (width / grid_width)
        self.box_h = int (height / self.h)
        print(f"Ratio: {ratio}")
        print(f"Grid width: {self.w}")
        print(f"Grid height: {self.h}")
        self.grid = [
            [
                (
                    random.randrange(
                        x * self.box_w + int(variance * self.box_w), 
                        (x+1) * self.box_w - int(variance * self.box_w)
                    ), 
                    random.randrange(
                        y * self.box_h + int(variance * self.box_h), 
                        (y+1) * self.box_h - int(variance * self.box_h)
                    )
                ) 
                for x in range(self.w)] 
            for y in range(self.h)]
