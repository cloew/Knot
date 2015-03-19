from distutils.core import setup

setup(name='knot',
      version='0.0.1',
      description="",
      author='',
      author_email='',
      packages=['knot',
                'knot.core',
                'knot.core.painters',
                'knot.core.positioning',
                'knot.core.sizing',
                'knot.events',
                'knot.loader',
                'knot.loader.token'],
     )