============
Contributing
============

|contributors|

.. |contributors| image:: https://img.shields.io/github/contributors/mborsetti/webchanges
    :target: https://github.com/mborsetti/airportsdata/pulls?q=
    :alt: contributors

Everyone is encouraged to contribute!

If you can provide a change as a pull request, please do so. If not, please open an issue `here
<https://github.com/mborsetti/airportdata/issues>`__ and someone will look into it.

Please provide a link to a primary source (e.g. national aviation authority such as `FAA <https://www.faa
.gov/air_traffic/flight_info/aeronav/aero_data/Airport_Data/>`__, `IATA
<https://www.iata.org/en/publications/directories/code-search/>__, etc.) to help out the data verification
process.  ARINC data (e.g. from `SkyVector <https://skyvector.com/airports>`__) is also a good source since, sadly, the
official ICAO Location Indicators are not made freely available to taxpayers (see `here
<https://store.icao.int/en/location-indicators-doc-7910>`__).

Python contributors can test changes locally with ``tox`` or by running:

.. code-block:: bash

  pip install -U airportsdata[testing]
  pytest tests/ -v


Thanks to the following for having contributed directly to this project:

* `Edward Weymouth <https://github.com/ed42311>`__
* `Michel Vidal-Naquet <https://github.com/micvn>`__
* `Błażej Cyrzon <https://github.com/bc291>`__
