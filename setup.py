#!/usr/bin/env python3

# this is run to install the project

import re
import sys

from setuptools import setup  # type: ignore[import]

import airportsdata as project

if sys.version_info < project.__min_python_version__:
    sys.exit(
        f'{project.__project_name__} requires Python version '
        f'{".".join(str(v) for v in project.__min_python_version__)} or newer.\n'
        f'You are running {sys.version}'
    )

# requirements = list(map(str.strip, open('requirements.txt').readlines()))
# requirements = ['typing_extensions; python_version < "3.8"']
# requirements_testing = list(map(str.strip, open('tests/requirements_testing.txt').readlines()))
requirements_testing = ['backports.zoneinfo; python_version < "3.9"', 'pytest', 'pytest-cov', 'tzdata; os_name == "nt"']
README_rst = open('README.rst').read()

SETUP = {
    'name': project.__project_name__,
    'version': project.__version__,
    'description': project.__doc__.split('\n\n', 1)[0].strip(),
    'long_description': README_rst,
    'long_description_content_type': 'text/x-rst',
    'author': re.match(r'(.*) <(.*)>', project.__author__).groups()[0],  # type: ignore[union-attr]
    'author_email': re.match(r'(.*) <(.*)>', project.__author__).groups()[1],  # type: ignore[union-attr]
    'url': project.__url__,
    'packages': [project.__project_name__],
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Intended Audience :: Developers',
    ],
    'license': project.__license__,
    # data_files is deprecated. It does not work with wheels, so it should be avoided.
    'package_dir': {'': '.'},
    'package_data': {'': ['*.csv', 'py.typed']},
    # 'exclude_package_data': {},
    # 'install_requires': requirements,
    # 'entry_points': {},
    'extras_require': {'testing': requirements_testing},
    'python_requires': f'>={".".join(str(v) for v in project.__min_python_version__)}',
    'project_urls': {
        'Bug Tracker': f'{project.__url__.rstrip("//")}/issues',
        'Source Code': project.__url__,
        'Documentation': f'{project.__url__.rstrip("//")}/blob/main/README.rst',
    },
}
setup(**SETUP)
