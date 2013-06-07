import cairo

from contextlib import contextmanager

svg = False

WIDTH = 1000
HEIGHT = 1000
if svg:
    surface = cairo.SVGSurface ("test1.svg", WIDTH, HEIGHT)
else:
    surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# tell Cairo what to draw, and where
ctx.set_source_rgb(1,.2,.2)
ctx.rectangle(100, 50, 35, 35)
ctx.fill()

# of course def a function so you don't repeat yourself
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
@contextmanager
def fit(ctx, move_x, move_y, scale_x, scale_y):
    ctx.save()
    ctx.translate(move_x, move_y)
    ctx.scale(scale_x, scale_y)
    yield ctx
    ctx.restore()

# it's a context manager, so we can trust that ctx.restore() will be called

with fit(ctx, 10, 50, 10, 2) as ctx_:
    ctx_.set_source_rgb(1,1,1)
    rectangle(ctx_)

## save for posterity
if svg:
    surface.finish()
else:
    surface.write_to_png("test1.png")