* All USA airports have been replaced with information sourced by the FAA. This consists of 12,566 operational airports
  located in the US and its territories, and covers country codes ``US``, ``PR`` (The Commonwealth of Puerto Rico),
  ``VI`` (The Virgin Islands of the United States), ``AS`` (The Territory of American Samoa), ``FM`` (The Federated
  States of Micronesia), ``GU`` (The Territory of Guam), ``MH`` (The Republic of the Marshall Islands), ``MP`` (The
  Commonwealth of the Northern Mariana Islands) and ``PW`` (The Republic of Palau).
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
