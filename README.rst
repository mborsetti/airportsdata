============
airportsdata
============

.. |ICAO| replace:: 28,863

.. |IATA| replace:: 6,549

.. |version| image:: https://img.shields.io/pypi/v/airportsdata.svg
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

Extensive database of current data for nearly every airport and landing strip in the world, with |ICAO| entries.

Each entry consists of the following data:

* ``icao``: ICAO (or FAA/TD LID) 4-alphanumeric code
* ``iata``: IATA 3-letter code (for |IATA| entries) or an empty string; these will be validated, going forward, against `IATA
  data <https://www.iata.org/en/publications/directories/code-search/>`__
* ``name``: official name (latin script)
* ``city``: city
* ``subd``: subdivision (e.g. state, province, region, etc.)
* ``country``: `ISO 3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ alpha-2 country code
  (plus ``XK`` for Kosovo)
* ``elevation``: MSL elevation (the highest point of the landing area) in feet
* ``lat``: latitude (decimal)
* ``lon``: longitude (decimal)
* ``tz``: timezone expressed as a `tz database name <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__
  (IANA-compliant). Originally sourced from `TimeZoneDB <https://timezonedb.com>`__

Best efforts are placed to review all contributions for accuracy, but accuracy cannot be guaranteed or should be
expected by users.  Please report any issues you may find `here
<https://github.com/mborsetti/airportsdata/blob/main/CONTRIBUTING.rst>`__.

Known issues:

* 219 aerodromes have IATA codes that are not in the `IATA database
  <https://www.iata.org/en/publications/directories/code-search/>`__ and may be incorrect
* A small, but unknown, number of aerodromes whose IATA code is missing (none in the major airports)
* No historical data

This project is a fork of https://github.com/mwgg/Airports

Python
======
|version| |support| |travis| |issues|

Install from `PyPi <https://pypi.org/project/airportsdata/>`__  using pip:

.. code-block:: bash

  pip install -U airportsdata

Once installed, to load the data into a dict:

.. code-block:: python

  import airportsdata
  airports = airportsdata.load()  # key is ICAO code

or

.. code-block:: python

  import airportsdata
  airports = airportsdata.load('IATA')  # key is IATA code

Raw data
========

CSV file with headers (UTF-8 encoding) downloadable from
`https://github.com/mborsetti/airportsdata/raw/main/airportsdata/airports.csv
<https://github.com/mborsetti/airportsdata/raw/main/airportsdata/airports.csv>`__

License
=======

|license|

Released under the `MIT License <https://opensource.org/licenses/MIT>`__ (see license `here
<https://github.com/mborsetti/airportsdata/blob/main/LICENSE>`__).
