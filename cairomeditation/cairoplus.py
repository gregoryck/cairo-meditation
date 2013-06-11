import cairo
from contextlib import contextmanager

WIDTH = 1000
HEIGHT = 1000


class Context(cairo.Context):


    def __init__(self, *arglist, **argdict):
        super(Context, self).__init__(*arglist, **argdict)

        #FIXME first in_box is in 1-1000 range; others are 0-1.0. What do I want?

    @contextmanager
    def fit(self, move_x, move_y, scale_x, scale_y):

        self.save()
        self.translate(move_x, move_y)
        self.scale(scale_x, scale_y)
        yield
        self.restore()

    @contextmanager
    def in_box(self, x_start, y_start, x_end, y_end, new_x_range=(0,1), new_y_range=(0,1)):
        self.save()
        device_x_start, device_y_start = self.user_to_device(x_start, y_start)
        device_x_end, device_y_end = self.user_to_device(x_end, y_end)

        desired_scale_x = new_x_range[1] - new_x_range[0]
        desired_scale_y = new_y_range[1] - new_y_range[0]
        scale_x = (device_x_end - device_x_start)  / (desired_scale_x * 1.0)
        scale_y = (device_y_end - device_y_start)  / (desired_scale_y * 1.0)
        self.identity_matrix()

        print device_x_start, device_y_start, device_x_end, device_y_end, scale_x, scale_y


        self.translate(device_x_start, device_y_start)
        self.scale(scale_x, scale_y)
        self.translate(-1 * new_x_range[0], -1 * new_y_range[0])
        yield
        self.restore()

    def quick_rect(self):
        # super(Context, self).rectangle(0,0,1,1)
        self.rectangle(0,0,1,1)
        self.fill()


