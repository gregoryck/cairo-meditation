from distutils.core import setup

setup(
    name='cairoplus',
    version='0.1',
    packages=['cairoplus',],
    long_description=open('README.rst').read(),
    scripts=[
             "scripts/draw.py",
            ],
    # data_files=[("etc/cairoplus/", [
                                        # ],
               # )],

)
