from setuptools import setup, find_packages
import sys, os


def read_file(filename):
    try:
        return open(filename, 'r').read()
    except: # Everything!
        return ''

version = '0.2'

setup(name='skeletons',
      version=version,
      description="Skeletons for server configs",
      long_description=read_file('README'),
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Framework :: Paste',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: Russian',
          'Programming Language :: Python',
          'Topic :: System :: Installation/Setup',
          'Topic :: Utilities',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
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
      lighttpd_mod_fcgi = skeletons:LighttpdModFastCGI
      #lighttpd_mod_proxy = skeletons:LighttpdModProxy
      #apache_backend = skeletons:ApacheBackend
      """,
      )
