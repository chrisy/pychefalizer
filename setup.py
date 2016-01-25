#!/usr/bin/env python

try:
    from setuptools import Command, setup
except ImportError:
    from distutils.core import Command, setup

import pychefalizer
long_description = pychefalizer.__doc__.rstrip() + "\n"
version = pychefalizer.version

class GenerateReadme(Command):
    description = "Generates README file from long_description"
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass
    def run(self):
        open("README","w").write(long_description)

setup(name='pychefalizer',
      version = version,
      description = 'Python enchefalizer',
      long_description = long_description,
      author = 'Chris Luke',
      author_email = 'chrisy@flirble.org',
      url = 'https://github.com/chrisy/pychefalizer',
      cmdclass = {'readme': GenerateReadme},
      packages = ['pychefalizer'],
      package_dir = {'pychefalizer': 'pychefalizer'},
      scripts = ['chefalizer'],
      requires = ['ply'],
      license = 'BSD',
      classifiers = [ "Topic :: Internet :: Name Service (DNS)",
                      "Programming Language :: Python :: 2",
                      "Programming Language :: Python :: 3",
                      ],
     )
