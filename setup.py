#!/usr/bin/env python3

# this is run to install the project

import re
import sys

from setuptools import setup

import airportsdata
project = airportsdata

if sys.version_info < project.__min_python_version__:
    sys.exit(f'{project.__project_name__} requires Python version '
             f'{".".join(str(v) for v in project.__min_python_version__)} or newer.\n'
             f'You are running {sys.version}')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
with open('README.rst') as f:
    README_rst = f.read()

print('Updating counts in README.rst')
README_rst = README_rst.splitlines(keepends=True)
for line in README_rst:
    if line.startswith('.. |ICAO| replace::'):
        line = f'.. |ICAO| replace:: {len(airportsdata.load("ICAO")):6}'
    elif line.startswith('.. |ICAO| replace::'):
        line = f'.. |ICAO| replace:: {len(airportsdata.load("IATA")):6}'
README_rst = ''.join(README_rst)
with open('README.rst', 'w') as f:
    f.write(README_rst)

SETUP = {
    'name': project.__project_name__,
    'version': project.__version__,
    'description': project.__doc__.split('\n\n', 1)[0].strip(),
    'long_description': README_rst,
    'long_description_content_type': 'text/x-rst',
    'author': re.match(r'(.*) <(.*)>', project.__author__).groups()[0],
    'author_email': re.match(r'(.*) <(.*)>', project.__author__).groups()[1],
    'url': project.__url__,
    'packages': [project.__project_name__],
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Intended Audience :: Developers'
    ],
    'license': project.__license__,
    # data_files is deprecated. It does not work with wheels, so it should be avoided.
    'package_dir': {'': '.'},
    'package_data': {'': ['*.csv']},
    # 'exclude_package_data': {},
    'install_requires': requirements,
    # 'entry_points': {},
    'extras_require': {'testing': ['pytest', 'flake8', 'backports.zoneinfo']},
    'python_requires': f'>={".".join(str(v) for v in project.__min_python_version__)}',
    'project_urls': {'Bug Tracker': f'{project.__url__.rstrip("//")}/issues',
                     'Source Code': project.__url__,
                     'Documentation': f'{project.__url__.rstrip("//")}/README.rst'}}
setup(**SETUP)

