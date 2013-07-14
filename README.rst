Cairo Plus
==========

A wrapper around PyCairo that adds features
    * Python context manager around translations and transformations of the Cairo context
    * Scale to an area by specifying that area's coordinates and the new x and y range
    * shortcuts to draw certain shapes (arrowed_rect)

Usage
-----

.. code-block:: python

    from cairoplus import Context
    # use as a cairo.context,
    # but with new methods

    @contextmanager
    def rotated(self, radians):

    @contextmanager
    def fit(self, move_x, move_y, scale_x, scale_y):

    @contextmanager
    def in_box(self, x_start, y_start, x_end, y_end, new_x_range=(0,1), new_y_range=(0,1)):

    @contextmanager

    @contextmanager
    def source_rgb(self, r,g,b):

    @contextmanager
    def source_rgba(self, r,g,b,a):

    def quick_rect(self, x=(0,1), y=(0,1)):

    def arrow(self, startx=0, endx=1):

    def arrowed_rect(self, startx=0, endx=1, max_device_pixels=30):

    def text_length(self, string):


