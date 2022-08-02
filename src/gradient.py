import numpy as np
from PIL import Image
class Gradient():

    # code modified from https://github.com/nkmk/python-snippets/blob/c1f8a97b5573c9daef9671845e8ee1269e806d27/notebook/numpy_generate_gradient_image.py
    def get_gradient_2d(self, start, stop, width, height, is_horizontal):
        if is_horizontal == None:
            horizontal = np.tile(np.linspace(start, stop, width), (height, 1))
            vertical = np.tile(np.linspace(start, stop, height), (width, 1)).T
            return [list(map(lambda xy: int((xy[0] + xy[1])/2), zip(horizontal[i], vertical[i]))) for i in range(len(horizontal))]
        elif is_horizontal:
            return np.tile(np.linspace(start, stop, width), (height, 1))
        else:
            return np.tile(np.linspace(start, stop, height), (width, 1)).T

    # code from https://github.com/nkmk/python-snippets/blob/c1f8a97b5573c9daef9671845e8ee1269e806d27/notebook/numpy_generate_gradient_image.py
    def get_gradient_3d(self, width, height, start_list, stop_list, is_horizontal_list):
        result = np.zeros((height, width, len(start_list)), dtype=float)

        for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
            result[:, :, i] = self.get_gradient_2d(start, stop, width, height, is_horizontal)

        return result

    def generate_gradient(self, width, height, start, stop):
        array = self.get_gradient_3d(width, height, start, stop, (False, None, True))
        return Image.fromarray(np.uint8(array))
