from distutils.core import setup

setup(name='knot',
      version='0.0.1',
      description="",
      author='',
      author_email='',
      packages=['knot',
                'knot.core',
                'knot.core.controllers',
                'knot.core.mods',
                'knot.core.painters',
                'knot.core.positioning',
                'knot.core.services',
                'knot.core.sizing',
                'knot.events',
                'knot.events.tracker',
                'knot.exceptions',
                'knot.forms',
                'knot.forms.controllers',
                'knot.forms.painters',
                'knot.forms.partials',
                'knot.loader',
                'knot.loader.config',
                'knot.loader.factory',
                'knot.loader.token',
                'knot.loader.token.detector',
                'knot.loader.token.value',
                'knot.policy',
                'knot.scope',
                'knot.watches',
                'knot.widget',
                'knot.loader.config.args',
                'knot.tabs',
                'knot.tabs.painters',
                'knot.tabs.controllers'],
      package_data = {'knot.core':['knot-pkg.json'],
                      'knot.forms':['knot-pkg.json'],
                      'knot.forms.partials':['*.knot']},
     )