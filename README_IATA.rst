.. |IATA_MACs| replace:: 41

.. |IATA_MACs_apts| replace:: 89

IATA resolution 011c adopted at the 3rd IATA Passenger Standards Conference October 2021 in PTC123(186), for intended
implementation date of 3 October 2022, defines |IATA_MACs| Multi Airport Cities (comprising of a total of
|IATA_MACs_apts| airports) which consist of a mix of identifiers that are identical to Airport ones (e.g. ``DXB``) and others that are unique (e.g. ``NYC``). As a tool for users, we provide the |IATA_MACs| IATA Multi Airport Cities

* in the table below;
* as a csv file named ``iata_macs.csv``; and
* as a Python dict containing the data for each individual airport of a Multi Airport City:

.. code-block:: python

   import airportsdata
   iata_macs = airportsdata.load_iata_macs()
   print(iata_macs['NYC'])

.. code-block::

   'airports': {'JFK': {'city': 'New York',
                        'country': 'US',
                        'elevation': 13.0,
                        'iata': 'JFK',
                        'icao': 'KJFK',
                        'lat': 40.63993,
                        'lid': 'JFK',
                        'lon': -73.77869,
                        'name': 'John F Kennedy International Airport',
                        'subd': 'New York',
                        'tz': 'America/New_York'},
                'LGA': {'city': 'New York',
                        'country': 'US',
                        'elevation': 20.6,
                        'iata': 'LGA',
                        'icao': 'KLGA',
                        'lat': 40.77725,
                        'lid': 'LGA',
                        'lon': -73.87261,
                        'name': 'Laguardia Airport',
                        'subd': 'New York',
                        'tz': 'America/New_York'}},
   'country': 'US',
   'name': 'New York'}


Please note that some GDSs and/or websites use their own custom-defined metropolitan areas, typically appropriating
codes that are not official IATA Location Identifiers (e.g. Travelport's ``QBA`` for the San Francisco Bay Area); these are not part of this database.

Also keep in mind that we do not have IATA Location Identifiers for surface transportation locations (we only support
airports).

**City Code Directory (CCD) – Multi Airport Cities list**

.. list-table::
   :header-rows: 1

   * - Country
     - City Code
     - City Name
     - Airport Code
     - Airport Name
   * - AE
     - DXB
     - Dubai
     - DWC
     - Al Maktoum Intl
   * - AE
     - DXB
     - Dubai
     - DXB
     - International
   * - AR
     - BUE
     - Buenos Aires
     - AEP
     - Jorge Newbery
   * - AR
     - BUE
     - Buenos Aires
     - EZE
     - Ministro Pistarini
   * - AU
     - MEL
     - Melbourne
     - AVV
     - Avalon
   * - AU
     - MEL
     - Melbourne
     - MEL
     - Melbourne Airport
   * - BE
     - BRU
     - Brussels
     - BRU
     - Brussels Airport
   * - BE
     - BRU
     - Brussels
     - CRL
     - Brussels S. Charleroi
   * - BR
     - BHZ
     - Belo Horizonte
     - CNF
     - Tancredo Neves Intl
   * - BR
     - BHZ
     - Belo Horizonte
     - PLU
     - Pampulha
   * - BR
     - RIO
     - Rio de Janeiro
     - GIG
     - Galeao-A.C.Jobim Intl
   * - BR
     - RIO
     - Rio de Janeiro
     - SDU
     - Santos Dumont
   * - BR
     - SAO
     - Sao Paulo
     - CGH
     - Congonhas
   * - BR
     - SAO
     - Sao Paulo
     - GRU
     - Guarulhos Intl
   * - BR
     - SAO
     - Sao Paulo
     - VCP
     - Viracopos-Campinas In
   * - CA
     - YTO
     - Toronto
     - YTZ
     - Billy Bishop City A/P
   * - CA
     - YTO
     - Toronto
     - YYZ
     - Lester B. Pearson Int
   * - CN
     - BJS
     - Beijing
     - PEK
     - Capital Intl
   * - CN
     - BJS
     - Beijing
     - PKX
     - Daxing Intl.
   * - CN
     - SHA
     - Shanghai
     - PVG
     - Pudong Intl
   * - CN
     - SHA
     - Shanghai
     - SHA
     - Hongqiao Intl
   * - ES
     - TCI
     - Tenerife
     - TFN
     - Tenerife-Norte
   * - ES
     - TCI
     - Tenerife
     - TFS
     - Tenerife-Sur
   * - FR
     - PAR
     - Paris
     - CDG
     - Charles de Gaulle
   * - FR
     - PAR
     - Paris
     - ORY
     - Orly
   * - GB
     - BFS
     - Belfast
     - BFS
     - International
   * - GB
     - BFS
     - Belfast
     - BHD
     - George Best City Apt
   * - GB
     - LON
     - London
     - LCY
     - City Airport
   * - GB
     - LON
     - London
     - LGW
     - Gatwick
   * - GB
     - LON
     - London
     - LHR
     - Heathrow
   * - GB
     - LON
     - London
     - LTN
     - Luton
   * - GB
     - LON
     - London
     - STN
     - Stansted
   * - ID
     - JKT
     - Jakarta
     - CGK
     - Soekarno-Hatta Intl
   * - ID
     - JKT
     - Jakarta
     - HLP
     - Halim Perdanakusuma
   * - ID
     - JOG
     - Yogyakarta
     - JOG
     - Adisutjipto
   * - ID
     - JOG
     - Yogyakarta
     - YIA
     - New Yogyakarta Int.
   * - IR
     - THR
     - Tehran
     - IKA
     - Imam Khomeini Intl
   * - IR
     - THR
     - Tehran
     - THR
     - Mehrabad Intl
   * - IS
     - REK
     - Reykjavik
     - KEF
     - Keflavik International
   * - IS
     - REK
     - Reykjavik
     - RKV
     - Reykjavik Domestic
   * - IT
     - MIL
     - Milan
     - BGY
     - Bergamo/Orio al Serio
   * - IT
     - MIL
     - Milan
     - LIN
     - Linate
   * - IT
     - MIL
     - Milan
     - MXP
     - Malpensa
   * - IT
     - ROM
     - Rome
     - CIA
     - Ciampino
   * - IT
     - ROM
     - Rome
     - FCO
     - Fiumicino
   * - JP
     - NGO
     - Nagoya
     - NGO
     - Chubu Centrair International
   * - JP
     - NGO
     - Nagoya
     - NKM
     - Nagoya (Komaki)
   * - JP
     - OSA
     - Osaka
     - ITM
     - Osaka Intl (Itami)
   * - JP
     - OSA
     - Osaka
     - KIX
     - Kansai International
   * - JP
     - OSA
     - Osaka
     - UKB
     - Kobe
   * - JP
     - SPK
     - Sapporo
     - CTS
     - New Chitose
   * - JP
     - SPK
     - Sapporo
     - OKD
     - Okadama
   * - JP
     - TYO
     - Tokyo
     - HND
     - Tokyo Intl (Haneda)
   * - JP
     - TYO
     - Tokyo
     - NRT
     - Narita Intl
   * - KR
     - SEL
     - Seoul
     - GMP
     - Gimpo International
   * - KR
     - SEL
     - Seoul
     - ICN
     - Incheon International
   * - SL
     - SLU
     - St Lucia
     - SLU
     - George F.L. Charles
   * - SL
     - SLU
     - St Lucia
     - UVF
     - Hewanorra Int’l
   * - NO
     - OSL
     - Oslo
     - OSL
     - Gardermoen
   * - NO
     - OSL
     - Oslo
     - TRF
     - Sandefjord-Torp
   * - RU
     - MOW
     - Moscow
     - DME
     - Domodedovo
   * - RU
     - MOW
     - Moscow
     - SVO
     - Sheremetyevo
   * - RU
     - MOW
     - Moscow
     - VKO
     - Vnukovo
   * - SE
     - STO
     - Stockholm
     - ARN
     - Arlanda
   * - SE
     - STO
     - Stockholm
     - BMA
     - Bromma
   * - SN
     - DKR
     - Dakar
     - DKR
     - Leopold Sedar Senghor
   * - SN
     - DKR
     - Dakar
     - DSS
     - Blaise Diagne Intl
   * - TH
     - BKK
     - Bangkok
     - BKK
     - Suvarnabhumi Airport
   * - TH
     - BKK
     - Bangkok
     - DMK
     - Don Mueang Int'l
   * - TR
     - ANK
     - Ankara
     - ANK
     - Etimesgut
   * - TR
     - ANK
     - Ankara
     - ESB
     - Esenboga
   * - TR
     - IST
     - Istanbul
     - ISL
     - Ataturk
   * - TR
     - IST
     - Istanbul
     - IST
     - Istanbul Airport
   * - TR
     - IST
     - Istanbul
     - SAW
     - Sabiha Gokcen
   * - TW
     - TPE
     - Taipei
     - TPE
     - Taoyuan International Airport
   * - TW
     - TPE
     - Taipei
     - TSA
     - Songshan
   * - UA
     - IEV
     - Kyiv
     - IEV
     - Kyiv International Airport
   * - UA
     - IEV
     - Kyiv
     - KBP
     - Boryspil Intl
   * - US
     - CHI
     - Chicago
     - MDW
     - Midway International
   * - US
     - CHI
     - Chicago
     - ORD
     - O'Hare International
   * - US
     - DFW
     - Dallas
     - DAL
     - Love Field
   * - US
     - DFW
     - Dallas
     - DFW
     - Dallas/Ft Worth Intl
   * - US
     - HOU
     - Houston
     - HOU
     - William P Hobby Airport
   * - US
     - HOU
     - Houston
     - IAH
     - George Bush Intercontinental
   * - US
     - NYC
     - New York
     - JFK
     - John F Kennedy Intl
   * - US
     - NYC
     - New York
     - LGA
     - LaGuardia
   * - US
     - WAS
     - Washington
     - DCA
     - Ronald Reagan National
   * - US
     - WAS
     - Washington
     - IAD
     - Dulles Intl
   * - ZA
     - JNB
     - Johannesburg
     - HLA
     - Lanseria International
   * - ZA
     - JNB
     - Johannesburg
     - JNB
     - \O. R. Tambo International Airport
