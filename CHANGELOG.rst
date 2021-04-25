*********
Changelog
*********

This changelog mostly follows `keep a changelog <https://keepachangelog.com/en/1.0.0/>`__. Release numbering is based
on the UTC date of the release.

`Contributions <https://github.com/mborsetti/airportdata/blob/master/CHANGELOG.rst>`__ always welcomed!


Version 20210425
================
* Multiple additions and fixes contributed by `Edward Weymouth <https://github.com/ed42311>`__ in `#1
  <https://github.com/mborsetti/airportsdata/pull/1>`__:

  * Added airport SDWQ/Alenquer Airport, BR
  * Fixed spelling for RJAN/Niijima Airport
  * Added ``iata`` entry for KOSA/Mount Pleasant Regional Airport
  * Added ``iata`` entry for YLIM/Limbunya Station Airport
  * Added ``iata`` entry for KFFO/Wright Patterson
  * Added ``iata`` entry for RJAN/Niijima Airport
  * Added ``iata`` entry for KCIN/Arthur N Neu Airport
  * Added ``iata`` entry for KTOR/Torrington Municipal Airport
  * Added ``iata`` entry for KSAC/Sacramento Executive Airport
  * Added ``iata`` entry for PADM/Marshall Don Hunter Sr Airport

Version 20201205
================
* Replaced hyphens with spaces when required  in ``subd`` for USA, Canada, Mexico, Australia, New Zealand and Italy and
  globally for some major english names (such as North xxx etc.)
* Fixed "Westrn-Australia" typo in ``subd`` (now "Western Australia")
* Fixed the ``subd`` for the following US airports as per `here <https://github.com/mwgg/Airports/pull/51>`__:

  * K2H0: old "Alabama"; new "Illinois" (Shelbyville)
  * KBLF: old "Illinois"; new "West Virginia" (Bluefield)
  * KBMG: old "Alabama"; new "Indiana" (Bloomington)
  * KBUU: old "Iowa"; new "Wisconsin" (Burlington)
  * KCDN: old "New York"; new "South Carolina" (Camden)
  * KCWI: old "Arkansas"; new "Iowa" (Clinton)
  * KCZG: old "Alabama"; new "New York" (Endicott)
  * KDAW: old "Missouri"; new "New Hampshire" (Rochester)
  * KDQH: old "Arizona"; new "Georgia" (Douglas)
  * KEFD: old "Connecticut"; new "Texas" (Houston)
  * KF22: old "Iowa"; new "Oklahoma" (Perry)
  * KFDW: old "Ohio"; new "South Carolina" (Winnsboro)
  * KFFZ: old "Alabama"; new "Arizona" (Mesa)
  * KGKY: old "Oregon"; new "Texas" (Arlington)
  * KGVT: old "California"; new "Texas" (Greenville)
  * KHOT: old "Iowa"; new "Arkansas" (Hot Springs)
  * KLKV: old "Colorado"; new "Oregon" (Lakeview)
  * KLNK: old "Montana"; new "Nebraska" (Lincoln)
  * KLOM: old "Florida"; new "Pennsylvania" (Philadelphia)
  * KMIC: old "California"; new "Minnesota" (Minneapolis)
  * KMKO: old "Florida"; new "Oklahoma" (Muskogee)
  * KMNZ: old "New York"; new "Texas" (Hamilton)
  * KMQY: old "Delaware"; new "Tennessee" (Smyrna)
  * KOCW: old "Georgia"; new "North Carolina" (Washington)
  * KONP: old "Arkansas"; new "Oregon" (Newport)
  * KPNM: old "Maine"; new "Minnesota" (Princeton)
  * KPOC: old "Minnesota"; new "California" (La Verne)
  * KPYM: old "Indiana"; new "Massachusetts" (Plymouth)
  * KRDM: old "Indiana"; new "Oregon" (Redmond)
  * KRMY: old "Colorado"; new "Michigan" (Marshall)
  * KSFF: old "Oregon"; new "Washington" (Spokane)
  * KSMD: old "Arkansas"; new "Indiana" (Fort Wayne)
  * KSQL: old "Arizona"; new "California" (San Carlos)
  * KUOS: old "Georgia"; new "Tennessee" (Sewanee)
  * KUVA: old "Florida"; new "Texas" (Uvalde)
  * PAMR: old "Iowa"; new "Alaska" (Anchorage)
  * PAPB: old "South Carolina"; new "Alaska" (St George)

Version 20201203
================
* Added WICA/Kertajati International Airport

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
* Added ZBAD/PKX. Source: ARINC via https://skyvector.com/airport/ZBAD/Beijing-Daxing-Airport. Matches official CAAC
  data (obtained by third-parties). https://github.com/mwgg/Airports/pull/40
* CZBF/ZBF province fix: The province for CZBF does not contain a dash (New Brunswick). Removal of dash to match the
  same text as all other NB airports. https://github.com/mwgg/Airports/pull/46
* Added WAHI/YIA Yogyakarta International Airport https://en.wikipedia.org/wiki/Yogyakarta_International_Airport
  https://github.com/mwgg/Airports/pull/48
* Updated UACC's IATA code from TSE to NQZ (Astana International). On 8 June 2020, the airport officially changed its
  three-character IATA airport code from TSE to NQZ.
  https://en.wikipedia.org/wiki/Nursultan_Nazarbayev_International_Airport
  https://translate.google.com/translate?sl=ru&tl=en&u=https%3A%2F%2Ftime.kz%2Farticles%2Fzloba%2F2020%2F06%2F08%2Fpereimenovan-on-teper
  https://github.com/mwgg/Airports/pull/49
* CYYG/YYG province correction. Charlottetown is in PEI, not Newfoundland. Simple change to reflect this.
  https://github.com/mwgg/Airports/pull/50
