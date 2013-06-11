import cairo
from cairomeditation import cairoplus


svg = False

WIDTH = 1000
HEIGHT = 1000
if svg:
    surface = cairo.SVGSurface ("test1.svg", WIDTH, HEIGHT)
else:
    surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairoplus.Context(surface)

# tell Cairo what to draw, and where
ctx.set_source_rgb(1,.2,.2)
with ctx.in_box(100, 50, 135, 85):
    ctx.quick_rect()


with ctx.fit(10, 50, 10, 2):
    ctx.set_source_rgb(1,1,1)
    ctx.quick_rect()

with ctx.in_box(500,0,1000,1000):
    # ctx.set_source_rgb(0,1,0)
    # ctx.quick_rect()
    # pass

    with ctx.in_box(0,.800,1.000,1.000):
        radial = cairo.RadialGradient(0.25, 0.25, 0.1,  0.5, 0.5, 0.5)
        radial.add_color_stop_rgb(0,  1.0, 0.8, 0.8)
        radial.add_color_stop_rgb(1,  0.9, 0.0, 0.0)

        for i in range(1, 10):
            for j in range(1, 10):
                ctx.rectangle(i/10.0 - 0.04, j/10.0 - 0.04, 0.08, 0.08)
        ctx.set_source(radial)
        ctx.fill()

        linear = cairo.LinearGradient(0.25, 0.35, 0.75, 0.65)
        linear.add_color_stop_rgba(0.00,  1, 1, 1, 0)
        linear.add_color_stop_rgba(0.25,  0, 1, 0, 0.5)
        linear.add_color_stop_rgba(0.50,  1, 1, 1, 0)
        linear.add_color_stop_rgba(0.75,  0, 0, 1, 0.5)
        linear.add_color_stop_rgba(1.00,  1, 1, 1, 0)

        ctx.rectangle(0.0, 0.0, 1, 1)
        ctx.set_source(linear)
        ctx.fill()

with ctx.in_box(0, 500, 500,1000,(4,10), (4,10)):
    with ctx.source_rgb(0,0,1):
        ctx.rectangle(4, 4, 3, 3)
        ctx.fill()
    radial = cairo.RadialGradient(0.25, 0.25, 0.1,  0.5, 0.5, 0.5)
    radial.add_color_stop_rgb(0,  1.0, 0.8, 0.8)
    radial.add_color_stop_rgb(1,  0.9, 0.0, 0.0)
    # with ctx.source(radial):
    with ctx.source_rgb(0,0.5,0):
        ctx.rectangle(7, 7, 3, 3)
        ctx.fill()



## save for posterity
if svg:
    surface.finish()
else:
    surface.write_to_png("test1.png")