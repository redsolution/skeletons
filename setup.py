from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='skeletons',
      version=version,
      description="Skeletons for server configs",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ivan Gromov',
      author_email='ivan.gromov@redsolution.ru',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      duply = skeletons:DuplyTemplate
      #lighttpd_mod_proxy = skeletons:LighttpdModProxy
      #lighttpd_mod_fcgi = skeletons:LighttpdModFastCGI
      #apache_backend = skeletons:ApacheBackend
      """,
      )
