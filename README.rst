========================
airportsdata |downloads|
========================

.. |ICAO| replace:: 28,223

.. |IATA| replace:: 7,859

.. |LID| replace:: 12,609

.. |pyversion| image:: https://img.shields.io/pypi/v/airportsdata.svg
    :target: https://pypi.org/project/airportsdata/
    :alt: pypi version
.. |support| image:: https://img.shields.io/pypi/pyversions/airportsdata.svg
    :target: https://pypi.org/project/airportsdata/
    :alt: supported Python version
.. |pypi_version| image:: https://img.shields.io/pypi/v/airportsdata.svg?label=
    :target: https://pypi.org/project/airportsdata/
    :alt: PyPI version
.. |format| image:: https://img.shields.io/pypi/format/airportsdata.svg
    :target: https://pypi.org/project/airportsdata/
    :alt: Kit format
.. |downloads| image:: https://static.pepy.tech/badge/airportsdata
    :target: https://www.pepy.tech/project/airportsdata
    :alt: PyPI downloads
.. |license| image:: https://img.shields.io/pypi/l/airportsdata.svg
    :target: https://pypi.org/project/airportsdata/
    :alt: license
.. |issues| image:: https://img.shields.io/github/issues-raw/mborsetti/airportsdata
    :target: https://github.com/mborsetti/airportsdata/issues
    :alt: issues
.. |CI| image:: https://github.com/mborsetti/airportsdata/actions/workflows/ci-cd.yaml/badge.svg?event=push
    :target: https://github.com/mborsetti/airportsdata/actions
    :alt: CI testing status
.. |coveralls| image:: https://coveralls.io/repos/github/mborsetti/airportsdata/badge.svg?branch=main
    :target: https://coveralls.io/github/mborsetti/airportsdata?branch=main
    :alt: code coverage by Coveralls
.. |status| image:: https://img.shields.io/pypi/status/airportsdata.svg
    :target: https://pypi.org/project/airportsdata/
    :alt: Package stability
.. |security| image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

Extensive database of location and timezone data for nearly every operational airport and landing strip in the world,
with |ICAO| entries.

Each entry consists of the following data:

* ``icao``: ICAO 4-letter Location Indicator (Doc 7910) or (if none) an internal Pseudo-ICAO Identifier [#]_ (|ICAO|
  entries);
* ``iata``: IATA 3-letter Location Code (|IATA| entries) or an empty string [#]_;
* ``name``: Official name (diacritized latin script);
* ``city``: City (diacritized latin script), ideally using the local language or English;
* ``subd``: Subdivision (e.g. state, province, region, etc.), ideally using the local-language or English names of
  `ISO 3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes>`__;
* ``country``: `ISO 3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ alpha-2 country code
  (plus ``XK`` for Kosovo);
* ``elevation``: MSL elevation of the highest point of the landing area, in feet (warning: it is often wrong);
* ``lat``: Latitude (decimal) of the `airport reference point
  <https://en.wikipedia.org/wiki/Airport_reference_point>`__ (max 5 or 6 decimal digits);
* ``lon``: Longitude (decimal) of the `airport reference point
  <https://en.wikipedia.org/wiki/Airport_reference_point>`__ (max 5 or 6 decimal digits);
* ``tz``: Timezone expressed as a `tz database name <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__
  (IANA-compliant);
* ``lid``: U.S. FAA Location Identifier (|LID| entries), or an empty string.

.. [#] See `here <https://github.com/mborsetti/airportsdata/blob/main/README_identifiers.rst>`__ for an explanation on
   how the Pseudo-ICAO Identifier is generated for airports and seaplane bases without an ICAO 4-letter Location
   Indicator.

.. [#] IATA Multi Airport Cities (MAC) are not not airports and therfore not included, but we provide a database and a 
   Python function that returns the above data for all the airports of a IATA MAC. Please see documentation `here
   <https://github.com/mborsetti/airportsdata/blob/main/README_IATA.rst>`__.

Best efforts are placed to review all contributions for accuracy, but accuracy cannot be guaranteed nor should be
expected by users.

Important notes:

* Timezone was originally sourced from `TimeZoneDB <https://timezonedb.com>`__;
* No historical data (closed airports are removed);
* No heliports without a IATA code;
* No sea bases without a IATA code;
* No surface transportation stations, even if they have an official IATA code.

Please report any issues you may find `here
<https://github.com/mborsetti/airportsdata/blob/main/CONTRIBUTING.rst>`__.

This project is a fork of https://github.com/mwgg/Airports. All new data submitted in this fork have been validated
against national `Aeronautical Information Publications (AIP) or equivalent
<https://github.com/mborsetti/airportsdata/blob/main/README_AIP.rst>`__ (or
ARINC database) and `IATA <https://www.iata.org/en/publications/directories/code-search/>`__ before publishing.

Raw data
========

A CSV (comma separated values) file, with headers and encoded in UTF-8, is downloadable from GitHub `here
<https://github.com/mborsetti/airportsdata/raw/main/airportsdata/airports.csv>`__.

Python
======
|pyversion| |support| |format| |status| |security| |CI| |coveralls| |issues|

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

Older Python versions are supported for 3 years after being obsoleted by a new major release (i.e. about 4 years
since their original release).

License |license|
=================

Released under the `MIT License <https://opensource.org/licenses/MIT>`__ (see license `here
<https://github.com/mborsetti/airportsdata/blob/main/LICENSE>`__).
