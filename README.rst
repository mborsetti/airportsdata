======================
airportsdata |version|
======================

.. |version| image:: https://img.shields.io/pypi/v/airportsdata.svg?label=
    :target: https://pypi.org/project/airportsdata/
    :alt: pypi version

.. |support| image:: https://img.shields.io/pypi/pyversions/airportsdata.svg
    :target: https://pypi.org/project/airportsdata/
    :alt: supported Python version

.. |license| image:: https://img.shields.io/pypi/l/airportsdata.svg
    :target: https://pypi.org/project/airportsdata/
    :alt: license

.. |issues| image:: https://img.shields.io/github/issues-raw/mborsetti/airportsdata
    :target: https://github.com/mborsetti/airportsdata/issues
    :alt: issues

.. |travis| image:: https://img.shields.io/travis/com/mborsetti/airportsdata?label=Travis%20CI
    :target: https://travis-ci.com/mborsetti/airportsdata
    :alt: Travis CI build status

A UTF-8 CSV database (with Python code to access it) of 28,867 entries with basic information about nearly every
airport and landing strip in the world.  Also includes IATA codes for 6,577 aerodromes.

Each entry consists of:

* ``icao``: ICAO 4-character code or FAA 3-character code
* ``iata``: IATA 3-letter code or an empty string
* ``name``: official name (latin script)
* ``city``: city
* ``subd``: subdivision (e.g. state, province, region, etc.)
* ``country``: ISO 3166-1 alpha 2-code + ``XK`` for Kosovo
* ``elevation``: MSL elevation (the highest point of the landing area) in feet
* ``lat``: latitude (decimal)
* ``lon``: longitude (decimal)
* ``tz``: timezone expressed in tz database name (IANA-compliant) string (empty string for ``AQ`` Antarctica). Originally sourced from `TimeZoneDB <https://timezonedb.com>`__

Best efforts are placed to review all contributions for accuracy but accuracy cannot be guaranteed or expeted.

This project is a fork of https://github.com/mwgg/Airports

Python
======
|support| |travis| |issues|

Install using pip

.. code-block:: bash

  pip install airportsdata

To load the data into a dict:

.. code-block:: python

  import airportsdata
  airports = airportsdata.load()  # key is ICAO code

or

.. code-block:: python

  import airportsdata
  airports = airportsdata.load('IATA')  # key is IATA code

Download
========

Download the file ``airports.csv`` from https://github.com/mborsetti/airportsdata/raw/main/airportsdata/airports.csv
or use git software

License
=======

|license|

Released under the `MIT License <https://opensource.org/licenses/MIT>`__. See the license `here
<https://github.com/mborsetti/airportsdata/blob/main/LICENSE>`__.
