=======================
Pseudo-ICAO Identifiers
=======================

For airports that lack an ICAO Location Indicator, we generate a Pseudo-ICAO Identifier as follows.

U.S. FAA-only entries
----------------------

This database uses FAA data for all operational public use airports in these ISO 3166-1 countries:

- ``AS`` (The Territory of American Samoa),
- ``FM`` (The Federated States of Micronesia),
- ``GU`` (The Territory of Guam),
- ``MH`` (The Republic of the Marshall Islands),
- ``MP`` (The Commonwealth of the Northern Mariana Islands),
- ``PR`` (The Commonwealth of Puerto Rico) (saved as subdivision "Puerto Rico" of country US),
- ``PW`` (The Republic of Palau),
- ``UM`` (The United States Minor Outlying Islands),
- ``US`` (The United States of America),
- ``VI`` (The Virgin Islands of the United States) (saved as subdivision "Virgin Islands" of country US).

Many of the airports in country ``US`` do not have an ICAO Location Indicator, but only have a Location Identifier
assigned by the FAA ('FAA LID'). For the purposes of this database, these have been given a Pseudo-ICAO Identifier as
follows:

* If the airport has a 4-digit FAA LID, the LID is used. These Identifiers are distinguishable from ICAO Location
  Indicators as they contain at least one character that is a number, while ICAO Location Indicators are all letters.
* If the airport has a 3-digit FAA LID, the LID is prefaced with '``K``' to generate a Pseudo-ICAO Identifier that is
  4 character long. To know if an entry in this database starting with ``K`` is a true ICAO Location Indicator or an
  internal Pseudo-ICAO Identifier, check the LID field.


IATA-only entries
-----------------

A few seaplane bases have a IATA Location Code but not an ICAO Location Indicator; for the purposes of this database,
these have been given a Pseudo-ICAO Identifier comprising of '``_``' (underscore) + the IATA Location Indicator.

An example is the Yas Island Seaplane Base in Abu Dhabi, which is assigned the internal Pseudo-ICAO Identifier of
'``_AYM``'.
