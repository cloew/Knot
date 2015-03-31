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
                'knot.loader.token',
                'knot.loader.token.parser',
                'knot.loader.factory',
                'knot.loader.token.detector',
                'knot.events.tracker',
                'knot.loader.config',
                'knot.core.controllers',
                'knot.loader.token.value',
                'knot.core.services'],
     )