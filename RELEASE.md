Incorporated latest FAA data and corrected ICAO designators, cities and time zones worldwide.

- Dropped support for Python 3.11; added Python 3.15 (supported: 3.12–3.15). A reminder that older Python versions are
  supported for 3 years after being obsoleted by a new major release (i.e. about 4 years since their original release).
- Updated ICAO designators for the following 22 airports (ARP and/or elevation also updated where the AIP differed):

  - EDBN/FNB, Neubrandenburg Airport, Neubrandenburg, Mecklenburg-Vorpommern, DE (was ETNU). Source: AIP Germany AD 2
    EDBN, 29-Oct-26.
  - EDQG/GHF, Giebelstadt Airport, Giebelstadt, Bayern, DE: duplicate ETEU (Giebelstadt Army Air Field) removed and its
    IATA GHF moved to EDQG. Source: AIP Germany AD 2 EDQG, 29-Oct-26.
  - GAKD/KYS, Kayes Dag Dag Airport, Kayes, Kayes, ML (was GAKY). Source: ASECNA eAIP Mali AD 2 GAKD.
  - SJZL    , Fazenda Vaca Mocha Airport, Caracol, Mato Grosso do Sul, BR (was SDXR); subdivision corrected from
    "Concepcion" and tz from "America/Asuncion" to "America/Campo_Grande".
  - SSZK    , Fazenda Água Santa Airport, Perdizes, Minas Gerais, BR (was SNHR, now Aero Roça, Luziânia).
  - SWHN    , Fazenda Colibri Airport, Selvíria, Mato Grosso do Sul, BR (was SWJQ).
  - SWJQ    , Fazenda São João Airport, Paranhos, Mato Grosso do Sul, BR (was SIXQ); subdivision corrected from
    "Canindeyu" and tz from "America/Asuncion" to "America/Campo_Grande".
  - SVPH    , Punta Gorda Airport, Punta Gorda, Monagas, VE (was SVDG, not in the AIP); city added. Source: AIP
    Venezuela AD 4.1, AMDT AIRAC 7.
  - SVPX/PPH, Perai Tepuy Airport, Perai-Tepui, Bolivar, VE (was SVPH, which is Punta Gorda in the AIP). Source: AIP
    Venezuela AD 4.1, AMDT AIRAC 7.
  - SVWS    , El Piñal Airport, , Apure, VE (was SVPX, El Pinal Airport). Source: AIP Venezuela AD 4.1, AMDT AIRAC 7.
  - UBLC/LHL, Lachin International Airport, Laçın, Laçın, AZ (was _LHL; opened 28-May-25); ARP and city corrected,
    elevation approximate (about 1,750 m).
  - VAGD/GDB, Gondia Airport, Gondia, Maharashtra, IN (was VA2C); iata GDB and city added.
  - VAJL/JLG, Jalgaon Airport, Jalgaon, Maharashtra, IN (was VA47); iata JLG and city added.
  - VEBU/PAB, Bilaspur Airport, Bilaspur, Chhattisgarh, IN (was VABI).
  - VEKO/HJR, Khajuraho Airport, Khajuraho, Madhya Pradesh, IN (was VAKJ).
  - VERP/RPR, Swami Vivekananda Airport, Raipur, Chhattisgarh, IN (was VARP, Raipur Airport, in Madhya Pradesh).
  - VEST/TNI, Satna Airport, Satna, Madhya Pradesh, IN (was VIST).
  - VIPG    , Naini Saini Airport, Pithoragarh, Uttarakhand, IN (was VIDF, Pithorgarh Airport).
  - VOBM/IXG, Belagavi Airport, Belagavi, Karnataka, IN (was VABM, Belgaum Airport).
  - VOHB/HBX, Hubballi Airport, Hubballi, Karnataka, IN (was VAHB, Hubli Airport).
  - VOND/NDC, Shri Guru Gobind Singh Ji Airport, Nanded, Maharashtra, IN (was VAND, Nanded Airport).
  - ZSBA/BFY, Bengbu Tenghu Airport, Bengbu, Anhui, CN (was _BFY). Source: Wikipedia.

  Indian airports: source AIP India AD 2, AMDT 10/2026. Brazilian airports: source ROTAER (DECEA AISWEB), D-AMDT
  44/26, and the ANAC aerodrome registers of 29-Oct-26.

- Added the following 39 airports (source: national AIP, AD 2 or, where there is none, AD 1.3, except CYEP and YGLG):

  - CYEP    , Edmonton / Parkland Airport, Edmonton, Alberta, CA. Source: ARINC via SkyVector (not in AIP Canada AD 2).
  - DITM/TOZ, Mahana Airport, Touba, Woroba, CI.
  - EFPR    , Redstone Aero Airport, Pyhtää, Kymenlaakso, FI.
  - ENRE    , Rena Airport, Rena, Hedmark, NO.
  - FCOD/OLL, Denis Sassou N'Guesso Airport, Ollombo, Plateaux, CG.
  - FGAN/NBN, Annobon Airport, San Antonio de Pale, Annobon, GQ.
  - FGMM    , Mongomo Airport, Mongomo, Wele-Nzas, GQ.
  - FGMY/GEM, General Obiang Airport, Mongomeyen, Wele-Nzas, GQ.
  - FMGB    , Amborodia Airport, Bekopaka, , MG.
  - FMMB    , Ambatomainty Airport, Ambatomainty, , MG.
  - FMNB    , Ankaizina Airport, Bealanana, , MG.
  - FOGL    , Lebamba Airport, Lebamba, Ngouni, GA.
  - FTAA    , Amdjarass Airport, Amdjarass, Ennedi-Est, TD.
  - GAMN    , Bengassi Airport, Manantali, Kayes, ML.
  - NTAM/RMT, Rimatara Airport, Rimatara, Iles-Australes, PF.
  - NTKU/NKP, Nukutepipi Airport, Nukutepipi, Iles-Tuamotu-Gambier, PF.
  - OMEF    , Emirates Falcons Aeroclub, Al Ain, Abu Dhabi, AE.
  - OMRJ    , Jazirah Aviation Club, Ras Al Khaimah, Raʼs-al-Khaymah, AE.
  - RKTL/UJN, Uljin Airport, Uljin, Gyeongsangbuk-do, KR.
  - VAAM/AVR, Amravati Airport, Amravati, Maharashtra, IN.
  - VAMA    , Mundra Airport, Mundra, Gujarat, IN.
  - VASD/SAG, Shirdi Airport, Shirdi, Maharashtra, IN.
  - VEDG/RDP, Durgapur Airport, Durgapur, West Bengal, IN.
  - VEJR/JGB, Jagdalpur Airport, Jagdalpur, Chhattisgarh, IN.
  - VERW/REW, Rewa Airport, Rewa, Madhya Pradesh, IN.
  - VIDT/DPP, Datia Airport, Datia, Madhya Pradesh, IN.
  - VIMB/MZS, Moradabad Airport, Moradabad, Uttar Pradesh, IN.
  - VOPN/PUT, Sri Sathya Sai Airport, Puttaparthi, Andhra Pradesh, IN.
  - VOSR/SDW, Sindhudurg Airport, Kudal, Maharashtra, IN.
  - VOVI    , Bhogapuram International Airport, Vizianagaram, Andhra Pradesh, IN.
  - VTSY/BTZ, Betong Airport, Betong, Yala, TH (iata BTZ moved from LTBE, Bursa Airport, TR).
  - YGLG/GEX, Geelong Airport, Geelong, Victoria, AU (not AIP-verified).
  - ZMDN/ULZ, Otgontenger Airport, Uliastai, Zavkhan, MN.
  - ZMHG    , Khatgal Airport, Khatgal, Hovsgol, MN.
  - ZMKB    , Khanbumbat Airport, Khanbogd, Oemnogovi, MN.
  - ZMMG    , Mandalgobi Airport, Saintsagaan, Dundgovi, MN.
  - ZMSF    , Sky Friend Airport, Nalaikh, Ulaanbaatar, MN.
  - ZMTT    , Tavan Tolgoi Airport, Tsogttsetsii, Oemnogovi, MN.
  - ZMUH/UNR, Undurkhaan Airport, Kherlen, Hentiy, MN.

- Updated IATA locator (and potentially other data) for the following 3 airports:

  - BGQO/JJU, Qaqortoq Airport, Qaqortoq, Kujalleq, GL: iata JJU added (inherited from the closed Qaqortoq Heliport).
    Source: AIP Greenland AD 2 BGQO, AIRAC AMDT 03/26.
  - KDJT/DJT, President Donald J Trump International Airport, West Palm Beach, Florida, US: iata changed from PBI
    (effective 18-Aug-26; PBI is now the West Palm Beach city code).
  - LTBE    , Bursa Airport, Bursa, Bursa, TR: iata BTZ deleted (now Betong Airport, VTSY).

- Updated other data for the following 14 airports:

  - 70TT    , Big Bend Valley Airport, Terlingua, Texas, US: tz changed from "America/Chihuahua" to "America/Chicago".
  - K1S1    , Eckhart International Airport, Porthill, Idaho, US: tz changed from "America/Creston" to
    "America/Los_Angeles".
  - K3T9    , Big Bend Ranch State Park Airport, Presidio, Texas, US: tz changed from "America/Chihuahua" to
    "America/Chicago".
  - K4Z5    , Horsfeld Airport, Horsfeld, Alaska, US: tz changed from "America/Whitehorse" to "America/Anchorage".
  - KD49    , Columbus Municipal Airport, Columbus, North Dakota, US: tz changed from "America/Regina" to
    "America/Chicago".
  - KP16    , Palmyra (Cooper) Airport, Palmyra Island Atoll, , UM: tz changed from "Pacific/Kiritimati" (UTC+14) to
    "Pacific/Midway" (UTC−11).
  - KT89    , Lajitas International Airport, Lajitas, Texas, US: tz changed from "America/Chihuahua" to
    "America/Chicago".
  - LLFK    , Fiq Airfield, Katzrin, Quneitra, IL: tz changed from "Asia/Damascus" to "Asia/Jerusalem".
  - OIBH/IAQ, Bahregan Airport, Bandar Deylam, Bushehr, IR: city changed from "Bushehr", latitude changed from
    29.839667 to 29.839722, longitude changed from 50.272167 to 50.272222. Source: AIP Iran AD 2 OIBH, AIRAC AMDT 4/23.
  - SNVY    , Fazenda Ouro Verde Airport, Paranhos, Mato Grosso do Sul, BR: subdivision changed from "Canindeyu", tz
    from "America/Asuncion" to "America/Campo_Grande", elevation from 1299 to 1417. Source: ROTAER.
  - SSBV    , Bela Vista Airport, Bela Vista, Mato Grosso do Sul, BR: subdivision added, tz changed from
    "America/Asuncion" to "America/Campo_Grande".
  - SSFE    , Estância Hércules Airport, Foz do Iguaçu, Paraná, BR: name changed from "Estancia Hercules Airport", city
    from "Foz Do Iguacu", subdivision from "Alto-Parana", tz from "America/Asuncion" to "America/Sao_Paulo", elevation
    from 558 to 584. Source: ROTAER.
  - SSHX    , Fazenda Jatobá Airport, Paranhos, Mato Grosso do Sul, BR: name changed from "Fazenda Jatoba Airport",
    subdivision from "Canindeyu", tz from "America/Asuncion" to "America/Campo_Grande". Source: ROTAER.
  - SWBV    , Auaris Airport, Amajari, Roraima, BR: city changed from "Boa Vista", elevation from 2336 to 2492,
    latitude from 4.01639 to 4.002778, longitude from -64.51861 to -64.495556. Source: ROTAER.

- Removed the following 4 airports:

  - OI20    , Bahregan Airport, , Bushehr, IR: duplicate of OIBH (same aerodrome, ARP within 100 m). Source: AIP Iran
    AD 2 OIBH.
  - SJOI    , Fazenda Jaguatirica Airport, Porto Murtinho, Alto-Paraguay, BR: not in ROTAER or the ANAC registers
    (SJOI is now a heliport in Indaiatuba).
  - SSZK    , Sao Carlos Airport, Caracol, Concepcion, BR: not in ROTAER or the ANAC registers (SSZK reassigned, see
    above).
  - SWHN    , Fazenda Nossa Senhora de Fatima Airport, Nova Monte Verde, Mato Grosso do Sul, BR: not in the ANAC
    registers (SWHN reassigned, see above).

- Added the missing `city` (city served) to 665 airports in 65 countries. Where the national AIP was reachable (219
  airports), the city and its spelling are those of AD 2.2 (direction and distance from city) or, failing that, of the
  AIP's aerodrome listing; see [README_AIP.rst](README_AIP.rst) for the AIPs used.
- Updated the latitude, longitude and/or elevation of 2 airports where no change exceeded 0.1 degrees or 30 feet
  (not itemized).
- Fixed `iata_macs.csv`: added JNB (O. R. Tambo International Airport) to the Johannesburg (JNB) Multi Airport City
  (IATA Resolution 011c lists both HLA and JNB).
- Replaced `tz` names retired by IANA, therefore missing from some operating systems' time zone
  databases, with their current equivalents in 39 airports.
- Replaced `tz` names belonging to a neighbouring country per IANA with the airport's own country's
  zone at the same local time in 51 airports.

Updated FAA data:

- Updated ICAO designators for the following airport:

  - PAFT/FLT, Flat Airport, Flat, Alaska, US (was KFLT).

- Updated FAA LIDs (and the pseudo-ICAO codes derived from them) for the following 2 airports:

  - 17WA    , Fly For Fun Airport, Vancouver, Washington, US: FAA LID changed from W56 to 17WA (was KW56).
  - 37MI    , Milwrick Flying M Airport, Lincoln, Michigan, US: FAA LID changed from 3L7 to 37MI (was K3L7).

- Added the following 40 airports:

  - 02TT    , Lunacity Ranch Airfield, Cumby, Texas, US.
  - 12IL    , Nichols Aero Airport, South Beloit, Illinois, US.
  - 17TA    , Joy Airport, Denton, Texas, US.
  - 19TT    , Gator Bend Airport, Montgomery, Texas, US.
  - 1AA1    , Kogru River Airport, Nuiqsut, Alaska, US.
  - 1IN2    , Jackson Field, Muncie, Indiana, US.
  - 1WA3    , Columbia Crest Winery Airport, Paterson, Washington, US.
  - 22IS    , Steward Rla Airport, Durand, Illinois, US.
  - 22TT    , Flying G Ranch Airport, Fredericksburg, Texas, US.
  - 26XA    , Li-Luframost Ranch Airport, Hamilton, Texas, US.
  - 29XS    , The Zoo Airport, Anderson, Texas, US.
  - 2TS4    , Circle R Ranch Airport, Malakoff, Texas, US.
  - 33MT    , Evaro Hills Estates Airpark, Missoula, Montana, US.
  - 39MN    , Gades Farm Airport, Montevideo, Minnesota, US.
  - 3IA4    , Cy Landing Airport, Dewitt, Iowa, US.
  - 3IA9    , Schnack Field, Malone, Iowa, US.
  - 40ND    , Gorder Farm Airport, Galchutt, North Dakota, US.
  - 4CO9    , Maria Vilma Field, Brighton, Colorado, US.
  - 4IA6    , Spies Field, De Witt, Iowa, US.
  - 51IL    , Roca Grande Rla Airport, Big Rock, Illinois, US.
  - 57OH    , Flying W Airport, Amanda, Ohio, US.
  - 5CO7    , Virga Ridge Field, Wellington, Colorado, US.
  - 66TS    , Fannin Field, Goliad, Texas, US.
  - 68MD    , Highrock Airfield, Rawlings, Maryland, US.
  - 6TE9    , Mc Kenzie Field, Avinger, Texas, US.
  - 6TN0    , Flying A Estates Airport, Tellico Plains, Tennessee, US.
  - 70CO    , Bonanza Airpark, Villa Grove, Colorado, US.
  - 7KY7    , Woodford Aviation Airport, Millville, Kentucky, US.
  - 82WY    , Miller Strip, Lusk, Wyoming, US.
  - 82XA    , Gfh Airport, Richmond, Texas, US.
  - 8WA2    , Island Aire Farms Airport, Cathlamet, Washington, US.
  - 95WY    , Rocking T Airport, Lusk, Wyoming, US.
  - 9FA9    , Flying Wm Airport, Groveland, Florida, US.
  - CO40    , Plane And Mane Airport, Franktown, Colorado, US.
  - K3B4    , Seacoast Airfield, Eliot, Maine, US.
  - OL73    , Ak Ranch Airport, Guthrie, Oklahoma, US.
  - TE23    , Bedias Executive Airport, Bedias, Texas, US.
  - TS19    , Uncle Raymonds Airport, Giddings, Texas, US.
  - TS33    , Fox Garden Aero Airport, Star, Texas, US.
  - WY70    , Lowmiller Airport, Lovell, Wyoming, US.

- Updated other data for the following 19 airports:

  - 04OR    , Collins Landing Strip, Mitchell, Oregon, US: elevation changed from 1500 to 1608, latitude changed from
    44.749855 to 44.733251, longitude changed from -120.201129 to -120.163702.
  - 14XS    , Nissix Air And Drone Port Airport, Davilla, Texas, US: name changed from "Isbell Ranch Airport".
  - 28FL    , Mount Up With Wings Airpark, Cresent City, Florida, US: name changed from "Jim Finlay Farm Airport".
  - 2CO2    , Las Arenas Earth And Sky Observatory Airport, Alamosa, Colorado, US: elevation changed from 7582 to 7625,
    latitude changed from 37.477822 to 37.47878, longitude changed from -105.615803 to -105.632431.
  - 2FA3    , Long Branch Farm Airport, Baker, Florida, US: name changed from "Long Branch Farms Airport", latitude
    changed from 30.812739 to 30.812827, longitude changed from -86.637361 to -86.640222.
  - 58KY    , Willow Island Airpark, Finchville, Kentucky, US: elevation changed from 740 to 701, latitude changed from
    38.121658 to 38.118754, longitude changed from -85.332556 to -85.330593.
  - 69IL    , Mitchell - Gillespie Airport, Marseilles, Illinois, US: name changed from "David Gillespie Airport".
  - 69OK    , Uncle Kenny's Aerodrome, Fairland, Oklahoma, US: name changed from "Green Country Airpark".
  - 93IL    , Schneider Rla Airport, Flanagan, Illinois, US: name changed from "Scneider Rla Airport".
  - K4A5    , Buffalo River Airport, Marshall, Arkansas, US: name changed from "Searcy County Airport".
  - K4U9    , Hyak Airbase Airport, Dell, Montana, US: name changed from "Dell Flight Strip", latitude changed from
    44.73575 to 44.735758, longitude changed from -112.719694 to -112.71969.
  - KBVN    , Albion Municipal/Ron Levander Field, Albion, Nebraska, US: name changed from "Albion Municipal Airport".
  - KGBG/GBG, Galesburg Regional Hw Timmons Airport, Galesburg, Illinois, US: name changed from "Harrel W Timmons
    Galesburg Regional Airport".
  - KGRF/GRF, Gray Army Air Field (Joint Base Lewis-McChord) Airport, Joint Base Lewis McChord, Washington, US: city
    changed from "Fort Lewis/Tacoma".
  - KSAW/MQT, Marquette Sawyer Regional Airport, Marquette, Michigan, US: name changed from "Marquette/Sawyer Regional
    Airport".
  - NA60    , Aslesen West Airport, Grandin, North Dakota, US: name changed from "Dakota Airport".
  - OK11    , Shelby Airport, Comanche, Oklahoma, US: name changed from "Ksa Orchards Airport".
  - TX22    , US Trinity Airport, Argyle, Texas, US: name changed from "Leroux Airport".
  - UT26    , Bryce Woodland Estates Landing Strip, Hatch, Utah, US: elevation changed from 7600 to 7722, latitude
    changed from 37.584426 to 37.537395, longitude changed from -112.392427 to -112.430074.

- Removed the following 29 airports:

  - 00IS     Hayenga's Cant Find Farms Airport, Kings, Illinois, US: LID not in A/FD.
  - 0LL4     Flaherty Field, La Salle, Illinois, US: LID not in A/FD.
  - 0WY1     Dorsey Creek Ranch Airport, Basin, Wyoming, US: LID not in A/FD.
  - 13KY     Miles Airport, Owensboro, Kentucky, US: LID not in A/FD.
  - 21OG     Ames Airport, Jefferson, Oregon, US: LID not in A/FD.
  - 2ND3     Casslindan Airport, Grand Forks, North Dakota, US: LID not in A/FD.
  - 60XA     Skyline Ranch Airport, Georgetown, Texas, US: LID not in A/FD.
  - 69TS     White Airport, Killeen, Texas, US: LID not in A/FD.
  - 7MI7     Walker Airport, Cooper, Michigan, US: LID not in A/FD.
  - 88OR     Tallman Airport, Lebanon, Oregon, US: LID not in A/FD.
  - 8PA3     Deer Meadows Airstrip, Weatherly, Pennsylvania, US: LID not in A/FD.
  - 9TX1     Bar S Ranch Airport, Giddings, Texas, US: LID not in A/FD.
  - CD23     Aero Bear Field, Calhan, Colorado, US: LID not in A/FD.
  - IL84     Douglas Airport, Colusa, Illinois, US: LID not in A/FD.
  - IL88     Earl Barnickel Airport, Compton, Illinois, US: LID not in A/FD.
  - K2E2     Sharpe's Strip, Emmett, Michigan, US: LID not in A/FD.
  - K55G     Arnold Field, Croswell, Michigan, US: LID not in A/FD.
  - KD59     Gowanda Airport, Gowanda, New York, US: LID not in A/FD.
  - LS10     Reynolds Airport, Westlake, Louisiana, US: LID not in A/FD.
  - MY66     North Star Ranch Airport, Onamia, Minnesota, US: LID not in A/FD.
  - ND44     Underwood Airport, Underwood, North Dakota, US: LID not in A/FD.
  - TE45     Buffalo Chips Airpark, Joshua, Texas, US: LID not in A/FD.
  - TX14     Boneyard Airstrip, Washington, Texas, US: LID not in A/FD.
  - TX45     Hawkeye Hunting Club Airport, Center, Texas, US: LID not in A/FD.
  - WI51     Del Monte Airport, Arlington, Wisconsin, US: LID not in A/FD.
  - XA12     Mcfarlin Ranch Airport, Bertram, Texas, US: LID not in A/FD.
  - XA96     En Gedi Ranch Airport, Canadian, Texas, US: LID not in A/FD.
  - XS21     H & S Airfield, Damon, Texas, US: LID not in A/FD.
  - XS27     Farm Air Service Airport, Nome, Texas, US: LID not in A/FD.

- Also updated the latitude, longitude and/or elevation of 79 airports where no change exceeded 0.1 degrees or 30 feet
  (not itemized).
