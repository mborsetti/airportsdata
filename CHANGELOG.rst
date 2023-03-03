*********
Changelog
*********

This changelog mostly follows `keep a changelog <https://keepachangelog.com/en/1.0.0/>`__. Release numbering is based
on the UTC date of the release.

`Contributions <https://github.com/mborsetti/airportdata/blob/master/CHANGELOG.rst>`__ always welcomed!


20230303
==================
* Better documented our use of pseudo-ICAO Identifiers.
* Reworded the IATA Multi Airport Cities page.
* Removed IATA code QUS from DNGU, Gusau Airport, Gusau, Zamfara, Nigeria (code not in IATA database).
* Implemented suggestions made upstream by `Nicolas Bridoux
  <https://github.com/Bridouille>`__ in issue `#80 <https://github.com/mborsetti/airportsdata/issues/80>`__:

  * Added:

    - AYLO/LWI, Lowai Airstrip, Lowai, Morobe Province, Papua New Guinea
    - LTCW/YKO, Yüksekova Selahaddin Eyyubi Airport, Yüksekova, Hakkari, Turkey
    - MPRH/RIH, Río Hato Airport, Río Hato, Coclé, Panama
    - UWSG/GSV, Gagarin Airport, Saratov, Saratov, Russia
    - ZSSM/SQJ, Sanming Shaxian Airport, Sanming, Fujian, China
  * Added IATA code and updated ICAO one:

    - VEDH/DBR, Darbhanga Airport, Bihar, India (was VE89)
    - VOTK/TCR, Tuticorin Southwest Airport, Tamil-Nadu, India (was VO80)
  * Added IATA code:

    - 5MS1/RFK, Rollang Field, Rolling Fork, Mississippi, USA
    - KTHM/THM, Thompson Falls Airport, Thompson Falls, Montana, USA
    - MMSM/NLU, Santa Lucia Air Force Base, Reyes Acozac, Mexico
    - SKSA/RVE, Los Colonizadores Airport, Saravena, Arauca, Colombia
    - SKVG/VGZ, Villagarzon Airport, Villagarzon, Putumayo, Colombia
    - YBGD/OCM, Boolgeeda Airport, Western Australia, Australia
* Added ``tox-ini-fmt`` to ``pre-commit`` to apply a consistent format to tox.ini files.


Version 20221121
==================
* All USA airports have been replaced with information sourced from the FAA. This consists of 12,566 operational
  airports located in the US and its territories, and covers country codes ``US``, ``PR`` (The Commonwealth of Puerto
  Rico), ``VI`` (The Virgin Islands of the United States), ``AS`` (The Territory of American Samoa), ``FM`` (The
  Federated States of Micronesia), ``GU`` (The Territory of Guam), ``MH`` (The Republic of the Marshall Islands),
  ``MP`` (The Commonwealth of the Northern Mariana Islands) and ``PW`` (The Republic of Palau).
* As a result of this upgrade, 379 airports that the FAA shows as permanently closed have been removed, and for
  other reasons the total net number of airports has decreased by an additional 387. Timezone information, when not
  available in the previous database, has been sourced from `TimeZoneDB  <https://timezonedb.com>`__.
* A new key ``lid`` has been added and contains the FAA LID (Location Identifier), which is generally either a 3
  character alphabetic or alphanumeric string or an alphanumeric one of 4 characters containing at least 1 number.
  For non-USA airports, this key contains an empty string.
* Airports in the US (and its territories) can now be retrieved by FAA LID by loading them with
  ``airportsdata.load('LID')``
* Added HAJJ/JIJ, Wilwal International Airport, Jijiga, Fafan, Ethiopia
* Added OENN/NUM, Neom Bay Airport, Neom, Tabuk, Saudi Arabia


Version 20221105.1
==================
* Added LLER/ETM, Ilan and Asaf Ramon Airport, Eilat, Southern District, Israel. Reported by `Andrzej Pomirski
  <https://github.com/Acrobot>`__ in issue `#17 <https://github.com/mborsetti/airportsdata/issues/17>`__.
* Added LENE, La Caminera Airport, Torrenueva, Ciudad Real, Spain. (Contributed upstream by `Vladimir Simakhin
  <https://github.com/vsimakhin>`__ in in PR `#78 <https://github.com/mwgg/Airports/pull/77>`__).


Version 20221101
==================
* Added IATA identifier to VEJH/JRG, Jharsuguda Airport, Veer Surendra Sai, Odisha, India and fixed city, elevation and
  coordinates. (Partially contributed upstream by `Nicolas Bridoux <https://github.com/Bridouille>`__ in issue `#74
  <https://github.com/mwgg/Airports/issues/74>`__).
* Fixed IATA identifier (was XHE) to LFTH/TLN, Toulon-Hyeres Airport, Toulon/Hyeres/Le Palyvestre,
  Provence-Alpes-Cote-d'Azur, France. (Partially contributed upstream by `Nicolas Bridoux
  <https://github.com/Bridouille>`__ in issue `#74 <https://github.com/mwgg/Airports/issues/74>`__).
* Added VEDO/DGH, Deoghar Airport, Deoghar, Jharkhand, India. (Partially contributed upstream by `Nicolas Bridoux
  <https://github.com/Bridouille>`__ in issue `#74 <https://github.com/mwgg/Airports/issues/74>`__).
* Adeed OEBT, Batha Airport, Batha, Saudi Arabia.
* Fixed multiple airports in the Emirate of Abu Dhabi, United Arab Emirates.
* Added LPSO, Ponte De Sôr Airport, Ponte de Sôr, Portalegre, Portugal. (Partially contributed upstream by `Vladimir
  Simakhin <https://github.com/vsimakhin>`__ in PR `#77 <https://github.com/mwgg/Airports/pull/77>`__).
* Removed testing/support for Python 3.7 (>3 years since release of Python 3.8).


Version 20221017
================
* Added SBJE/JJD, Comandante Ariston Pessoa Airport, Jijoca de Jericoacoara (Cruz), Ceará, Bazil. (Partially contributed
  upstream by `Nicolas Bridoux <https://github.com/Bridouille>`__ in issue `#74
  <https://github.com/mwgg/Airports/issues/74>`__).
* Added IATA identifier to YCWA/CJF, Coondewanna Airport, Western Australia, Australia and fixed elevation and
  coordinates. (Partially contributed upstream by `Nicolas Bridoux <https://github.com/Bridouille>`__ in issue `#74
  <https://github.com/mwgg/Airports/issues/74>`__).
* Fixed punctuation and accents of all Brazilian subdivisions (federative units).
* Support for Python 3.11.
* Added Python static type testing using `mypy`.


Version 20220921
================
* Updated ICAO identifiers, name and altitude of Kyrgyzstan airports present in their `AIP
  <http://kan.kg/ais/eaip/2022-10-06-AIRAC/html/index_commands.html>`__ (UCFL, UCFM, UCFO, UCFP) and added IATA
  identifier to UCFL/IKU. (Partially contributed upstream by `Vladimir Simakhin <https://github.com/vsimakhin>`__ in PR
  `#69 <https://github.com/mwgg/Airports/pull/69>`__).
* Replaced UAJT Turkestan Airport, Turkistan, Ongtuestik-Qazaqstan, Kazakhstan (decommissioned) with UAIT/HSA
  Turkistan International Airport, Turkistan, Ongtuestik-Qazaqstan, Kazakhstan (replacement aerodrome).
  Source: `AIP <https://www.ans.kz/AIP/eAIP/2022-10-06-AIRAC/html/index-en-GB.html>`__
  (note: here we use the AIP/IATA official name even though the new airport also carries the name of Hazret
  Sultan International Airport). (Partially contributed upstream by `vort3 <https://github.com/vort3>`__ in PR `#71
  <https://github.com/mwgg/Airports/pull/71>`__).
* Updated names and elevation of all Kazakhstani aerodromes present in their `AIP
  <https://www.ans.kz/AIP/eAIP/2022-10-06-AIRAC/html/index-en-GB.html>`__, adding UASU and UASZ airports.
* Fixed the IATA identifier for UASS/PLX, Semey International Airport, Semey, East Kazakhstan, Kazakhstan (found DLX, a
  non-existend IATA identifier).


Version 20220917
================
* Added SLAL/SRE, Alcantarí International Airport, Sucre, Chuquisaca, Bolivia (partially contributed upstream by `687er
  <https://github.com/687er>`__  in PR `#70 <https://github.com/mwgg/Airports/pull/70>`__).
* Removed SRE IATA code from Juana Azurduy De Padilla Airport, Sucre, Chuquisaca, Bolivia (same partial contribution).
* Updated ZSOF/HFE to Hefei Xinqiao International Airport, Hefei, Anhui, China (was Hefei Luogang International
  Airport, which has been repurposed) (same partial contribution).


Version 20220913
================
* Added KXWA/XWA, Williston Basin International Airport, Williston, North Dakota, USA.
* Updated ME26 from defunct Super Cub Field, Westbrook, Maine, USA to Ragmuff Airport, Greenville, Maine, USA.


Version 20220831
===============
* Added UBTT/ZXT, Zabrat Airport, Baku, Bakı, Azerbaijan.


Version 20220824
================
* Added RPEN/ENI, El Nido Airport, El Nido, Palawan, Philippines (partially contributed upstream by `Leon Braun
  <https://github.com/OBrown92>`__  in PR `#65 <https://github.com/mwgg/Airports/pull/65>`__; fixed ICAO).
* Added ``py.typed`` marker file to implement `PEP 561 <https://peps.python.org/pep-0561/>`__.


Version 20220805
================
* Added ICAO Location Indicator EPKZ to OSZ, Koszalin Zegrze Airport, West Pomerania, Poland (contributed by `Błażej
  Cyrzon <https://github.com/bc291>`__ in PR `#15 <https://github.com/mborsetti/airportsdata/pull/15>`__).
* Added IATA Location Code FKN to KFKN, Franklin Municipal John Beverly Rose Airport, Franklin, Virginia, USA
  (contributed by `Błażej Cyrzon <https://github.com/bc291>`__ in PR `#15
  <https://github.com/mborsetti/airportsdata/pull/15>`__).


Version 20220731
================
* Added UECT/TLK, Talakan Airport, Lenskiy Ulus, Sakha, Russia (contributed by Vladimir Simakhin
  <https://github.com/vsimakhin>`__ upstream in PR `#60  <https://github.com/mwgg/Airports/pull/60>`__.
* Updated name and added IATA code to KORL/ORL, Orlando Executive Airport, Orlando, Florida, USA (partially
  contributed upstream by `jeremiahmorton20 <https://github.com/jeremiahmorton20>`__ in PR `#61
  <https://github.com/mwgg/Airports/pull/61>`__).
* Fixed city of KIAD/IAD, Washington Dulles International Airport, Dulles, Virginia, USA (contributed upstream by `Glenn
  Rempe <https://github.com/grempe>`__ in PR `#63  <https://github.com/mwgg/Airports/pull/63>`__).
  * Updated elevation of EDDB/SXF, Berlin Brandenburg Airport, Berlin, Germany (contributed upstream by `Vladimir
  Simakhin <https://github.com/vsimakhin>`__ in PR `#64  <https://github.com/mwgg/Airports/pull/64>`__).


Version 20220625
==================
* The source distribution is now available on PyPI to support certain packagers like `fpm` (contributed by Joe Groocock
  <https://github.com/frebib>`__ in PR `#14 <https://github.com/mborsetti/airportsdata/pull/14>`__).


Version 20220608
==================
* Added IATA identifier OGD to KOGD Ogden Hinckley Airport, Ogden, Utah, United States of America
  (contributed by `Spencer Yoder <https://github.com/Spencer-Yoder>`__ in PR `#13
  <https://github.com/mborsetti/airportsdata/pull/13>`__).
* Added IATA identifier PVU to KPVU Provo Municipal Airport, Provo, Utah, United States of America
  (contributed by `Spencer Yoder <https://github.com/Spencer-Yoder>`__ in PR `#13
  <https://github.com/mborsetti/airportsdata/pull/13>`__).
* Updated name from McCarran International Airport to Harry Reid International Airport for KLAS/LAS in Las Vegas,
  Nevada, United States of America (contributed by `Spencer Yoder <https://github.com/Spencer-Yoder>`__ in PR `#13
  <https://github.com/mborsetti/airportsdata/pull/13>`__).


Version 20220518
==================
* Added IATA identifier WMI to EPMO Warsaw Modlin Airport, Warsaw, Mazovia, Poland (contributed upstream by `drewblin
  <https://github.com/drewblin>`__ in PR `#59 <https://github.com/mwgg/Airports/pull/59>`__).


Version 20220512
==================
* Fixed ICAO identifier of LYPR/PRN Pristina International Airport, Prishtina, Pristina, Kosovo (was BKPR)
  (contributed by `Błażej Cyrzon <https://github.com/bc291>`__ in PR `#12
  <https://github.com/mborsetti/airportsdata/pull/12>`__).
* Added IATA code for KMDD Midland Airpark, Midland, Texas, USA (contributed upstream by
  `Henry A Schimke <https://github.com/hschimke>`__ in `#58 <https://github.com/mwgg/Airports/pull/58>`__).
* Added README_IATA with a list of IATA Multi Airport Cities.


Version 20220406
==================
* Added README to explain how airports with only an U.S. FAA or Transport Canada Location Identifier (FAA/TC LID) are
  listed in this database
* Removed support for Python 3.6, which has reached `end-of-life
  <https://devguide.python.org/devcycle/#end-of-life-branches>`__ and is no longer receiving security updates.
* Fixed FAOR/JNB O. R. Tambo International Airport, Johannesburg, Gauteng, South Africa (contributed upstream by
  `Waldgeister <https://github.com/Waldgeister>`__ in `#57 <https://github.com/mwgg/Airports/pull/57>`__).
* Removed defunct GMMC/CAS Anfa Airport, Casablanca, Casablanca-Settat, Morocco.
* Added WAWP/KXB Sangia Nibandera Airport, Kolaka, Southeast Sulawesi, Indonesia.
* Fixed FAA LID airports 06R to K06R and K15 to KK15.
* Added testing to ensure that all ICAO entries have 4 characters.


Version 20220107
==================
* Replaced MHSC/XPL Coronel Enrique Soto Cano Air Base, Comayagua, Comayagua, Honduras with MHPR/XPL
  Comayagua-Palmerola International Airport due to its conversion to a civil airport (started operations in
  October 2021) and retirement of MHSC.
* Fixed typo in name of LHBP/BUD Budapest Liszt Ferenc International Airport, Budapest, Budapest, Hungary (contributed
  upstream by `benelori <https://github.com/benelori>`__ in `#56 <https://github.com/mwgg/Airports/pull/56>`__).
  
Version 20211228.2
==================
* Upstream contributions by `rysiekpl <https://github.com/rysiekpl>`__ in `#54
  <https://github.com/mwgg/Airports/pull/55>`__:

  * Added EBMB Melsbroek Air Base, Brussels, Flanders, Belgium
  * Added EPEK Ełk-Makosieje Airport, Giże, Warmia-Masuria, Poland
  * Added EPGM Giżycko-Mazury Residence, Giżycko, Warmia-Masuria, Poland
  * Fixed ``icao`` of EPRU/CZW Częstochowa-Rudniki Airport (was EPCH)
  * Added EPSY Olsztyn-Mazury Airport, Szymany, Warmia-Mazury, Poland
  * Added EPWT Watorowo Airport, Watorowo, Kuyavian-Pomerania, Poland
  * Added ``iata`` ZWK to EPSU Suwalki Airport
* Restored most diacritical marks to ``icao`` entries starting with ``EP`` (Poland)


Version 20211228.1
==================
* Added KL52 Oceano County Airport, Oceano, California, United States of America (contributed by 
  `Michel Vidal-Naquet <https://github.com/micvn>`__ in `#8 <https://github.com/mborsetti/airportsdata/pull/8>`__)

Version 20211228
================
* Added KO69 Petaluma Municipal Airport, Petaluma, California, United States of America (contributed upstream by 
  `Michel Vidal-Naquet <https://github.com/micvn>`__ in `#55 <https://github.com/mwgg/Airports/pull/55>`__)

Version 20211030.1
==================
* Added VEKI/KBK Kushinagar Airport, Kushinagar, Uttar Pradesh, India (started operations on 20 October 2021)

Version 20211005
==================
* Support for Python 3.10

Version 20210926
==================
* Renamed KSJG to Northeast Florida Regional Airport (formerly St Augustine Airport)
* Upstream contributions by `himelsaha29 <https://github.com/himelsaha29>`__ in `#53
  <https://github.com/mwgg/Airports/pull/53>`__:

  * Added ``iata`` UST to KSJG Northeast Florida Regional Airport
  * Added UAAL/USJ Usharal Airport, Usharal, Kazakhstan
  * Added city to YBLN/BQB Busselton Regional Airport, Busselton, WA, Australia
* Python code now has more extensive type hints

Version 20210921
==================
* Added ZMCK/UBN Chinggis Khaan International Airport, Ulanbaatar, Mongolia (started operations on 4 July
  2021)
* Renamed ZMUB/ULN to Buyant-Ukhaa International Airport (formerly Chinggis Khaan International Airport, until 30 June
  2021)

Version 20210814.1
==================
* Updated EDDB (formerly IATA SXF) to be the new Berlin Brandenburg Airport (IATA BER)

Version 20210608.3
==================
* Added VVVD Van Don International Airport, Vân Đồn, Vietnam
* Fixed elevation being saved as float (with '.0' decimal) instead of integer; file is smaller as a result, with no
  change in precision
* Removed non-breaking spaces found in names of 4 airports
* Internal: implemented the `pathlib <https://docs.python.org/3/library/pathlib.html>`__ library

Version 20210525
================
* Added ``iata`` entry for PGUA/Andersen Air Force Base

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
