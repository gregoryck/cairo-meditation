from distutils.core import setup

setup(
    name='cairomeditation',
    version='0.1',
    packages=['cairomeditation',],
    long_description=open('README.rst').read(),
    scripts=[
             "scripts/draw.py",
            ],
    # data_files=[("etc/cairomeditation/", [
                                        # ],
               # )],

)
