*********
Changelog
*********

This changelog mostly follows `keep a changelog <https://keepachangelog.com/en/1.0.0/>`__. Release numbering is based
on the UTC date of the release.

`Contributions <https://github.com/mborsetti/airportdata/blob/master/CHANGELOG.rst>`__ always welcomed!


Version 20201108
================

* Added airport OPIS/Islamabad International Airport and moved IATA code IST from OPRN/Benazir Bhutto International
  Airport https://github.com/mwgg/Airports/issues/47
* Improved testing, including validation of ``tz`` entries
* 100% of entries now have ``tz``
* Fixed and add data for Antarctica entries
* Changed deprecated ``tz`` ``'America/Godthab'`` to ``'America/Nook'``
* Changed deprecated ``tz`` ``'US/Mountain'`` to ``'America/Denver'``
* Fixed typo in ``tz`` entry for WAHI/YIA
* Added ``iata`` entry for WIMN/Silangit Airport: ``DTB``
* Fixed ``iata`` entry for K1O5/Montague-Yreka Rohrer Field to ``ROF``
* Fixed ``iata`` entry for KBPG/Big Spring Mc Mahon-Wrinkle Airport to ``HCA``
* Fixed ``iata`` entry for PAWS/Wasilla Airport to ``WWA``
* Fixed ``iata`` entry for CYDM/Ross River Airport to ``XRR``
* Fixed ``iata`` entry for CZBB/Vancouver / Boundary Bay Airport to ``YDT``
* Fixed ``iata`` entry for CZEE/Kelsey Airport to ``KES``
* Fixed ``iata`` entry for CZFG/Pukatawagan Airport to ``XPK``
* Fixed ``iata`` entry for CZNG/Poplar River Airport to ``XPP``
* Fixed ``iata`` entry for CZSN/South Indian Lake Airport to ``XSI``
* Fixed ``iata`` entry for CZWH/Lac Brochet Airport to ``XLB``
* Removed incorrect ``iata`` ``'---'`` from EHOW/Oostwold Airport
* Removed various incorrect ``iata`` entries from airports in US, CA and IT
* Removed KPFN/Panama City–Bay County International Airport (closed on October 1, 2010, now a development)
* Removed KS98/Vista Field (closed on December 31, 2013)
* Removed OK03/Downtown Airpark (defunct)
* Removed SVDA/La Tortuga Punta Delgada Airport (nonexistent)
* Changed incorrect ``icao`` of EK_2/Femø Airfield to ``EKFM``
* Capitalized all ``iata`` entries

Version 20201107a
=================

Milestone
---------
Initial working release of `airportdata` as a reworked fork of https://github.com/mwgg/Airports. Changes below are
relative to the project as of this date (latest commit 974436a on Jun 14 2020).

Changed
-------
* Renamed key ``state`` to ``subd`` as it contains state, province, region, etc.
* Converted to CSV format, roughly halving the file size
* Test for data integrity before publishing
* Created Python package for easy inclusion in Python projects and `published it to PyPi
  <https://pypi.org/project/airportsdata/>`__
* Fixed ``iata`` key so it is always of string type (converted existing ``'0'`` and ``Null`` to ``''``)
* Removed duplicate IATA entries for GOI, PDG and VNS (now only in VOGO, WIEE and VEBN respectively)
* Changed ``tz`` from ``'Maldives'`` to ``'Indian/Maldives'`` per IANA standard
* Changed non-standard ``country`` ``'KS'`` to ``'XK'`` as per https://en.wikipedia.org/wiki/ISO_3166-2:RS
* Added 679 IATA codes for US airports in the Kxxx range missing them https://github.com/mwgg/Airports/pull/39
* Added 16 IATA codes for Canadian airports in the Cxxx range missing them https://github.com/mwgg/Airports/pull/40
* Added ZBAD/PKX. Source: ARINC via https://skyvector.com/airport/ZBAD/Beijing-Daxing-Airport. Matches official CAAC data
  (obtained by third-parties). https://github.com/mwgg/Airports/pull/40
* CZBF/ZBF province fix: The province for CZBF does not contain a dash (New Brunswick). Removal of dash to match the same
  text as all other NB airports. https://github.com/mwgg/Airports/pull/46
* Added WAHI/YIA Yogyakarta International Airport https://en.wikipedia.org/wiki/Yogyakarta_International_Airport
  https://github.com/mwgg/Airports/pull/48
* Updated UACC's IATA code from TSE to NQZ (Astana International). On 8 June 2020, the airport officially changed its
  three-character IATA airport code from TSE to NQZ.
  https://en.wikipedia.org/wiki/Nursultan_Nazarbayev_International_Airport
  https://translate.google.com/translate?sl=ru&tl=en&u=https%3A%2F%2Ftime.kz%2Farticles%2Fzloba%2F2020%2F06%2F08%2Fpereimenovan-on-teper
  https://github.com/mwgg/Airports/pull/49
* CYYG/YYG province correction. Charlottetown is in PEI, not Newfoundland. Simple change to reflect this.
  https://github.com/mwgg/Airports/pull/50
