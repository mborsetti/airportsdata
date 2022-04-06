* Added README to explain how airports with only an U.S. FAA or Transport Canada Location Identifier location identifier
  (FAA/TC LID) are listed in this database
* Removed support for Python 3.6, which has reached `end-of-life
  <https://devguide.python.org/devcycle/#end-of-life-branches>`__ and is no longer receiving security updates.
* Fixed FAOR/JNB O. R. Tambo International Airport, Johannesburg, Gauteng, South Africa (contributed upstream by
  `Waldgeister <https://github.com/Waldgeister>`__ in `#57 <https://github.com/mwgg/Airports/pull/57>`__).
* Removed defunct GMMC/CAS Anfa Airport, Casablanca, Casablanca-Settat, Morocco.
* Added WAWP/KXB Sangia Nibandera Airport, Kolaka, Southeast Sulawesi, Indonesia.
* Fixed FAA LID airports 06R to K06R and K15 to KK15.
* Added testing to ensure that all ICAO entries have 4 characters.
