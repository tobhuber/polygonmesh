from random import Random

class Grid():
    def __init__(self, width, height, grid_width, variance):
        random = Random()
        random.seed()
        ratio = height / width 
        self.h = int(round(ratio * grid_width))
        self.w = grid_width
        self.box_w = width / grid_width
        self.box_h = height / self.h
        self.grid = [
            [
                (
                    random.randrange(
                        int(round(x * self.box_w + variance * self.box_w)), 
                        int(round((x+1) * self.box_w - variance * self.box_w))
                    ), 
                    random.randrange(
                        int(round(y * self.box_h + variance * self.box_h)), 
                        int(round((y+1) * self.box_h - variance * self.box_h))
                    )
                ) 
                for x in range(self.w)] 
            for y in range(self.h)]
