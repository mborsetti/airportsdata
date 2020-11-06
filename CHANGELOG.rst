*********
Changelog
*********

This changelog mostly follows `keep a changelog <https://keepachangelog.com/en/1.0.0/>`__. Release numbering is based
on the UTC date of the release.

Unreleased
==========
* None

`Contributions <https://github.com/mborsetti/airportdata/blob/master/CHANGELOG.rst>`__ always welcomed!

Version 20201106
================

Milestone
---------
Initial release of `airportdata` as a reworked fork of https://github.com/mwgg/Airports of the same date
(latest commit 974436a on Jun 14 2020).  Changes below are relative to this database.

Changed
-------
* Renamed key ``state`` to ``subdivision`` (could be state, province, region, etc.)
* Converted to CSV format (roughly halving the file size)
* Built tests for data integrity checking
* Created Python package for easy inclusion
* Published in PyPi
* Fixed ``iata`` key so it is always of string type (converted existing ``'0'`` and ``Null`` to ``''``)
* Removed duplicate IATA codes ``GOI``, ``PDG``, ``VNS`` (now only in VOGO, WIEE and VEBN respectively)
* Changed tz from ``'Maldives'`` to ``'Indian/Maldives'`` per IANA standard
* Changed non-standard "country code" from ``KS`` to ``XK`` per https://en.wikipedia.org/wiki/ISO_3166-2:RS
* Added 679 IATA codes for US airports in the Kxxx range missing them https://github.com/mwgg/Airports/pull/39
* Added 16 IATA codes for Canadian airports in the Cxxx range missing them https://github.com/mwgg/Airports/pull/40
* Added ZBAD. Source: ACARS via https://skyvector.com/airport/ZBAD/Beijing-Daxing-Airport. Matches official CAAC data
  (obtained by third-parties). https://github.com/mwgg/Airports/pull/40
* CZBF Province fix: The province for CZBF does not contain a dash (New Brunswick). Removal of dash to match the same
  text as all other NB airports. https://github.com/mwgg/Airports/pull/46
* Added WAHI/YIA Yogyakarta International Airport t https://en.wikipedia.org/wiki/Yogyakarta_International_Airport
  https://github.com/mwgg/Airports/pull/48
* Updated UACC's IATA code from TSE to NQZ (Astana International). On 8 June 2020, the airport officially changed its
  three-character IATA airport code from TSE to NQZ.
  https://en.wikipedia.org/wiki/Nursultan_Nazarbayev_International_Airport
  https://translate.google.com/translate?sl=ru&tl=en&u=https%3A%2F%2Ftime.kz%2Farticles%2Fzloba%2F2020%2F06%2F08%2Fpereimenovan-on-teper
  https://github.com/mwgg/Airports/pull/49
* CYYG province correction. Charlottetown is in PEI, not Newfoundland. Simple change to reflect this.
  https://github.com/mwgg/Airports/pull/50
