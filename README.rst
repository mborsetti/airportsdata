============
airportsdata
============

.. |ICAO| replace:: 28,141

.. |IATA| replace:: 6,550

.. |LID| replace:: 12,567

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

.. |CI| image:: https://github.com/mborsetti/airportsdata/workflows/Tests/badge.svg?branch=main
    :target: https://github.com/mborsetti/airportsdata/actions
    :alt: CI testing status

.. |coveralls| image:: https://coveralls.io/repos/github/mborsetti/airportsdata/badge.svg?branch=main
    :target: https://coveralls.io/github/mborsetti/airportsdata?branch=main
    :alt: code coverage by Coveralls


Extensive database of location and timezone data for nearly every operational airport and landing strip in the world,
with |ICAO| entries.

Each entry consists of the following data:

* ``icao``: ICAO 4-letter DOC7910 Location Indicator or (if none) an internal Pseudo-ICAO Identifier[*] (|ICAO| entries)
* ``iata``: IATA 3-letter Location Code (|IATA| entries) or an empty string[#]
* ``name``: Official name (latin script)
* ``city``: City
* ``subd``: Subdivision (e.g. state, province, region, etc.)
* ``country``: `ISO 3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ alpha-2 country code
  (plus ``XK`` for Kosovo)
* ``elevation``: MSL elevation (the highest point of the landing area) in feet; it is often wrong
* ``lat``: Latitude (decimal)
* ``lon``: Longitude (decimal)
* ``tz``: Timezone expressed as a `tz database name <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__
  (IANA-compliant) or an empty string for Antarctica
* ``lid``: U.S. FAA Location Identifier (|LID| entries), or an empty string

.. [*] See `here <https://github.com/mborsetti/airportsdata/blob/main/README_identifiers.rst>`__ for an explanation on
   how the Pseudo-ICAO Identifier is generated for airports and seaplane bases without an ICAO 4-letter Location
   Indicator.

.. [#] IATA Multi Airport Cities are not not airports so are not included, but we provide a database and a Python
   function that returns the above data for all of their component airports of a IATA MAC. Please see documentation
   `here <https://github.com/mborsetti/airportsdata/blob/main/README_IATA.rst>`__.

Best efforts are placed to review all contributions for accuracy, but accuracy cannot be guaranteed nor should be
expected by users.

Known issues:

* A small, but unknown, number of aerodromes are missing their IATA Location Code (none are major ones);
* Timezone was originally sourced from `TimeZoneDB <https://timezonedb.com>`__ and is missing for Antarctica;
* No historical data (closed airports are removed).

Please report any issues you may find `here
<https://github.com/mborsetti/airportsdata/blob/main/CONTRIBUTING.rst>`__.

This project is a fork of https://github.com/mwgg/Airports. All new data submitted in this fork have been validated
against national `Aeronauical Information Publications (AIP) or equivalent
<https://github.com/mborsetti/airportsdata/blob/main/README_AIP.rst>`__ (or
ARINC database) and `IATA <https://www.iata.org/en/publications/directories/code-search/>`__ before publishing.

Raw data
========

A CSV (comma separated values) file with headers (UTF-8 encoding) is downloadable from GitHub `here
<https://github.com/mborsetti/airportsdata/raw/main/airportsdata/airports.csv>`__.

Python
======
|version| |support| |CI| |coveralls| |issues|

Install from `PyPi <https://pypi.org/project/airportsdata/>`__  using pip:

.. code-block:: bash

  pip install -U airportsdata

Once installed, to load the data into a dict:

.. code-block:: python

   import airportsdata
   airports = airportsdata.load()  # key is the ICAO identifier (the default)
   print(airports['KJFK'])

or

.. code-block:: python

   import airportsdata
   airports = airportsdata.load('IATA')  # key is the IATA location code
   print(airports['JFK'])

or

.. code-block:: python

   import airportsdata
   airports = airportsdata.load('LID')  # key is the FAA LID
   print(airports['01AA'])

License
=======

|license|

Released under the `MIT License <https://opensource.org/licenses/MIT>`__ (see license `here
<https://github.com/mborsetti/airportsdata/blob/main/LICENSE>`__).
