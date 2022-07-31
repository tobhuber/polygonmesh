class PolygonService():

    def generate_polygons(self, grid, width, height):
        core = self._generate_core(grid)
        top = self._generate_top_edge(grid, width)
        left = self._generate_left_edge(grid, height)
        right = self._generate_right_edge(grid, width, height)
        bottom = self._generate_bottom_edge(grid, width, height)
        return top + left + core + right + bottom

    def _generate_core(self, grid):
        core_polygons = []
        for x in range(grid.w - 1):
            for y in range(grid.h -1):
                core_polygons.append([grid.grid[y][x], grid.grid[y][x+1], grid.grid[y+1][x+1]])
                core_polygons.append([grid.grid[y][x], grid.grid[y+1][x], grid.grid[y+1][x+1]])
        return core_polygons

    def _generate_left_edge(self, grid, height): 
        left_edge_polygons = []
        for y in range(grid.h - 1):
            left_edge_polygons.append([
                (0, y * grid.box_h),
                (0, (y + 1) * grid.box_h),
                grid.grid[y][0]
            ])
            left_edge_polygons.append([
                (0, (y + 1) * grid.box_h),
                grid.grid[y][0],
                grid.grid[y + 1][0]
            ])
        left_edge_polygons.append([
            (0, (grid.h - 1) * grid.box_h),
            (0, height),
            grid.grid[grid.h - 1][0]
        ])
        return left_edge_polygons

    def _generate_right_edge(self, grid, width, height):
        right_edge_polygons = []
        for y in range(grid.h - 1):
            right_edge_polygons.append([
                (width, y * grid.box_h),
                (width, (y + 1) * grid.box_h),
                grid.grid[y][grid.w - 1]
            ])
            right_edge_polygons.append([
                (width, (y + 1) * grid.box_h),
                grid.grid[y][grid.w - 1],
                grid.grid[y + 1][grid.w - 1]
            ])
        right_edge_polygons.append([
            (width, (grid.h - 1) * grid.box_h),
            (width, height),
            grid.grid[grid.h - 1][grid.w - 1]
        ])
        return right_edge_polygons
    
    def _generate_top_edge(self, grid, width):
        top_edge_polygons = []
        for x in range(grid.w - 1):
            top_edge_polygons.append([
                (x * grid.box_w, 0),
                ((x + 1) * grid.box_w, 0),
                grid.grid[0][x]
            ])
            top_edge_polygons.append([
                ((x + 1) * grid.box_w, 0),
                grid.grid[0][x],
                grid.grid[0][x + 1]
            ])
        top_edge_polygons.append([
            ((grid.w - 1) * grid.box_w, 0),
            (width, 0),
            grid.grid[0][grid.w - 1]
        ])
        return top_edge_polygons

    def _generate_bottom_edge(self, grid, width, height):
        bottom_edge_polygons = []
        for x in range(grid.w - 1):
            bottom_edge_polygons.append([
                (x * grid.box_w, height),
                ((x + 1) * grid.box_w, height),
                grid.grid[grid.h - 1][x]
            ])
            bottom_edge_polygons.append([
                ((x + 1) * grid.box_w, height),
                grid.grid[grid.h - 1][x],
                grid.grid[grid.h - 1][x + 1]
            ])
        bottom_edge_polygons.append([
            ((grid.w - 1) * grid.box_w, height),
            (width, height),
            grid.grid[grid.h - 1][grid.w - 1]
        ])
        return bottom_edge_polygons