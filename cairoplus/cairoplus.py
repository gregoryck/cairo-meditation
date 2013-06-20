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

        # print device_x_start, device_y_start, device_x_end, device_y_end, scale_x, scale_y


        self.translate(device_x_start, device_y_start)
        self.scale(scale_x, scale_y)
        self.translate(-1 * new_x_range[0], -1 * new_y_range[0])
        yield
        self.restore()

    @contextmanager
    def source(self, source):
        self.save()
        self.set_source(source)
        yield
        self.restore()

    @contextmanager
    def source_rgb(self, r,g,b):
        self.save()
        self.set_source_rgb(r,g,b)
        yield
        self.restore()

    @contextmanager
    def source_rgba(self, r,g,b,a):
        self.save()
        self.set_source_rgba(r,g,b,a)
        yield
        self.restore()


    def quick_rect(self, x=(0,1), y=(0,1)):
        # super(Context, self).rectangle(0,0,1,1)
        self.rectangle(x[0],y[0],x[1]-x[0],y[1]-y[0])
        self.fill()

    def arrow(self, startx=0, endx=1):
        self.move_to(startx, 0)
        self.line_to(endx, 0.5)
        self.line_to(startx, 1)
        self.close_path()
        self.fill()

    def arrowed_rect(self, startx=0, endx=1, max_device_pixels=30):
        arrow_startx_0 = 0
        arrow_endx_0, end_y_0 = self.device_to_user_distance(max_device_pixels,0)
        if arrow_endx_0 > endx:
            self.arrow(startx, endx)
        else:
            arrow_offset = endx - arrow_endx_0
            arrow_startx, arrow_endx = arrow_startx_0 + arrow_offset, arrow_endx_0 + arrow_offset
            assert arrow_endx == endx, (arrow_endx, endx)
            self.quick_rect((startx, arrow_startx))
            self.arrow(arrow_startx, endx)
