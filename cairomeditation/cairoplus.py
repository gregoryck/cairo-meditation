import cairo
from contextlib import contextmanager

def rectangle(ctx):
    ctx.rectangle(0,0,10,10)
    ctx.fill()

rectangle(ctx)
# why doesn't rectangle take arguments?

# strictly speaking, it doesn't have to
ctx.save()
ctx.translate(100,100)
ctx.scale(10,10)
ctx.set_source_rgb(0,.2,.2)
rectangle(ctx)
ctx.restore()

#by scaling and translating before drawing the rectangle,
# we can get the same effect

# let's save that trick for later
class CairoContextPlus(cairo.context):

    currentwidth
    currentheight

    @contextmanager
    def fit(self, move_x, move_y, scale_x, scale_y):

        ctx.save()
        ctx.translate(move_x, move_y)
        ctx.scale(scale_x, scale_y)
        yield self
        ctx.restore()

    def this_box(self, x_start, y_start, x_end, y_end):

        device_x_start, device_y_start = self.user_to_device(x_start, y_start)
        device_x_end, device_y_end = self.user_to_device(x_end, y_end)

        scale_x = (x_end - x_start) / (self.currentwidth * 1.0)
        scale_y = (y_end - y_start) / (self.currentheight * 1.0)





# it's a context manager, so we can trust that ctx.restore() will be called

with fit(ctx, 10, 50, 10, 2) as ctx_:
    ctx_.set_source_rgb(1,1,1)
    rectangle(ctx_)

## save for posterity
if svg:
    surface.finish()
else:
    surface.write_to_png("test1.png")