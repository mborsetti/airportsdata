#########
Changelog
#########

This changelog mostly follows `keep a changelog <https://keepachangelog.com/en/1.0.0/>`__. Release numbering is based
on the UTC date of the release.

`Contributions <https://github.com/mborsetti/airportdata/blob/master/CHANGELOG.rst>`__ always welcomed!


Version 2026.08.03
==================

* Updated ICAO designators for the following 5 airports:

  - SBJH/JHF, São Paulo Catarina Executive Airport, São Roque, São Paulo, BR (was SBHJ).
  - SNZB    , Rancho Sumidor Airport, Rio Do Oeste, Santa Catarina, BR (was SSRS).
  - SSRS/BRB Barreirinhas Airport, , Maranhão, BR (was SBRR).
  - UZTC    , Chirchik Airport, Chirchik, Toshkent, UZ (was UA66).
  - ZSJX/JNH, Jiaxing Nanhu Airport, Jiaxing, Zhejiang, CN (was _JNH).

* Added the following airport:

  - ZSYA/YTY, Yangzhou Taizhou Airport, Yangzhou, Jiangsu, CN.

* Updated IATA locator (and potentially other data) for the following 2 airports:

  - KDJT/PBI, President Donald J Trump International Airport, West Palm Beach, Florida, US: iata PBI added (moved from KPBI, a duplicate in error).
  - SBMT    , Campo de Marte Airport, Sao Paulo, São Paulo, BR: iata "SAO" deleted.

* Updated other data for the following 4 airports:

  - LTFM/IST, Istanbul Airport, Arnavutköy, Istanbul, Istanbul, TR: city changed from "Istanbul".
  - SBNT    , Campo Augusto Severo Airport (Base Aérea de Natal), Parnamirim, Rio Grande do Norte, BR: name changed from
    "Augusto Severo Airport (Base Aérea de Natal)".
  - WIMM/KNO, Polonia International Airport, Medan, Sumatra Island, North Sumatra, ID: latitude changed from 3.55806 to
    3.637847, longitude changed from 98.6717 to 98.870566.
  - YSWS/WSI, Western Sydney International (Nancy-Bird Walton) Airport, Badgerys Creek, New South Wales, AU: name
    changed from "Western Sydney Airport (under construction)".

* Removed the following airport:

  - KPBI/PBI Palm Beach International Airport, West Palm Beach, Florida, US (duplicate in error of KDJT).


Version 2026.08.02
==================

* Support for Python 3.10 has been dropped. As a reminder, older Python versions are supported for 3
  years after being superseded by a new major release (i.e. approximately 4 years after their initial release).

Incorporated latest FAA data.

* Added the following 102 airports:

  - 01TA    , Hd Farm & Ranch Airport, Burnet, Texas, US.
  - 03WY    , Perala Field, Sundance, Wyoming, US.
  - 0MN8    , Fagen Field, Granite Falls, Minnesota, US.
  - 0TX8    , Lz Mustang Airport, Kosse, Texas, US.
  - 0TX9    , Card Aerodrome, Greenville, Texas, US.
  - 10AN    , Hilton Field, Delta Junction, Alaska, US.
  - 18TA    , West Kerr Ranch Airport, Junction, Texas, US.
  - 1AZ2    , Kirkland Valley Airport, Kirkland, Arizona, US.
  - 1TN7    , Paynes Landing Airport, Lynchburg, Tennessee, US.
  - 1XA0    , Dw Airport, Gustine, Texas, US.
  - 20NV    , Iveson Ranch Airport, Gerlach, Nevada, US.
  - 24TT    , Mccutchen Landings Airport, Mertzon, Texas, US.
  - 26AL    , S.C. Stagner Field, Saraland, Alabama, US.
  - 26ND    , Fleck Airfield, Mandan, North Dakota, US.
  - 2AL4    , Tranquility Base Airport, Springville, Alabama, US.
  - 2LA3    , Baham Airstrip, Opelousas, Louisiana, US.
  - 2MI8    , Cackleberry Airport, Dexter, Michigan, US.
  - 34TA    , Zq Ranch Airport, Wolfe City, Texas, US.
  - 36TT    , Skyview 360 Airport, Round Mountain, Texas, US.
  - 3ID9    , West Mountain Airport, Cascade, Idaho, US.
  - 3IN1    , Weimer Field, Knightstown, Indiana, US.
  - 3KY1    , Big Sky Adventures Airport, Nicholasville, Kentucky, US.
  - 3OK1    , Rotorhead Ranch Airport, Ramona, Oklahoma, US.
  - 3TX2    , Lewis Field, Ravenna, Texas, US.
  - 45NE    , Mitchell Field, Amherst, Nebraska, US.
  - 45NK    , Negrich Field, Mayfield, New York, US.
  - 45TA    , Quihi Creek Vineyard Airport, Hondo, Texas, US.
  - 47IL    , Ebert Field, Ashton, Illinois, US.
  - 49AL    , Pleasant View Farm Airport, Elberta, Alabama, US.
  - 4OK8    , Justice Field, Stillwater, Oklahoma, US.
  - 52IL    , Denham Rla Airport, Windsor, Illinois, US.
  - 55IL    , Ebert Field Rla Airport, Ashton, Illinois, US.
  - 58FL    , Blackwater Landing Airport, Gainesville, Florida, US.
  - 58IL    , Charles Park Rla Airport, Stanford, Illinois, US.
  - 58SC    , Cherry Grove Airport, Green Sea, South Carolina, US.
  - 62LA    , Tow's Field, Erath, Louisiana, US.
  - 68KY    , Double C Field, Benton, Kentucky, US.
  - 69TE    , Deer Pasture Airport, Lampasas, Texas, US.
  - 6OK7    , Bryan Brothers Ranch Airport, Welch, Oklahoma, US.
  - 70TN    , Roberts Roost Airport, Sparta, Tennessee, US.
  - 72OH    , No Fly Zone Airport, Casstown, Ohio, US.
  - 76NR    , Pathfinder Field, Raeford, North Carolina, US.
  - 78TN    , Earhart Landing Airport, Madison, Tennessee, US.
  - 79AZ    , Sentiel Airport, Marana, Arizona, US.
  - 79MS    , Thornton Field, Seminary, Mississippi, US.
  - 7ME7    , Stevens Field, Sebec, Maine, US.
  - 82AZ    , Ridgeline Airpark, Green Valley, Arizona, US.
  - 83TN    , Highland Ridge Field, Lafayette, Tennessee, US.
  - 86IL    , Wenona Rla Airport, Wenona, Illinois, US.
  - 8AL8    , Sanca Farm Skyport Airport, Robertsdale, Alabama, US.
  - 8FA8    , Flying H Airport, Lake Placid, Florida, US.
  - 92XA    , Morgenroth Airport, Victoria, Texas, US.
  - 93NR    , Raleigh East Airport, Knightdale, North Carolina, US.
  - 9OK5    , Possumhaw Airport, Welch, Oklahoma, US.
  - 9WI8    , Fletcher Airport, Spring Prairie, Wisconsin, US.
  - 9WI9    , Carlson Airport, Superior, Wisconsin, US.
  - 9WN1    , Courtney Plummer Airport, Winneconne, Wisconsin, US.
  - 9WN2    , Voyager Village Airstrip, Webster, Wisconsin, US.
  - 9WN5    , Lodi Lakeland Airport, Lodi, Wisconsin, US.
  - 9WN6    , Oostburg Airport, Oostburg, Wisconsin, US.
  - 9WS2    , Antique Aerodrome, De Pere, Wisconsin, US.
  - 9XA4    , Chimera Aerodrome, Venus, Texas, US.
  - 9XS1    , The Landing Airport, Hill, Texas, US.
  - 9XS4    , Mc Keon Aviation Airport, Denison, Texas, US.
  - 9XS6    , Sudan Airport, Sudan, Texas, US.
  - CD02    , Scenic Mesa Ranch Airport, Hotchkiss, Colorado, US.
  - IL73    , Clair Rla Airport, Loraine, Illinois, US.
  - K11T    , Rocking L Airport, Sonora, Texas, US.
  - K35W    , Port Washington/Didier Field, Port Washington, Wisconsin, US.
  - K51C    , Orban Airport, Dewitt, Michigan, US.
  - K7KS    , Coyote Creek Airport, Fuley, Kansas, US.
  - K8SD    , Bowdle Municipal Airport, Bowdle, South Dakota, US.
  - KDJT    , President Donald J Trump International Airport, West Palm Beach, Florida, US.
  - KOK2    , Red River Airport, Kingston, Oklahoma, US.
  - KRYA    , Wray Municipal Airport, Wray, Colorado, US.
  - KTF9    , Taylor Flat Airport, Dutch John, Utah, US.
  - MD85    , Oag Unmanned Center Airport, Piney Point, Maryland, US.
  - MI98    , Poulter Field, Chelsea, Michigan, US.
  - MT85    , Dawsons Landing Airport, Worden, Montana, US.
  - NR57    , Hawks Nest Airport, Kenly, North Carolina, US.
  - OI71    , Germack Airport, Geneva, Ohio, US.
  - OI88    , Ada Airport, Ada, Ohio, US.
  - OL03    , Ledford Farm Airport, Nida, Oklahoma, US.
  - OL51    , Rivercamp Airport, Carter, Oklahoma, US.
  - PR36    , Cocal Airport, Toa Baja, Puerto Rico, US.
  - PS36    , Swank Airport, Clarksburg, Pennsylvania, US.
  - TA09    , Flying W Airstrip, Uvalde, Texas, US.
  - TA88    , Borich Sky Ranch Airport, Coupland, Texas, US.
  - TS28    , Cherry Heights Flugplatz Airport, Fredericksburg, Texas, US.
  - TT36    , Myrtle Creek Ranch Airport, Franklin, Texas, US.
  - TT54    , Whiskey Hotel Airpark, Fredericksburg, Texas, US.
  - TT61    , Salado Bluffs Airport, Salado, Texas, US.
  - TT68    , U Ranch Airport, Sterling City, Texas, US.
  - TT80    , Pecan Valley Airport, Killeen, Texas, US.
  - TT86    , Buffalo Ridge Airport, Stephenville, Texas, US.
  - TT94    , Cedar Creek Ranch Airport, Barksdale, Texas, US.
  - TX65    , Pinto Creek Airport, Brackettville, Texas, US.
  - VG19    , Sawyer Airport, New Church, Virginia, US.
  - WI26    , Flying Fox Airport, Williams Bay, Wisconsin, US.
  - WN40    , Coupeville Airpark, Coupeville, Washington, US.
  - WT05    , Quartzite Air Ranch Airport, Chewelah, Washington, US.
  - WY36    , Bakers Field, Powell, Wyoming, US.

* The FAA has assigned ICAO codes to the following 16 Alaska airports, previously listed under pseudo-ICAO codes;
  their IATA codes and other data are unchanged, and the pseudo-ICAO entries have been removed:

  - PAAB/ATT, Atmautluak Airport, Atmautluak, Alaska, US (was K4A2).
  - PAAC/PQS, Pilot Station Airport, Pilot Station, Alaska, US (was K0AK).
  - PAAE/KOZ, Ouzinkie Airport, Ouzinkie, Alaska, US (was K4K5).
  - PAAF/MNT, Minto Al Wright Airport, Minto, Alaska, US (was K51Z).
  - PAAG/   , Chandalar Shelf Airport, Chandalar Camp, Alaska, US (was K5CD).
  - PAAH/   , Kantishna Airport, Kantishna, Alaska, US (was K5Z5).
  - PAAJ/WTL, Tuntutuliak Airport, Tuntutuliak, Alaska, US (was KA61).
  - PAAO/   , Lake Louise Airport, Lake Louise, Alaska, US (was KZ55).
  - PAAR/KBC, Birch Creek Airport, Birch Creek, Alaska, US (was KZ91).
  - PAAS/WBB, Stebbins Airport, Stebbins, Alaska, US (was KWBB).
  - PAAU/SXP, Nunam Iqua Airport, Nunam Iqua, Alaska, US (was KSXP).
  - PAAV/KEK, Ekwok Airport, Ekwok, Alaska, US (was KKEK).
  - PAAW/KEB, Nanwalek Airport, Nanwalek, Alaska, US (was KKEB).
  - PAAX/CXC, Chitina Airport, Chitina, Alaska, US (was KCXC).
  - PAAY/CKX, Chicken Airport, Chicken, Alaska, US (was KCKX).
  - PORI/ORI, Port Lions Airport, Port Lions, Alaska, US (was KORI).
* Updated other data for the following 146 airports:

  - 05XS    , Johnson Memorial Airport, Wilmot, Arkansas, US: elevation changed from 105 to 111, latitude changed from
    33.0785 to 33.079221, longitude changed from -91.561833 to -91.561553.
  - 08LS    , Aileron Airport, Grand Coteau, Louisiana, US: name changed from "Aeleron Airport", elevation changed from
    51 to 58, latitude changed from 30.40925 to 30.409173, longitude changed from -92.033167 to -92.0331.
  - 15TT    , Aeroplex Airfield, Lucas, Texas, US: elevation changed from 542 to 550, latitude changed from 33.115943 to
    33.116223, longitude changed from -96.551425 to -96.551686.
  - 17MT    , Lakeshore Heritage Airpark, Kalispell, Montana, US: name changed from "Abel Ranch Airport".
  - 19NY    , Four Seasons Airport, Reading, New York, US: elevation changed from 1650 to 1676, latitude changed from
    42.406177 to 42.407131, longitude changed from -77.960836 to -76.962705.
  - 1GA6    , Grand Oaks Plantation Airport, Sasser, Georgia, US: name changed from "Grand Oak Plantation Airport".
  - 1OH1    , Ohio Air Spray Airport, Quincy, Ohio, US: name changed from "S And S Field".
  - 1TE5    , Flying J Airport, Hearne, Texas, US: name changed from "Corpora Airport", latitude changed from 30.816303
    to 30.813889, longitude changed from -96.601081 to -96.602222.
  - 1TX0    , Middle Fork Ranch Airport, Lampasas, Texas, US: name changed from "Yancey Creek Ranch Airport".
  - 1XS2    , Skye Dance Airport, Elgin, Texas, US: Type of root['elevation changed from int to float and value changed
    from 532 to 541.2, latitude changed from 30.380762 to 30.382255, longitude changed from -97.427498 to -97.425682.
  - 2FA5    , Thunderbird Airpark, Crescent City, Florida, US: name changed from "Thunderbird Air Park".
  - 31MA    , Norm's Field, Belchertown, Massachusetts, US: elevation changed from 479 to 470, latitude changed from
    42.261944 to 42.262167, longitude changed from -72.408611 to -72.408952.
  - 33WY    , Skidmo Air Airport, Etna, Wyoming, US: name changed from "Skidmo Airport".
  - 34IL    , G Bray Airport, Lewistown, Illinois, US: elevation changed from 550 to 557, latitude changed from
    40.362542 to 40.362187, longitude changed from -90.108452 to -90.110055.
  - 36MO    , Harrison Pvt Airport, Rolla, Missouri, US: elevation changed from 1050 to 1056, latitude changed from
    37.852819 to 37.852864, longitude changed from -91.646819 to -91.64684.
  - 3NR4    , Parrish Airport, Elizabeth City, North Carolina, US: name changed from "Crabbe Airport".
  - 3PS2    , Pobo Field, Bedford, Pennsylvania, US: name changed from "Lynn Field".
  - 3TE3    , Nevada Airpark, Nevada, Texas, US: name changed from "Lazy Dog Ranch Airpark".
  - 3VG5    , Kinman Airport, Altavista, Virginia, US: Type of root['elevation changed from float to int and value
    changed from 699.7 to 694.
  - 4GA9    , Larry Watson Memorial Airport, Cumming, Georgia, US: name changed from "Ebeneezer Airport".
  - 4MS9    , Providence Airpark, Canton, Mississippi, US: elevation changed from 240 to 206, latitude changed from
    32.665972 to 32.662918, longitude changed from -90.067639 to -90.067487.
  - 4NK2    , Cary Field, Greenwich, New York, US: name changed from "Tracy Field".
  - 4XS2    , Felton Field, Paradise, Texas, US: name changed from "Teate Field".
  - 53FD    , Charlottes Field, Tallahassee, Florida, US: name changed from "Charlotte's Field".
  - 54WI    , Flyplassen Airport, Woodville, Wisconsin, US: latitude changed from 45.008297 to 44.964237, longitude
    changed from -92.275188 to -92.295333.
  - 55LL    , Sky Soaring Airport, Union, Illinois, US: elevation changed from 884 to 891, latitude changed from
    42.154191 to 42.153998, longitude changed from -88.511476 to -88.511771.
  - 5AK0    , Trading Bay Production Airport, Trading Bay, Alaska, US: elevation changed from 200 to 195, latitude
    changed from 60.815549 to 60.816881, longitude changed from -151.798917 to -151.799682.
  - 63MT    , Blains Airport, Billings, Montana, US: name changed from "Billings Flying Service Airport".
  - 64NC    , Fields Airport, Pleasant Garden, North Carolina, US: elevation changed from 820 to 822, latitude changed
    from 35.901944 to 35.906529, longitude changed from -79.7725 to -79.721744.
  - 6FD6    , Hilson Field, Eustis, Florida, US: name changed from "Rose Ranch Airport".
  - 74AK    , Maud Road Strip, Palmer, Alaska, US: elevation changed from 222 to 319, latitude changed from 61.582311 to
    61.583819, longitude changed from -148.996981 to -148.997306.
  - 74LA    , Promised Landings Airport, Prairieville, Louisiana, US: elevation changed from 7 to 4, latitude changed
    from 30.31164 to 30.31194, longitude changed from -90.835818 to -90.835885.
  - 76WA    , Luckie Farms Airport, Everett, Washington, US: name changed from "Heineck Farm Airport".
  - 7NC7    , Lewis Airstrip, Walnut Cove, North Carolina, US: elevation changed from 650 to 1022, latitude changed from
    36.346804 to 36.379894, longitude changed from -80.173659 to -80.173824.
  - 88XA    , Top Fun Ranch Airport, Anna, Texas, US: name changed from "Tejas Stone Ranch Airport".
  - 8TX0    , Hub Field, Jewett, Texas, US: Type of root['elevation changed from int to float and value changed from 361
    to 346.3, latitude changed from 31.428389 to 31.430654, longitude changed from -96.134861 to -96.134619.
  - 8WA7    , Mcguire Field, St John, Washington, US: name changed from "Gossard Field".
  - 9MT0    , Pale Morning Dun Ranch Airport, Fort Smith, Montana, US: elevation changed from 3220 to 3126.
  - 9PS8    , Manor Landing Airport, Gettysburg, Pennsylvania, US: elevation changed from 560 to 566, latitude changed
    from 39.81315 to 39.812639, longitude changed from -77.294983 to -77.302731.
  - 9SD8    , Oakleaf Airport, Hartford, South Dakota, US: elevation changed from 1625 to 1603, latitude changed from
    43.58331 to 43.582397, longitude changed from -96.950333 to -96.944982.
  - AL71    , Willow Point Airport, Our Town, Alabama, US: elevation changed from 551 to 552, latitude changed from
    32.803738 to 32.803304, longitude changed from -85.980519 to -85.980881.
  - CA92/PYS, Paradise Skypark Airport, Paradise, California, US: Type of root['elevation changed from int to float and
    value changed from 1300 to 1346.8.
  - FD23    , Rutland Runway Airport, Rutland, Florida, US: city changed from "Inverness".
  - ID89    , Big Flat Airport, Carmen, Idaho, US: name changed from "Lindberg Private Airport".
  - IL02    , Ravenwood Airport, Zion, Illinois, US: name changed from "Herbert C Maas Airport".
  - IL57    , Cottonwood Airport, Bloomington, Illinois, US: elevation changed from 765 to 746, latitude changed from
    40.421981 to 40.422605, longitude changed from -89.020634 to -89.020966.
  - IN31    , Bitar Field, Pendleton, Indiana, US: elevation changed from 870 to 882, latitude changed from 40.022263 to
    40.021497, longitude changed from -85.753588 to -85.753889.
  - K08F    , City Of Coalgate Airport, Coalgate, Oklahoma, US: elevation changed from 615 to 617, latitude changed from
    34.531759 to 34.529489, longitude changed from -96.233054 to -96.233097.
  - K0I2    , Brazil Clay County/Charles B Hall Field, Brazil, Indiana, US: name changed from "Brazil Clay County
    Airport".
  - K1B1/HCC, Columbia County Airport, Hudson, New York, US: elevation changed from 198.1 to 198.4, latitude changed
    from 42.291306 to 42.291295, longitude changed from -73.710333 to -73.710323.
  - K1G0    , Wood County Regional Airport, Bowling Green, Ohio, US: name changed from "Wood County Airport".
  - K1G3    , Kent State University Airport, Kent, Ohio, US: elevation changed from 1134.4 to 1134.5, latitude changed
    from 41.151389 to 41.151378, longitude changed from -81.415111 to -81.415119.
  - K1H2    , Effingham County Regional Airport, Effingham, Illinois, US: elevation changed from 585.2 to 585.3,
    latitude changed from 39.070444 to 39.070176, longitude changed from -88.533528 to -88.532548.
  - K1K1    , Lloyd Stearman Field, Benton, Kansas, US: elevation changed from 1364.1 to 1364.3, longitude changed from
    -97.113222 to -97.11325.
  - K1L9    , Parowan Airport, Parowan, Utah, US: Type of root['elevation changed from int to float and value changed
    from 5930 to 5926.9, latitude changed from 37.859639 to 37.859614, longitude changed from -112.815861 to
    -112.815906.
  - K1Q1    , Kingtech Field, Strathmore, California, US: name changed from "Eckert Field".
  - K2A8    , Addison Airport, Addison, Alabama, US: name changed from "Addison Municipal Airport".
  - K3A2    , The New Tazewell/Wayne Coffey Municipal Airport, Tazewell, Tennessee, US: name changed from "New Tazewell
    Municipal Airport".
  - K55M    , Jb West Municipal Airport Airport, Star City, Arkansas, US: name changed from "Star City Municipal
    Airport".
  - K8J7    , Tomlinson Field, New Rockford, North Dakota, US: elevation changed from 1533 to 1535, latitude changed
    from 47.696387 to 47.696165, longitude changed from -99.131229 to -99.131486.
  - K8U8    , Townsend Airport, Townsend, Montana, US: name changed from "Broadwater County Airport".
  - K94C    , Gilbert Field, Rio, Wisconsin, US: elevation changed from 921 to 927, latitude changed from 43.451603 to
    43.451586, longitude changed from -89.25417 to -89.254911.
  - K9W8    , Chanceford Airport, Brogue, Pennsylvania, US: name changed from "Baublitz Commercial Airport".
  - KADS/ADS, Addison Airport, Dallas, Texas, US: elevation changed from 644.6 to 644.2, latitude changed from 32.968556
    to 32.968554, longitude changed from -96.836444 to -96.836453.
  - KADT    , Atwood/Rawlins County Airport, Atwood, Kansas, US: name changed from "Atwood-Rawlins County City-County
    Airport".
  - KAPG/APG, Phillips Army Air Field (Aberdeen Proving Ground) Airport, Aberdeen, Maryland, US: name changed from
    "Phillips Army Air Field", city changed from "Aberdeen Proving Grounds (Aberdeen)".
  - KASL/ASL, Harrison County Airport, Marshall, Texas, US: Type of root['elevation changed from int to float and value
    changed from 357 to 357.1, latitude changed from 32.5205 to 32.520495, longitude changed from -94.307778 to
    -94.307772.
  - KBRY/BRY, Samuels Field, Bardstown, Kentucky, US: elevation changed from 668.8 to 669.3, latitude changed from
    37.814333 to 37.814322.
  - KC89    , Sylvania Airport, Sturtevant, Wisconsin, US: Type of root['elevation changed from float to int and value
    changed from 788.3 to 789, latitude changed from 42.70325 to 42.703247, longitude changed from -87.958972 to
    -87.958993.
  - KCBE/CBE, Greater Cumberland Regional Airport, Cumberland, Maryland, US: Type of root['elevation changed from int to
    float and value changed from 775 to 757.8, latitude changed from 39.615306 to 39.615667, longitude changed from
    -78.761478 to -78.762282.
  - KCCY/CCY, Northeast Iowa Regional Airport, Charles City, Iowa, US: Type of root['elevation changed from float to int
    and value changed from 1125.2 to 1125, latitude changed from 43.072504 to 43.073058, longitude changed from
    -92.610809 to -92.610446.
  - KCOE/COE, Coeur D'Alene Airport, Coeur D'Alene, Idaho, US: name changed from "Coeur D'Alene/Pappy Boyington Field".
  - KCSM/CSM, Infinity One Oklahoma Spaceport Airport, Burns Flat, Oklahoma, US: name changed from "Clinton/Sherman
    Airport".
  - KCWA/CWA, Central Wisconsin Airport, Mosinee, Wisconsin, US: elevation changed from 1277.2 to 1277.3.
  - KDIJ    , Driggs/Reed Memorial Airport, Driggs, Idaho, US: Type of root['elevation changed from float to int and
    value changed from 6257.2 to 6257, latitude changed from 43.746257 to 43.746267, longitude changed from -111.0913 to
    -111.091285.
  - KDTN/DTN, Shreveport Downtown Airport, Shreveport, Louisiana, US: elevation changed from 179.3 to 179.5, longitude
    changed from -93.743835 to -93.743836.
  - KDTO    , Denton Enterprise Airport, Denton, Texas, US: elevation changed from 642.7 to 642.8.
  - KE45    , Groveland/Yosemite Airport, Groveland, California, US: name changed from "Pine Mountain Lake Airport".
  - KELD/ELD, South Arkansas Regional At Goodwin Field, El Dorado, Arkansas, US: elevation changed from 276.8 to 277.1.
  - KEYE    , Eagle Creek Airpark, Indianapolis, Indiana, US: elevation changed from 822.5 to 822.9.
  - KFCS/FCS, Butts Army Air Field (Fort Carson) Airport, Fort Carson, Colorado, US: Type of root['elevation changed
    from float to int and value changed from 5874.3 to 5841, longitude changed from -104.756481 to -104.75648.
  - KFHU/FHU, Sierra Vista Municipal-Libby Army Air Field, Fort Huachuca Sierra Vista, Arizona, US: elevation changed
    from 4719.1 to 4718.8, latitude changed from 31.588472 to 31.588461, longitude changed from -110.344389 to
    -110.344375.
  - KGCY/GCY, Greeneville Municipal Airport, Greeneville, Tennessee, US: elevation changed from 1607.5 to 1607.8,
    latitude changed from 36.195722 to 36.195734, longitude changed from -82.811361 to -82.811366.
  - KGFK/GFK, Grand Forks International Airport, Grand Forks, North Dakota, US: elevation changed from 845.1 to 845.2,
    longitude changed from -97.175692 to -97.175685.
  - KHEF/MNZ, Washington Manassas/Harry P Davis Field, Washington, District of Columbia, US: name changed from "Manassas
    Regional/Harry P Davis Field".
  - KISW/ISW, Alexander Field South Wood County Airport, Wisconsin Rapids, Wisconsin, US: Type of root['elevation
    changed from int to float and value changed from 1021 to 1021.2, latitude changed from 44.360355 to 44.360356,
    longitude changed from -89.839039 to -89.839043.
  - KJKL    , Julian Carroll Airport, Jackson, Kentucky, US: elevation changed from 1380.9 to 1380.8, latitude changed
    from 37.593861 to 37.593859, longitude changed from -83.31725 to -83.317241.
  - KL32    , Jonesville Airport, Jonesville, Louisiana, US: Type of root['elevation changed from int to float and value
    changed from 56 to 56.3, latitude changed from 31.620258 to 31.62025, longitude changed from -91.834292 to
    -91.834278.
  - KM17    , Bolivar Municipal Airport, Bolivar, Missouri, US: Type of root['elevation changed from float to int and
    value changed from 1092.3 to 1093, latitude changed from 37.596107 to 37.596561, longitude changed from -93.347699
    to -93.347708.
  - KM54    , Lebanon Municipal Airport, Lebanon, Tennessee, US: Type of root['elevation changed from float to int and
    value changed from 588.4 to 588, longitude changed from -86.31569 to -86.315689.
  - KMBS/MBS, Mbs International Airport, Saginaw, Michigan, US: elevation changed from 668.2 to 668.3.
  - KMDD/MDD, Midland Airpark, Midland, Texas, US: elevation changed from 2805.4 to 2805.1, latitude changed from
    32.03657 to 32.036545, longitude changed from -102.101528 to -102.101512.
  - KMEM/MEM, Frederick W Smith International/Memphis Airport, Memphis, Tennessee, US: name changed from "Frederick W
    Smith International Airport".
  - KMGM/MGM, Montgomery Regional (Dannelly Field) Airport, Montgomery, Alabama, US: Type of root['elevation changed
    from int to float and value changed from 232 to 221.1.
  - KMKL/MKL, Jackson Regional Airport, Jackson, Tennessee, US: elevation changed from 433.3 to 434.8, latitude changed
    from 35.599881 to 35.59988.
  - KMTC/MTC, Selfridge Angb Airport, Mount Clemens, Michigan, US: Type of root['elevation changed from float to int and
    value changed from 579.5 to 580, latitude changed from 42.613894 to 42.612511, longitude changed from -82.83691 to
    -82.836958.
  - KMTV    , Blue Ridge Airport, Martinsville, Virginia, US: Type of root['elevation changed from float to int and
    value changed from 940.9 to 948, latitude changed from 36.630752 to 36.63145, longitude changed from -80.018338 to
    -80.019952.
  - KO08    , Sidney Pickels Field, Colusa, California, US: name changed from "Colusa County Airport".
  - KO88    , Rio Vista Municipal Airport, Rio Vista, California, US: elevation changed from 22.6 to 22.5, latitude
    changed from 38.193389 to 38.193383, longitude changed from -121.703639 to -121.703634.
  - KOCF/OCF, Ocala International-Jim Taylor Field, Ocala, Florida, US: elevation changed from 89.7 to 90.1, latitude
    changed from 29.171877 to 29.171876, longitude changed from -82.224115 to -82.224114.
  - KOCH/OCH, Nacogdoches A L Mangham Jr Regional Airport, Nacogdoches, Texas, US: elevation changed from 343.1 to
    343.2, latitude changed from 31.577764 to 31.577769, longitude changed from -94.710111 to -94.71013.
  - KOCW/OCW, Washington-Warren Airport, Washington, North Carolina, US: elevation changed from 37.4 to 37.7, latitude
    changed from 35.570472 to 35.571938, longitude changed from -77.049806 to -77.049764.
  - KOIC/OIC, Lt Warren Eaton Airport, Norwich, New York, US: elevation changed from 1024.4 to 1024.2, latitude changed
    from 42.566556 to 42.566559, longitude changed from -75.524111 to -75.524112.
  - KOQU/NCO, Quonset State Airport, North Kingstown, Rhode Island, US: elevation changed from 18.3 to 18.2, latitude
    changed from 41.597408 to 41.597407.
  - KOQW    , Maquoketa Municipal Airport, Maquoketa, Iowa, US: elevation changed from 769.4 to 773.6, latitude changed
    from 42.050083 to 42.050694, longitude changed from -90.738806 to -90.739194.
  - KORF/ORF, Norfolk International Airport, Norfolk, Virginia, US: elevation changed from 26.4 to 26.2, latitude
    changed from 36.894604 to 36.895631, longitude changed from -76.201229 to -76.198865.
  - KORL/ORL, Orlando Executive Airport, Orlando, Florida, US: elevation changed from 112.6 to 112.5.
  - KP04/BSQ, Bisbee Municipal Airport, Bisbee, Arizona, US: elevation changed from 4780 to 4790, latitude changed from
    31.36399 to 31.368867, longitude changed from -109.883129 to -109.883568.
  - KPJC    , Zelienople Municipal Airport, Zelienople, Pennsylvania, US: Type of root['elevation changed from int to
    float and value changed from 907 to 907.1, longitude changed from -80.1611 to -80.161101.
  - KPOY/POY, Powell Municipal Airport, Powell, Wyoming, US: elevation changed from 5095.7 to 5096.1, latitude changed
    from 44.867167 to 44.867222, longitude changed from -108.793417 to -108.793368.
  - KPQN    , Pipestone Municipal Airport, Pipestone, Minnesota, US: elevation changed from 1736.7 to 1736.8, latitude
    changed from 43.982137 to 43.982133.
  - KPRO/PRO, Perry Municipal Airport, Perry, Iowa, US: Type of root['elevation changed from int to float and value
    changed from 1013 to 1013.1.
  - KPTD    , Potsdam Municipal/Damon Field, Potsdam, New York, US: elevation changed from 473.9 to 474.3, longitude
    changed from -74.948444 to -74.948433.
  - KRDM/RDM, Roberts Field/Redmond Municipal Airport, Redmond, Oregon, US: name changed from "Roberts Field".
  - KRMN    , Washington Executive/Stafford Regional Airport, Stafford, Virginia, US: name changed from "Stafford
    Regional Airport".
  - KRNM    , Ramona Airport, Ramona, California, US: elevation changed from 1394.6 to 1394.9, latitude changed from
    33.039167 to 33.039159, longitude changed from -116.91525 to -116.915258.
  - KRPH    , Graham Municipal Airport, Graham, Texas, US: Type of root['elevation changed from int to float and value
    changed from 1123 to 1122.8, latitude changed from 33.110722 to 33.110726, longitude changed from -98.554778 to
    -98.554777.
  - KRQB/WBR, Roben-Hood Airport, Big Rapids, Michigan, US: elevation changed from 989.8 to 994.2, latitude changed from
    43.722639 to 43.722811, longitude changed from -85.504056 to -85.50532.
  - KS01    , Conrad Airport, Conrad, Montana, US: elevation changed from 3547.9 to 3548.4, latitude changed from
    48.168278 to 48.168274, longitude changed from -111.976444 to -111.976429.
  - KS36    , Crest Airfield, Covington, Washington, US: name changed from "Norman Grier Field".
  - KS39/PRZ, Prineville Airport, Prineville, Oregon, US: Type of root['elevation changed from int to float and value
    changed from 3251 to 3250.7.
  - KS92    , Fish Lake Usfs Airport, Fish Lake, Idaho, US: name changed from "Fish Lake /Usfs/ Airport".
  - KSAC/SAC, Sacramento Executive Airport, Sacramento, California, US: elevation changed from 23.6 to 23.4, longitude
    changed from -121.4933 to -121.493301.
  - KSJC/SJC, Norman Y Mineta San Jose International Airport, San Jose, California, US: elevation changed from 62.2 to
    62.3.
  - KSTC/STC, St Cloud Sky Central Airport, St Cloud, Minnesota, US: name changed from "St Cloud Regional Airport".
  - KU01    , Savage Field, American Falls, Idaho, US: Type of root['elevation changed from int to float and value
    changed from 4419 to 4420.2, latitude changed from 42.797317 to 42.797316.
  - KUIN/UIN, Quincy Regional-Baldwin Field, Quincy, Illinois, US: elevation changed from 768.7 to 768.5, longitude
    changed from -91.192404 to -91.192405.
  - KWDR/WDR, Barrow County Airport, Winder, Georgia, US: elevation changed from 934.3 to 934.4, latitude changed from
    33.98269 to 33.982879, longitude changed from -83.667217 to -83.667415.
  - MN88    , Landeplatz Airport, Searles, Minnesota, US: elevation changed from 995 to 987, latitude changed from
    44.228889 to 44.230343, longitude changed from -94.415278 to -94.415076.
  - MO06    , Discovery Bay At Norwalk Landing Airport, Shell Knob, Missouri, US: elevation changed from 1054 to 1065,
    latitude changed from 36.622378 to 36.622501, longitude changed from -93.539942 to -93.539922.
  - MS77    , Conner Field, Inverness, Mississippi, US: name changed from "Lang Flying Service Airport".
  - NC58    , Gryder-Teague Airport, Taylorsville, North Carolina, US: elevation changed from 1190 to 1180, latitude
    changed from 35.920966 to 35.918514, longitude changed from -81.120081 to -81.119582.
  - OH40    , Shannons Landing Airport, Radnor, Ohio, US: name changed from "Eylesair Airport".
  - PACJ/CKD, Crooked Creek Airport, Crooked Creek, Alaska, US: elevation changed from 177.2 to 182.5, latitude changed
    from 61.871118 to 61.871119.
  - PACK/CYF, Chefornak Airport, Chefornak, Alaska, US: elevation changed from 54.1 to 53.9, latitude changed from
    60.136806 to 60.136796, longitude changed from -164.279056 to -164.279049.
  - PAEW/WWT, Mertarvik Airport, Mertarvik, Alaska, US: elevation changed from 345.5 to 345.2, latitude changed from
    60.810393 to 60.810402, longitude changed from -164.499472 to -164.49944.
  - PN54    , Akm Airfield, Columia Cross Roads, Pennsylvania, US: elevation changed from 1393 to 1411, latitude changed
    from 41.841667 to 41.83784, longitude changed from -76.745833 to -76.745303.
  - SD78    , Anderson Aerial Spraying Airport, Kennebec, South Dakota, US: elevation changed from 1750 to 1758,
    latitude changed from 43.901528 to 43.900763, longitude changed from -99.878861 to -99.878341.
  - TJVQ/VQS, Antonio Rivera Rodriguez Airport, Isla De Vieques, Puerto Rico, US: Type of root['elevation changed from
    int to float and value changed from 49 to 48.2, latitude changed from 18.134811 to 18.134806, longitude changed from
    -65.493617 to -65.493611.
  - TN12    , Fuller Field, Lewisburg, Tennessee, US: name changed from "Hudgin Air Airport".
  - TN65    , Long Meadow Airstrip, Murfreesboro, Tennessee, US: city changed from "Murfreesburg".
  - TS36    , Silver Wings Airport, Fredericksburg, Texas, US: city changed from "Fredricksburg".
  - VG12    , Simpsonville Airport, Rhoadesville, Virginia, US: elevation changed from 400 to 398, latitude changed from
    38.333464 to 38.3173, longitude changed from -77.866383 to -77.867414.
  - VG40    , Woody Field, Rocky Mount, Virginia, US: elevation changed from 1150 to 1157, latitude changed from
    36.886822 to 36.886914, longitude changed from -79.863925 to -79.863957.
  - WY58    , Hilty Field, Wheatland, Wyoming, US: name changed from "Hilty Private Strip".
  - XS25    , Flying C Airport, Needville, Texas, US: name changed from "Flying C Ranch Airport".

* Removed the following 239 airports:

  - 00KY     Robbins Roost Airport, Stanford, Kentucky, US: LID not in A/FD (FAA LID: 00KY)
  - 00NY     Weiss Airfield, West Bloomfield, New York, US: LID not in A/FD (FAA LID: 00NY)
  - 01TE     Smith Field, Forney, Texas, US: LID not in A/FD (FAA LID: 01TE)
  - 02MN     Gregory Airport, Cambridge, Minnesota, US: LID not in A/FD (FAA LID: 02MN)
  - 04MT     Pluhar Airport, Cohagen, Montana, US: LID not in A/FD (FAA LID: 04MT)
  - 05TS     Dew Drop Airport, Justin, Texas, US: LID not in A/FD (FAA LID: 05TS)
  - 06TX     Diamond N Ranch Airport, Hockley, Texas, US: LID not in A/FD (FAA LID: 06TX)
  - 08FA     Duda Airstrip, La Belle, Florida, US: LID not in A/FD (FAA LID: 08FA)
  - 09GA     Sunbelt Strip, Moultrie, Georgia, US: LID not in A/FD (FAA LID: 09GA)
  - 0AR2     Mission Field-Marotti Memorial Airport, Crawfordsville, Arkansas, US: LID not in A/FD (FAA LID: 0AR2)
  - 0IA8     Hannen Airport, Center Point, Iowa, US: LID not in A/FD (FAA LID: 0IA8)
  - 0LA1     Double H Ranch Airport, Gonzales, Louisiana, US: LID not in A/FD (FAA LID: 0LA1)
  - 0MO0     Ferros Ranch-Aero Airport, Clinton, Missouri, US: LID not in A/FD (FAA LID: 0MO0)
  - 0NY1     Russell Field, Northumberland, New York, US: LID not in A/FD (FAA LID: 0NY1)
  - 0OK3     Mckinley Ranch Airport, Geary, Oklahoma, US: LID not in A/FD (FAA LID: 0OK3)
  - 0SD0     Lenling Airport, Glencross, South Dakota, US: LID not in A/FD (FAA LID: 0SD0)
  - 0SD1     Lodi Airport, Wakonda, South Dakota, US: LID not in A/FD (FAA LID: 0SD1)
  - 0TS1     Dooley Airport, Justin, Texas, US: LID not in A/FD (FAA LID: 0TS1)
  - 0TS9     Mcclellan Creek Airport, Mclean, Texas, US: LID not in A/FD (FAA LID: 0TS9)
  - 0XS6     Lakeside Beach Airport, Spicewood, Texas, US: LID not in A/FD (FAA LID: 0XS6)
  - 10TE     Gottwald Field, Harwood, Texas, US: LID not in A/FD (FAA LID: 10TE)
  - 11CL     Hansen Airport, Adelanto, California, US: LID not in A/FD (FAA LID: 11CL)
  - 11TS     Pt Enterprise D&W Ranch Airport, Mexia, Texas, US: LID not in A/FD (FAA LID: 11TS)
  - 11TT     Rocking L Airport, Sonora, Texas, US: LID not in A/FD (FAA LID: 11TT)
  - 12MI     John's Airport, Davison, Michigan, US: LID not in A/FD (FAA LID: 12MI)
  - 19PA     Lake Airport, Millville, Pennsylvania, US: LID not in A/FD (FAA LID: 19PA)
  - 19TA     Lagrone Ranch Airport, Mc Clendon-Chisholm, Texas, US: LID not in A/FD (FAA LID: 19TA)
  - 1LL2     Spring Brook Airport, Seneca, Illinois, US: LID not in A/FD (FAA LID: 1LL2)
  - 1LL7     Edwin G Bennett Airport, Sheffield, Illinois, US: LID not in A/FD (FAA LID: 1LL7)
  - 1TA8     Rio Pinto Ranch Airport, Bracketville, Texas, US: LID not an AIRPORT: RIO PINTO RANCH (FAA LID: 1TA8)
  - 1TE7     Ray Farm Airport, Floresville, Texas, US: LID not in A/FD (FAA LID: 1TE7)
  - 1TX4     New Gulf Airport, New Gulf, Texas, US: LID not in A/FD (FAA LID: 1TX4)
  - 20TA     Mag Drop Airport, Bells, Texas, US: LID not in A/FD (FAA LID: 20TA)
  - 20TS     Bains Private Airport, Bandera, Texas, US: LID not in A/FD (FAA LID: 20TS)
  - 23ND     Anderson Airport, Rogers, North Dakota, US: LID not in A/FD (FAA LID: 23ND)
  - 23NY     Jolamtra Landing Area Airport, Bath, New York, US: LID not in A/FD (FAA LID: 23NY)
  - 25NV     Parker Carson Airport, Carson City, Nevada, US: LID not in A/FD (FAA LID: 25NV)
  - 25WA     Hart Ranch Airport, Tonasket, Washington, US: LID not in A/FD (FAA LID: 25WA)
  - 26IN     Haven Center Airport, Fort Wayne, Indiana, US: LID not in A/FD (FAA LID: 26IN)
  - 27MT     Rahn Airport, Kalispell, Montana, US: LID not in A/FD (FAA LID: 27MT)
  - 28XS     Flying G Airport, Kaufman, Texas, US: LID not in A/FD (FAA LID: 28XS)
  - 2CA3     Crosswinds Airport, Twentynine Palms, California, US: LID not in A/FD (FAA LID: 2CA3)
  - 2FA4     Southern Ranch Airport, Clewiston, Florida, US: LID not in A/FD (FAA LID: 2FA4)
  - 2GE7     Petty Farms Airport, Crandall, Georgia, US: LID not in A/FD (FAA LID: 2GE7)
  - 2MD3     Fly Away Farm Airport, Boyds, Maryland, US: LID not in A/FD (FAA LID: 2MD3)
  - 2MU9     Monroe Field, Hawk Point, Missouri, US: LID not in A/FD (FAA LID: 2MU9)
  - 2TA1     Gravco Airport, Lufkin, Texas, US: LID not in A/FD (FAA LID: 2TA1)
  - 2TS5     Paducah Airport, Paducah, Texas, US: LID not in A/FD (FAA LID: 2TS5)
  - 2UT5     Charlevoix Airport, New Harmony, Utah, US: LID not in A/FD (FAA LID: 2UT5)
  - 2XS6     Foster Ranch Airport, Utopia, Texas, US: LID not in A/FD (FAA LID: 2XS6)
  - 31AZ     Benson Airport, Benson, Arizona, US: LID not in A/FD (FAA LID: 31AZ)
  - 34MS     Colle Field, Gautier, Mississippi, US: LID not in A/FD (FAA LID: 34MS)
  - 36GA     Lola Landing Airport, Conyers, Georgia, US: LID not in A/FD (FAA LID: 36GA)
  - 38AK     Mels Airport, Wasilla, Alaska, US: LID not in A/FD (FAA LID: 38AK)
  - 38NY     Greenlawn Farm Airport, Dundee, New York, US: LID not in A/FD (FAA LID: 38NY)
  - 39MS     Benton Farms Airport, Clinton, Mississippi, US: LID not in A/FD (FAA LID: 39MS)
  - 3GA5     Diamond R Ranch Airport, Villa Rica, Georgia, US: LID not in A/FD (FAA LID: 3GA5)
  - 3LA1     Wilder Airport, Kinder, Louisiana, US: LID not in A/FD (FAA LID: 3LA1)
  - 3LS8     The Place Airport, Folsom, Louisiana, US: LID not in A/FD (FAA LID: 3LS8)
  - 3MA5     Westport Airport, Westport, Massachusetts, US: LID not in A/FD (FAA LID: 3MA5)
  - 3MO6     Kitty Hawk Estates Airport, Kearney, Missouri, US: LID not in A/FD (FAA LID: 3MO6)
  - 3MS6     E E Lane Airport, Flora, Mississippi, US: LID not in A/FD (FAA LID: 3MS6)
  - 3NY3     De Ronda Airport, Springfield, New York, US: LID not in A/FD (FAA LID: 3NY3)
  - 3OK9     Jazz Ranch Airport, Shawnee, Oklahoma, US: LID not in A/FD (FAA LID: 3OK9)
  - 3PA4     Giffin Airport, Leraysville, Pennsylvania, US: LID not in A/FD (FAA LID: 3PA4)
  - 3TA9     Chacon Creek Ranch Airport, Crystal City, Texas, US: LID not in A/FD (FAA LID: 3TA9)
  - 3VA5     Goose Hunt Farm Airport, Leesburg, Virginia, US: LID not in A/FD (FAA LID: 3VA5)
  - 40OH     Bucks Airport, Newbury, Ohio, US: LID not in A/FD (FAA LID: 40OH)
  - 44KS     Vankirk Airport, Wichita, Kansas, US: LID not in A/FD (FAA LID: 44KS)
  - 44NY     Tomcat Airport, Fort Plain, New York, US: LID not in A/FD (FAA LID: 44NY)
  - 45FL     Moss Meadows Airport, Live Oak, Florida, US: LID not in A/FD (FAA LID: 45FL)
  - 47NY     Elk Creek Airport, Borden, New York, US: LID not in A/FD (FAA LID: 47NY)
  - 48MY     Bosch Farm Airport, Montevideo, Minnesota, US: LID not an AIRPORT: BOSCH FARM (FAA LID: 48MY)
  - 4KS5     Maize Airport, Wichita/Maize/, Kansas, US: LID not an AIRPORT: MAIZE (FAA LID: 4KS5)
  - 4KY7     Mueller Farm Airport, Verona, Kentucky, US: LID not in A/FD (FAA LID: 4KY7)
  - 4MI4     Davids Landing Airport, St Clair, Michigan, US: LID not in A/FD (FAA LID: 4MI4)
  - 4MO4     Liberty Landing Airport, Liberty, Missouri, US: LID not in A/FD (FAA LID: 4MO4)
  - 4NC6     Cane Creek Airport, Fletcher, North Carolina, US: LID not in A/FD (FAA LID: 4NC6)
  - 4NY1     Orange Poultry Farm Airport, Chester, New York, US: LID not in A/FD (FAA LID: 4NY1)
  - 4OR1     Bryant Airport, Madras, Oregon, US: LID not in A/FD (FAA LID: 4OR1)
  - 4TX4     Birk Airport, Kennedale, Texas, US: LID not in A/FD (FAA LID: 4TX4)
  - 4XA5     Dave Eby Field, Burkburnett, Texas, US: LID not in A/FD (FAA LID: 4XA5)
  - 4XS9     Cajun Hills Ranch Airport, Wimberley, Texas, US: LID not in A/FD (FAA LID: 4XS9)
  - 50FD     Cattle Creek Ranch Airport, Altha, Florida, US: LID not in A/FD (FAA LID: 50FD)
  - 51GA     Smith Field, Tyrone, Georgia, US: LID not in A/FD (FAA LID: 51GA)
  - 51TX     N D Ranch Airport, Van, Texas, US: LID not in A/FD (FAA LID: 51TX)
  - 52TS     Fall Creek Air Ranch Airport, Spicewood, Texas, US: LID not in A/FD (FAA LID: 52TS)
  - 55NM     Burris Ranch Nr 1 Airport, Belen, New Mexico, US: LID not in A/FD (FAA LID: 55NM)
  - 59WA     Sorrell Airport, Tenino, Washington, US: LID not in A/FD (FAA LID: 59WA)
  - 5AK2     Howards Airport, North Pole, Alaska, US: LID not in A/FD (FAA LID: 5AK2)
  - 5GA0     Gable Branch Airport, Haralson, Georgia, US: LID not in A/FD (FAA LID: 5GA0)
  - 5ND0     Stiehl Airport, Buford, North Dakota, US: LID not in A/FD (FAA LID: 5ND0)
  - 5PS5     Chestnut Hill Airport, Duncannon, Pennsylvania, US: LID not in A/FD (FAA LID: 5PS5)
  - 5SD3     Bowdle Municipal Airport, Bowdle, South Dakota, US: LID not in A/FD (FAA LID: 5SD3)
  - 5TS2     Chan-C Airport, Coupland, Texas, US: LID not in A/FD (FAA LID: 5TS2)
  - 61MU     Farris Strip, Faucett, Missouri, US: LID not in A/FD (FAA LID: 61MU)
  - 61ND     Bakke Airport, Larimore, North Dakota, US: LID not in A/FD (FAA LID: 61ND)
  - 61XA     Qz Ranch Airport, Mckinney, Texas, US: LID not in A/FD (FAA LID: 61XA)
  - 62IS     Wilson Airport, Fithian, Illinois, US: LID not in A/FD (FAA LID: 62IS)
  - 62NC     Hickory Hill Airport, Havelock, North Carolina, US: LID not in A/FD (FAA LID: 62NC)
  - 6CL8     Harley Airport, Stockton, California, US: LID not in A/FD (FAA LID: 6CL8)
  - 6MD1     Dileo Field, Denton, Maryland, US: LID not in A/FD (FAA LID: 6MD1)
  - 6WA3     Green Acres Airport, Basin City, Washington, US: LID not in A/FD (FAA LID: 6WA3)
  - 70LA     Roland Airport, Hineston, Louisiana, US: LID not in A/FD (FAA LID: 70LA)
  - 76NC     Dunroamin Farms Airport, Enfield, North Carolina, US: LID not in A/FD (FAA LID: 76NC)
  - 7MO4     Flintlock Field, Platte City, Missouri, US: LID not in A/FD (FAA LID: 7MO4)
  - 81FL     The Flying Horseman Ranch Airport, Gainesville, Florida, US: LID not in A/FD (FAA LID: 81FL)
  - 81OK     Twin Lakes Ranch Airport, Granite, Oklahoma, US: LID not in A/FD (FAA LID: 81OK)
  - 81OR     Wagontire Airport, Burns, Oregon, US: LID not in A/FD (FAA LID: 81OR)
  - 85TA     Mena Airport, Lillian, Texas, US: LID not in A/FD (FAA LID: 85TA)
  - 87NE     Knox Landing Airport, York, Nebraska, US: LID not in A/FD (FAA LID: 87NE)
  - 8OA5     Camp Crook Municipal Airport, Camp Crook, South Dakota, US: LID not in A/FD (FAA LID: 8OA5)
  - 8TA9     Star Dusters Airport, Washington, Louisiana, US: LID not in A/FD (FAA LID: 8TA9)
  - 8TN9     Bull Run Airport, Covington, Tennessee, US: LID not in A/FD (FAA LID: 8TN9)
  - 8TX8     Weeks Airport, Premont, Texas, US: LID not in A/FD (FAA LID: 8TX8)
  - 91ME     J & S Field, Stetson, Maine, US: LID not in A/FD (FAA LID: 91ME)
  - 93VA     Timberdoodle Airport, Amherst, Virginia, US: LID not in A/FD (FAA LID: 93VA)
  - 94MN     Ag Spray Inc Airport, Barnesville, Minnesota, US: LID not in A/FD (FAA LID: 94MN)
  - 99MI     Newport Meadows Airport, Newport, Michigan, US: LID not in A/FD (FAA LID: 99MI)
  - 9NC4     Jiles Field, Gates, North Carolina, US: LID not in A/FD (FAA LID: 9NC4)
  - 9SD7     Beaman Airport, Selby, South Dakota, US: LID not in A/FD (FAA LID: 9SD7)
  - AK79     Jolly Field, Wasilla, Alaska, US: LID not in A/FD (FAA LID: AK79)
  - AL97     Williamson Farm Airport, Loxley, Alabama, US: LID not in A/FD (FAA LID: AL97)
  - FD48     Deep Forest Airport, Jacksonville, Florida, US: LID not in A/FD (FAA LID: FD48)
  - FD74     Gamebird Groves Airstrip, West Melbourne, Florida, US: LID not in A/FD (FAA LID: FD74)
  - FL83     Whiskey Throttle Field, Panama City, Florida, US: LID not in A/FD (FAA LID: FL83)
  - GA59     Antique Acres Airport, Barnesville, Georgia, US: LID not in A/FD (FAA LID: GA59)
  - HI03     Hanamaulu Airstrip, Hanamaulu, Hawaii, US: LID not in A/FD (FAA LID: HI03)
  - HI05     Honokaa Airstrip, Honokaa, Hawaii, US: LID not in A/FD (FAA LID: HI05)
  - HI27     Upper Paauilo Airstrip, Paauilo, Hawaii, US: LID not in A/FD (FAA LID: HI27)
  - HI28     Pahala Airstrip, Pahala, Hawaii, US: LID not in A/FD (FAA LID: HI28)
  - HI46     Hi 23 Airstrip, Puhi, Hawaii, US: LID not in A/FD (FAA LID: HI46)
  - IA35     Ruckl Airport, Council Bluffs, Iowa, US: LID not in A/FD (FAA LID: IA35)
  - II26     Ashby Airport, Remington, Indiana, US: LID not in A/FD (FAA LID: II26)
  - II32     Raceway Airport, Chandler, Indiana, US: LID not in A/FD (FAA LID: II32)
  - IL05     Shumway Innernational Airport, Effingham, Illinois, US: LID not in A/FD (FAA LID: IL05)
  - IN49     Pherigo Airport, Shelbyville, Indiana, US: LID not in A/FD (FAA LID: IN49)
  - IS83     Untied Acres Airport, Belvidere, Illinois, US: LID not in A/FD (FAA LID: IS83)
  - K0D7     Ada Airport, Ada, Ohio, US: LID not in A/FD (FAA LID: 0D7)
  - K0E0     Moriarty Municipal Airport, Moriarty, New Mexico, US: LID not in A/FD (FAA LID: 0E0)
  - K0E8     Crownpoint Airport, Crownpoint, New Mexico, US: LID not in A/FD (FAA LID: 0E8)
  - K0E9     Corydon Airport, Corydon, Iowa, US: LID not in A/FD (FAA LID: 0E9)
  - K1E2     Terlingua Ranch Airport, Alpine, Texas, US: LID not in A/FD (FAA LID: 1E2)
  - K1E4     Palo Duro Airport, Amarillo, Texas, US: LID not in A/FD (FAA LID: 1E4)
  - K1E7     Buffalo Airport, Amarillo, Texas, US: LID not in A/FD (FAA LID: 1E7)
  - K1E8     Degrasse Moores Airport, Degrasse, New York, US: LID not in A/FD (FAA LID: 1E8)
  - K1H6     Harvey Young Airport, Tulsa, Oklahoma, US: LID not in A/FD (FAA LID: 1H6)
  - K2E2     Sharpe's Strip, Emmett, Michigan, US: LID not in A/FD (FAA LID: 2E2)
  - K2E5     Dell City Municipal Airport, Dell City, Texas, US: LID not in A/FD (FAA LID: 2E5)
  - K2E6     Groton Municipal Airport, Groton, South Dakota, US: LID not in A/FD (FAA LID: 2E6)
  - K2E7     Mc Lean/Gray County Airport, Mc Lean, Texas, US: LID not in A/FD (FAA LID: 2E7)
  - K2E8     Cackleberry Airport, Dexter, Michigan, US: LID not in A/FD (FAA LID: 2E8)
  - K2V5     Wray Municipal Airport, Wray, Colorado, US: LID not in A/FD (FAA LID: 2V5)
  - K3E0     Miami-Roberts County Airport, Miami, Texas, US: LID not in A/FD (FAA LID: 3E0)
  - K4E7     Ellendale Municipal Airport, Ellendale, North Dakota, US: LID not in A/FD (FAA LID: 4E7)
  - K4E8     Richardton Airport, Richardton, North Dakota, US: LID not in A/FD (FAA LID: 4E8)
  - K5E9     Packer Airport, Radnor, Ohio, US: LID not in A/FD (FAA LID: 5E9)
  - K6E5     Wilder Airport, Desmet, South Dakota, US: LID not in A/FD (FAA LID: 6E5)
  - K7D9     Germack Airport, Geneva, Ohio, US: LID not in A/FD (FAA LID: 7D9)
  - K7MI     Flugplatz Airport, Lexington, Michigan, US: LID not in A/FD (FAA LID: 7MI)
  - KO74     Elliotts Landing Airport, Mount Victory, Ohio, US: LID not in A/FD (FAA LID: O74)
  - KT93     Follett/Lipscomb County Airport, Follett, Texas, US: LID not in A/FD (FAA LID: T93)
  - KW17     Raleigh East Airport, Knightdale, North Carolina, US: LID not in A/FD (FAA LID: W17)
  - LA21     Chloe Airport, Lake Charles, Louisiana, US: LID not in A/FD (FAA LID: LA21)
  - LA26     Unicorn Airport, Folsom, Louisiana, US: LID not in A/FD (FAA LID: LA26)
  - LA30     Phoenix Airport, Rayne, Louisiana, US: LID not in A/FD (FAA LID: LA30)
  - LL91     Hillman Airport, Rock City, Illinois, US: LID not in A/FD (FAA LID: LL91)
  - MA77     Blueberry Hill Airport, Washington, Massachusetts, US: LID not in A/FD (FAA LID: MA77)
  - MA86     Kendalls Lndg Area Airport, Windsor, Massachusetts, US: LID not in A/FD (FAA LID: MA86)
  - MD82     Ragged Island Airport, Cambridge, Maryland, US: LID not in A/FD (FAA LID: MD82)
  - MI01     Fasel Field, Avoca, Michigan, US: LID not in A/FD (FAA LID: MI01)
  - MI44     D J Airport, Mount Pleasant, Michigan, US: LID not in A/FD (FAA LID: MI44)
  - MI76     Reading Airport, Fennville, Michigan, US: LID not in A/FD (FAA LID: MI76)
  - MO15     C2K Airport, Fair Grove, Missouri, US: LID not in A/FD (FAA LID: MO15)
  - MS30     Abide Airpark, Greenville, Mississippi, US: LID not in A/FD (FAA LID: MS30)
  - MT30     Trapper Creek Strip, Conner, Montana, US: LID not in A/FD (FAA LID: MT30)
  - MT42     Hasskamp Airport, Three Forks, Montana, US: LID not in A/FD (FAA LID: MT42)
  - MT62     Jefferson River Airport, Twin Bridges, Montana, US: LID not in A/FD (FAA LID: MT62)
  - MU13     Wray Airfield, Parnell, Missouri, US: LID not in A/FD (FAA LID: MU13)
  - MU78     Taylor Field, Waynesville, Missouri, US: LID not in A/FD (FAA LID: MU78)
  - MY80     Rosenberg Airport, Ceylon, Minnesota, US: LID not in A/FD (FAA LID: MY80)
  - NA05     Kraig Farms Airport, Sheldon, North Dakota, US: LID not in A/FD (FAA LID: NA05)
  - NA06     Bouret Ranch Airport, Sheyenne, North Dakota, US: LID not in A/FD (FAA LID: NA06)
  - NA65     Anderson Strip, Hoople, North Dakota, US: LID not in A/FD (FAA LID: NA65)
  - NA71     M Bodvig Airstrip, Tappen, North Dakota, US: LID not in A/FD (FAA LID: NA71)
  - NA88     Regan Airstrip, Regan, North Dakota, US: LID not in A/FD (FAA LID: NA88)
  - NA90     Circle Z Landing Strip, Underwood, North Dakota, US: LID not in A/FD (FAA LID: NA90)
  - NC00     Moretz Riverside Landing Airport, Sanford, North Carolina, US: LID not in A/FD (FAA LID: NC00)
  - ND52     True North Airpark, West Fargo, North Dakota, US: LID not in A/FD (FAA LID: ND52)
  - ND59     Grieve Airport, Buffalo, North Dakota, US: LID not in A/FD (FAA LID: ND59)
  - ND72     Lonetree Airstrip, Harvey, North Dakota, US: LID not in A/FD (FAA LID: ND72)
  - ND92     Ll Landing Airport, Turtle Lake, North Dakota, US: LID not in A/FD (FAA LID: ND92)
  - NE09     Simpson Airport, Norfolk, Nebraska, US: LID not in A/FD (FAA LID: NE09)
  - NE59     Pester Airport, Lincoln, Nebraska, US: LID not in A/FD (FAA LID: NE59)
  - NJ59     Ekdahl Airport, Freehold, New Jersey, US: LID not in A/FD (FAA LID: NJ59)
  - NK24     Tilden Airport, Montour Falls, New York, US: LID not in A/FD (FAA LID: NK24)
  - NK76     Grammar Airport, Geneva, New York, US: LID not in A/FD (FAA LID: NK76)
  - NK91     Boyle's Landing Airport, Sharon Springs, New York, US: LID not in A/FD (FAA LID: NK91)
  - NM20     Epic Paramotor Airport, Deming, New Mexico, US: LID not in A/FD (FAA LID: NM20)
  - NM25     Lincoln Station Airport, Corona, New Mexico, US: LID not in A/FD (FAA LID: NM25)
  - NM26     Luna Landing Airport, Deming, New Mexico, US: LID not in A/FD (FAA LID: NM26)
  - NM27     Sanostee Airport, Gallup, New Mexico, US: LID not in A/FD (FAA LID: NM27)
  - NM29     Rosebud Airport, Rosebud, New Mexico, US: LID not in A/FD (FAA LID: NM29)
  - NM38     Double V Ranch Airport, Fort Sumner, New Mexico, US: LID not in A/FD (FAA LID: NM38)
  - NM49     J & M Farms Airport, Willard, New Mexico, US: LID not in A/FD (FAA LID: NM49)
  - NM52     Camco Ranch Airport, Nara Visa, New Mexico, US: LID not in A/FD (FAA LID: NM52)
  - NM87     Jenkins Airport, Roswell, New Mexico, US: LID not in A/FD (FAA LID: NM87)
  - NV17     Youngberg Ranch Airport, Lemmon Valley, Nevada, US: LID not in A/FD (FAA LID: NV17)
  - NY34     Randall's Roost Airport, Cameron, New York, US: LID not in A/FD (FAA LID: NY34)
  - OH24     Markley Farm Airport, Orrville, Ohio, US: LID not in A/FD (FAA LID: OH24)
  - OI31     Pheasant Run Airport, Leroy, Ohio, US: LID not in A/FD (FAA LID: OI31)
  - OK18     Grand Isle Airport, Adair, Oklahoma, US: LID not in A/FD (FAA LID: OK18)
  - PA30     East Penn Airport, Andreas, Pennsylvania, US: LID not in A/FD (FAA LID: PA30)
  - PA65     Hi-Vu Airport, Coplay, Pennsylvania, US: LID not in A/FD (FAA LID: PA65)
  - PA68     Bugs Airport, Nazareth, Pennsylvania, US: LID not in A/FD (FAA LID: PA68)
  - PA82     Grayce Farms Airport, Fleetville, Pennsylvania, US: LID not in A/FD (FAA LID: PA82)
  - PN90     Ranch-Aero Airport, Roulette, Pennsylvania, US: LID not in A/FD (FAA LID: PN90)
  - PS52     Alberter Farms Airport, Johnstown, Pennsylvania, US: LID not in A/FD (FAA LID: PS52)
  - SC16     Curry Airport, Hartsville, South Carolina, US: LID not in A/FD (FAA LID: SC16)
  - SC19     Lamar Airport, Lamar, South Carolina, US: LID not in A/FD (FAA LID: SC19)
  - SC38     Pocotaligo Airport, Manning, South Carolina, US: LID not in A/FD (FAA LID: SC38)
  - SC87     Avinger Field, Vance, South Carolina, US: LID not in A/FD (FAA LID: SC87)
  - SD44     Cook Field, Chamberlain, South Dakota, US: LID not in A/FD (FAA LID: SD44)
  - SD47     Hunt Field, Eagle Butte, South Dakota, US: LID not in A/FD (FAA LID: SD47)
  - SD48     Blomberg 42 Ranch Pvt Airport, Faith, South Dakota, US: LID not in A/FD (FAA LID: SD48)
  - SD49     Hite Airport, Ferney, South Dakota, US: LID not in A/FD (FAA LID: SD49)
  - SD50     Harrold Municipal Airport, Harrold, South Dakota, US: LID not in A/FD (FAA LID: SD50)
  - SD90     Mitchells Strip, Spearfish, South Dakota, US: LID not in A/FD (FAA LID: SD90)
  - SD97     Oller Airport, Vivian, South Dakota, US: LID not in A/FD (FAA LID: SD97)
  - SN94     Amy Airport, Minneola, Kansas, US: LID not in A/FD (FAA LID: SN94)
  - TA12     Flying B Ranch Airport, Waller, Texas, US: LID not in A/FD (FAA LID: TA12)
  - TA50     Wilkeys Airport, Larue, Texas, US: LID not in A/FD (FAA LID: TA50)
  - TE72     Taylor Field, Bivins, Texas, US: LID not in A/FD (FAA LID: TE72)
  - TN74     Will A Hildreth Farm Airport, Lenoir City, Tennessee, US: LID not in A/FD (FAA LID: TN74)
  - TS46     Hopf Field, Llano, Texas, US: LID not in A/FD (FAA LID: TS46)
  - VA72     Covington Airport, Martinsville, Virginia, US: LID not in A/FD (FAA LID: VA72)
  - VG43     Arrowpoint Airport, Madison, Virginia, US: LID not in A/FD (FAA LID: VG43)
  - VT01     Teal Farm Airport, Huntington, Vermont, US: LID not in A/FD (FAA LID: VT01)
  - WY38     Orchard Ranch Airport, Ten Sleep, Wyoming, US: LID not in A/FD (FAA LID: WY38)

* Also updated the latitude and/or longitude of 39 airports where no change exceeded 0.1 degrees (not itemized).


Version 2026.06.24
==================

* Updated the following 2 airports:

  - BGQO    , Qaqortoq Airport, Qaqortoq, Kujalleq, GL: name changed from "Qaqortoq Airport (scheduled to open on
    16-Apr-2026)", elevation changed from 489 to 505, latitude changed from 60.765833 to 60.766111, longitude changed
    from -46.065 to -46.074722.
  - LLER/ETM, Ilan and Asaf Ramon Airport, Eilat, Southern District, IL: country changed from "IS".


Version 2026.03.25
==================
* Added the following 2 airports:

  - BGQO/   , Qaqortoq Airport (scheduled to open on 16-Apr-2026), Qaqortoq, Kujalleq, GL.
  - YSWS/WSI, Western Sydney Airport (under construction), Badgerys Creek, New South Wales, AU.

Version 2026.03.15
==================

Version numbering contains periods for ease of reading.

Contribution by `Priyansh Kumar Singh <https://github.com/Nik-code>`__ in `#60 <https://github.com/mborsetti/airportsdata/pull/60>`__
-------------------------------------------------------------------------------------------------------------------------------------

* Added the following 16 airports:

  - HLMS/MRA, Misrata International Airport, Misrata, Misrata, LY.
  - LTCV/NKT, Şırnak Şerafettin Elçi Airport, Şırnak, Şırnak, TR.
  - MRAF/ACO, Cobano Airport, C?bano, Puntarenas, CR.
  - MZCK/CUK, Caye Caulker Airport, Caye Caulker, Belize, BZ.
  - MZPL/PLJ, Placencia Airport, Placencia, Stann Creek, BZ.
  - SBJA/JJG, Humberto Ghizzo Bortoluzzi Regional Airport, Jaguaruna, Santa Catarina, BR.
  - ZBDH/BPE, Qinhuangdao Beidaihe Airport, Qinhuangdao, Hebei, CN.
  - ZBLF/LFQ, Linfen Yaodu Airport, Linfen, Shanxi, CN.
  - ZBLL/LLV, L?liang Dawu Airport, L?liang, Shanxi, CN.
  - ZGXX/DXJ, Xiangxi Biancheng Airport, Xiangxi, Hunan, CN.
  - ZLXH/GXH, Gannan Xiahe Airport, Xiahe, Gansu, CN.
  - ZSHZ/HZA, Heze Mudan Airport, Heze, Shandong, CN.
  - ZUKD/KGT, Garze Kangding Airport, Kangding, Sichuan, CN.
  - ZWAL/ACF, Aral Talim Airport, Aral, Xinjiang, CN.
  - ZWQT/JBK, Qitai Jiangbulake Airport, Qitai, Xinjiang, CN.
  - ZWSC/QSZ, Shache Airport, Shache, Xinjiang, CN.

* Updated IATA locator (and potentially other data) for the following 2 airports:

  - OIBP/PGU, Persian Gulf International Airport, Asaluyeh, Bushehr, IR: iata PGU added, city changed from "Asalouyeh",
    latitude changed from 27.3796 to 27.37944, longitude changed from 52.7377 to 52.7375.
  - VIDX/HDO, Hindon Airport, Ghaziabad, Uttar Pradesh, IN: iata HDO added, name changed from "Hindon Air Force Station",
    city added, latitude changed from 28.7077 to 28.70579, longitude changed from 77.3589 to 77.342137.

Other update
------------

* Updated other data for the following airport:

  - LWSK/SKP, Skopje International Airport, Skopje, Ilinden, MK: name changed from "Skopje Alexander the Great Airport".


Version 20260304
================

* Added the following airport:

  - ZBSN/TVS, Tangshan Sannühe Airport, Tangshan, Hebei, CN.


Version 20260208
================

Updated US FAA data to Digital - Chart Supplement (d-CS) released on 22 January 2026. Coverage: United States, Puerto
Rico, U.S. Virgin Islands, and the Pacific Territories.

* Added the following 427 airports:

  - 00TN    , Thompson Farms Airport, Lebanon, Tennessee, US (FAA LID: 00TN)
  - 01TX    , Beulah Field, Graham, Texas, US (FAA LID: 01TX)
  - 01WI    , Kilo Kilo Aerodrome, Wausau, Wisconsin, US (FAA LID: 01WI)
  - 02AN    , Emerald Ridge Airport, Homer, Alaska, US (FAA LID: 02AN)
  - 02NM    , Ffr Animas Landing Strip, Animas, New Mexico, US (FAA LID: 02NM)
  - 03CO    , Blue Water Airport, Saguache, Colorado, US (FAA LID: 03CO)
  - 03FL    , Greens Farm Field, Cape Coral, Florida, US (FAA LID: 03FL)
  - 05NR    , Fox Field, Mebane, North Carolina, US (FAA LID: 05NR)
  - 05UT    , Sand Cove Ranch Airport, Veyo, Utah, US (FAA LID: 05UT)
  - 07TE    , Peak 7 Ranch Airport, Gainesville, Texas, US (FAA LID: 07TE)
  - 08AN    , Base Camp Airstrip, Palmer, Alaska, US (FAA LID: 08AN)
  - 08UT    , Pinelodge Rwy Airport, La Sal, Utah, US (FAA LID: 08UT)
  - 09AN    , Kachemak Landing Airport, Homer, Alaska, US (FAA LID: 09AN)
  - 09MT    , Paint Creek Ranch Airport, Sula, Montana, US (FAA LID: 09MT)
  - 09UT    , Rustler Canyon Airstrip, Moab, Utah, US (FAA LID: 09UT)
  - 0AZ1    , Eagletail Airport, Tonopah, Arizona, US (FAA LID: 0AZ1)
  - 0WI5    , Dog Run Airport, Mondovi, Wisconsin, US (FAA LID: 0WI5)
  - 0WI6    , Pickel Point Airport, Platteville, Wisconsin, US (FAA LID: 0WI6)
  - 10KY    , Gills' Landing Field, Elkton, Kentucky, US (FAA LID: 10KY)
  - 11OR    , Nail Spring Ranch Airport, Bonanza, Oregon, US (FAA LID: 11OR)
  - 11TT    , Rocking L Airport, Sonora, Texas, US (FAA LID: 11TT)
  - 12TA    , Balentine Woodbine Airport, Alvarado, Texas, US (FAA LID: 12TA)
  - 12UT    , Red Annie Ranch Airport, Moab, Utah, US (FAA LID: 12UT)
  - 13TT    , Sunset Ranch Airport, Mico, Texas, US (FAA LID: 13TT)
  - 14TA    , Windy Hill Airport, Iowa Park, Texas, US (FAA LID: 14TA)
  - 14VT    , Crossroad Airport, Newport Center, Vermont, US (FAA LID: 14VT)
  - 15TT    , Aeroplex Airfield, Lucas, Texas, US (FAA LID: 15TT)
  - 16SC    , Horseshoe Landing Airport, Cross Anchor, South Carolina, US (FAA LID: 16SC)
  - 16UT    , Hinrichsen Field, Perry, Utah, US (FAA LID: 16UT)
  - 17WT    , Lathrop Field, Davenport, Washington, US (FAA LID: 17WT)
  - 18GE    , Lefty's Landing Airport, Uvalda, Georgia, US (FAA LID: 18GE)
  - 18NR    , Suggs Field, Kinston, North Carolina, US (FAA LID: 18NR)
  - 19ME    , Estcourt Airport, Estcourt, Maine, US (FAA LID: 19ME)
  - 1LA9    , Jeff Isl Airport, Lafayette, Louisiana, US (FAA LID: 1LA9)
  - 1TN2    , Pops Landing Airport, Sparta, Tennessee, US (FAA LID: 1TN2)
  - 1UT9    , Stirling Farms Airport, Leeds, Utah, US (FAA LID: 1UT9)
  - 21TT    , William Noble Higgins Memorial Aerodrome, Normangee, Texas, US (FAA LID: 21TT)
  - 21UT    , Glastar Airport, Stockton, Utah, US (FAA LID: 21UT)
  - 24CO    , Caddoa Creek Airport, Caddoa, Colorado, US (FAA LID: 24CO)
  - 24LA    , Pk Field, Prairieville, Louisiana, US (FAA LID: 24LA)
  - 24NR    , Indian Creek Airport, Lincolnton, North Carolina, US (FAA LID: 24NR)
  - 24PS    , Spring Hill Airport, Sterling, Pennsylvania, US (FAA LID: 24PS)
  - 26AS    , Marvell West Airport, Marvell, Arkansas, US (FAA LID: 26AS)
  - 26GA    , Little Airport, Summerville, Georgia, US (FAA LID: 26GA)
  - 26IA    , Midway View Farms Airport, Correctionville, Iowa, US (FAA LID: 26IA)
  - 26IL    , Straeter Rla Airport, Highland, Illinois, US (FAA LID: 26IL)
  - 27PS    , Van Blarcom Airport, Columbia Cross Roads, Pennsylvania, US (FAA LID: 27PS)
  - 28DE    , Albanna Aviation Airport, Felton, Delaware, US (FAA LID: 28DE)
  - 28NE    , Big Thunder Airport, Clarkson, Nebraska, US (FAA LID: 28NE)
  - 29ID    , Patterson Field, Emmett, Idaho, US (FAA LID: 29ID)
  - 29IL    , Judd Farms Airport, Lostant, Illinois, US (FAA LID: 29IL)
  - 2AK7    , Helio Airport, Big Lake, Alaska, US (FAA LID: 2AK7)
  - 2KY0    , Skyfall Airport, Scottsville, Kentucky, US (FAA LID: 2KY0)
  - 2MO8    , Bob White Airport, El Dorado Springs, Missouri, US (FAA LID: 2MO8)
  - 2MY5    , Sevcik Farms Airport, Faribault, Minnesota, US (FAA LID: 2MY5)
  - 2ND8    , Fiebiger Airport, Montplier, North Dakota, US (FAA LID: 2ND8)
  - 2NK5    , Eagles Eye Airport, North Bay, New York, US (FAA LID: 2NK5)
  - 2SD8    , Wings On The Prairie Airport, Sioux Falls, South Dakota, US (FAA LID: 2SD8)
  - 2UT9    , Glogen Farms Airport, Wellsville, Utah, US (FAA LID: 2UT9)
  - 30AZ    , Kielberg Canyon Airport, Tucson, Arizona, US (FAA LID: 30AZ)
  - 31GE    , Tailwind Ranch Airport, Gordon, Georgia, US (FAA LID: 31GE)
  - 31ID    , Thunder Ridge Airport, Sandpioint, Idaho, US (FAA LID: 31ID)
  - 32ID    , Chimney Creek Airport, Fairfield, Idaho, US (FAA LID: 32ID)
  - 32NR    , Sandy Creek Airport, Mooresville, North Carolina, US (FAA LID: 32NR)
  - 32TT    , The Mesquite Bean Airport, Ovalo, Texas, US (FAA LID: 32TT)
  - 33IA    , Marine Farms Field, Wilton, Iowa, US (FAA LID: 33IA)
  - 33NC    , Easley Acres Airport, Lucama, North Carolina, US (FAA LID: 33NC)
  - 34IN    , Old Glory Field, Fort Wayne, Indiana, US (FAA LID: 34IN)
  - 34NY    , Horizon Air Airport, Waterloo, New York, US (FAA LID: 34NY)
  - 34PA    , Lykens Valley Flying Assoc Airport, Elizabethville, Pennsylvania, US (FAA LID: 34PA)
  - 35AZ    , Lima Hana Field, Sunizona, Arizona, US (FAA LID: 35AZ)
  - 35CN    , Cat Ag Air Airport, Newman, California, US (FAA LID: 35CN)
  - 35IA    , Frazier Airport, De Witt, Iowa, US (FAA LID: 35IA)
  - 35ID    , Bluebird Airport, Salmon, Idaho, US (FAA LID: 35ID)
  - 35NR    , Friendship Field, Mars Hill, North Carolina, US (FAA LID: 35NR)
  - 36IA    , Tonner Field, Beaman, Iowa, US (FAA LID: 36IA)
  - 37CN    , Cecil Ranch Airport, Grimes, California, US (FAA LID: 37CN)
  - 37IA    , Nemo Field, De Witt, Iowa, US (FAA LID: 37IA)
  - 38IA    , Garys Airport, Estherville, Iowa, US (FAA LID: 38IA)
  - 38IL    , Hamer Rla Airport, Dana, Illinois, US (FAA LID: 38IL)
  - 38MS    , Yellow Dog Airport, Isola, Mississippi, US (FAA LID: 38MS)
  - 38WT    , Northstar Airport, Davenport, Washington, US (FAA LID: 38WT)
  - 39ID    , Getaway Field, Kendrick, Idaho, US (FAA LID: 39ID)
  - 39IL    , Kieser Field, Bloomington, Illinois, US (FAA LID: 39IL)
  - 39MS    , Benton Farms Airport, Clinton, Mississippi, US (FAA LID: 39MS)
  - 39MT    , Flying E Ranch Airport, Helena, Montana, US (FAA LID: 39MT)
  - 39TT    , Sugar Creek Field, Cleburne, Texas, US (FAA LID: 39TT)
  - 3AK9    , Skyland Airpark, Willow/Caswell, Alaska, US (FAA LID: 3AK9)
  - 3MO7    , Kelly Field, Bonne Terre, Missouri, US (FAA LID: 3MO7)
  - 3TN4    , Dunlap Airpark, Dunlap, Tennessee, US (FAA LID: 3TN4)
  - 3VG5    , Kinman Airport, Altavista, Virginia, US (FAA LID: 3VG5)
  - 3WN1    , Digger Doug Airport, Dodgeville, Wisconsin, US (FAA LID: 3WN1)
  - 40OR    , Medella Bison Ranch Airport, Ashland, Oregon, US (FAA LID: 40OR)
  - 41MO    , Sawyer Creek Airport, Rogersville, Missouri, US (FAA LID: 41MO)
  - 41NR    , Monarch Field, Mocksville, North Carolina, US (FAA LID: 41NR)
  - 42IN    , Gaerte Airport, Avilla, Indiana, US (FAA LID: 42IN)
  - 42MT    , Crown Ranch Airpark, Seeley Lake, Montana, US (FAA LID: 42MT)
  - 42NE    , Jones Airport, Benkelman, Nebraska, US (FAA LID: 42NE)
  - 42TS    , Hye Sky Farms Airport, Hye, Texas, US (FAA LID: 42TS)
  - 42TX    , Magee Airport, Wolfe City, Texas, US (FAA LID: 42TX)
  - 43AS    , Griffin Airport, Helena, Arkansas, US (FAA LID: 43AS)
  - 43IA    , Giggity Acres Airport, Dewitt, Iowa, US (FAA LID: 43IA)
  - 43ID    , Harris Ridge Airport, Kooskia, Idaho, US (FAA LID: 43ID)
  - 43MT    , Government Mountain Airport, Noxon, Montana, US (FAA LID: 43MT)
  - 44NK    , Bengtsson Field, Gilboa, New York, US (FAA LID: 44NK)
  - 47GE    , Flylander Farm Airport, Summerville, Georgia, US (FAA LID: 47GE)
  - 47ID    , Flying Thunderbolt Ranch Airport, Emmett, Idaho, US (FAA LID: 47ID)
  - 47MT    , 66 Ranch Airstrip, Ennis, Montana, US (FAA LID: 47MT)
  - 48ID    , Ski Valley Airpark, Mc Call, Idaho, US (FAA LID: 48ID)
  - 48LA    , Countryside Airport, Jennings, Louisiana, US (FAA LID: 48LA)
  - 48MY    , Bosch Farm Airport, Montevideo, Minnesota, US (FAA LID: 48MY)
  - 48NR    , Blackbriar Airport, Pelham, North Carolina, US (FAA LID: 48NR)
  - 49ID    , R7 Aero Airport, Fruitland, Idaho, US (FAA LID: 49ID)
  - 4AR4    , Rice Field, Corning, Arkansas, US (FAA LID: 4AR4)
  - 4FA1    , Rockin G Ranch Airport, Umatilla, Florida, US (FAA LID: 4FA1)
  - 4FA2    , Croom A Chobee Airport, Bushnell, Florida, US (FAA LID: 4FA2)
  - 4KY8    , Sargents Field, West Liberty, Kentucky, US (FAA LID: 4KY8)
  - 4MD5    , Hunting Creek Farm Airport, Prince Frederick, Maryland, US (FAA LID: 4MD5)
  - 4MO5    , Jj Gyro Park Airport, Gerald, Missouri, US (FAA LID: 4MO5)
  - 4MT4    , West Wind Airfield, Reed Point, Montana, US (FAA LID: 4MT4)
  - 4OR1    , Bryant Airport, Madras, Oregon, US (FAA LID: 4OR1)
  - 4OR9    , Country Squire Airpark, Sandy, Oregon, US (FAA LID: 4OR9)
  - 4PN8    , Swift Run Field, New Oxford, Pennsylvania, US (FAA LID: 4PN8)
  - 4TA6    , Comanche Caves Ranch Airport, Hunt, Texas, US (FAA LID: 4TA6)
  - 4TN9    , Island Bend Farms Airport, Bath Springs, Tennessee, US (FAA LID: 4TN9)
  - 4VG3    , King Fisher Field, Pennington Gap, Virginia, US (FAA LID: 4VG3)
  - 51AL    , Ardmore Airport, Ardmore, Alabama, US (FAA LID: 51AL)
  - 51AS    , Burks Airport, Helena, Arkansas, US (FAA LID: 51AS)
  - 51ID    , Little Weiser Airport, Little Valley, Idaho, US (FAA LID: 51ID)
  - 52MO    , Rainbow Avn Stol Airport, Kingsville, Missouri, US (FAA LID: 52MO)
  - 52NR    , Derksen Airport, Goldston, North Carolina, US (FAA LID: 52NR)
  - 52OA    , Area 52 Airport, Alexandria, Ohio, US (FAA LID: 52OA)
  - 53AZ    , Oms Uas Test Range, Kingman, Arizona, US (FAA LID: 53AZ)
  - 53MT    , Pass Creek Airport, Belgrade, Montana, US (FAA LID: 53MT)
  - 53NR    , Barker Private Stol Airport, Asheville, North Carolina, US (FAA LID: 53NR)
  - 54MA    , Wolf River Airport, Rossville, Tennessee, US (FAA LID: 54MA)
  - 54NR    , Bethany Airport, Reidsville, North Carolina, US (FAA LID: 54NR)
  - 54TN    , Argonaut Airstrip, Collierville, Tennessee, US (FAA LID: 54TN)
  - 55FL    , Parts And Sparks Airport, Bunnell, Florida, US (FAA LID: 55FL)
  - 55NR    , Fivepoints Field, Oakboro, North Carolina, US (FAA LID: 55NR)
  - 55UT    , Shipley Field, Tremonton, Utah, US (FAA LID: 55UT)
  - 56MO    , Flying E Field, Fulton, Missouri, US (FAA LID: 56MO)
  - 57MI    , Historic Acme Skyport Airport, Acme, Michigan, US (FAA LID: 57MI)
  - 57PN    , Victor Curtis Airport, Mansfield, Pennsylvania, US (FAA LID: 57PN)
  - 58TN    , Stol-It Farm Airport, Linden, Tennessee, US (FAA LID: 58TN)
  - 59CO    , Nilhas Aero Ranch Airport, Pierce, Colorado, US (FAA LID: 59CO)
  - 59TN    , Wynnburg Airport, Ridgely, Tennessee, US (FAA LID: 59TN)
  - 5AK9    , Grandview Subdivision Airport, Palmer, Alaska, US (FAA LID: 5AK9)
  - 5AN5    , Chinitna West Glacier Airport, Homer, Alaska, US (FAA LID: 5AN5)
  - 5IG9    , Kramer Airfield, Sulphur Springs, Indiana, US (FAA LID: 5IG9)
  - 5IL7    , Redeker Airport, Milford, Illinois, US (FAA LID: 5IL7)
  - 5KS3    , Birddog Field, Plainville, Kansas, US (FAA LID: 5KS3)
  - 5KY2    , Papaws Landing Airport, Shelbyville, Kentucky, US (FAA LID: 5KY2)
  - 5KY6    , Hp Field, Graham, Kentucky, US (FAA LID: 5KY6)
  - 5MI2    , Harrisville Airport, Harrisville, Michigan, US (FAA LID: 5MI2)
  - 5NK6    , Nautical Mile Airport, Fort Plain, New York, US (FAA LID: 5NK6)
  - 5WA4    , Boisselle Airport, White Swan, Washington, US (FAA LID: 5WA4)
  - 60AS    , Junior Smith Airport, Elaine, Arkansas, US (FAA LID: 60AS)
  - 60GE    , Flying B Farm Airport, Arnoldsville, Georgia, US (FAA LID: 60GE)
  - 60WN    , Letties Landing Airport, Centerville, Washington, US (FAA LID: 60WN)
  - 61KS    , West Branch Airport, Eureka, Kansas, US (FAA LID: 61KS)
  - 62KT    , Rogers Airfield, Ravenna, Kentucky, US (FAA LID: 62KT)
  - 62MA    , Field Of Dreams Airport, North Dighton, Massachusetts, US (FAA LID: 62MA)
  - 63TN    , Providence Landing Airport, Madisonville, Tennessee, US (FAA LID: 63TN)
  - 64GE    , Wcc Airport, Tallapoosa, Georgia, US (FAA LID: 64GE)
  - 64TN    , Hallelujah Farm Airport, Pulaski, Tennessee, US (FAA LID: 64TN)
  - 66AR    , Hoerler Farms Airport, Siloam Springs, Arkansas, US (FAA LID: 66AR)
  - 6AL0    , Flying Tigers Winery & Resort Airport, Heflin, Alabama, US (FAA LID: 6AL0)
  - 6AL5    , Big Sky Farms Airport, Speed, Alabama, US (FAA LID: 6AL5)
  - 6AR5    , Tidwell Flying Service Airport, Carlisle, Arkansas, US (FAA LID: 6AR5)
  - 6CO5    , Maga Field, Wiggins, Colorado, US (FAA LID: 6CO5)
  - 6KS7    , Bug Field, Haven, Kansas, US (FAA LID: 6KS7)
  - 6KS8    , Towanda Farms Airport, Towanda, Kansas, US (FAA LID: 6KS8)
  - 6TX0    , Yancey Creek Ranch North Airport, Lampasas, Texas, US (FAA LID: 6TX0)
  - 71TA    , Chumchal Farms Airport, Wharton, Texas, US (FAA LID: 71TA)
  - 72AR    , Caddo Lndg Airport, Glenwood, Arkansas, US (FAA LID: 72AR)
  - 73TS    , South Trap Airport, Christoval, Texas, US (FAA LID: 73TS)
  - 74LA    , Promised Landings Airport, Prairieville, Louisiana, US (FAA LID: 74LA)
  - 74ND    , Metz Field, Northwood, North Dakota, US (FAA LID: 74ND)
  - 74TN    , Hog Lot Landing Airport, Hixson, Tennessee, US (FAA LID: 74TN)
  - 75CO    , Mrw Farms Airfield, Nunn, Colorado, US (FAA LID: 75CO)
  - 75FA    , Brownville Airport, Arcadia, Florida, US (FAA LID: 75FA)
  - 75NC    , Meylor Landing Airport, Stokesdale, North Carolina, US (FAA LID: 75NC)
  - 77MT    , Ferguson Airport, Billings, Montana, US (FAA LID: 77MT)
  - 78AR    , Cedar Crest Airstrip, Diamond City, Arkansas, US (FAA LID: 78AR)
  - 78VA    , Rassawek Airstrip, Columbia, Virginia, US (FAA LID: 78VA)
  - 79MT    , Johny Creek Airport, Baker, Montana, US (FAA LID: 79MT)
  - 79NR    , Wyatt Airport, Elizabeth City, North Carolina, US (FAA LID: 79NR)
  - 79SC    , Green Sea Airport, Green Sea, South Carolina, US (FAA LID: 79SC)
  - 7AK0    , Hillside Airstrip, Susitna, Alaska, US (FAA LID: 7AK0)
  - 7IL3    , Flying Q Farm Airport, Marengo, Illinois, US (FAA LID: 7IL3)
  - 7KS6    , Deep Creek Airport, Manhattan, Kansas, US (FAA LID: 7KS6)
  - 7KS8    , Moore Short Field Landing Airport, Topeka, Kansas, US (FAA LID: 7KS8)
  - 7KY4    , Spring Creek Airpark, Albany, Kentucky, US (FAA LID: 7KY4)
  - 7MO5    , Buckhorn Airport, Bakersfield, Missouri, US (FAA LID: 7MO5)
  - 7MO8    , Laughlin Airport, Foster, Missouri, US (FAA LID: 7MO8)
  - 7OK7    , Panhandle Airport, Optima, Oklahoma, US (FAA LID: 7OK7)
  - 7OR2    , Flying Squirrel Ranch Airport, Lostine, Oregon, US (FAA LID: 7OR2)
  - 7TA4    , V Bar Airstrip, Fairfield, Texas, US (FAA LID: 7TA4)
  - 7VA5    , Long Island Airport, Long Island, Virginia, US (FAA LID: 7VA5)
  - 80AL    , Sunflower Ranch Airport, Tyler, Alabama, US (FAA LID: 80AL)
  - 80AR    , King Airport, Helena, Arkansas, US (FAA LID: 80AR)
  - 81TN    , Southfork Airport, Bristol, Tennessee, US (FAA LID: 81TN)
  - 81XA    , Buttermilk Air Strip, Florence, Texas, US (FAA LID: 81XA)
  - 82AR    , Barton Airport, Barton, Arkansas, US (FAA LID: 82AR)
  - 82ME    , Red Pine Grove Airport, Clayton Lake, Maine, US (FAA LID: 82ME)
  - 82TA    , Hoelscher Ag Airport, San Angelo, Texas, US (FAA LID: 82TA)
  - 83MS    , Jolley Field, Pelahatchie, Mississippi, US (FAA LID: 83MS)
  - 83NR    , Wootens Airport, Statesville, North Carolina, US (FAA LID: 83NR)
  - 84TN    , Elkins Field, Andersonville, Tennessee, US (FAA LID: 84TN)
  - 86OA    , Bordner Airport, Bowling Green, Ohio, US (FAA LID: 86OA)
  - 87KS    , Hayland Airport, Dorrance, Kansas, US (FAA LID: 87KS)
  - 87MS    , Maloney Airport, Tupelo, Mississippi, US (FAA LID: 87MS)
  - 87NR    , Columbia Airstrip, Columbia, North Carolina, US (FAA LID: 87NR)
  - 87TN    , Rainey Airport, Obion, Tennessee, US (FAA LID: 87TN)
  - 88GA    , Epic Field, Hamilton, Georgia, US (FAA LID: 88GA)
  - 88MI    , Eagle Ii Airport, Lewiston, Michigan, US (FAA LID: 88MI)
  - 88OK    , Boice Field, Marlow, Oklahoma, US (FAA LID: 88OK)
  - 89NE    , Mccardles Airport, Blair, Nebraska, US (FAA LID: 89NE)
  - 89NR    , Georgia Rd Field, Mocksville, North Carolina, US (FAA LID: 89NR)
  - 8CD4    , Basin Field, Elizabeth, Colorado, US (FAA LID: 8CD4)
  - 8IL3    , Alms Rla Airport, Sullivan, Illinois, US (FAA LID: 8IL3)
  - 8MO1    , Life Farm Airport, Springfield, Missouri, US (FAA LID: 8MO1)
  - 8MO4    , Mans Field, Annapolis, Missouri, US (FAA LID: 8MO4)
  - 8VA9    , Valley View Airport, Nokesville, Virginia, US (FAA LID: 8VA9)
  - 8WV3    , Snowshoe Airport, Mingo, West Virginia, US (FAA LID: 8WV3)
  - 8XA6    , Blackjack Field, Aubrey, Texas, US (FAA LID: 8XA6)
  - 90AR    , Alos Field, Jonesboro, Arkansas, US (FAA LID: 90AR)
  - 90FD    , Citrus Hedging Ranch Airport, Okeechobee, Florida, US (FAA LID: 90FD)
  - 91AS    , Crumrod Airport, Elaine, Arkansas, US (FAA LID: 91AS)
  - 91ME    , J & S Field, Stetson, Maine, US (FAA LID: 91ME)
  - 91TN    , Powder Mill Field, Ashland City, Tennessee, US (FAA LID: 91TN)
  - 91XS    , Stark Field, Merkel, Texas, US (FAA LID: 91XS)
  - 92TN    , Freedom Field, Bradyville, Tennessee, US (FAA LID: 92TN)
  - 93FA    , Psycho Field, Baker, Florida, US (FAA LID: 93FA)
  - 94MD    , Conquest Field, Centreville, Maryland, US (FAA LID: 94MD)
  - 94TN    , Airborne Acres Airport, Campbellsville, Tennessee, US (FAA LID: 94TN)
  - 94TT    , Evridge Farms Airport, Midkiff, Texas, US (FAA LID: 94TT)
  - 95MO    , Green Berry Airport, Eagle Rock, Missouri, US (FAA LID: 95MO)
  - 95SC    , Buckeye Field, Williston, South Carolina, US (FAA LID: 95SC)
  - 96AL    , Bent Oak Airport, Bay Minette, Alabama, US (FAA LID: 96AL)
  - 96FA    , Duette Training Facility Airport, Duette, Florida, US (FAA LID: 96FA)
  - 97KS    , Wingit Field, Augusta, Kansas, US (FAA LID: 97KS)
  - 98AA    , Golden Eagle Airpark, Homer, Alaska, US (FAA LID: 98AA)
  - 98SC    , Cowtown Airport, Govan, South Carolina, US (FAA LID: 98SC)
  - 99TA    , Echtle Field, Castroville, Texas, US (FAA LID: 99TA)
  - 99TT    , Star K Ranch Airport, Agua Nueva, Texas, US (FAA LID: 99TT)
  - 9AL6    , Flying Hog Farm Airport, Columbia, Alabama, US (FAA LID: 9AL6)
  - 9KS3    , Lucky Dog Airport, Dodge City, Kansas, US (FAA LID: 9KS3)
  - 9KS8    , Gators Place Airport, Towanda, Kansas, US (FAA LID: 9KS8)
  - 9KS9    , South Fork Airpark, Cheney, Kansas, US (FAA LID: 9KS9)
  - 9MY7    , Mikes Aerodrome, Albany, Minnesota, US (FAA LID: 9MY7)
  - 9TX3    , Horan Airport, Plainview, Texas, US (FAA LID: 9TX3)
  - 9TX4    , Flying H Ranch Airport, Liberty Hill, Texas, US (FAA LID: 9TX4)
  - 9TX5    , Camp Bullis Als (Cals) Airport, San Antonio, Texas, US (FAA LID: 9TX5)
  - 9TX6    , Beggs Ranch Airport, Post, Texas, US (FAA LID: 9TX6)
  - 9TX7    , Hitex Airport, Pottsboro, Texas, US (FAA LID: 9TX7)
  - 9VA0    , Bath Alum Airport, Warm Springs, Virginia, US (FAA LID: 9VA0)
  - 9VA1    , Holly Point Airport, Mathews, Virginia, US (FAA LID: 9VA1)
  - 9VA4    , Franwood Farms Inc Airport, New Market, Virginia, US (FAA LID: 9VA4)
  - 9VA6    , Saunders Field, Richmond, Virginia, US (FAA LID: 9VA6)
  - 9VG9    , Jucapa Farms Airport, Winchester, Virginia, US (FAA LID: 9VG9)
  - 9WA4    , Piper Canyon Airport, Goldendale, Washington, US (FAA LID: 9WA4)
  - 9WA7    , Albritton Airport, Buckley, Washington, US (FAA LID: 9WA7)
  - 9WI1    , Black Otter Airport, Hortonville, Wisconsin, US (FAA LID: 9WI1)
  - 9WI2    , Flying Dollar Ranch Airport, Maribel, Wisconsin, US (FAA LID: 9WI2)
  - 9WI3    , Buchholz Farm Airport, Morrison, Wisconsin, US (FAA LID: 9WI3)
  - 9WI4    , Faken Airport, New Berlin, Wisconsin, US (FAA LID: 9WI4)
  - 9WI5    , Tamarack Airport, Palmyra, Wisconsin, US (FAA LID: 9WI5)
  - 9WI6    , Kitty Hawk Estates Airport, Polar, Wisconsin, US (FAA LID: 9WI6)
  - AK07    , Longmere Lake Air Strip, Soldotna, Alaska, US (FAA LID: AK07)
  - AK80    , Malnarick Park Airport, Houston, Alaska, US (FAA LID: AK80)
  - AL47    , Belforest Field, Daphne, Alabama, US (FAA LID: AL47)
  - AL61    , Elk Haven Airport, Rogersville, Alabama, US (FAA LID: AL61)
  - AS04    , Hubbards Airport, Marvell, Arkansas, US (FAA LID: AS04)
  - AS11    , Rohrscheib Airport, Helena, Arkansas, US (FAA LID: AS11)
  - AS31    , Carpenter Field, Jonesboro, Arkansas, US (FAA LID: AS31)
  - AS91    , Gaylons Airport, Elaine, Arkansas, US (FAA LID: AS91)
  - AZ19    , Woods Bay Winery Airport, Willcox, Arizona, US (FAA LID: AZ19)
  - CD05    , Shkyview Airport, Gardner, Colorado, US (FAA LID: CD05)
  - CL44    , Latierra Airport, Murrieta, California, US (FAA LID: CL44)
  - CO32    , Las Mesitas Airport, Antonito, Colorado, US (FAA LID: CO32)
  - CO61    , Ak Su Airport, Canon City, Colorado, US (FAA LID: CO61)
  - CT21    , Sunnyvale Field, North Stonington, Connecticut, US (FAA LID: CT21)
  - FA63    , Foxraven Field, Brooksville, Florida, US (FAA LID: FA63)
  - FD23    , Rutland Runway Airport, Inverness, Florida, US (FAA LID: FD23)
  - GE56    , Smith Field, Greensboro, Georgia, US (FAA LID: GE56)
  - GE61    , Brownstone Airpark, Cave Spring, Georgia, US (FAA LID: GE61)
  - ID89    , Lindberg Private Airport, Carmen, Idaho, US (FAA LID: ID89)
  - IL54    , Burns Field, Shippman, Illinois, US (FAA LID: IL54)
  - IN37    , Creekbend Airport, Elletsville, Indiana, US (FAA LID: IN37)
  - IN47    , Powell Airport, Atlanta, Indiana, US (FAA LID: IN47)
  - K17Q    , Hiebert Airfield, Goessel, Kansas, US (FAA LID: 17Q)
  - K1T8    , Bulverde Airpark, San Antonio, Texas, US (FAA LID: 1T8)
  - K1UT    , Fremont Island Lower Airport, Hooper, Utah, US (FAA LID: 1UT)
  - K28X    , Green Acres Airfield, Pampa, Texas, US (FAA LID: 28X)
  - K2UT    , Fremont Island Upper Airport, Hooper, Utah, US (FAA LID: 2UT)
  - K3JA    , Yates Center Municipal Airport, Yates Center, Kansas, US (FAA LID: 3JA)
  - K3K4    , Borth Field, Meade, Kansas, US (FAA LID: 3K4)
  - K3KS    , Hf Strip, Fowler, Kansas, US (FAA LID: 3KS)
  - K3OK    , Biggs Airport Airport, Wellston, Oklahoma, US (FAA LID: 3OK)
  - K6KS    , Butler Airpark, Rose Hill, Kansas, US (FAA LID: 6KS)
  - K73G    , Cherry Field, Nunica, Michigan, US (FAA LID: 73G)
  - K76A    , Efs Airport, Shoffner, Arkansas, US (FAA LID: 76A)
  - K7ME    , Fort Kent Municipal Airport, Fort Kent, Maine, US (FAA LID: 7ME)
  - K7S1    , 7 Oaks Flight Park Airport, Fairfax, South Carolina, US (FAA LID: 7S1)
  - K93M    , Rueter Airfield, Palmyra, Missouri, US (FAA LID: 93M)
  - K9U0    , Turner Airport, Turner, Montana, US (FAA LID: 9U0)
  - K9U1    , Wilsall Airport, Wilsall, Montana, US (FAA LID: 9U1)
  - K9U7    , Currant Ranch Airport, Currant, Nevada, US (FAA LID: 9U7)
  - K9V5    , Modisett Airport, Rushville, Nebraska, US (FAA LID: 9V5)
  - K9V6    , Martin Municipal Airport, Martin, South Dakota, US (FAA LID: 9V6)
  - K9V7    , Eads Municipal Airport, Eads, Colorado, US (FAA LID: 9V7)
  - K9V9    , Chamberlain Municipal Airport, Chamberlain, South Dakota, US (FAA LID: 9V9)
  - K9VG    , Campbell Field, Weirwood, Virginia, US (FAA LID: 9VG)
  - K9W8    , Baublitz Commercial Airport, Brogue, Pennsylvania, US (FAA LID: 9W8)
  - K9W9    , Clio Crop Care Airport, Clio, South Carolina, US (FAA LID: 9W9)
  - KBFZ    , Albertville Regional/Thomas J Brumlik Field, Albertville, Alabama, US (FAA LID: BFZ)
  - KC57    , Millers Landing Airport, Elsie, Michigan, US (FAA LID: C57)
  - KC88    , Tkaczyk Field, Oakley, Michigan, US (FAA LID: C88)
  - KK22    , Mills Field, South Hutchinson, Kansas, US (FAA LID: K22)
  - KL80    , Monache Meadows Airport, Lone Pine, California, US (FAA LID: L80)
  - KM64    , Jenkinson Airport, Meade, Kansas, US (FAA LID: M64)
  - KN49    , Rose Quartz Ranch Airport, Stagecoach, Nevada, US (FAA LID: N49)
  - KOK1    , Stearmans Roost Airport, Vinita, Oklahoma, US (FAA LID: OK1)
  - KS44    , Plains Municipal Airport, Plains, Kansas, US (FAA LID: S44)
  - KSVR    , South Valley Regional Airport, Salt Lake City, Utah, US (FAA LID: SVR)
  - KT47    , Finney Field, Howe, Texas, US (FAA LID: T47)
  - KX16    , Tailwheel Acres Airport, Valley View, Texas, US (FAA LID: X16)
  - MI03    , Gentner Strip, Ruth, Michigan, US (FAA LID: MI03)
  - MI17    , Joyce Binns Memorial Airport, Blissfield, Michigan, US (FAA LID: MI17)
  - MI31    , Nartron Field, Reed City, Michigan, US (FAA LID: MI31)
  - MI34    , Fancy Field, Au Gres, Michigan, US (FAA LID: MI34)
  - MI45    , Lost Creek Airport, Luzerne, Michigan, US (FAA LID: MI45)
  - MN21    , Pietenpol Field, Cherry Grove, Minnesota, US (FAA LID: MN21)
  - MN26    , North Lake Landing Airport, Lindstrom, Minnesota, US (FAA LID: MN26)
  - MS44    , Fighting Bayou Airport, Minter City, Mississippi, US (FAA LID: MS44)
  - MS51    , Memory Landing Airport, Brookhaven, Mississippi, US (FAA LID: MS51)
  - MS62    , Frisbee Lndg Airport, Valley Park, Mississippi, US (FAA LID: MS62)
  - MS92    , Paul's Flying Svc Airport, Dundee, Mississippi, US (FAA LID: MS92)
  - MT63    , Dog Leg Airport, East Helena, Montana, US (FAA LID: MT63)
  - MT73    , Wolf Creek Airport, Stanford, Montana, US (FAA LID: MT73)
  - MT84    , Candylands Airport, Big Arm, Montana, US (FAA LID: MT84)
  - MT92    , Garoutte Ranch Airport, Reed Point, Montana, US (FAA LID: MT92)
  - MT96    , Ram Ranch Runway Airport, Helena, Montana, US (FAA LID: MT96)
  - MY02    , Demmers Field, Jordan, Minnesota, US (FAA LID: MY02)
  - MY43    , Moyer Airport, Holloway, Minnesota, US (FAA LID: MY43)
  - MY88    , Henning/Boldt Airport, Rushmore, Minnesota, US (FAA LID: MY88)
  - NC76    , Rondo Airport, Tryon, North Carolina, US (FAA LID: NC76)
  - ND15    , Simon Field, Hannover, North Dakota, US (FAA LID: ND15)
  - ND29    , Flying M Ranch Airport, Hatton, North Dakota, US (FAA LID: ND29)
  - ND38    , Blu Skyz Airport, Minot, North Dakota, US (FAA LID: ND38)
  - ND56    , Rustad Airport, White Shield, North Dakota, US (FAA LID: ND56)
  - ND58    , Gudgel Airport, Colfax, North Dakota, US (FAA LID: ND58)
  - ND64    , Rue Ranch Airfield, Sheyenne, North Dakota, US (FAA LID: ND64)
  - ND83    , Allmaras Aviation Airport, New Rockford, North Dakota, US (FAA LID: ND83)
  - ND84    , Skaar Farm Airfield, New Rockford, North Dakota, US (FAA LID: ND84)
  - NE53    , Stuhlmiller Field, Alliance, Nebraska, US (FAA LID: NE53)
  - NE85    , Jims Agri-Air Airport, Sutton, Nebraska, US (FAA LID: NE85)
  - NK35    , Mariwill Airport, Moravia, New York, US (FAA LID: NK35)
  - NM61    , Runway Bay Airport, Logan, New Mexico, US (FAA LID: NM61)
  - NR13    , Daghita Airport, Norlina, North Carolina, US (FAA LID: NR13)
  - NR76    , Barker Field, Linden, North Carolina, US (FAA LID: NR76)
  - NY39    , Hard Barn Cargas Farm Airport, Sinclairville, New York, US (FAA LID: NY39)
  - NY75    , Stol Performance Airport, Bennington, New York, US (FAA LID: NY75)
  - OH09    , One Shot Airport, Howard, Ohio, US (FAA LID: OH09)
  - OH51    , Kathamel Airport, Versailles, Ohio, US (FAA LID: OH51)
  - OH95    , Tailwheel Lane Airport, Circleville, Ohio, US (FAA LID: OH95)
  - OK29    , Travis Airport, Marietta, Oklahoma, US (FAA LID: OK29)
  - OK56    , Sopwith Ldg Airport, Lexington, Oklahoma, US (FAA LID: OK56)
  - OL42    , Semper Fi Lndg Airport, Spiro, Oklahoma, US (FAA LID: OL42)
  - OL46    , Reed Aero Airport, Erick, Oklahoma, US (FAA LID: OL46)
  - OL47    , Hallum Ranch Airport, Wewoka, Oklahoma, US (FAA LID: OL47)
  - OL49    , Walnut Creek Landing Airport, Blanchard, Oklahoma, US (FAA LID: OL49)
  - OL55    , Blackberry Hill Airport, Perkins, Oklahoma, US (FAA LID: OL55)
  - OL60    , Stol In Airport, Catoosa, Oklahoma, US (FAA LID: OL60)
  - OL68    , B&S Ranch Airport, Bristow, Oklahoma, US (FAA LID: OL68)
  - OL70    , Skyroads Airport, Ninnekah, Oklahoma, US (FAA LID: OL70)
  - OR48    , Placer Airport, Grants Pass, Oregon, US (FAA LID: OR48)
  - OR77    , Beggs Airstrip, Aumsville, Oregon, US (FAA LID: OR77)
  - OR88    , Valley View Airport, Estacada, Oregon, US (FAA LID: OR88)
  - PA55    , Brokenstraw Airport, Pittsfield, Pennsylvania, US (FAA LID: PA55)
  - SD15    , Fleurish Farm Airport, Elk Point, South Dakota, US (FAA LID: SD15)
  - TA77    , Flyers Ridge Airport, Willis, Texas, US (FAA LID: TA77)
  - TA90    , Doublewide Ranch Airport, Granbury, Texas, US (FAA LID: TA90)
  - TA95    , Central Custom Ag Aviation Airport, Hartley, Texas, US (FAA LID: TA95)
  - TE02    , Rivet Ranch Airport, Dublin, Texas, US (FAA LID: TE02)
  - TE35    , Fill Or Kill Airport, Walnut Springs, Texas, US (FAA LID: TE35)
  - TE40    , B.S. Air Ranch Airport, Ennis, Texas, US (FAA LID: TE40)
  - TE54    , Wright Airport, San Angelo, Texas, US (FAA LID: TE54)
  - TN09    , Bearhawks Den Airport, Carthage, Tennessee, US (FAA LID: TN09)
  - TN81    , Rattlesnake Ridge Airport, Indian Mound, Tennessee, US (FAA LID: TN81)
  - TN95    , Ridgely Airport, Ridgely, Tennessee, US (FAA LID: TN95)
  - TS87    , Plane & Fancy Airport, Fort Mckavett, Texas, US (FAA LID: TS87)
  - TT11    , Goggans Airfield, Sulphur Springs, Texas, US (FAA LID: TT11)
  - TT18    , Lionwood Airport, Bellville, Texas, US (FAA LID: TT18)
  - TT26    , Cross L Ranch Airport, Iraan, Texas, US (FAA LID: TT26)
  - TT27    , Johnson Ranch Airport, Justiceburg, Texas, US (FAA LID: TT27)
  - TT29    , Davidson Farms Airport, Roxton, Texas, US (FAA LID: TT29)
  - TT34    , Newberry Ranches Airport, Langtry, Texas, US (FAA LID: TT34)
  - TT35    , Mount Sharp Airpark, Wimberley, Texas, US (FAA LID: TT35)
  - TT47    , Adams Field, Anna, Texas, US (FAA LID: TT47)
  - TT53    , Aeromigos Airfield, Terlingua, Texas, US (FAA LID: TT53)
  - TT57    , Mangham Airport, Mullin, Texas, US (FAA LID: TT57)
  - TT73    , Vogt's Vista Airport, Canton, Texas, US (FAA LID: TT73)
  - TX14    , Boneyard Airstrip, Washington, Texas, US (FAA LID: TX14)
  - TX32    , Yellowstone Air Park, Santo, Texas, US (FAA LID: TX32)
  - VG31    , Nester Funny Farm Airport, Laurel Fork, Virginia, US (FAA LID: VG31)
  - VG44    , Frontier Airport, Dillwyn, Virginia, US (FAA LID: VG44)
  - VG65    , Bigler Airfield, Franktown, Virginia, US (FAA LID: VG65)
  - VG67    , Stuart Red House Field, Appomattox, Virginia, US (FAA LID: VG67)
  - VT72    , Villeneuve Field, Jericho, Vermont, US (FAA LID: VT72)
  - VT76    , Little Goose Farm Airport, Lincoln, Vermont, US (FAA LID: VT76)
  - WI52    , M & F Landing Airport, Greenleaf, Wisconsin, US (FAA LID: WI52)
  - WN19    , Bell-Aire Airport, Toppenish, Washington, US (FAA LID: WN19)
  - WN22    , Bar U View Airport, Washtucna, Washington, US (FAA LID: WN22)
  - WN28    , Hird Airport, Livingston, Wisconsin, US (FAA LID: WN28)
  - WS84    , Cran Bog N Airport, Warrens, Wisconsin, US (FAA LID: WS84)
  - WT03    , Twisted Prop Airport, Prescott, Washington, US (FAA LID: WT03)
  - WT18    , Meise Field, Moses Lake, Washington, US (FAA LID: WT18)
  - WT32    , Hart Airport, Hartline, Washington, US (FAA LID: WT32)
  - WY41    , 5 Springs Airport, Lovell, Wyoming, US (FAA LID: WY41)
  - WY45    , Michael Skypark Airport, Hillsdale, Wyoming, US (FAA LID: WY45)
  - WY56    , Pierce Ranch Airport, Hulett, Wyoming, US (FAA LID: WY56)
  - WY58    , Hilty Private Strip, Wheatland, Wyoming, US (FAA LID: WY58)
  - XA81    , Homerun Airport, Honey Grove, Texas, US (FAA LID: XA81)
  - XS16    , Flying K Ranch Airport, Ledbetter, Texas, US (FAA LID: XS16)

* Updated data for the following 533 airports:

  - 01ID    , Lava Hot Springs Airpark, Lava Hot Springs, Idaho, US: name changed from "Lava Hot Springs Airport",
    elevation changed from 5268.0 to 5300.0
  - 04CA    , Gray Butte Field, Palmdale, California, US: elevation changed from 3028.0 to 3039.0
  - 04IL    , Full Throttle Airport, Hudson, Illinois, US: name changed from "Schertz Aerial Service - Hudson Airport"
  - 04TT    , Brushy Creek Ranch Airport, Utopia, Texas, US: name changed from "4D Ranch Airport", elevation changed
    from 1550.0 to 1550.5
  - 05ME    , Drisko Kelley Airport, Jonesboro, Maine, US: name changed from "Drisko Airport"
  - 07FA/OCA, Ocean Reef Club Airport, Key Largo, Florida, US: elevation changed from 6.0 to 6.4
  - 07TS    , Cross Country Estates Marshall Field, Georgetown, Texas, US: elevation changed from 690.0 to 689.0
  - 07VA    , Alpha Hotel Airport, Clover, Virginia, US: elevation changed from 350.0 to 440.0
  - 0PN0    , Lakeview Airport, Sheakeyville, Pennsylvania, US: name changed from "Fletcher Airport", elevation changed
    from 1335.0 to 1317.0
  - 14NC    , Camp Davis Mcolf Airport, Holly Ridge, North Carolina, US: longitude changed from -77.5 to -77.6
  - 14WS    , Gillette's Lakewood Lodge Airport, Stone Lake, Wisconsin, US: name changed from "Lakewood Lodge Airport"
  - 15WA    , Oomrang Air Airport, Stanwood, Washington, US: name changed from "Sunset Airport", elevation changed from
    156.0 to 121.0
  - 17XA    , Mandyland Airport, Floresville, Texas, US: name changed from "Hunter Field", city changed from
    "Jacksonville", elevation changed from 580.0 to 406.0, latitude changed from 32.0 to 29.0, longitude changed from
    -95.3 to -98.3
  - 19NE    , Hoyt Airport, Mc Cook/Culbertson, Nebraska, US: elevation changed from 2707.0 to 2700.0
  - 19TS    , Silverhorn Ranch Airport, Freer, Texas, US: elevation changed from 691.0 to 691.4
  - 1CO4    , Clifford Field, Olathe, Colorado, US: elevation changed from 5560.0 to 5598.0
  - 1ID4    , Oasis Airpark, Boise, Idaho, US: name changed from "Red Baron Airpark"
  - 1XS0    , Itll Do Airfield, Sandia, Texas, US: elevation changed from 153.0 to 156.0
  - 22IL    , Horseshoe Mound Airport, Galena, Illinois, US: name changed from "Heller Airport"
  - 22XS    , Longhorn Aux Landing Strip, Fort Hood (Killeen), Texas, US: city changed from "Fort Cavazos (Killeen)"
  - 23XS    , Shorthorn Aux Landing Strip, Fort Hood (Killeen), Texas, US: city changed from "Fort Cavazos (Killeen)"
  - 25GA    , Jj's Ranch Airport, Douglasville, Georgia, US: name changed from "Miller Farm Airport"
  - 27NR    , C A G Farms Airport, Angier, North Carolina, US: elevation changed from 310.0 to 319.0
  - 28NK    , Clayton Airfield, Clayton, New York, US: name changed from "Ritchie Airfield"
  - 2AL5    , Flying H Ranch Airport, Fort Payne, Alabama, US: name changed from "Flying J Ranch Airport"
  - 2FA1    , Sawgrass Airport, Ormond Beach, Florida, US: name changed from "Squillacote Airport"
  - 2FA6    , Central Florida Airpark, Coleman, Florida, US: name changed from "Freeflight Airpark"
  - 2IL7    , Ben Emge Airport, Belleville, Illinois, US: elevation changed from 555.0 to 551.0
  - 2KY5    , Womstead Field, Olive Hill, Kentucky, US: elevation changed from 1050.0 to 1062.0
  - 30ID    , 4Z Ranch Airport, Hailey, Idaho, US: elevation changed from 5552.0 to 5556.0
  - 33TA    , Lake Bonanza Airport, Montgomery, Texas, US: elevation changed from 301.0 to 291.0
  - 35NK    , Airborne Acres Airport, Lyndonville, New York, US: name changed from "Tiger Paw Aerodrome"
  - 3AK4    , Johnson Airport, Kenai, Alaska, US: name changed from "Kenai Floatplane Services Airport"
  - 3NC6    , Mc Cachren Field, Harrisburg, North Carolina, US: elevation changed from 565.0 to 581.0
  - 3OH6    , Youngpeter Airport, Delphos, Ohio, US: elevation changed from 815.0 to 806.0
  - 3VA4    , Bill Davenport Memorial Airport, Warsaw, Virginia, US: elevation changed from 10.0 to 7.9
  - 41TT    , Rancho Paraiso Airport, Mountain Home, Texas, US: elevation changed from 2097.0 to 2095.7
  - 42AK    , Bear Tooth Airport, Nuiqsut, Alaska, US: name changed from "Willow Conocophillips Airport", elevation
    changed from 100.8 to 92.5, longitude changed from -152.1 to -152.0
  - 48TE    , 4M Ranch Airfield, Langtry, Texas, US: elevation changed from 1824.0 to 1900.0
  - 48TS    , Kevin Lee Berry Field, Rocksprings, Texas, US: name changed from "Fox Airport", city changed from "New
    Braunfels", elevation changed from 650.0 to 1716.0, latitude changed from 29.7 to 29.9, longitude changed from -98.2
    to -100.0
  - 4WN4    , Geis Field, Fredonia, Wisconsin, US: elevation changed from 851.0 to 852.0
  - 50FL    , Zoltak Landing Airport, Jay, Florida, US: name changed from "Odom's Flying Service Airport"
  - 50PA    , Pegasus Air Park, Stroudsburg, Pennsylvania, US: elevation changed from 620.0 to 630.0, longitude changed
    from -75.3 to -75.4
  - 54CL    , Lake Riverside Estates Airport, Anza, California, US: elevation changed from 3410.0 to 3404.0
  - 57AK    , Fly8Ma Pilot Lodge Airport, Big Lake, Alaska, US: elevation changed from 220.0 to 212.0
  - 5AZ9    , Regeneration Airport, Fort Thomas, Arizona, US: elevation changed from 2750.0 to 2779.0
  - 5CL1    , Robert Oliver Airpark, Santa Margarita, California, US: name changed from "Hart Ranch Airport"
  - 5CL7    , Gene Wash Reservoir Airport, Parker Dam, California, US: elevation changed from 850.0 to 898.0
  - 5CL8    , Northshore Airport, Arvin, California, US: name changed from "Creekside Airport"
  - 5GA3    , Eagles Landing Airport, Williamson, Georgia, US: elevation changed from 980.0 to 932.0
  - 5KY5    , Seven Springs Farms Airport, Cadiz, Kentucky, US: name changed from "Lowe Airport"
  - 63NY    , Windshear Airport, Youngstown, New York, US: name changed from "Windsor Airport"
  - 65AR    , Pleasant Hill Airport, Newark, Arkansas, US: elevation changed from 412.0 to 416.0
  - 67FL    , Bald Eagle Airfield- Myakka Head Airport, Zolfo Springs, Florida, US: name changed from "Myakka Head
    Airport"
  - 69MO    , Brilhart's Farmport Airport, Higbee, Missouri, US: name changed from "Hess-Mckeown Airport"
  - 6TS8    , Rabb And Nobra Airport, Industry, Texas, US: elevation changed from 400.0 to 417.0
  - 79FL    , Good Dog Landing Airport, Chiefland, Florida, US: name changed from "Neal Field"
  - 7AK8    , Crosswinds Landing Airport, Wasilla, Alaska, US: name changed from "Hess Airport"
  - 7GA2    , Alyssas Animal Sanctuary Air Park, Valdosta, Georgia, US: elevation changed from 229.0 to 179.0
  - 7IN9    , The Last Resort Airport, Springport, Indiana, US: elevation changed from 1070.0 to 1075.0
  - 7KY3    , Soggy Bottom Farm Airport, Winchester, Kentucky, US: name changed from "Little Mount International
    Airport", city changed from "Taylorsville", elevation changed from 750.0 to 912.0, latitude changed from 38.1 to
    37.9, longitude changed from -85.2 to -84.3
  - 7XS0    , Polly Ranch Airport, Friendswood, Texas, US: elevation changed from 24.0 to 22.0
  - 80PN    , Hanover Airpark Inc Airport, Hookstown, Pennsylvania, US: name changed from "Hanny Beaver Airpark Inc
    Airport"
  - 81IL    , Illinois Antique Airfield, Minier, Illinois, US: name changed from "Illinois Valley Parachute Club
    Airport"
  - 83TX    , Texas A & M - Rellis Airport, Bryan, Texas, US: name changed from "Texas A & M Flight Test Station
    Airport", elevation changed from 264.0 to 260.0
  - 88PA    , Mc Coy Airport, Clinton, Pennsylvania, US: elevation changed from 1200.0 to 1188.0
  - 8FA4    , New Smyrna Beach Airport, Samsula, Florida, US: name changed from "Coe Field"
  - 8NC4    , Twin Silos Airport, Pittsboro, North Carolina, US: name changed from "Dead Dog Airport"
  - 8PA1    , Dee Jay Airport, Ono, Pennsylvania, US: elevation changed from 505.0 to 514.0
  - 94TS    , Hidden Springs Ranch Airport, Sulphur Springs, Texas, US: elevation changed from 485.0 to 484.0
  - 97MT    , Cabin Creek Landing Airport, Marion, Montana, US: elevation changed from 3999.0 to 3929.1
  - 9KY9    , Paintsville-Prestonsburg-Combs Field, Paintsville, Kentucky, US: elevation changed from 624.0 to 625.0
  - 9NM9    , Spaceport America Airport, Truth Or Consequences, New Mexico, US: elevation changed from 4595.0 to 4622.0
  - AK51    , Big Creek Airport, King Salmon, Alaska, US: elevation changed from 88.0 to 101.6
  - AK59    , King Ranch Airport, Sutton, Alaska, US: elevation changed from 1350.0 to 1310.0
  - AL84    , Velox Airport, Robertsdale, Alabama, US: elevation changed from 125.0 to 132.0, latitude changed from 30.6
    to 30.5
  - AZ57    , Pilots Rest Airport, Paulden, Arizona, US: elevation changed from 4482.0 to 4450.0
  - AZ82    , Mogollon Airpark, Overgaard, Arizona, US: elevation changed from 6657.0 to 6652.0
  - AZ90    , Hangar Haciendas Airport, Laveen, Arizona, US: elevation changed from 1225.0 to 1226.0, latitude changed
    from 33.4 to 33.3
  - CD15    , High Plains Airport Airport, Simla, Colorado, US: name changed from "Schantz Airstrip"
  - CL04    , Skyway Estates Airport, Elk Grove, California, US: name changed from "Sky Way Estates Airport", elevation
    changed from 92.0 to 93.1
  - CL46    , Quail Lake Sky Park Airport, Gorman/Lancaster, California, US: elevation changed from 3370.0 to 3372.0
  - CO12    , Van Aire Airport, Brighton, Colorado, US: elevation changed from 5055.0 to 5061.0
  - DE15    , Reliance Airport, Seaford, Delaware, US: name changed from "Pevey Airport"
  - FL34    , Eglin Aux Field 6 Airport, Valparaiso, Florida, US: name changed from "Eglin Test Site B6 Airport",
    elevation changed from 120.0 to 128.0
  - FL59    , Buckingham Field, Lehigh Acres, Florida, US: city changed from "Fort Myers", elevation changed from 23.0
    to 20.0
  - FL75    , Indian Hammock Airport, Fort Drum, Florida, US: elevation changed from 65.0 to 64.0
  - GA46    , High Point Airport, High Point/Cumberland Island, Georgia, US: city changed from "St Mary'S"
  - HI49    , Kaluakoi Airport, Kaunakakai, Hawaii, US: name changed from "Panda Airport"
  - IN31    , Bitar Field, Pendleton, Indiana, US: name changed from "Hanna Airfield"
  - IN51    , Windy Knoll Airport, Sheridan, Indiana, US: elevation changed from 920.0 to 915.0
  - K06U/KPT, Jackpot/Hayden Field, Jackpot, Nevada, US: elevation changed from 5224.1 to 5223.7
  - K0A9    , William B Greene Jr Regional Airport, Elizabethton, Tennessee, US: name changed from "Elizabethton
    Municipal Airport"
  - K0B4    , Hartington Municipal/Bud Becker Field, Hartington, Nebraska, US: name changed from "Hartington Municipal/
    Bud Becker Field"
  - K0J0    , Abbeville Municipal Airport, Abbeville, Alabama, US: elevation changed from 463.1 to 468.3
  - K0J8    , Flying Ten Airport, Archer, Florida, US: elevation changed from 90.0 to 92.0
  - K0S5    , Nezperce Municipal Airport, Nezperce, Idaho, US: elevation changed from 3201.0 to 3204.0
  - K0W3    , Harford County Airport, Churchville, Maryland, US: elevation changed from 411.5 to 411.6
  - K11V    , Easton/Valley View Airport, Greeley, Colorado, US: name changed from "Easton/Valley View/ Airport"
  - K11Y    , Flying Feathers Airport, Chilton, Wisconsin, US: elevation changed from 917.0 to 913.0
  - K15M    , Segars Field, Iuka, Mississippi, US: name changed from "Iuka Airport"
  - K1A5    , Macon County Airport, Franklin, North Carolina, US: elevation changed from 2034.0 to 2033.9
  - K1F7    , Airpark East Airport, Dallas, Texas, US: elevation changed from 510.0 to 500.0
  - K1H2    , Effingham County Regional Airport, Effingham, Illinois, US: name changed from "Effingham County Memorial
    Airport"
  - K1L4    , Kidwell Airport, Cal Nev Ari, Nevada, US: elevation changed from 2605.0 to 2602.0
  - K1M5    , Douglas Hunter Field, Portland, Tennessee, US: elevation changed from 817.2 to 817.6
  - K1S6    , Priest River Municipal Airport, Priest River, Idaho, US: elevation changed from 2193.0 to 2192.8
  - K22I    , Vinton County Airport, Mc Arthur, Ohio, US: elevation changed from 958.0 to 954.2
  - K24F    , Cypress River Airport, Jefferson, Texas, US: elevation changed from 221.2 to 221.6
  - K25J    , Randolph County Airport, Cuthbert, Georgia, US: name changed from "Lower Chattahoochee Regional Airport"
  - K28J    , Palatka Municipal/Lt Kay Larkin Field, Palatka, Florida, US: name changed from "Palatka Municipal - Lt Kay
    Larkin Field"
  - K2B3/NWH, Parlin Field, Newport, New Hampshire, US: elevation changed from 785.0 to 783.9
  - K2E6    , Groton Municipal Airport, Groton, South Dakota, US: elevation changed from 1306.0 to 1310.0
  - K2K9    , Haskell Airport, Haskell, Oklahoma, US: elevation changed from 588.0 to 587.0
  - K2M2    , Lawrenceburg/Lawrence County (Fleeman Field) Airport, Lawrenceburg, Tennessee, US: name changed from
    "Lawrenceburg-Lawrence County Airport"
  - K2VA    , Zangger Vintage Airpark, Larchwood, Iowa, US: elevation changed from 1477.0 to 1478.0
  - K2W3    , Swanson Field, Eatonville, Washington, US: name changed from "Swanson Airport"
  - K2W6/LTW, St Mary's County Regional Airport, Leonardtown, Maryland, US: elevation changed from 141.8 to 141.6
  - K33R    , Groveton/Trinity County Airport, Groveton, Texas, US: name changed from "Groveton-Trinity County Airport"
  - K35A/USC, Union County, Troy Shelton Field, Union, South Carolina, US: elevation changed from 610.2 to 609.9
  - K37T    , Calico Rock Municipal Airport, Calico Rock, Arkansas, US: name changed from "Calico Rock-Izard County
    Airport"
  - K38U    , Wayne Wonderland Airport, Loa, Utah, US: elevation changed from 7029.0 to 7027.4
  - K39K    , Dragoon Creek Airport, Lyndon, Kansas, US: name changed from "Versaair Services Airport"
  - K3AU    , Augusta Municipal Airport, Augusta, Kansas, US: elevation changed from 1328.0 to 1325.5
  - K3CK    , Lake In The Hills Airport, Chicago/Lake In The Hills, Illinois, US: elevation changed from 887.3 to 887.2
  - K3D2    , Ephraim/Gibraltar Airport, Ephraim, Wisconsin, US: elevation changed from 763.2 to 773.1
  - K3M9    , Warren Municipal/John B Frazer Jr Field, Warren, Arkansas, US: name changed from "Warren Municipal
    Airport"
  - K41U/NTJ, Sanpete County Regional Airport, Manti, Utah, US: name changed from "Manti-Ephraim Airport"
  - K42A    , Melbourne Municipal/John E Miller Field, Melbourne, Arkansas, US: name changed from "Melbourne Municipal -
    John E Miller Field"
  - K42J    , Keystone Heights Airport, Keystone Heights, Florida, US: elevation changed from 196.0 to 195.6
  - K49C    , Camp Lake Airport, Camp Lake, Wisconsin, US: elevation changed from 755.0 to 749.0
  - K4A2/ATT, Atmautluak Airport, Atmautluak, Alaska, US: elevation changed from 19.4 to 18.6
  - K4A6    , Scottsboro Municipal-Word Field, Scottsboro, Alabama, US: elevation changed from 650.3 to 650.5
  - K4J5    , Quitman Brooks County Airport, Quitman, Georgia, US: elevation changed from 184.8 to 184.9
  - K4N4    , Lidgerwood Municipal Airport, Lidgerwood, North Dakota, US: elevation changed from 1081.0 to 1082.0
  - K51M    , Oscoda County/Dennis Kauffman Memorial Airport, Mio, Michigan, US: elevation changed from 1033.0 to 1032.8
  - K51R    , Madisonville Municipal Airport, Madisonville, Texas, US: elevation changed from 286.7 to 286.4
  - K57C    , East Troy Municipal Airport, East Troy, Wisconsin, US: elevation changed from 860.2 to 860.4
  - K5A1    , Norwalk/Huron County Airport, Norwalk, Ohio, US: name changed from "Norwalk-Huron County Airport"
  - K5R4    , Holk Field At Foley Municipal Airport, Foley, Alabama, US: name changed from "Foley Municipal Airport"
  - K5S6    , Cape Blanco State Airport, Sixes, Oregon, US: elevation changed from 214.0 to 202.0
  - K5V5    , Shiprock Airstrip, Shiprock, New Mexico, US: elevation changed from 5272.4 to 5272.6
  - K5W5    , Southern Wake Regional Airport, Raleigh, North Carolina, US: name changed from "Triple W Airport",
    elevation changed from 244.0 to 243.0
  - K61C    , Fort Atkinson Municipal Airport, Fort Atkinson, Wisconsin, US: elevation changed from 799.9 to 800.1
  - K61D    , Virgil L Williams Plainwell Municipal Airport, Plainwell, Michigan, US: name changed from "Plainwell
    Municipal Airport"
  - K63S    , Colville Municipal Airport, Colville, Washington, US: elevation changed from 1888.0 to 1883.0
  - K6G5    , Barnesville/Bradfield Airport, Barnesville, Ohio, US: name changed from "Barnesville-Bradfield Airport",
    elevation changed from 1312.2 to 1312.3
  - K6G8    , Brooklyn Airport, Brooklyn, Michigan, US: elevation changed from 987.0 to 981.0
  - K6I2    , Lebanon Springfield/George Hoerter Field, Springfield, Kentucky, US: name changed from "Lebanon
    Springfield-George Hoerter Field", elevation changed from 871.1 to 871.2
  - K6V4    , Wall Municipal Airport, Wall, South Dakota, US: elevation changed from 2812.7 to 2813.3
  - K6Y9    , Prickett-Grooms Field, Sidnaw, Michigan, US: elevation changed from 1372.0 to 1377.0
  - K73F    , Wings For Christ International Flt Academy Airport, Waco, Texas, US: name changed from "Wings For Christ
    International Flight Academy Airport"
  - K78A    , Swan Creek Airport, Jonesville, North Carolina, US: elevation changed from 1135.0 to 1137.0
  - K79C    , Brennand Airport, Neenah, Wisconsin, US: elevation changed from 850.0 to 844.0
  - K7D8    , Gates Airport, Garrettsville, Ohio, US: elevation changed from 1110.0 to 1104.0
  - K7K7    , Graham Field, North Sioux City, South Dakota, US: elevation changed from 1107.0 to 1109.0
  - K7W6    , Hyde County Airport, Engelhard, North Carolina, US: elevation changed from 6.3 to 6.7
  - K84D    , Cheyenne Eagle Butte Airport, Eagle Butte, South Dakota, US: elevation changed from 2448.7 to 2448.8
  - K8GK    , Gallatin County Airport, Sparta, Kentucky, US: elevation changed from 830.0 to 830.4
  - K8U8    , Broadwater County Airport, Townsend, Montana, US: name changed from "Townsend Airport"
  - K90F    , Broken Bow Municipal Airport, Broken Bow, Oklahoma, US: name changed from "Broken Bow Airport"
  - K94C    , Gilbert Field, Rio, Wisconsin, US: elevation changed from 925.0 to 921.0, latitude changed from 43.4 to
    43.5
  - K94K    , Cassville Municipal Airport, Cassville, Missouri, US: elevation changed from 1482.6 to 1482.7
  - K9A0    , Lumpkin County-Wimpys Airport, Dahlonega, Georgia, US: elevation changed from 1328.8 to 1329.0
  - K9A5    , Barwick Lafayette Airport, Lafayette, Georgia, US: elevation changed from 776.3 to 776.4
  - K9D1    , Gregory Municipal/Flynn Field, Gregory, South Dakota, US: name changed from "Gregory Municipal - Flynn
    Field"
  - K9K7    , Ellsworth Municipal Airport, Ellsworth, Kansas, US: elevation changed from 1632.7 to 1632.9
  - K9R5    , Hunt Airport, Portland, Texas, US: elevation changed from 40.0 to 38.0
  - KAAS    , Taylor County Airport, Campbellsville, Kentucky, US: elevation changed from 920.5 to 921.0
  - KABY/ABY, Southwest Georgia Regional Airport, Albany, Georgia, US: elevation changed from 196.2 to 196.1
  - KACK/ACK, Nantucket Memorial Airport, Nantucket, Massachusetts, US: elevation changed from 46.7 to 46.8
  - KACZ    , Wallace-Pender Airport, Wallace, North Carolina, US: name changed from "Henderson Field"
  - KAFF/AFF, Usaf Academy Davis Airfield, Colorado Springs, Colorado, US: name changed from "Davis Field (Usaf Academy
    Field) Airport"
  - KAFO/AFO, Afton Lincoln County/General Boyd L Eddins Field, Afton, Wyoming, US: name changed from "Afton Municipal
    Airport"
  - KAHH/AHH, Amery Municipal Airport, Amery, Wisconsin, US: elevation changed from 1087.9 to 1088.1
  - KAHQ    , Wahoo Municipal Airport, Wahoo, Nebraska, US: elevation changed from 1223.7 to 1225.6
  - KAID/AID, Anderson Regional Airport, Anderson, Indiana, US: name changed from "Anderson Municipal-Darlington Field"
  - KAIZ/AIZ, Lee C Fine Memorial Airport, Kaiser/Lake Ozark, Missouri, US: elevation changed from 868.9 to 868.8
  - KANB/ANB, Anniston Regional Airport, Anniston, Alabama, US: elevation changed from 612.0 to 612.1
  - KANK/SLT, Salida/Harriett Alexander Field, Salida, Colorado, US: elevation changed from 7522.8 to 7523.0
  - KAPH/APH, Ap Hill Lz (Fort Ap Hill) Airport, Bowling Green, Virginia, US: name changed from "Mary Walker Lz Airport"
  - KATL/ATL, Hartsfield/Jackson Atlanta International Airport, Atlanta, Georgia, US: name changed from "Hartsfield -
    Jackson Atlanta International Airport"
  - KAUH    , Aurora Municipal/Al Potter Field, Aurora, Nebraska, US: name changed from "Aurora Municipal - Al Potter
    Field"
  - KAUN/AUN, Auburn Municipal Airport, Auburn, California, US: elevation changed from 1538.4 to 1538.2
  - KAXA/AXG, Algona Municipal Airport, Algona, Iowa, US: elevation changed from 1216.0 to 1216.1
  - KAXN/AXN, Alexandria Regional/Chandler Field, Alexandria, Minnesota, US: name changed from "Chandler Field"
  - KBAC    , Barnes County Municipal Airport, Valley City, North Dakota, US: elevation changed from 1401.6 to 1401.7
  - KBBP/BTN, Marlboro County Jetport/H E Avent Field, Bennettsville, South Carolina, US: name changed from "Marlboro
    County Jetport - H E Avent Field"
  - KBCB/BCB, Virginia Tech/Montgomery Executive Airport, Blacksburg, Virginia, US: elevation changed from 2119.5 to
    2119.4
  - KBFF/BFF, Scottsbluff/Western Nebraska Regional/Wm  B Heilig Field, Scottsbluff, Nebraska, US: name changed from
    "Western Nebraska Regional/William B Heilig Field"
  - KBJJ/BJJ, Wayne County Airport, Wooster, Ohio, US: elevation changed from 1135.8 to 1135.5
  - KBKE/BKE, Baker City Municipal Airport, Baker City, Oregon, US: elevation changed from 3373.4 to 3373.2
  - KBKT/BKT, Allan C Perkinson/Blackstone Army Air Field, Blackstone, Virginia, US: name changed from "Allen C
    Perkinson Blackstone Army Air Field"
  - KBKV    , Brooksville-Tampa Bay Regional Airport, Brooksville, Florida, US: elevation changed from 76.0 to 76.1
  - KBLF/BLF, Mercer County Airport, Bluefield, West Virginia, US: elevation changed from 2856.7 to 2856.8
  - KBPG/HCA, Big Spring/Mc Mahon-Wrinkle Airport, Big Spring, Texas, US: name changed from "Big Spring Mc Mahon-Wrinkle
    Airport", elevation changed from 2572.9 to 2572.8
  - KBQR    , Buffalo-Lancaster Regional Airport, Buffalo, New York, US: city changed from "Lancaster"
  - KBTL/BTL, Battle Creek Executive At Kellogg Field, Battle Creek, Michigan, US: elevation changed from 951.8 to 951.6
  - KBVN    , Albion Municipal Airport, Albion, Nebraska, US: elevation changed from 1806.2 to 1806.4
  - KBVY/BVY, Beverly Regional Airport, Beverly, Massachusetts, US: elevation changed from 107.3 to 107.2
  - KC09    , Morris Municipal/James R Washburn Field, Morris, Illinois, US: name changed from "Morris Municipal - James
    R Washburn Field"
  - KCAE/CAE, Columbia Metro Airport, Columbia, South Carolina, US: elevation changed from 236.0 to 235.9
  - KCAO/CAO, Clayton Municipal Airpark, Clayton, New Mexico, US: elevation changed from 4969.6 to 4969.8
  - KCDN/CDN, Woodward Field, Camden, South Carolina, US: elevation changed from 302.2 to 302.5
  - KCGC    , Crystal River/Davis Field, Crystal River, Florida, US: name changed from "Crystal River-Capt Tom Davis
    Field"
  - KCKC/GRM, Grand Marais/Cook County Airport, Grand Marais, Minnesota, US: elevation changed from 1803.1 to 1803.0
  - KCKF    , Crisp County-Cordele Airport, Cordele, Georgia, US: elevation changed from 309.5 to 309.6
  - KCKN/CKN, Crookston Municipal/Kirkwood Field, Crookston, Minnesota, US: elevation changed from 900.3 to 896.7
  - KCKP    , Cherokee County Regional Airport, Cherokee, Iowa, US: elevation changed from 1226.4 to 1227.0
  - KCLT/CLT, Charlotte/Douglas International Airport, Charlotte, North Carolina, US: longitude changed from -80.9 to
    -81.0
  - KCLW/CLW, Clearwater Executive Airport, Clearwater, Florida, US: name changed from "Clearwater Air Park"
  - KCMX/CMX, Houghton County Memorial Airport, Hancock, Michigan, US: elevation changed from 1095.2 to 1095.1
  - KCNI    , Cherokee County Regional Airport, Canton, Georgia, US: elevation changed from 1219.1 to 1219.8
  - KCNU/CNU, Chanute Martin Johnson Airport, Chanute, Kansas, US: elevation changed from 1003.1 to 1002.5
  - KCOU/COU, Columbia Regional Airport, Columbia, Missouri, US: elevation changed from 889.3 to 889.4
  - KCPC    , Columbus County Regional Airport, Whiteville, North Carolina, US: name changed from "Columbus County
    Municipal Airport"
  - KCPF    , Wendell H Ford Airport, Hazard, Kentucky, US: elevation changed from 1256.4 to 1256.8
  - KCPU    , Calaveras County/Maury Rasmussen Field, San Andreas, California, US: name changed from "Calaveras County-
    Maury Rasmussen Field"
  - KCRP/CRP, Corpus Christi International Airport, Corpus Christi, Texas, US: elevation changed from 46.1 to 46.2
  - KCTJ    , West Georgia Regional/O V Gray Field, Carrollton, Georgia, US: name changed from "West Georgia Regional -
    O V Gray Field", elevation changed from 1164.5 to 1164.6
  - KCWV    , Claxton-Evans County Airport, Claxton, Georgia, US: elevation changed from 111.6 to 111.5
  - KD07    , Faith Municipal Airport, Faith, South Dakota, US: elevation changed from 2584.2 to 2584.3
  - KD50    , Crosby Municipal Airport, Crosby, North Dakota, US: elevation changed from 1950.1 to 1952.7
  - KD74    , Chorman Airport, Farmington, Delaware, US: elevation changed from 66.0 to 65.0
  - KDCA    , Ronald Reagan Washington Ntl Airport, Washington, District of Columbia, US: iata changed from "DCA", subd
    changed from "Dist. Of Columbia"
  - KDDH    , William H Morse State Airport, Bennington, Vermont, US: elevation changed from 826.8 to 826.6
  - KDED    , Deland Municipal-Sidney H Taylor Field, Deland, Florida, US: elevation changed from 79.1 to 79.2
  - KDET/DET, Coleman A Young Municipal Airport, Detroit, Michigan, US: elevation changed from 625.8 to 624.2
  - KDIJ    , Driggs/Reed Memorial Airport, Driggs, Idaho, US: elevation changed from 6231.0 to 6257.2
  - KDLL    , Baraboo/Wisconsin Dells Regional Airport, Baraboo, Wisconsin, US: elevation changed from 979.3 to 980.2
  - KDNS/DNS, Denison Municipal Airport, Denison, Iowa, US: elevation changed from 1274.0 to 1274.3
  - KDVK    , Stuart Powell Field, Danville, Kentucky, US: elevation changed from 1022.0 to 1021.4
  - KDYL/DYL, Doylestown Airport, Doylestown, Pennsylvania, US: elevation changed from 393.7 to 393.5
  - KDZJ    , Blairsville Airport, Blairsville, Georgia, US: elevation changed from 1907.2 to 1906.9
  - KE14/ESO, Ohkay Owingeh Airport, Espanola, New Mexico, US: elevation changed from 5790.0 to 5760.2
  - KE60    , Eloy Municipal Airport, Eloy, Arizona, US: elevation changed from 1511.2 to 1511.1
  - KEKY    , Bessemer Ntl Airport, Bessemer, Alabama, US: name changed from "Bessemer Airport"
  - KETB/ETB, West Bend Municipal Airport, West Bend, Wisconsin, US: elevation changed from 887.2 to 887.9
  - KEVB    , New Smyrna Beach Municipal (Jack Bolt Field) Airport, New Smyrna Beach, Florida, US: name changed from
    "New Smyrna Beach Municipal Airport"
  - KEVV/EVV, Evansville Regional Airport, Evansville, Indiana, US: elevation changed from 421.9 to 421.7
  - KEVW/EVW, Evanston-Uinta County Burns Field, Evanston, Wyoming, US: elevation changed from 7142.5 to 7142.7
  - KEWR/EWR, Newark Liberty International Airport, Newark, New Jersey, US: elevation changed from 17.4 to 17.5
  - KF17    , Center Municipal Airport, Center, Texas, US: elevation changed from 318.6 to 318.7
  - KF41    , Ennis Municipal Airport, Ennis, Texas, US: elevation changed from 500.1 to 500.3
  - KF82    , Lubbock Executive Airpark, Lubbock, Texas, US: elevation changed from 3200.0 to 3175.7
  - KF87    , Union Parish Airport, Farmerville, Louisiana, US: elevation changed from 121.0 to 118.7
  - KFBG/FBG, Simmons Army Air Field, Fort Bragg, North Carolina, US: city changed from "Fort Liberty", elevation
    changed from 244.1 to 243.3
  - KFFM/FFM, Fergus Falls Regional Airport, Fergus Falls, Minnesota, US: name changed from "Fergus Falls
    Municipal/Einar Mickelson Field", elevation changed from 1182.6 to 1182.4
  - KFFT/FFT, Capital City Airport, Frankfort, Kentucky, US: elevation changed from 812.3 to 812.5
  - KFLD/FLD, Fond Du Lac County Airport, Fond Du Lac, Wisconsin, US: elevation changed from 808.4 to 808.6
  - KFLT/FLT, Flat Airport, Flat, Alaska, US: elevation changed from 309.0 to 343.0
  - KFME/FME, Fort Meade Executive Airport, Fort Meade (Odenton), Maryland, US: name changed from "Tipton Airport",
    elevation changed from 150.0 to 149.5
  - KFMY/FMY, Page Field, Fort Myers, Florida, US: elevation changed from 17.1 to 17.0
  - KFNB    , Brenner Field, Falls City, Nebraska, US: elevation changed from 984.0 to 983.9
  - KFRG/FRG, Republic Airport, Farmingdale, New York, US: elevation changed from 81.0 to 81.6
  - KFWB    , Branson West Municipal/Emerson Field, Branson West, Missouri, US: name changed from "Branson West
    Municipal - Emerson Field"
  - KFXY/FXY, Forest City Municipal/Trimble Field, Forest City, Iowa, US: name changed from "Forest City Municipal
    Airport"
  - KFZG    , Fitzgerald Municipal Airport, Fitzgerald, Georgia, US: elevation changed from 364.8 to 364.7
  - KFZI    , Donald P Miller Airport, Fostoria, Ohio, US: name changed from "Fostoria Metro Airport"
  - KGBG/GBG, Harrel W Timmons Galesburg Regional Airport, Galesburg, Illinois, US: name changed from "Galesburg
    Municipal Airport"
  - KGBR/GBR, Great Barrington Airport, Great Barrington, Massachusetts, US: name changed from "Walter J Koladza
    Airport"
  - KGEU    , Glendale Regional Airport, Glendale, Arizona, US: name changed from "Glendale Municipal Airport"
  - KGFK/GFK, Grand Forks International Airport, Grand Forks, North Dakota, US: elevation changed from 844.6 to 845.1
  - KGKY    , Arlington Municipal Airport, Arlington, Texas, US: elevation changed from 628.2 to 628.3
  - KGLH/GLH, Greenville Mid-Delta Airport, Greenville, Mississippi, US: elevation changed from 130.5 to 130.7
  - KGOO    , Nevada County Airport, Grass Valley, California, US: elevation changed from 3157.6 to 3157.7
  - KGRK/GRK, Robert Gray Army Air Field, Fort Hood (Killeen), Texas, US: city changed from "Fort Cavazos (Killeen)"
  - KGRN/GRN, Gordon Municipal Airport, Gordon, Nebraska, US: elevation changed from 3562.1 to 3562.4
  - KGSH/GSH, Goshen Municipal Airport, Goshen, Indiana, US: elevation changed from 826.6 to 826.4
  - KGUP/GUP, Gallup Municipal Airport, Gallup, New Mexico, US: elevation changed from 6472.3 to 6472.6
  - KGVE/GVE, Gordonsville Municipal Airport, Gordonsville, Virginia, US: elevation changed from 454.0 to 452.0
  - KGWB    , Auburn/Dekalb Executive Airport, Auburn, Indiana, US: name changed from "De Kalb County Airport"
  - KGWR    , Gwinner/Roger Melroe Field, Gwinner, North Dakota, US: name changed from "Gwinner-Roger Melroe Field"
  - KGWS/GWS, Kgws Sumers Airpark, Glenwood Springs, Colorado, US: name changed from "Glenwood Springs Municipal
    Airport"
  - KGXF    , Gila Bend Af Aux Airport, Gila Bend, Arizona, US: elevation changed from 883.0 to 881.0
  - KGYY/GYY, Gary/Chicago International Airport, Gary/Chicago, Indiana, US: city changed from "Gary"
  - KHAD    , Irwins Sky Ranch Airport, Casper, Wyoming, US: name changed from "Harford Field"
  - KHEF    , Manassas Regional/Harry P Davis Field, Washington, District of Columbia, US: iata changed from "MNZ", subd
    changed from "Dist. Of Columbia"
  - KHLC/HLC, Hill City Municipal Airport, Hill City, Kansas, US: elevation changed from 2238.1 to 2238.4
  - KHLR/HLR, Yoakum-Defrenn Army Heliport, Fort Hood (Killeen), Texas, US: city changed from "Fort Cavazos (Killeen)"
  - KHLX    , Twin County Airport, Galax Hillsville, Virginia, US: elevation changed from 2693.6 to 2693.7
  - KHNR    , Harlan Municipal Airport, Harlan, Iowa, US: elevation changed from 1231.0 to 1230.9
  - KHQM/HQM, Bowerman Field, Hoquiam, Washington, US: name changed from "Bowerman Airport"
  - KHQU    , Thomson/Mcduffie County Airport, Thomson, Georgia, US: name changed from "Thomson-Mcduffie County Airport"
  - KHSP/HSP, Ingalls Field, Hot Springs, Virginia, US: elevation changed from 3792.7 to 3792.4
  - KHUM/HUM, Houma-Terrebonne Airport, Houma, Louisiana, US: elevation changed from 9.0 to 8.5
  - KHVC    , Hopkinsville-Christian County Airport, Hopkinsville, Kentucky, US: elevation changed from 563.5 to 563.6
  - KHXD/HHH, Hilton Head Airport, Hilton Head Island, South Carolina, US: elevation changed from 19.4 to 19.3
  - KHYR/HYR, Sawyer County Airport, Hayward, Wisconsin, US: elevation changed from 1216.0 to 1215.9
  - KHZD    , Sgt Lee Russell Carroll County Airport, Huntingdon, Tennessee, US: name changed from "Carroll County
    Airport"
  - KI20/OTN, Ed-Air Airport, Oaktown, Indiana, US: latitude changed from 38.9 to 38.8
  - KI34    , Greensburg Municipal Airport, Greensburg, Indiana, US: elevation changed from 912.0 to 908.9
  - KI69    , Clermont County Airport, Batavia, Ohio, US: elevation changed from 843.1 to 843.5
  - KI80    , Noblesville Airport, Noblesville, Indiana, US: elevation changed from 821.0 to 830.0
  - KI86    , Ed Newlon Field, New Lexington, Ohio, US: name changed from "Perry County Airport"
  - KI96    , Columbia-Adair County Airport, Columbia, Kentucky, US: elevation changed from 818.0 to 819.0
  - KIAD    , Washington Dulles International Airport, Washington, District of Columbia, US: iata changed from "IAD",
    subd changed from "Dist. Of Columbia"
  - KICL/ICL, Schenck Field, Clarinda, Iowa, US: elevation changed from 995.8 to 995.9
  - KIFA/IFA, Iowa Falls Municipal Airport, Iowa Falls, Iowa, US: elevation changed from 1136.8 to 1137.4
  - KIMS/MDN, Madison Regional Airport, Madison, Indiana, US: name changed from "Madison Municipal Airport"
  - KIOB    , Mount Sterling/Montgomery County Airport, Mount Sterling, Kentucky, US: elevation changed from 1019.3 to
    1019.5
  - KIPJ    , Lincoln County Regional Airport, Lincolnton, North Carolina, US: name changed from "Lincolnton-Lincoln
    County Regional Airport"
  - KIWA/AZA, Mesa Gateway Airport, Phoenix, Arizona, US: name changed from "Phoenix-Mesa Gateway Airport"
  - KIZG/FRY, White Mountain Regional Airport, Fryeburg, Maine, US: name changed from "Eastern Slopes Regional Airport"
  - KJAC/JAC, Jackson Hole Airport, Jackson, Wyoming, US: elevation changed from 6450.7 to 6451.3
  - KJDN/JDN, Jordan Airport, Jordan, Montana, US: elevation changed from 2666.3 to 2667.0
  - KJES    , Jesup-Wayne County Airport, Jesup, Georgia, US: elevation changed from 107.1 to 107.5
  - KJFX    , Walker County/Bevill Field, Jasper, Alabama, US: name changed from "Walker County-Bevill Field"
  - KJGG    , Waltrip Williamsburg Executive Airport Airport, Williamsburg, Virginia, US: name changed from
    "Williamsburg-Jamestown Airport"
  - KJHN    , Stanton County Municipal Airport, Johnson City, Kansas, US: city changed from "Johnson"
  - KJVY    , Clark Regional Airport, Jeffersonville, Indiana, US: elevation changed from 477.6 to 477.7
  - KJXI    , Fox Stephens Field/Gilmer Municipal Airport, Gilmer, Texas, US: name changed from "Fox Stephens Field /
    Gilmer Municipal Airport"
  - KK50    , Cook Airfield, Rose Hill, Kansas, US: elevation changed from 1343.9 to 1342.0
  - KK52    , Cpt Ben Smith Airfield/Monroe City Airport, Monroe City, Missouri, US: name changed from "Cpt Ben Smith
    Airfield - Monroe City Airport"
  - KK62    , Gene Snyder Airport, Falmouth, Kentucky, US: elevation changed from 899.4 to 899.7
  - KK78    , Abilene Municipal Airport, Abilene, Kansas, US: elevation changed from 1152.5 to 1152.9
  - KL18    , Fallbrook Community Airpark, Fallbrook, California, US: elevation changed from 708.0 to 710.9
  - KL31    , St Tammany Regional Airport, Covington, Louisiana, US: elevation changed from 39.0 to 37.7
  - KLAA/LAA, Southeast Colorado Regional Airport, Lamar, Colorado, US: elevation changed from 3705.5 to 3705.3
  - KLAF/LAF, Purdue University Airport, Lafayette, Indiana, US: elevation changed from 605.9 to 605.8
  - KLAN/LAN, Capital Region International Airport, Lansing, Michigan, US: elevation changed from 860.8 to 860.5
  - KLAS/LAS, Harry Reid International Airport, Las Vegas, Nevada, US: elevation changed from 2181.2 to 2183.1
  - KLBT/LBT, Lumberton Regional Airport, Lumberton, North Carolina, US: elevation changed from 124.5 to 124.6
  - KLCH/LCH, Lake Charles Regional Airport, Lake Charles, Louisiana, US: elevation changed from 14.6 to 14.5
  - KLEX/LEX, Blue Grass Airport, Lexington, Kentucky, US: elevation changed from 979.3 to 979.5
  - KLFI/LFI, Langley Afb Airport, Hampton, Virginia, US: elevation changed from 8.0 to 8.4
  - KLFT/LFT, Lafayette Regional/Paul Fournet Field, Lafayette, Louisiana, US: elevation changed from 41.7 to 40.9
  - KLGA/LGA, Laguardia Airport, New York, New York, US: elevation changed from 20.6 to 20.7
  - KLNA/LNA, Palm Beach County Park Airport, West Palm Beach, Florida, US: elevation changed from 14.2 to 14.4
  - KLNP/LNP, Lonesome Pine Airport, Wise, Virginia, US: elevation changed from 2684.3 to 2684.8
  - KLOU/LOU, Bowman Field, Louisville, Kentucky, US: elevation changed from 545.6 to 545.5
  - KLRF/LRF, Little Rock Afb Airport, Jacksonville, Arkansas, US: elevation changed from 312.0 to 308.9
  - KLSB/LSB, Lordsburg Municipal Airport, Lordsburg, New Mexico, US: elevation changed from 4289.0 to 4287.9
  - KLSF/LSF, Lawson Army Air Field (Fort Benning) Airport, Fort Benning (Columbus), Georgia, US: name changed from
    "Lawson Army Air Field (Fort Moore) Airport", city changed from "Fort Moore (Columbus)"
  - KLUK/LUK, Cincinnati Municipal/Lunken Field, Cincinnati, Ohio, US: elevation changed from 483.3 to 481.6
  - KLUL/LUL, Hesler/Noble Field, Laurel, Mississippi, US: name changed from "Hesler-Noble Field"
  - KLUM    , Menomonie Municipal/Score Field, Menomonie, Wisconsin, US: elevation changed from 895.1 to 895.0
  - KLWC/LWC, Lawrence Regional Airport, Lawrence, Kansas, US: elevation changed from 833.3 to 833.2
  - KLXT    , Kansas City/Lee's Summit Regional Airport, Lee'S Summit, Missouri, US: name changed from "Lee's Summit
    Municipal Airport"
  - KM04    , Covington Municipal Airport, Covington, Tennessee, US: elevation changed from 280.1 to 280.2
  - KMAO    , Marion County Airport, Marion, South Carolina, US: elevation changed from 92.3 to 92.7
  - KMBG/MBG, Mobridge Municipal Airport, Mobridge, South Dakota, US: elevation changed from 1716.2 to 1716.1
  - KMBT    , Murfreesboro Municipal Airport, Murfreesboro, Tennessee, US: elevation changed from 614.1 to 614.2
  - KMEI/MEI, Key Field, Meridian, Mississippi, US: elevation changed from 298.0 to 297.8
  - KMEM/MEM, Frederick W Smith International Airport, Memphis, Tennessee, US: name changed from "Memphis International
    Airport"
  - KMFR/MFR, Rogue Valley International/Medford Airport, Medford, Oregon, US: name changed from "Rogue Valley
    International - Medford Airport"
  - KMGM/MGM, Montgomery Regional (Dannelly Field) Airport, Montgomery, Alabama, US: elevation changed from 221.1 to
    232.0
  - KMHK/MHK, Manhattan Regional Airport, Manhattan, Kansas, US: elevation changed from 1066.0 to 1066.1
  - KMI1    , Denton Farms Airport, Clare, Michigan, US: elevation changed from 849.0 to 851.0
  - KMKC/MKC, Kansas City Downtown/Wheeler Field, Kansas City, Missouri, US: name changed from "Charles B Wheeler
    Downtown Airport", elevation changed from 756.8 to 756.9
  - KMKG/MKG, Muskegon County Airport, Muskegon, Michigan, US: elevation changed from 628.5 to 628.2
  - KMKL/MKL, Jackson Regional Airport, Jackson, Tennessee, US: name changed from "Mc Kellar-Sipes Regional Airport"
  - KMLS/MLS, Frank Wiley Field, Miles City, Montana, US: elevation changed from 2634.2 to 2634.1
  - KMNM/MNM, Menominee Regional Airport, Menominee, Michigan, US: elevation changed from 624.6 to 624.9
  - KMO3    , Stockton Lake Airport, Stockton, Missouri, US: name changed from "Stockton Municipal Airport"
  - KMOR/MOR, Moore-Murrell Airport, Morristown, Tennessee, US: elevation changed from 1313.1 to 1312.8
  - KMSS/MSS, Massena International-Richards Field, Massena, New York, US: elevation changed from 221.4 to 221.5
  - KMSY/MSY, Louis Armstrong New Orleans International Airport, New Orleans, Louisiana, US: elevation changed from 3.7
    to 3.0
  - KMTH/MTH, The Florida Keys Marathon International Airport, Marathon, Florida, US: elevation changed from 5.2 to 7.3
  - KMTN/MTN, Martin State Airport, Baltimore, Maryland, US: elevation changed from 21.5 to 22.2
  - KMUI/MUI, Muir Army Heliport (Fort Indiantown Gap) Heliport, Fort Indiantown Gap (Annville), Pennsylvania, US: name
    changed from "Muir Army Air Field (Fort Indiantown Gap) Airport"
  - KMUO/MUO, Mountain Home Afb Airport, Mountain Home, Idaho, US: elevation changed from 2996.3 to 2995.9
  - KN41    , Mount Tobe Airport, Waterbury, Connecticut, US: name changed from "Waterbury Airport"
  - KN63    , Meadow Brook Field, Walnut Cove, North Carolina, US: elevation changed from 631.0 to 647.0
  - KN68    , Franklin County Regional Airport, Chambersburg, Pennsylvania, US: elevation changed from 687.9 to 687.8
  - KNID    , China Lake Naws (Armitage Field) Airport, China Lake, California, US: elevation changed from 2284.0 to
    2288.2
  - KNJW    , Joe Williams Nolf Airport, Meridian, Mississippi, US: elevation changed from 538.8 to 538.5
  - KNKX/NKX, Miramar Mcas (Joe Foss Field) Airport, San Diego, California, US: elevation changed from 477.1 to 476.9
  - KNMM    , Meridian Nas (Mc Cain Field) Airport, Meridian, Mississippi, US: elevation changed from 315.8 to 315.7
  - KNQI/NQI, Kingsville Nas Airport, Kingsville, Texas, US: elevation changed from 50.0 to 49.7
  - KO20    , Kingdon Airpark, Lodi, California, US: elevation changed from 15.0 to 18.1
  - KO48    , Salmon Bar Airport, Imnaha, Oregon, US: name changed from "Salmom Bar Airport"
  - KO79    , Sierraville Dearwater Airport, Sierraville, California, US: elevation changed from 4984.0 to 4989.7
  - KO81    , Tulelake Municipal Airport, Tulelake, California, US: elevation changed from 4044.0 to 4048.7
  - KOAK/OAK, Oakland San Francisco Bay Airport, Oakland, California, US: name changed from "Metro Oakland International
    Airport"
  - KOEO/OEO, L O Simenstad Municipal Airport, Osceola, Wisconsin, US: elevation changed from 905.5 to 905.6
  - KOFF/OFF, Offutt Afb Airport, Omaha, Nebraska, US: elevation changed from 1048.6 to 1048.2
  - KOFP    , Hanover County Municipal Airport, Richmond/Ashland, Virginia, US: elevation changed from 206.5 to 206.8
  - KOKC/OKC, Okc Will Rogers International Airport, Oklahoma City, Oklahoma, US: name changed from "Will Rogers World
    Airport", elevation changed from 1295.8 to 1295.5
  - KOKK/OKK, Kokomo Municipal Airport, Kokomo, Indiana, US: elevation changed from 832.3 to 832.2
  - KOLG    , Solon Springs Municipal Airport, Solon Springs, Wisconsin, US: elevation changed from 1102.1 to 1102.0
  - KOMN    , Ormond Beach Municipal Airport, Ormond Beach, Florida, US: elevation changed from 27.9 to 28.1
  - KONA/ONA, Winona Municipal/Max Conrad Field, Winona, Minnesota, US: name changed from "Winona Municipal-Max Conrad
    Field"
  - KORL/ORL, Orlando Executive Airport, Orlando, Florida, US: name changed from "Executive Airport"
  - KOSC/OSC, Oscoda/Wurtsmith Airport, Oscoda, Michigan, US: elevation changed from 633.1 to 633.0
  - KOVE/OVE, Oroville Municipal Airport, Oroville, California, US: elevation changed from 194.3 to 194.2
  - KOVL    , Olivia Regional Airport, Olivia, Minnesota, US: elevation changed from 1076.0 to 1079.9
  - KOVS    , Boscobel Airport, Boscobel, Wisconsin, US: elevation changed from 672.8 to 672.6
  - KOZR/OZR, Cairns Army Air Field (Fort Rucker) Airport, Fort Rucker, Alabama, US: name changed from "Cairns Army Air
    Field (Fort Novosel) Airport", city changed from "Fort Novosel (Ozark)"
  - KOZW    , Livingston County/Spencer J Hardy Airport, Howell, Michigan, US: name changed from "Livingston County
    Spencer J Hardy Airport"
  - KP01    , Eric Marcus Municipal Airport, Ajo, Arizona, US: elevation changed from 1458.0 to 1450.0
  - KPAH/PAH, Barkley Regional Airport, Paducah, Kentucky, US: elevation changed from 410.9 to 410.4
  - KPAM/PAM, Tyndall Afb Airport, Panama City, Florida, US: elevation changed from 17.4 to 17.1
  - KPAN/PJB, Payson Airport, Payson, Arizona, US: elevation changed from 5156.8 to 5160.4
  - KPAO/PAO, Palo Alto Airport, Palo Alto, California, US: elevation changed from 6.8 to 6.7
  - KPBX/PVL, Pike County/Hatcher Field, Pikeville, Kentucky, US: elevation changed from 1470.2 to 1464.5
  - KPCD    , Perryville Regional Airport, Perryville, Missouri, US: elevation changed from 371.7 to 372.6
  - KPDT/PDT, Eastern Oregon Regional At Pendleton Airport, Pendleton, Oregon, US: elevation changed from 1494.2 to
    1494.0
  - KPEO    , Penn Yan/Yates County Airport, Penn Yan, New York, US: name changed from "Penn Yan/Yates City Airport"
  - KPHG    , Phillipsburg Municipal Airport, Phillipsburg, Kansas, US: elevation changed from 1906.8 to 1910.1
  - KPIL    , Cameron County Airport, Port Isabel, Texas, US: name changed from "Port Isabel-Cameron County Airport"
  - KPJC    , Zelienople Municipal Airport, Zelienople, Pennsylvania, US: elevation changed from 897.8 to 907.0
  - KPLU    , Pierce County/Thun Field, Puyallup, Washington, US: name changed from "Pierce County - Thun Field"
  - KPMP/PPM, Pompano Beach Airpark, Pompano Beach, Florida, US: elevation changed from 19.4 to 19.3
  - KPRC/PRC, Prescott Regional/Ernest A Love Field, Prescott, Arizona, US: name changed from "Prescott Regional -
    Ernest A Love Field"
  - KPRZ    , Portales Municipal Airport, Portales, New Mexico, US: elevation changed from 4078.0 to 4077.8
  - KPSC/PSC, Tri-Cities Airport, Pasco, Washington, US: elevation changed from 410.4 to 410.3
  - KPSF/PSF, Pittsfield Municipal Airport, Pittsfield, Massachusetts, US: elevation changed from 1188.4 to 1188.5
  - KPSP/PSP, Palm Springs International Airport, Palm Springs, California, US: elevation changed from 476.4 to 476.6
  - KPYP    , Centre Piedmont/Cherokee County Regional Airport, Centre, Alabama, US: name changed from "Centre-Piedmont-
    Cherokee County Regional Airport"
  - KRAL/RAL, Riverside Airport, Riverside, California, US: name changed from "Riverside Municipal Airport"
  - KRDD/RDD, Redding Regional Airport, Redding, California, US: elevation changed from 504.7 to 505.0
  - KRFI    , Rusk County Airport, Henderson, Texas, US: elevation changed from 442.0 to 441.9
  - KRGA    , Central Kentucky Regional Airport, Richmond, Kentucky, US: elevation changed from 1002.5 to 1002.3
  - KRGK    , Red Wing Regional Airport, Red Wing, Minnesota, US: elevation changed from 777.9 to 778.1
  - KRIW/RIW, Central Wyoming Regional Airport, Riverton, Wyoming, US: elevation changed from 5515.9 to 5516.0
  - KRMG/RMG, Richard B Russell Regional - J H Towers Field, Rome, Georgia, US: elevation changed from 644.1 to 644.0
  - KRMN    , Stafford Regional Airport, Stafford, Virginia, US: elevation changed from 211.2 to 219.1
  - KRVS/RVS, Tulsa Riverside Airport, Tulsa, Oklahoma, US: elevation changed from 637.9 to 638.2
  - KRZL/RNZ, Jasper County Airport, Rensselaer, Indiana, US: elevation changed from 698.2 to 698.3
  - KS36    , Norman Grier Field, Covington, Washington, US: city changed from "Kent"
  - KS39/PRZ, Prineville Airport, Prineville, Oregon, US: elevation changed from 3251.2 to 3251.0
  - KSAD/SAD, Safford Regional/1Lt Duane Spalsbury Field, Safford, Arizona, US: name changed from "Safford Regional
    Airport"
  - KSBM/SBM, Sheboygan County Memorial International Airport, Sheboygan, Wisconsin, US: name changed from "Sheboygan
    County Memorial Airport", elevation changed from 755.2 to 755.3
  - KSCK/SCK, Stockton Metro Airport, Stockton, California, US: elevation changed from 33.2 to 32.6
  - KSCR    , Siler City Municipal Airport, Siler City, North Carolina, US: elevation changed from 615.4 to 615.6
  - KSDY/SDY, Sidney-Richland Regional Airport, Sidney, Montana, US: elevation changed from 1985.3 to 1985.1
  - KSFB/SFB, Orlando Sanford International Airport, Orlando, Florida, US: elevation changed from 54.9 to 54.8
  - KSGJ/UST, St Augustine Airport, St Augustine, Florida, US: name changed from "Northeast Florida Regional Airport"
  - KSPA/SPA, Spartanburg Downtown Memorial/Simpson Field, Spartanburg, South Carolina, US: elevation changed from 801.9
    to 802.0
  - KSPI/SPI, Abraham Lincoln Capital Airport, Springfield, Illinois, US: elevation changed from 597.8 to 597.9
  - KSTP/STP, St Paul Downtown Holman Field, St Paul, Minnesota, US: elevation changed from 705.4 to 705.0
  - KSTS/STS, Charles M Schulz/Sonoma County Airport, Santa Rosa, California, US: name changed from "Charles M Schulz -
    Sonoma County Airport"
  - KSUS/SUS, Spirit Of St Louis Airport, St Louis, Missouri, US: elevation changed from 463.2 to 463.3
  - KSUX/SUX, Sioux Gateway/Brig General Bud Day Field, Sioux City, Iowa, US: elevation changed from 1098.4 to 1098.5
  - KSYR/SYR, Syracuse Hancock International Airport, Syracuse, New York, US: elevation changed from 421.4 to 421.1
  - KT28    , Cain Airport, Slidell, Texas, US: elevation changed from 890.0 to 917.0
  - KT36    , Paul Pittman Memorial Airport, Tylertown, Mississippi, US: elevation changed from 384.0 to 384.2
  - KT54    , Lane Airpark, Rosenberg, Texas, US: elevation changed from 94.0 to 94.1
  - KT69    , Sinton Airport, Sinton, Texas, US: name changed from "Alfred C 'Bubba' Thomas Airport"
  - KT82    , Gillespie County Airport, Fredericksburg, Texas, US: elevation changed from 1694.7 to 1694.9
  - KTAN    , Taunton Municipal/King Field, Taunton, Massachusetts, US: name changed from "Taunton Municipal - King
    Field", elevation changed from 41.5 to 41.3
  - KTEB/TEB, Teterboro Airport, Teterboro, New Jersey, US: elevation changed from 8.4 to 8.3
  - KTFP    , Ingleside Regional Airport, Ingleside, Texas, US: name changed from "Mccampbell-Porter Airport"
  - KTIF    , Thomas County Airport, Thedford, Nebraska, US: elevation changed from 2925.0 to 2925.4
  - KTIX/TIX, Space Coast Regional Airport, Titusville, Florida, US: elevation changed from 33.8 to 34.0
  - KTPA/TPA, Tampa International Airport, Tampa, Florida, US: elevation changed from 26.4 to 26.5
  - KTRI/TRI, Tri-Cities Airport, Bristol/Johnson/Kingsport, Tennessee, US: elevation changed from 1518.7 to 1518.6
  - KTSO    , Carroll County/Tolson Airport, Carrollton, Ohio, US: name changed from "Carroll County-Tolson Airport"
  - KTUL/TUL, Tulsa International Airport, Tulsa, Oklahoma, US: elevation changed from 677.5 to 677.8
  - KTVY    , Bolinder Field/Tooele Valley Airport, Tooele, Utah, US: name changed from "Bolinder Field-Tooele Valley
    Airport"
  - KTYQ    , Indianapolis Executive Airport, Indianapolis, Indiana, US: elevation changed from 922.3 to 922.2
  - KU01    , Savage Field, American Falls, Idaho, US: name changed from "American Falls Airport"
  - KU52    , Beaver Municipal Airport, Beaver, Utah, US: elevation changed from 5863.3 to 5863.2
  - KU86    , Fairfield/Frostenson Airfield, Fairfield, Idaho, US: name changed from "Frostenson Field"
  - KUKF/IKB, Wilkes County Airport, North Wilkesboro, North Carolina, US: elevation changed from 1303.1 to 1303.4
  - KUT9    , West Desert Airpark, Fairfield, Utah, US: elevation changed from 4890.0 to 4886.0
  - KVBT    , Bentonville Municipal/Louise M Thaden Field, Bentonville, Arkansas, US: elevation changed from 1298.1 to
    1297.9
  - KVCB    , Nut Tree Airport, Vacaville, California, US: elevation changed from 116.9 to 116.6
  - KVCT/VCT, Victoria Regional Airport, Victoria, Texas, US: elevation changed from 115.2 to 115.1
  - KVJI/VJI, Virginia Highlands Airport, Abingdon, Virginia, US: elevation changed from 2087.4 to 2087.5
  - KVLD/VLD, Valdosta Regional Airport, Valdosta, Georgia, US: elevation changed from 203.2 to 203.1
  - KVNW    , Van Wert County Airport, Van Wert, Ohio, US: elevation changed from 787.1 to 786.9
  - KVQQ/VQQ, Cecil Airport, Jacksonville, Florida, US: elevation changed from 79.6 to 79.5
  - KVTA    , Licking County Regional Airport, Newark, Ohio, US: name changed from "Newark-Heath Airport"
  - KW11    , Lake Country Airport, Sullivan, Wisconsin, US: name changed from "Sullivan Airport"
  - KW29    , Bay Bridge Airport, Stevensville, Maryland, US: elevation changed from 14.8 to 14.5
  - KW50    , Davis Airport, Laytonsville, Maryland, US: longitude changed from -77.1 to -77.2
  - KWVL/WVL, Waterville Regional Airport, Waterville, Maine, US: name changed from "Waterville Robert Lafleur Airport"
  - KX01    , Everglades Airpark, Everglades City, Florida, US: elevation changed from 5.0 to 4.0
  - KX10    , Belle Glade State Municipal Airport, Belle Glade, Florida, US: elevation changed from 14.0 to 10.6
  - KX21    , Arthur Dunn Air Park, Titusville, Florida, US: elevation changed from 30.0 to 30.3
  - KX60    , Williston Regional Airport, Williston, Florida, US: name changed from "Williston Municipal Airport"
  - KX63/HUC, Dr Hermenegildo Ortiz Quinones Airport, Humacao, Puerto Rico, US: elevation changed from 35.1 to 34.8
  - KY51    , Viroqua Municipal Airport, Viroqua, Wisconsin, US: elevation changed from 1291.7 to 1292.0
  - KY89    , Kalkaska City Airport, Kalkaska, Michigan, US: elevation changed from 1030.0 to 1029.0
  - KY95    , Hillman Airport, Hillman, Michigan, US: elevation changed from 852.0 to 853.0
  - KYNG/YNG, Youngstown/Warren Regional Airport, Youngstown/Warren, Ohio, US: elevation changed from 1191.6 to 1191.5
  - MD48    , Long Green Valley Airstrip, Long Green, Maryland, US: name changed from "Albrecht Airstrip"
  - MI23    , Scott/Saginaw Valley Field, Bridgeport, Michigan, US: name changed from "Mckimmy Field", elevation changed
    from 600.0 to 602.0
  - MS20    , Mach 1 Jet Port Airport, Brandon, Mississippi, US: elevation changed from 377.0 to 415.0, latitude changed
    from 32.5 to 32.4
  - MT86    , Bar E Airport, Helena, Montana, US: elevation changed from 3875.0 to 4090.0
  - MU38    , Milan-Bogard Skyport Airport, Milan, Missouri, US: name changed from "Bogard-Cowgill Airport"
  - ND40    , Rau Field, Medina, North Dakota, US: elevation changed from 1855.0 to 1857.0, longitude changed from -99.3
    to -99.2
  - NH38    , Dolittle Field, Albany, New Hampshire, US: name changed from "Leavitt Airport"
  - NJ24    , Warren Grove Range Airport, Burlington County, New Jersey, US: elevation changed from 105.0 to 135.0
  - NV00    , The Airport Club Airport, Pahrump, Nevada, US: name changed from "Valley View Airport", elevation changed
    from 2740.0 to 2736.6
  - NY76    , Neverland Airport, Cattaraugus, New York, US: elevation changed from 1901.0 to 1959.0
  - NY95    , Creekside Airport, Bloomfield, New York, US: city changed from "Holcomb", elevation changed from 820.0 to
    798.0
  - OG49    , Country Twilight Airport, Corvallis, Oregon, US: name changed from "Coca Cola Airport"
  - OK14    , Walker Family Farm Airport, Mountain Park, Oklahoma, US: name changed from "Woodlake Airport", city
    changed from "Alva", elevation changed from 1420.0 to 1426.0, latitude changed from 36.8 to 34.7, longitude changed
    from -98.7 to -98.9
  - OK24    , Colby Field, Lone Grove, Oklahoma, US: elevation changed from 930.0 to 923.0
  - OK50    , Flysooner Field, Beggs, Oklahoma, US: name changed from "Flying H Ranch Airport"
  - OK93    , Airman Acres Airport, Collinsville, Oklahoma, US: elevation changed from 695.0 to 694.0
  - OL99    , Lookout Airport, Homer, Alaska, US: elevation changed from 1310.0 to 1208.0
  - OR79    , Fallen Rock Airport, Redmond, Oregon, US: name changed from "Flying Alpaca Airport"
  - PA53    , Cosklos Elkview Airport, Carbondale, Pennsylvania, US: elevation changed from 1710.0 to 1737.0
  - PADY/KKH, Kongiganak Airport, Kongiganak, Alaska, US: elevation changed from 32.7 to 39.6
  - PAGN/AGN, Angoon Seaplane Base, Angoon, Alaska, US: lid changed from "" to "AGN"
  - PAHN/HNS, Haines Airport, Haines, Alaska, US: elevation changed from 15.3 to 29.1
  - PGUM/GUM, Guam International Airport, Tamuning, , GU: city changed from "Guam"
  - PHJR/JRF, Kalaeloa (John Rodgers Field) Airport, Kapolei, Hawaii, US: elevation changed from 30.0 to 32.3
  - PHKO/KOA, Ellison Onizuka Kona International At Keahole Airport, Kailua-Kona, Hawaii, US: city changed from
    "Kailua/Kona", elevation changed from 48.6 to 50.5
  - PHNL/HNL, Daniel K Inouye International Airport, Honolulu, Hawaii, US: elevation changed from 12.6 to 13.5
  - PKMJ/MAJ, Amata Kabua International Airport, Majuro Atoll, , MH: elevation changed from 6.6 to 6.5
  - SC99    , Whiteplains Airport, Lexington, South Carolina, US: elevation changed from 525.0 to 524.0
  - SN47    , Converse Farm Airport, Eskridge, Kansas, US: elevation changed from 1231.0 to 1229.0, latitude changed
    from 38.8 to 38.7
  - TA24    , Smoky Bend Ranch Airport, Mullin, Texas, US: elevation changed from 1326.0 to 1342.4
  - TA66    , Freedom Springs Ranch Airport, Pipe Creek, Texas, US: elevation changed from 1384.0 to 1379.0
  - TA85    , Chips Airport, Seguin, Texas, US: elevation changed from 573.0 to 576.0
  - TE38    , Loghouse /Stol Airport, Goodrich, Texas, US: name changed from "Loghouse /Stol/ Airport", elevation
    changed from 184.0 to 179.0
  - TISX/STX, Henry E Rohlsen Airport, Christiansted, Virgin Islands, US: elevation changed from 74.1 to 73.2
  - TJAB/ARE, Antonio/Nery/Juarbe Pol Airport, Arecibo, Puerto Rico, US: elevation changed from 20.8 to 20.5
  - TJBQ/BQN, Rafael Hernandez Airport, Aguadilla, Puerto Rico, US: elevation changed from 237.2 to 237.7
  - TJCP/CPX, Benjamin Rivera Noriega Airport, Isla De Culebra, Puerto Rico, US: elevation changed from 49.0 to 42.9
  - TJIG/SIG, Fernando Luis Ribas Dominicci Airport, San Juan, Puerto Rico, US: elevation changed from 9.8 to 9.6
  - TJMZ/MAZ, Eugenio Maria De Hostos Airport, Mayaguez, Puerto Rico, US: elevation changed from 27.7 to 28.7
  - TJPS/PSE, Mercedita Airport, Ponce, Puerto Rico, US: elevation changed from 28.4 to 36.7
  - TJRV/NRR, Jose Aponte De La Torre Airport, Ceiba, Puerto Rico, US: elevation changed from 38.1 to 38.5
  - TN49    , Bellwood Field, Lebanon, Tennessee, US: elevation changed from 589.0 to 590.0
  - TN87    , Montvale Airpark, Maryville, Tennessee, US: elevation changed from 1030.0 to 1037.0
  - VA42    , Dogwood Airpark, Fredericksburg, Virginia, US: elevation changed from 180.0 to 183.9
  - VG25    , Robinson Airport, Bedford, Virginia, US: elevation changed from 850.0 to 947.0
  - VG37    , Greenway Airfield, Whaleyville, Virginia, US: name changed from "Umphlett Airstrip"
  - WA07    , Cross Winds Airport, Clayton, Washington, US: name changed from "Barker Airport", city changed from "Mount
    Vernon", elevation changed from 5.0 to 2150.0, latitude changed from 48.4 to 48.0, longitude changed from -122.3 to
    -117.5
  - WA45    , Olympic Field, Discovery Bay/Maynard, Washington, US: elevation changed from 500.0 to 460.0
  - WA87    , Parkside Airpark, Battle Ground, Washington, US: elevation changed from 275.0 to 271.0
  - WA93    , Eliza Island Airport, Bellingham, Washington, US: elevation changed from 8.0 to 11.0
  - WA97    , Talus Ranch Airport, Odessa, Washington, US: name changed from "Buena Airport", city changed from "Buena",
    elevation changed from 830.0 to 1690.0, latitude changed from 46.4 to 47.4, longitude changed from -120.3 to -118.8
  - WI69    , Air Troy Estates Airport, East Troy, Wisconsin, US: name changed from "Air Troy Estates - Restricted
    Airport"
  - WN98    , Northern Trails Aviation Airport, Birchwood, Wisconsin, US: name changed from "Florida North Airport"
  - WT44    , Michair Airport, Cathlamet, Washington, US: elevation changed from 13.0 to 7.3
  - WV12    , Mallory Airport, South Charleston, West Virginia, US: elevation changed from 880.0 to 885.0

* Removed the following 292 airports:

  - 00MD    , Slater Field, Federalsburg, Maryland, US is no longer listed in the FAA A/FD (old FAA LID: 00MD)
  - 01IS    , William E Koenig Airport, Dow, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 01IS)
  - 02VA    , The Greenhouse Airport, Culpeper, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 02VA)
  - 07CO    , Comanche Creek Airport, Kiowa, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: 07CO)
  - 08NC    , Whiteheart Farm Airport, Lewisville, North Carolina, US is no longer listed in the FAA A/FD (old FAA LID:
    08NC)
  - 09MO    , Hogue Farm Airport, Willard, Missouri, US is no longer listed in the FAA A/FD (old FAA LID: 09MO)
  - 0MU1    , Sunderland Airport, Avilla, Missouri, US is no longer listed in the FAA A/FD (old FAA LID: 0MU1)
  - 0PA6    , Hostetler Airport, Huntingdon, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 0PA6)
  - 0PN4    , Kitner Airport, New Bloomfield, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 0PN4)
  - 0SD7    , Porch Ranch Airport, Wanblee, South Dakota, US is no longer listed in the FAA A/FD (old FAA LID: 0SD7)
  - 0TS4    , Ullrich Airport, Ledbetter, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 0TS4)
  - 0VA9    , Handy Strip, Gloucester Court House, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 0VA9)
  - 0WI8    , Oconomowoc Airport, Oconomowoc, Wisconsin, US: Closed Indefinitely (old FAA LID: 0WI8)
  - 0WI9    , Mc Manus Hoonch-Na-Shee-Kaw Airport, Oregon, Wisconsin, US is no longer listed in the FAA A/FD (old FAA
    LID: 0WI9)
  - 12CO    , Omega 1 Airport, Hotchkiss, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: 12CO)
  - 12IL    , Hawker Airport, Kankakee, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 12IL)
  - 12XA    , Wood Farm Airfield, Gardendale, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 12XA)
  - 12XS    , Mc Croskey Field, Butlerville, Arkansas, US is no longer listed in the FAA A/FD (old FAA LID: 12XS)
  - 14NK    , Mountain View Airport, Kingsbury, New York, US is no longer listed in the FAA A/FD (old FAA LID: 14NK)
  - 16IS    , Kellums Airport, Goreville, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 16IS)
  - 17KY    , Lester Airfield, Sacramento, Kentucky, US is no longer listed in the FAA A/FD (old FAA LID: 17KY)
  - 17PS    , Mountain Crest Airport, Tidioute, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 17PS)
  - 1IL1    , Horsefeathers Ranch Airport, Irving, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 1IL1)
  - 1IS4    , Swan Valley Farm Airport, Lanark, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 1IS4)
  - 1PN1    , Napodano Airport, Transfer, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 1PN1)
  - 1SC3    , Stol-It Farm Airport, Fair Play, South Carolina, US is no longer listed in the FAA A/FD (old FAA LID:
    1SC3)
  - 1TT8    , Bulverde Airpark, San Antonio, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 1TT8)
  - 1WI8    , Jorgensen - Stoller Airport, Algoma, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID: 1WI8)
  - 1WI9    , Blackhawk Island Airport, Fort Atkinson, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID:
    1WI9)
  - 1XA6    , Tailwheel Acres Airport, Valley View, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 1XA6)
  - 20NC    , Mountain View Airport, Sherrills Ford, North Carolina, US is no longer listed in the FAA A/FD (old FAA
    LID: 20NC)
  - 20WA    , Skyraider Skyranch Airport, Yelm, Washington, US is no longer listed in the FAA A/FD (old FAA LID: 20WA)
  - 21FA    , Rockledge Airport, Rockledge, Florida, US is no longer listed in the FAA A/FD (old FAA LID: 21FA)
  - 21GE    , Deer Crossing Airport, Cleveland, Georgia, US is no longer listed in the FAA A/FD (old FAA LID: 21GE)
  - 23IS    , Clark Airport, Plymouth, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 23IS)
  - 23VG    , Murdock's Holly Bu Airport, Boydton, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 23VG)
  - 24AK    , Toad Lake Strip, Meadow Lakes, Alaska, US is no longer listed in the FAA A/FD (old FAA LID: 24AK)
  - 26AL    , Richardson Field, Mobile, Alabama, US is no longer listed in the FAA A/FD (old FAA LID: 26AL)
  - 29AZ    , Paloma Ranch Airport, Paloma, Arizona, US is not an AIRPORT or SEAPLANE BASE per FAA A/FD: ABRAZO BUCKEYE
    HOSPITAL, HELIPORT (old FAA LID: 29AZ)
  - 29NH    , Cleary Airport, Auburn, New Hampshire, US is no longer listed in the FAA A/FD (old FAA LID: 29NH)
  - 29WI    , Whittlesey Cranberry Company Airport, Babcock, Wisconsin, US is no longer listed in the FAA A/FD (old FAA
    LID: 29WI)
  - 2AR2    , Davidson Field, Sage, Arkansas, US is no longer listed in the FAA A/FD (old FAA LID: 2AR2)
  - 2AR5    , Ashmore Field, Centerton, Arkansas, US is no longer listed in the FAA A/FD (old FAA LID: 2AR5)
  - 2CO1    , Cherokee Trail Ranch Airport, Peyton, Colorado, US is not an AIRPORT or SEAPLANE BASE per FAA A/FD:
    UCHEALTH LONGS PEAK, HELIPORT (old FAA LID: 2CO1)
  - 2FL8    , Tiger Lake Airport, River Ranch, Florida, US is no longer listed in the FAA A/FD (old FAA LID: 2FL8)
  - 2IS4    , Ritter Field, Illinois City, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 2IS4)
  - 2KS5    , Plains Municipal Airport, Plains, Kansas, US is no longer listed in the FAA A/FD (old FAA LID: 2KS5)
  - 2KY3    , Plane-O-Field Airport, Bowling Green, Kentucky, US is no longer listed in the FAA A/FD (old FAA LID: 2KY3)
  - 2LL1    , Cwian Field, Sheridan, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 2LL1)
  - 2LL9    , George Airport, Somonauk, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 2LL9)
  - 2MD0    , Anderson Farm Airport, Marion, Maryland, US is no longer listed in the FAA A/FD (old FAA LID: 2MD0)
  - 2MI0    , Cherry Field, Nunica, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 2MI0)
  - 2MN1    , Winter Strip, Gluek, Minnesota, US is no longer listed in the FAA A/FD (old FAA LID: 2MN1)
  - 2MY4    , Miller Airport, Clear Lake, Minnesota, US is no longer listed in the FAA A/FD (old FAA LID: 2MY4)
  - 2PA7    , Egolf Airport, Landisburg, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 2PA7)
  - 2TX3    , La Fonda Ranch Airport, Brackettville, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 2TX3)
  - 2VA8    , Brandywyne Farms Airport, Holland, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 2VA8)
  - 31KS    , Mills Field, South Hutchinson, Kansas, US is no longer listed in the FAA A/FD (old FAA LID: 31KS)
  - 31TS    , Flyers Field, Greenville, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 31TS)
  - 32PA    , Perkiomen Valley Airport, Collegeville, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID:
    32PA)
  - 32VA    , Old South Aerodrome, Abingdon, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 32VA)
  - 33OI    , Soaring Horse Airport, Chatham Township, Ohio, US is no longer listed in the FAA A/FD (old FAA LID: 33OI)
  - 35WI    , Barker Strip, East Troy, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID: 35WI)
  - 36CO    , Fat Chance Airport, Peyton, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: 36CO)
  - 37PA    , Roadcap Airport, Middleburg, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 37PA)
  - 38FA    , Blue Springs Airport, Madison, Florida, US is not an AIRPORT or SEAPLANE BASE per FAA A/FD: DYER CHEVROLET
    LAKE WALES, HELIPORT (old FAA LID: 38FA)
  - 38KS    , Hiebert  Airfield, Goessel, Kansas, US is not an AIRPORT or SEAPLANE BASE per FAA A/FD: FLYING M RANCH,
    ULTRALIGHT (old FAA LID: 38KS)
  - 3CO0    , Sky Island Ranch Airport, Delta, Colorado, US: Closed Indefinitely (old FAA LID: 3CO0)
  - 3FL8    , Hart Airport, Malone, Florida, US is no longer listed in the FAA A/FD (old FAA LID: 3FL8)
  - 3IL2    , Sweedler Airport, Elwood, Illinois, US is not an AIRPORT or SEAPLANE BASE per FAA A/FD: IDOC-MENARD,
    HELIPORT (old FAA LID: 3IL2)
  - 3IN8    , Ddt Field, Culver, Indiana, US is no longer listed in the FAA A/FD (old FAA LID: 3IN8)
  - 3IS7    , Foote Airport, Wenona, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 3IS7)
  - 3KY1    , Goode Airpark, Utica, Kentucky, US is no longer listed in the FAA A/FD (old FAA LID: 3KY1)
  - 3LL3    , Kibler Airport, Marshall, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 3LL3)
  - 3MN9    , Schumacher Airport, Oster, Minnesota, US is no longer listed in the FAA A/FD (old FAA LID: 3MN9)
  - 3NY6    , Six Ponds Airport, Duanesburg, New York, US is no longer listed in the FAA A/FD (old FAA LID: 3NY6)
  - 3TE6    , Skellytown Airport, Skellytown, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 3TE6)
  - 3TX2    , Flying S Farm Airport, Justin, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 3TX2)
  - 3VA1    , The Meadows Airport, Warrenton, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 3VA1)
  - 3VG4    , Murdocks Flying V Airport, Boydton, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 3VG4)
  - 43OK    , Biggs Skypatch Airport, Wellston, Oklahoma, US is no longer listed in the FAA A/FD (old FAA LID: 43OK)
  - 46CO    , Huerfano Ag Airport, Pueblo, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: 46CO)
  - 46MI    , Rotors & Wings Airport, Webberville, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 46MI)
  - 47TA    , Pleasure Field, Prosper, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 47TA)
  - 48CO    , Shaull Farm Airstrip, Nunn, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: 48CO)
  - 48MD    , Le Champ Airport, Princess Anne, Maryland, US is no longer listed in the FAA A/FD (old FAA LID: 48MD)
  - 4CO8    , Kelgun Airport, Castle Rock, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: 4CO8)
  - 4IA7    , Witcombe Field, Cedar Falls, Iowa, US is no longer listed in the FAA A/FD (old FAA LID: 4IA7)
  - 4IS1    , Plain Crazy Airport, Carthage, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 4IS1)
  - 4KS7    , Butler Airpark, Rose Hill, Kansas, US is no longer listed in the FAA A/FD (old FAA LID: 4KS7)
  - 4LL9    , Alan B Janssen Airport, Morrisonville, Illinois, US is no longer listed in the FAA A/FD (old FAA LID:
    4LL9)
  - 4MN5    , Kapaun-Wilson Field, Graceville, Minnesota, US is no longer listed in the FAA A/FD (old FAA LID: 4MN5)
  - 4PS5    , Muddy Creek Airport, Carmicheal, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 4PS5)
  - 4TA8    , Perry Ranch Airport, Ozona, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 4TA8)
  - 4VA3    , Flying W Airport, Richmond, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 4VA3)
  - 50AZ    , Rocky Ridge Airport, Rocky Ridge, Arizona, US is no longer listed in the FAA A/FD (old FAA LID: 50AZ)
  - 51OH    , Agner Airport, Ottawa, Ohio, US is no longer listed in the FAA A/FD (old FAA LID: 51OH)
  - 52AR    , Ira's Airstrip, Greenbrier, Arkansas, US is no longer listed in the FAA A/FD (old FAA LID: 52AR)
  - 54AL    , Belforest Field, Daphne, Alabama, US is no longer listed in the FAA A/FD (old FAA LID: 54AL)
  - 55FD    , Dotson Airport, Baker, Florida, US: Closed Indefinitely (old FAA LID: 55FD)
  - 56OG    , Horn Airport, Stayton, Oregon, US is no longer listed in the FAA A/FD (old FAA LID: 56OG)
  - 57KY    , Belcher Regional Airport, Belcher, Kentucky, US is no longer listed in the FAA A/FD (old FAA LID: 57KY)
  - 58IL    , Spangler Airport, Manteno, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 58IL)
  - 5KS1    , Threshing Bee Airport, Mc Louth, Kansas, US is no longer listed in the FAA A/FD (old FAA LID: 5KS1)
  - 5ND3    , Craig Private Airport, Bathgate, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: 5ND3)
  - 5OK3    , Stearmans Roost Airport, Vinita, Oklahoma, US is no longer listed in the FAA A/FD (old FAA LID: 5OK3)
  - 5TE6    , Keystone Ranch Airport, San Angelo, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 5TE6)
  - 5TE8    , Willis N Clark Airport, Miami, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 5TE8)
  - 5TN5    , Thomas Field, Jonesborough, Tennessee, US is no longer listed in the FAA A/FD (old FAA LID: 5TN5)
  - 5VG2    , Foster Field, Mathews, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 5VG2)
  - 5WA9    , Brush Prairie Aerodrome, Brush Prairie, Washington, US is no longer listed in the FAA A/FD (old FAA LID:
    5WA9)
  - 5XS3    , Wilber Farms Airport, Winnie, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 5XS3)
  - 65KS    , Griffith Field, Downs, Kansas, US is no longer listed in the FAA A/FD (old FAA LID: 65KS)
  - 68KY    , Lee's Airpark, Somerset, Kentucky, US is no longer listed in the FAA A/FD (old FAA LID: 68KY)
  - 68LA    , Pilkinton Airstrip, Bossier City, Louisiana, US is no longer listed in the FAA A/FD (old FAA LID: 68LA)
  - 68TS    , Bishop Field, Royse City, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 68TS)
  - 6FD7    , Thomson Airfield, Ellenton, Florida, US is no longer listed in the FAA A/FD (old FAA LID: 6FD7)
  - 6IL0    , Hoerr Rla Airport, Peoria, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 6IL0)
  - 6LA2    , Capozzoli Airport, Prairieville, Louisiana, US is no longer listed in the FAA A/FD (old FAA LID: 6LA2)
  - 6LL0    , Williamson Airport, Neoga, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 6LL0)
  - 6LL2    , Young Airport, Viola, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 6LL2)
  - 6MN8    , Underland Airstrip, Medford, Minnesota, US is no longer listed in the FAA A/FD (old FAA LID: 6MN8)
  - 6NJ9    , Bridgeport-Cahill Field, Bridgeport, New Jersey, US is no longer listed in the FAA A/FD (old FAA LID:
    6NJ9)
  - 6OK0    , White Airport, Kingfisher, Oklahoma, US is no longer listed in the FAA A/FD (old FAA LID: 6OK0)
  - 6PA6    , Air Haven Airport, Moscow, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 6PA6)
  - 70IL    , Murphy Farms Airport, Farmersville, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 70IL)
  - 70VA    , Burnt Chimney Airport, Burnt Chimney, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: 70VA)
  - 74CA    , Flying Gluepie Ranch Airport, Fiddletown, California, US: Closed Indefinitely (old FAA LID: 74CA)
  - 74NC    , Benton Farm Airport, Whartonville, North Carolina, US is no longer listed in the FAA A/FD (old FAA LID:
    74NC)
  - 75OA    , Darby Dan Airport, Columbus, Ohio, US is no longer listed in the FAA A/FD (old FAA LID: 75OA)
  - 76WN    , Hacklander Airport, Janesville, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID: 76WN)
  - 77MO    , Springhill Airport, Mount Vernon, Missouri, US: Closed Indefinitely (old FAA LID: 77MO)
  - 78KY    , Mountain View Airfield, Winchester, Kentucky, US is no longer listed in the FAA A/FD (old FAA LID: 78KY)
  - 78NE    , Stava Airport, Brainard, Nebraska, US is no longer listed in the FAA A/FD (old FAA LID: 78NE)
  - 7FD1    , Lykes Fort Basinger Airport, Lorida, Florida, US is no longer listed in the FAA A/FD (old FAA LID: 7FD1)
  - 7GE5    , Sunset Strip, Centralhatchee, Georgia, US is no longer listed in the FAA A/FD (old FAA LID: 7GE5)
  - 7II3    , Schroeder Private Airport, Mount Vernon, Indiana, US is no longer listed in the FAA A/FD (old FAA LID:
    7II3)
  - 7IL8    , Cody Port Airport, Harding, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 7IL8)
  - 7NA2    , Undlin Airstrip, Lansford, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: 7NA2)
  - 7ND5    , Buchmiller Airport, Bowdon, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: 7ND5)
  - 7TS3    , Sunny V Ranch Airport, Sisterdale, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 7TS3)
  - 80ME    , Bayley's Field, Scarborough, Maine, US is no longer listed in the FAA A/FD (old FAA LID: 80ME)
  - 82NY    , Silvernails Field, Gallatin, New York, US is no longer listed in the FAA A/FD (old FAA LID: 82NY)
  - 84ND    , Kyllo Airport, Mc Canna, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: 84ND)
  - 84PN    , Draco Airport, Stewartstown, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: 84PN)
  - 85MN    , Christison Airport, Plainview, Minnesota, US is no longer listed in the FAA A/FD (old FAA LID: 85MN)
  - 87CO    , Young's Strip, Bennett, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: 87CO)
  - 89IL    , Dean Schwenk Airport, Pesotum, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 89IL)
  - 89TS    , Carter Ranch Airport, Oakwood, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 89TS)
  - 8CL2    , Lucchetti Ranch Airport, Elk Grove, California, US is no longer listed in the FAA A/FD (old FAA LID: 8CL2)
  - 8CO0    , Kent Airport, Wiggins, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: 8CO0)
  - 8CO2    , William Leon Schawo Airport, Briggsdale, Colorado, US is no longer listed in the FAA A/FD (old FAA LID:
    8CO2)
  - 8NA5    , Liechty Farm Airport, Montpelier, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: 8NA5)
  - 94GA    , Snow Hill Airstrip, Unadilla, Georgia, US is no longer listed in the FAA A/FD (old FAA LID: 94GA)
  - 94NH    , Tucker Farm Airport, Andover, New Hampshire, US is no longer listed in the FAA A/FD (old FAA LID: 94NH)
  - 96FD    , Citrus Hedging Ranch Airport, Okeechobee, Florida, US is no longer listed in the FAA A/FD (old FAA LID:
    96FD)
  - 99AZ    , Eagletail Ranch Airport, Tonopah, Arizona, US is no longer listed in the FAA A/FD (old FAA LID: 99AZ)
  - 99KS    , Elm Creek Farms Airport, Medicine Lodge, Kansas, US is no longer listed in the FAA A/FD (old FAA LID:
    99KS)
  - 9FA5    , Marshall Swamp Airport, Ocala, Florida, US is no longer listed in the FAA A/FD (old FAA LID: 9FA5)
  - 9FD7    , Fort Atkinson Plantation Airpark, Day, Florida, US: Closed Indefinitely (old FAA LID: 9FD7)
  - 9IS9    , Johnston Airport, Heyworth, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: 9IS9)
  - 9KS1    , Hartland Airport, Wellsville, Kansas, US is no longer listed in the FAA A/FD (old FAA LID: 9KS1)
  - 9OK7    , Prairie Ridge Airport, Stratford, Oklahoma, US is no longer listed in the FAA A/FD (old FAA LID: 9OK7)
  - AR55    , R V Stewart Field, North Little Rock, Arkansas, US is no longer listed in the FAA A/FD (old FAA LID: AR55)
  - CA13    , Reedley College Airport, Reedley, California, US is no longer listed in the FAA A/FD (old FAA LID: CA13)
  - CA19    , Camanche Skypark Airport, Ione, California, US is no longer listed in the FAA A/FD (old FAA LID: CA19)
  - CA38    , Totem Pole Ranch Airport, Calpine, California, US is no longer listed in the FAA A/FD (old FAA LID: CA38)
  - CA40    , Central Valley Aviation Inc Airport, Selma, California, US is no longer listed in the FAA A/FD (old FAA
    LID: CA40)
  - CD02    , Skyote Airport, Steamboat Springs, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: CD02)
  - CO54    , G W Flanders Ranch Strip, Falcon, Colorado, US is no longer listed in the FAA A/FD (old FAA LID: CO54)
  - CO58    , Wings N Things Airpark & Museum Airport, Firestone, Colorado, US is no longer listed in the FAA A/FD (old
    FAA LID: CO58)
  - CT36    , Gager Field, Bozrah, Connecticut, US is no longer listed in the FAA A/FD (old FAA LID: CT36)
  - CT66    , Cambrown Airport, Washington, Connecticut, US is no longer listed in the FAA A/FD (old FAA LID: CT66)
  - FD84    , Delta Airport, Lake City, Florida, US is no longer listed in the FAA A/FD (old FAA LID: FD84)
  - FL57    , Carter Airport, Apopka, Florida, US is no longer listed in the FAA A/FD (old FAA LID: FL57)
  - FL61    , Mc Ginley Airport, Ocala, Florida, US is no longer listed in the FAA A/FD (old FAA LID: FL61)
  - GA48    , Mclendon Airport, Edison, Georgia, US is no longer listed in the FAA A/FD (old FAA LID: GA48)
  - GA82    , Rust Airstrip, Woolsey, Georgia, US is no longer listed in the FAA A/FD (old FAA LID: GA82)
  - IA54    , Anderson Airport, Dubuque, Iowa, US is no longer listed in the FAA A/FD (old FAA LID: IA54)
  - IA56    , Farrar Airport, Farrar, Iowa, US is no longer listed in the FAA A/FD (old FAA LID: IA56)
  - ID41    , Stibnite Airport, Yellow Pine, Idaho, US is no longer listed in the FAA A/FD (old FAA LID: ID41)
  - IN11    , Arrowhead Farm Airport, Bourbon, Indiana, US is no longer listed in the FAA A/FD (old FAA LID: IN11)
  - IN18    , Hook Field, Harlan, Indiana, US is no longer listed in the FAA A/FD (old FAA LID: IN18)
  - IN80    , Roberson Airport, English, Indiana, US is no longer listed in the FAA A/FD (old FAA LID: IN80)
  - IN90    , Wietbrock Airport, Lowell, Indiana, US is no longer listed in the FAA A/FD (old FAA LID: IN90)
  - IS02    , Dietchweiler Airport, Watseka, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: IS02)
  - IS24    , Harris Airport, Ramsey, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: IS24)
  - IS80    , Uncle Chuck's Airport, De Kalb, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: IS80)
  - K01T    , Rocking L Airport, Sonora, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 01T)
  - K0N6    , Albanna Aviation Airport, Felton, Delaware, US is no longer listed in the FAA A/FD (old FAA LID: 0N6)
  - K15W    , Dennis Farms Airport, Laingsburg, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 15W)
  - K1M3    , Ardmore Airport, Ardmore, Alabama, US is no longer listed in the FAA A/FD (old FAA LID: 1M3)
  - K2N4    , Owasco Airfield, Moravia, New York, US is no longer listed in the FAA A/FD (old FAA LID: 2N4)
  - K3B4    , Seacoast Airfield, Eliot, Maine, US: Closed Indefinitely (old FAA LID: 3B4)
  - K3B5    , Twitchell Airport, Turner, Maine, US is no longer listed in the FAA A/FD (old FAA LID: 3B5)
  - K3D8    , Bordner Airport, Bowling Green, Ohio, US is no longer listed in the FAA A/FD (old FAA LID: 3D8)
  - K3V0    , Custer State Park Airport, Fairburn, South Dakota, US is no longer listed in the FAA A/FD (old FAA LID:
    3V0)
  - K42V    , Jones Airport, Benkelman, Nebraska, US is no longer listed in the FAA A/FD (old FAA LID: 42V)
  - K48G    , Gavagan Field, Yale, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 48G)
  - K48Y    , Piney Pinecreek Border Airport, Pinecreek, Minnesota, US is no longer listed in the FAA A/FD (old FAA LID:
    48Y)
  - K49N    , Lufker Airport, East Moriches, New York, US is not an AIRPORT or SEAPLANE BASE per FAA A/FD: None,  (old
    FAA LID: 49N)
  - K4D1    , Three Castles Airpark, Wonewoc, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID: 4D1)
  - K4Y1    , Raether Airport, Howell, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 4Y1)
  - K54M    , Wolf River Airport, Rossville, Tennessee, US is no longer listed in the FAA A/FD (old FAA LID: 54M)
  - K5S9    , Valley View Airport, Estacada, Oregon, US is no longer listed in the FAA A/FD (old FAA LID: 5S9)
  - K5Y0    , Harrisville Airport, Harrisville, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 5Y0)
  - K5Y4    , Lost Creek Airport, Luzerne, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 5Y4)
  - K7C5    , Sig Field, Montezuma, Iowa, US is no longer listed in the FAA A/FD (old FAA LID: 7C5)
  - K7F5    , Canton-Hackney Airport, Canton, Texas, US is no longer listed in the FAA A/FD (old FAA LID: 7F5)
  - K7K8    , Martin Field, So Sioux City, Nebraska, US is no longer listed in the FAA A/FD (old FAA LID: 7K8)
  - K7N7    , Oldmans Township Airport, Pedricktown, New Jersey, US is no longer listed in the FAA A/FD (old FAA LID:
    7N7)
  - K89Y    , Maidens Airport, Williamston, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 89Y)
  - K8A0    , Albertville Regional/Thomas J Brumlik Field, Albertville, Alabama, US is no longer listed in the FAA A/FD
    (old FAA LID: 8A0)
  - K8B5    , Tanner-Hiller Airport, Barre/Barre Plains, Massachusetts, US is no longer listed in the FAA A/FD (old FAA
    LID: 8B5)
  - K8M8    , Eagle Ii Airport, Lewiston, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: 8M8)
  - K9G1    , Pittsburgh Northeast Airport, Pittsburgh, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA
    LID: 9G1)
  - KA09    , Eagle Airpark, Bullhead City, Arizona, US is no longer listed in the FAA A/FD (old FAA LID: A09)
  - KC02/XES, Grand Geneva Resort Airport, Lake Geneva, Wisconsin, US: Closed Indefinitely (old FAA LID: C02)
  - KC72    , Cross Winds Airport, Clayton, Washington, US is no longer listed in the FAA A/FD (old FAA LID: C72)
  - KF31    , Lake Texoma State Park Airport, Kingston, Oklahoma, US is no longer listed in the FAA A/FD (old FAA LID:
    F31)
  - KL54    , Agua Caliente Springs Airport, Agua Caliente Springs, California, US is no longer listed in the FAA A/FD
    (old FAA LID: L54)
  - KM31    , Arnold Field, Halls, Tennessee, US is no longer listed in the FAA A/FD (old FAA LID: M31)
  - KO14    , Skyroads Airport, Ninnekah, Oklahoma, US is no longer listed in the FAA A/FD (old FAA LID: O14)
  - KP15    , Brokenstraw Airport, Pittsfield, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: P15)
  - KS48    , Country Squire Airpark, Sandy, Oregon, US is no longer listed in the FAA A/FD (old FAA LID: S48)
  - KS79    , Green Sea Airport, Green Sea, South Carolina, US is no longer listed in the FAA A/FD (old FAA LID: S79)
  - KU42    , South Valley Regional Airport, Salt Lake City, Utah, US is no longer listed in the FAA A/FD (old FAA LID:
    U42)
  - KW19    , Verona Airport, Verona, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID: W19)
  - KX54    , Benger Air Park, Friona, Texas, US is no longer listed in the FAA A/FD (old FAA LID: X54)
  - KXA0    , Prose Field, Justin, Texas, US: Closed Indefinitely (old FAA LID: XA0)
  - KZ92    , Harsens Island Airport, Harsens Island, Michigan, US is no longer listed in the FAA A/FD (old FAA LID:
    Z92)
  - LL09    , Air Estates Inc Airport, Mundelein, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: LL09)
  - LL24    , Sunset Acres Airport, Manteno, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: LL24)
  - LL27    , Blythe Field, Macomb, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: LL27)
  - LL32    , C D Maulding Airport, Paxton, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: LL32)
  - LL53    , Olson Airport, Plato Center, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: LL53)
  - LL64    , Ralph E Daniels Airport, Putnam, Illinois, US is no longer listed in the FAA A/FD (old FAA LID: LL64)
  - ME00    , Fort Fairfield Airport, Fort Fairfield, Maine, US is no longer listed in the FAA A/FD (old FAA LID: ME00)
  - ME14    , Bald Mountain Airport, Camden, Maine, US is no longer listed in the FAA A/FD (old FAA LID: ME14)
  - MI56    , Dune Bird Airport, Leland, Michigan, US is no longer listed in the FAA A/FD (old FAA LID: MI56)
  - MO25    , Shatto Farm Airport, Osborn, Missouri, US is no longer listed in the FAA A/FD (old FAA LID: MO25)
  - MT74    , Sikorski Ranch Airport, Ekalaka, Montana, US is no longer listed in the FAA A/FD (old FAA LID: MT74)
  - MT88    , Campbell Ranch Airport, Marion, Montana, US is no longer listed in the FAA A/FD (old FAA LID: MT88)
  - MU03    , Stockwell Field, Brookfield, Missouri, US is no longer listed in the FAA A/FD (old FAA LID: MU03)
  - MU46    , Arrowhead Airpark, Belton, Missouri, US is no longer listed in the FAA A/FD (old FAA LID: MU46)
  - NA99    , Bakko Airstrip, Walcott, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: NA99)
  - NC20    , Canaan Air Base Airport, New Bern, North Carolina, US is no longer listed in the FAA A/FD (old FAA LID:
    NC20)
  - NC45    , Enfield-Shearin Airport, Enfield, North Carolina, US is no longer listed in the FAA A/FD (old FAA LID:
    NC45)
  - ND01    , Nelson Airport, Amenia, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: ND01)
  - ND20    , Gensrich Airport, Hatton, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: ND20)
  - ND24    , Inkster Airport, Inkster, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: ND24)
  - ND49    , Krause Private Airport, Wyndmere, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: ND49)
  - ND78    , Wilcox Farm Airport, Ayr, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: ND78)
  - ND89    , Mutschler Field, Clementsville, North Dakota, US is no longer listed in the FAA A/FD (old FAA LID: ND89)
  - NH20    , Ward Field, Sanbornton, New Hampshire, US is no longer listed in the FAA A/FD (old FAA LID: NH20)
  - NH43    , Murphy-Sherwood Park Airport, Nottingham, New Hampshire, US is no longer listed in the FAA A/FD (old FAA
    LID: NH43)
  - NK04    , Shepard Airport, Constantia, New York, US is no longer listed in the FAA A/FD (old FAA LID: NK04)
  - NR10    , Pink Hill Airport, Pink Hill, North Carolina, US is no longer listed in the FAA A/FD (old FAA LID: NR10)
  - NV35    , Hudson Airport, Austin, Nevada, US is no longer listed in the FAA A/FD (old FAA LID: NV35)
  - NY13    , D'Amico Airport, Lyons, New York, US is no longer listed in the FAA A/FD (old FAA LID: NY13)
  - OA11    , Heitman Field, Anna, Ohio, US is no longer listed in the FAA A/FD (old FAA LID: OA11)
  - OA40    , Autumn Orchard Airport, Louisville, Ohio, US is no longer listed in the FAA A/FD (old FAA LID: OA40)
  - OA85    , Riverview Airport, Dresden, Ohio, US is no longer listed in the FAA A/FD (old FAA LID: OA85)
  - OK13    , Erroport Airport, Mounds, Oklahoma, US is no longer listed in the FAA A/FD (old FAA LID: OK13)
  - OK74    , Flying H Airport, Ashland, Oklahoma, US is no longer listed in the FAA A/FD (old FAA LID: OK74)
  - OMU9    , Kollmeyer Airport, Pilot Grove, Missouri, US is no longer listed in the FAA A/FD (old FAA LID: OMU9)
  - PS69    , Barnhart Airport, Flinton, Pennsylvania, US is no longer listed in the FAA A/FD (old FAA LID: PS69)
  - SC51    , Too Goo Doo Farms Airport, Meggett, South Carolina, US is no longer listed in the FAA A/FD (old FAA LID:
    SC51)
  - SC75    , Oolenoy Valley Airport, Pickens, South Carolina, US is no longer listed in the FAA A/FD (old FAA LID:
    SC75)
  - SD13    , Hofer Airport, Doland, South Dakota, US is no longer listed in the FAA A/FD (old FAA LID: SD13)
  - SN12    , Jenkinson Airport, Meade, Kansas, US is no longer listed in the FAA A/FD (old FAA LID: SN12)
  - TA49    , Keno Field, Andice, Texas, US is not an AIRPORT or SEAPLANE BASE per FAA A/FD: CHRISTUS MOTHER FRANCES
    ATHENS, HELIPORT (old FAA LID: TA49)
  - TS05    , La Buena Vida Airport, Woodsboro, Texas, US is no longer listed in the FAA A/FD (old FAA LID: TS05)
  - TX11    , Ross Planes Airport, Cross Plains, Texas, US is not an AIRPORT or SEAPLANE BASE per FAA A/FD: DHS LAREDO,
    HELIPORT (old FAA LID: TX11)
  - TX78    , Block Ranch Airport, Alvarado, Texas, US is no longer listed in the FAA A/FD (old FAA LID: TX78)
  - TX81    , Robotek Airport, Gainesville, Texas, US is no longer listed in the FAA A/FD (old FAA LID: TX81)
  - TX91    , Madeira Airpark, Garland, Texas, US is no longer listed in the FAA A/FD (old FAA LID: TX91)
  - VA32    , Longs Airport, Edinburg, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: VA32)
  - VA56    , Wells Airport, Ivor, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: VA56)
  - VA66    , Breeden Airport, Catlett, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: VA66)
  - VA94    , Plainview Airport, Powhatan, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: VA94)
  - VG01    , Eureka Airport, Keysville, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: VG01)
  - VG33    , Bull Farm Airport, Cape Charles, Virginia, US is no longer listed in the FAA A/FD (old FAA LID: VG33)
  - WI19    , Cacic Airport, Montello, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID: WI19)
  - WI28    , Walters Agri-Center Airport, Rio Creek, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID:
    WI28)
  - WN05    , Harris Airport, Toledo, Washington, US is no longer listed in the FAA A/FD (old FAA LID: WN05)
  - WN10    , Mount St Helen's Aero Ranch Airport, Cougar, Washington, US is no longer listed in the FAA A/FD (old FAA
    LID: WN10)
  - WN20    , Van De Plasch Airport, Monroe, Washington, US is no longer listed in the FAA A/FD (old FAA LID: WN20)
  - WN99    , Hayes Road Airport, Durand, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID: WN99)
  - WS23    , R & S Landing Strip, Merrill, Wisconsin, US is no longer listed in the FAA A/FD (old FAA LID: WS23)
  - WY00    , Red Reflet Ranch Airport, Ten Sleep, Wyoming, US is no longer listed in the FAA A/FD (old FAA LID: WY00)
  - XS28    , Green Acres Airfield, Pampa, Texas, US is no longer listed in the FAA A/FD (old FAA LID: XS28)


Version 20260205
================

* Added the following 5 airports:

  - SBSG/NAT, Greater Natal International Airport, São Gonçalo do Amarante, Rio Grande do Norte, BR.
  - SCQP/ZCO, La Araucanía Airport (Temuco), Freire, Aisen, CL.
  - SSTE/TSQ, Torres Airport, Torres, Rio Grande do Sul, BR.
  - VQBT/BUT, Bathbalathang Domestic Airport, Jakar, Bumthang, BT.
  - ZYYK/YKH, Yingkou Lanqi Airport, Yingkou, Liaoning, CN.

* Updated IATA locator (and other data) for the following 8 airports:

  - 90WA/WDN, Waldron Airstrip, East Sound, Washington, US: iata added.
  - KANJ/SSM, Sault Ste Marie Municipal/Sanderson Field, Sault Ste Marie, Michigan, US: iata added.
  - KBDH/ILL, Willmar Municipal/John L Rice Field, Willmar, Minnesota, US: iata added.
  - KODO/ODT, Odessa-Schlemeyer Field, Odessa, Texas, US: iata added.
  - LKCS/JCL, Ceske Budejovice Airport, Ceske Budejovice, Jihocesky, CZ: iata added.
  - SBNT    , Augusto Severo Airport (Base Aérea de Natal), Parnamirim, Rio Grande do Norte, BR: iata "NAT" deleted,
    name changed from "Augusto Severo Airport", city changed from "Natal".
  - SCTC    , Maquehue Airport, Temuco, Araucania, CL: iata deleted.
  - URRY    , Zavetnoe Airport, , Rostov, RU: iata deleted.

* Updated Belgium/Luxembourg for the following 18 major and military airports to match AIP data:

  - EBAW/ANR, Antwerp International Airport (Deurne), Antwerp, Flanders, BE: elevation changed from 39 to 32, latitude
    changed from 51.1894 to 51.1122, longitude changed from 4.46028 to 4.2737.
  - EBBE    , Beauvechain Air Base, Beauvechain, Wallonia, BE: elevation changed from 370 to 362, latitude changed from
    50.7586 to 50.4528, longitude changed from 4.76833 to 4.4601.
  - EBBL    , Kleine Brogel Air Base, Kleine Brogel, Flanders, BE: elevation changed from 200 to 192, latitude changed
    from 51.1683 to 51.1006, longitude changed from 5.47 to 5.2812.
  - EBBR/BRU, Brussels Airport, Brussels, Flanders, BE: elevation changed from 184 to 175, latitude changed from 50.9014
    to 50.5405, longitude changed from 4.48444 to 4.2904.
  - EBBX    , Jehonville Air Base, Bertrix, Wallonia, BE: elevation changed from 1514 to 1503, latitude changed from
    49.8917 to 49.533, longitude changed from 5.22389 to 5.1326.
  - EBCI/CRL, Brussels South Charleroi Airport, Brussels, Wallonia, BE: elevation changed from 614 to 606, latitude
    changed from 50.4592 to 50.2736, longitude changed from 4.45382 to 4.271.
  - EBCV    , Chievres Air Base, Chievres, Wallonia, BE: latitude changed from 50.5758 to 50.3433, longitude changed
    from 3.831 to 3.4952.
  - EBDT    , Schaffen Airport, Diest, Flanders, BE: elevation changed from 100 to 92, latitude changed from 50.9992 to
    51.0005, longitude changed from 5.06556 to 5.0345.
  - EBFN    , Koksijde Air Base, Koksijde, Flanders, BE: elevation changed from 20 to 11, latitude changed from 51.0903
    to 51.0525, longitude changed from 2.65278 to 2.391.
  - EBFS    , Florennes Air Base, Florennes, Wallonia, BE: elevation changed from 935 to 927, latitude changed from
    50.2433 to 50.1436, longitude changed from 4.64583 to 4.3845.
  - EBKT/KJK, Wevelgem Airport, Wevelgem, Flanders, BE: elevation changed from 64 to 55, latitude changed from 50.8172
    to 50.4907, longitude changed from 3.20472 to 3.1233.
  - EBLG/LGG, Liege Airport, Liege, Wallonia, BE: elevation changed from 659 to 651, latitude changed from 50.6374 to
    50.3811, longitude changed from 5.44322 to 5.2634.
  - EBMB    , Melsbroek Air Base, Brussels, Flanders, BE: elevation changed from 184 to 175, latitude changed from
    50.90139 to 50.5405, longitude changed from 4.48444 to 4.2904.
  - EBOS/OST, Ostend-Bruges International Airport, Ostend, Flanders, BE: elevation changed from 13 to 7, latitude
    changed from 51.1989 to 51.1156, longitude changed from 2.86222 to 2.5144.
  - EBSU    , Saint Hubert Air Base, Saint Hubert, Wallonia, BE: elevation changed from 1930 to 1922, latitude changed
    from 50.0344 to 50.0203, longitude changed from 5.44081 to 5.2624.
  - EBUL    , Ursel Air Base, Ursel, Flanders, BE: elevation changed from 95 to 67, latitude changed from 51.1442 to
    51.0839, longitude changed from 3.47556 to 3.2832.
  - EBWE    , Weelde Air Base, Weelde, Flanders, BE: elevation changed from 105 to 97, latitude changed from 51.3948 to
    51.2339, longitude changed from 4.96019 to 4.5733.
  - ELLX/LUX, Luxembourg-Findel International Airport, Luxembourg, Luxembourg, LU: latitude changed from 49.6266 to
    49.3724, longitude changed from 6.21152 to 6.1216.

* Updated other data for the following 4 airports:

  - CYDO/YDO, Dolbeau Lac-Saint-Jean Airport, Saint-Félicien, Quebec, CA: name changed from "Dolbeau St Felicien
    Airport", city changed from "Dolbeau-St-Felicien".
  - VANM/NMI, Navi Mumbai International Airport, Navi Mumbai, Maharashtra, IN: latitude changed from 18.994383 to
    18.593978, longitude changed from 73.070264 to 73.041295.
  - YTNG/ZBL, Thangool (Biloela) Airport, Biloela, Queensland, AU: name changed from "Thangool Airport".
  - ZGZJ/ZHA, Zhanjiang Wuchuan Airport, Zhanjiang, Guangdong, CN: name changed from "Zhanjiang Airport".

* Updated the following 101 Indonesian airports' name and/or province:

  - WAHI/YIA, Yogyakarta International Airport, Yogyakarta, Java Island, Yogyakarta, ID: city changed from "Yogyakarta-
    Java Island".
  - WALE    , Melak Airport, Melak, Borneo Island, , ID: city changed from "Melak-Borneo Island".
  - WALG/TJS, Tanjung Harapan Airport, Tanjung Selor, Borneo Island, East Kalimantan, ID: city changed from "Tanjung
    Selor-Borneo Island".
  - WALJ/DTD, Datadawai Airport, Datadawai, Borneo Island, East Kalimantan, ID: city changed from "Datadawai-Borneo
    Island".
  - WALK/BEJ, Barau(Kalimaru) Airport, Tanjung Redep, Borneo Island, East Kalimantan, ID: city changed from "Tanjung
    Redep-Borneo Island".
  - WALL/BPN, Sepinggan International Airport, Balikpapan, Borneo Island, East Kalimantan, ID: city changed from
    "Balikpapan-Borneo Island".
  - WALQ    , Muara Badak Pujangan Airport, Muara Badak, Borneo Island, East Kalimantan, ID: city changed from "Muara
    Badak-Borneo Island".
  - WALS/AAP, Aji Pangeran Tumenggung Pranoto International Airport, Samarinda, Borneo Island, East Kalimantan, ID: city
    changed from "Samarinda-Borneo Island".
  - WALT/TSX, Tanjung Santan Airport, Santan, Borneo Island, East Kalimantan, ID: city changed from "Santan-Borneo
    Island".
  - WALX    , Mangkajang Airport, Mangkajang, Borneo Island, East Kalimantan, ID: city changed from "Mangkajang-Borneo
    Island".
  - WAOC/BTW, Batu Licin Airport, Batu Licin, Borneo Island, South Kalimantan, ID: city changed from "Batu Licin-Borneo
    Island".
  - WAOI/PKN, Iskandar Airport, Pangkalanbun, Borneo Island, Central Kalimantan, ID: city changed from "Pangkalanbun-
    Borneo Island".
  - WAON/TJG, Warukin Airport, Tanta-Tabalong, Borneo Island, South Kalimantan, ID: city changed from "Tanta-Tabalong-
    Borneo Island".
  - WAOO/BDJ, Syamsudin Noor Airport, Banjarmasin, Borneo Island, South Kalimantan, ID: city changed from "Banjarmasin-
    Borneo Island".
  - WAOS/SMQ, Sampit(Hasan) Airport, Sampit, Borneo Island, Central Kalimantan, ID: city changed from "Sampit-Borneo
    Island".
  - WARA/MLG, Abdul Rachman Saleh Airport, Malang, Java Island, East Java, ID: city changed from "Malang-Java Island".
  - WARC/CPF, Cepu Airport, Tjepu, Java Island, Central Java, ID: city changed from "Tjepu-Java Island".
  - WARI    , Iswahyudi Airport, Madiun, Java Island, East Java, ID: city changed from "Madiun-Java Island".
  - WARJ/JOG, Adi Sutjipto International Airport, Yogyakarta, Java Island, Yogyakarta, ID: city changed from
    "Yogyakarta-Java Island".
  - WARQ/SOC, Adi Sumarmo Wiryokusumo Airport, Sukarata(Solo), Java Island, Central Java, ID: city changed from
    "Sukarata(Solo)-Java Island".
  - WARS/SRG, Achmad Yani Airport, Semarang, Java Island, Central Java, ID: city changed from "Semarang-Java Island".
  - WI1A    , Nusawiru Airport, Pangandaran, Java Island, West Java, ID: city changed from "Pangandaran-Java Island".
  - WI1B    , Batujajar Airport, Bandung, Java Island, West Java, ID: city changed from "Bandung-Java Island".
  - WI1C    , Rumpin Airport, Rumpin, Java Island, West Java, ID: city changed from "Rumpin-Java Island".
  - WI1G    , Gading Wonosari Airport, Wonosari, Java Island, Yogyakarta, ID: city changed from "Wonosari-Java Island".
  - WI1S    , Simpangtiga Redelong Airport, Tingkeum, Sumatra Island, Aceh, ID: city changed from "Tingkeum-Sumatra
    Island".
  - WIAG/AKQ, Menggala Airport, Menggala, Sumatra Island, , ID: city changed from "Menggala-Sumatra Island".
  - WIAK    , Margahayu Airport, Bandung, Java Island, West Java, ID: city changed from "Bandung-Java Island".
  - WIAP    , Banyumas Airport, Banyumas, Java Island, Central Java, ID: city changed from "Banyumas-Java Island", subd
    added.
  - WIBB/PKU, Sultan Syarif Kasim Ii (Simpang Tiga) Airport, Pekanbaru, Sumatra Island, Riau, ID: city changed from
    "Pekanbaru-Sumatra Island".
  - WIBD/DUM, Pinang Kampai Airport, Dumai, Sumatra Island, Riau, ID: city changed from "Dumai-Sumatra Island".
  - WIBS    , Sungai Pakning Bengkalis Airport, Bengkalis, Sumatra Island, Riau, ID: city changed from "Bengkalis-
    Sumatra Island".
  - WICB    , Budiarto Airport, Tangerang, Java Island, West Java, ID: city changed from "Tangerang-Java Island".
  - WICC/BDO, Husein Sastranegara International Airport, Bandung, Java Island, West Java, ID: city changed from
    "Bandung-Java Island".
  - WICD/CBN, Penggung Airport, Cirebon, Java Island, West Java, ID: city changed from "Cirebon-Java Island".
  - WICM/TSY, Cibeureum Airport, Tasikmalaya, Java Island, West Java, ID: city changed from "Tasikmalaya-Java Island".
  - WICT/TKG, Radin Inten II (Branti) Airport, Bandar Lampung, Sumatra Island, Lampung, ID: city changed from "Bandar
    Lampung-Sumatra Island", subd added.
  - WIDD/BTH, Hang Nadim Airport, Batam, Batam Island, Riau Islands, ID: city changed from "Batam Island", subd added.
  - WIDE/PPR, Pasir Pangaraan Airport, Pasir Pengarayan, Sumatra Island, Riau, ID: city changed from "Pasir Pengarayan-
    Sumatra Island".
  - WIEE/PDG, Minangkabau Airport, Ketaping/Padang, Sumatra Island, West Sumatra, ID: city changed from
    "Ketaping/Padang-Sumatra Island".
  - WIHL/CXP, Tunggul Wulung Airport, Cilacap, Java Island, Central Java, ID: city changed from "Cilacap-Java Island",
    subd added.
  - WIHP/PCB, Pondok Cabe Air Base, Jakarta, Jakarta, ID: subd added.
  - WIII/CGK, Soekarno-Hatta International Airport, Jakarta, Jakarta, ID: subd added.
  - WIIK    , Kalijati Airport, Kalijati, Java Island, West Java, ID: city changed from "Kalijati-Java Island".
  - WIIR    , Pelabuhan Ratu Airport, Pelabuhan Ratu, Java Island, West Java, ID: city changed from "Pelabuhan Ratu-Java
    Island".
  - WIKL    , Silampari Airport, Lubuk Linggau, Sumatra Island, South Sumatra, ID: city changed from "Lubuk Linggau-
    Sumatra Island", subd added.
  - WIMA    , Labuhan Bilik Airport, Labuhan Bilik, Sumatra Island, North Sumatra, ID: city changed from "Labuhan Bilik-
    Sumatra Island", subd added.
  - WIMB/GNS, Binaka Airport, Gunung Sitoli, Nias Island, North Sumatra, ID: city changed from "Gunung Sitoli-Nias
    Island".
  - WIME/AEG, Aek Godang Airport, Padang Sidempuan, Sumatra Island, North Sumatra, ID: city changed from "Padang
    Sidempuan-Sumatra Island", subd added.
  - WIMG    , Sutan Sjahrir Air Force Base, Padang, Sumatra Island, West Sumatra, ID: city changed from "Padang-Sumatra
    Island", subd added.
  - WIMH    , Helvetia Airport, Helvetia, Sumatra Island, North Sumatra, ID: city changed from "Helvetia-Sumatra
    Island".
  - WIMK/MES, Soewondo Air Force Base, Medan, Sumatra Island, North Sumatra, ID: city changed from "Medan", subd added.
  - WIML    , Kisaran Airport, Kisaran, Sumatra Island, Aceh, ID: city changed from "Kisaran-Sumatra Island".
  - WIMM/KNO, Polonia International Airport, Medan, Sumatra Island, North Sumatra, ID: city changed from "Medan-Sumatra
    Island", subd added.
  - WIMN/DTB, Silangit Airport, Tingkeum, Sumatra Island, North Sumatra, ID: city changed from "Tingkeum-Sumatra
    Island".
  - WIMO    , Bandar Udara Lasondre, Tanah Masa Island, Batu Islands, North Sumatra, ID: city added, subd added.
  - WIMP/SIW, Parapat Airport, Parapat, Sumatra Island, North Sumatra, ID: city changed from "Parapat-Sumatra Island",
    subd added.
  - WIMR    , Pematang Siantar, Pematang Siantar, Sumatra Island, North Sumatra, ID: city changed from "Pematang
    Siantar-Sumatra Island".
  - WIMS/FLZ, Dr Ferdinand Lumban Tobing Airport, Sibolga, Sumatra Island, North Sumatra, ID: city changed from
    "Sibolga-Sumatra Island".
  - WIMT    , Tebing Tinggi Airport, Tabbing Tinggi, Sumatra Island, North Sumatra, ID: city changed from "Tabbing
    Tinggi-Sumatra Island".
  - WIOB    , Bengkayang Airport, Bengkayang, Borneo Island, West Kalimantan, ID: city changed from "Bengkayang-Borneo
    Island".
  - WIOD/TJQ, Buluh Tumbang (H A S Hanandjoeddin) Airport, Tanjung Pandan, Belitung Island, Belitung, ID: city changed
    from "Tanjung Pandan-Belitung Island", subd changed from "Bangka–Belitung-Islands".
  - WIOG/NPO, Nanga Pinoh I Airport, Nanga Pinoh, Borneo Island, West Kalimantan, ID: city changed from "Nanga Pinoh-
    Borneo Island".
  - WIOI    , Singkawang Airport, Singkawang, Borneo Island, West Kalimantan, ID: city changed from "Sinkawang-Borneo
    Island", subd added.
  - WIOK/KTG, Ketapang (Rahadi Usman) Airport, Ketapang, Borneo Island, West Kalimantan, ID: name changed from
    "Ketapang(Rahadi Usman) Airport", city changed from "Ketapang-Borneo Island", subd added.
  - WION/NTX, Ranai Airport, Ranai, Natuna Besar Island, Riau Islands, ID: city changed from "Ranai-Natuna Besar
    Island".
  - WIOO/PNK, Supadio Airport, Pontianak, Borneo Island, West Kalimantan, ID: city changed from "Pontianak-Borneo
    Island".
  - WIOP/PSU, Pangsuma Airport, Putussibau, Borneo Island, West Kalimantan, ID: city changed from "Putussibau-Borneo
    Island".
  - WIOS    , Sintang (Susilo) Airport, Sintang, Borneo Island, West Kalimantan, ID: name changed from "Sintang(Susilo)
    Airport", city changed from "Sintang-Borneo Island", subd added.
  - WIPA/DJB, Sultan Thaha Airport, Jambi, Sumatra Island, Jambi, ID: city changed from "Jambi-Sumatra Island", subd
    added.
  - WIPB/LLJ, Silampari, Lubuk Linggau, Sumatra Island, South Sumatra, ID: city changed from "Lubuk Linggau".
  - WIPD    , Banding Agung Airport, Pasar Banding Agung, Sumatra Island, South Sumatra, ID: city changed from "Pasar
    Bandingagung-Sumatra Island", subd added.
  - WIPF    , Kuala Tungkal Airport, Kuala Tungkal, Sumatra Island, Jambi, ID: city changed from "Kuala Tungkal-Sumatra
    Island".
  - WIPK/PGK, Pangkal Pinang (Depati Amir) Airport, Pangkal Pinang, Palaubangka Island, Bangka Belitung Islands, ID:
    city changed from "Pangkal Pinang-Palaubangka Island", subd changed from "South Sumatra".
  - WIPL/BKS, Padang Kemiling (Fatmawati Soekarno) Airport, Bengkulu, Sumatra Island, Bengkulu, ID: city changed from
    "Bengkulu-Sumatra Island", subd added.
  - WIPO/WYK, Gatot Subrato Airport, Batu Raja, Sumatra Island, Lampung, ID: city changed from "Batu Raja-Sumatra
    Island".
  - WIPP/PLM, Sultan Mahmud Badaruddin Ii Airport, Palembang, Sumatra Island, South Sumatra, ID: city changed from
    "Palembang-Sumatra Island".
  - WIPQ/PDO, Pendopo Airport, Talang Gudang, Sumatra Island, South Sumatra, ID: city changed from "Talang Gudang-
    Sumatra Island".
  - WIPR/RGT, Japura Airport, Rengat, Sumatra Island, Riau Islands, ID: city changed from "Rengat-Sumatra Island".
  - WIPU/MPC, Muko Muko Airport, Muko Muko, Sumatra Island, Bengkulu, ID: city changed from "Muko Muko-Sumatra Island",
    subd added.
  - WIPV/KLQ, Keluang Airport, Keluang, Sumatra Island, South Sumatra, ID: city changed from "Keluang-Sumatra Island",
    subd added.
  - WIPY    , Bentayan Airport, Bentayan, Sumatra Island, South Sumatra, ID: city changed from "Bentayan-Sumatra
    Island", subd added.
  - WITA/TPK, Teuku Cut Ali Airport, Tapak Tuan, Sumatra Island, Aceh, ID: city changed from "Tapak Tuan-Sumatra
    Island".
  - WITC/MEQ, Cut Nyak Dien Airport, Peureumeue, Sumatra Island, Aceh, ID: name changed from "Seunagan Airport", city
    changed from "Peureumeue-Sumatra Island", elevation changed from 10 to 7.
  - WITG    , Lasikin Airport, Lubang, Simeulue Island, Aceh, ID: city changed from "Lubang-Simeulue Island", subd
    added.
  - WITL/LSX, Lhok Sukon Airport, Lhok Sukon, Sumatra Island, Aceh, ID: city changed from "Lhok Sukon-Sumatra Island".
  - WITM/LSW, Malikus Saleh Airport, Lhok Seumawe, Sumatra Island, Aceh, ID: city changed from "Lhok Seumawe-Sumatra
    Island".
  - WITN/SBG, Maimun Saleh Airport, Sabang, We Island, Aceh, ID: city changed from "Sabang-We Island".
  - WITS    , Seumayam Airport, Seumayam, Sumatra Island, Aceh, ID: city changed from "Seumayam-Sumatra Island".
  - WITT/BTJ, Sultan Iskandarmuda Airport, Banda Aceh, Sumatra Island, Aceh, ID: city changed from "Banda Aceh-Sumatra
    Island".
  - WRBU    , Buntok Airport, Buntok, Borneo Island, Central Kalimantan, ID: city changed from "Buntok-Borneo Island".
  - WRLB/LBW, Long Bawan Airport, Long Bawan, Borneo Island, North Kalimantan, ID: city changed from "Long Bawan-Borneo
    Island".
  - WRLC/BXT, Bontang Airport, Bontang, Borneo Island, East Kalimantan, ID: city changed from "Bontang-Borneo Island".
  - WRLH/TNB, Tanah Grogot Airport, Tanah Grogot, Borneo Island, East Kalimantan, ID: city changed from "Tanah Grogot-
    Borneo Island".
  - WRLL    , Balikpapan Airport, Seppingan, Borneo Island, East Kalimantan, ID: city changed from "Seppingan-Borneo
    Island".
  - WRLM    , Malinau Airport, Malinau, Borneo Island, South Kalimantan, ID: city changed from "Malinau-Borneo Island".
  - WRLN    , Long Mawang Airport, Long Mawang, Borneo Island, North Kalimantan, ID: city changed from "Long Mawang-
    Borneo Island".
  - WRLP/LPU, Long Apung Airport, Long Apung, Borneo Island, East Kalimantan, ID: city changed from "Long Apung-Borneo
    Island".
  - WRLU    , Sangkulirang Airport, Sangkulirang, Borneo Island, East Kalimantan, ID: city changed from "Sangkulirang-
    Borneo Island".
  - WRLW    , Muara Wahau Airport, Muara Wahau, Borneo Island, East Kalimantan, ID: city changed from "Muara Wahau-
    Borneo Island".
  - WRSP    , Surabaya Airport, Surabaya, Java Island, , ID: city changed from "Surabaya-Java Island".

* Removed the following airport:

  - SBTR/TSQ, Torres Airport, Torres, Rio Grande do Sul, BR (change in ICAO designator to SSTE).

Version 20251008
================

* VDPP/PNH, Phnom Penh International Airport, Phnom Penh, Phnom Penh, KH, has been removed as it is now officially
  closed. It has been replaced by VDTI/KTI, Techo International Airport, Phnom Penh, Phnom Penh, KH (already in the
  database).

* Uzbekistan has officially dropped its old "UT" ICAO prefix in favor of "UZ" effective on 2 October 2025. The
  following 29 airports have been updated:

  - UZ1M    , Kakaydy Airport, Goran, Surxondaryo, UZ.
  - UZ1N    , Karshi South Airport, Karshi, Qashqadaryo, UZ.
  - UZ1O    , Beleuli North Airport, Beleuli, Karakalpakstan, UZ.
  - UZ1P    , Kagan South Airport, Kagan, Bukhara, UZ.
  - UZ1Q    , Pakhtakor Airport, Pakhtakor, Jizzax, UZ.
  - UZ77    , Kungrad Airport, Kungrad, Karakalpakstan, UZ.
  - UZKA/AZN, Andizhan Airport, Andizhan, Andijon, UZ.
  - UZKF/FEG, Fergana Airport, Fergana, Fergana, UZ.
  - UZKK/OQN, Kokand Airport, Kokand, Fergana, UZ.
  - UZKN/NMA, Namangan Airport, Namangan, Namangan, UZ.
  - UZNM    , Muynak Airport, Muynak, Karakalpakstan, UZ.
  - UZNN/NCU, Nukus Airport, Nukus, Karakalpakstan, UZ.
  - UZNT    , Turtkul Airport, Turtkul, Karakalpakstan, UZ.
  - UZNU/UGC, Urgench Airport, Urgench, Xorazm, UZ.
  - UZSA/NVI, Navoi Airport, Navoi, Navoiy, UZ.
  - UZSB/BHK, Bukhara Airport, Bukhara, , UZ.
  - UZSH    , Shakhristabz Airport, Shakhristabz, Qashqadaryo, UZ.
  - UZSK/KSQ, Karshi Airport, Karshi, Qashqadaryo, UZ.
  - UZSL    , Karshi Khanabad Airport, Khanabad, Qashqadaryo, UZ.
  - UZSM    , Tandy Bulak Airport, Tandy Bulak, Navoiy, UZ.
  - UZSN/AFS, Sugraly Airport, Zarafshan, Navoiy, UZ.
  - UZSR    , Sariasiya Airport, Sariasiya, Surxondaryo, UZ.
  - UZSS/SKD, Samarkand Airport, Samarkand, , UZ.
  - UZST/TMJ, Termez Airport, Termez, Surxondaryo, UZ.
  - UZSU    , Uchkuduk Airport, Uchkuduk, Navoiy, UZ.
  - UZTP    , Tashkent East Airport, Tashkent, Toshkent, UZ.
  - UZTT/TAS, Tashkent International Airport, Tashkent, Toshkent-Shahri, UZ.
  - UZTZ/OMN, Zomin Airport, Lyaylyakul, Jizzax, UZ.

* Updated other data for the following 2 airports:

  - EHOW    , Oostwold Airport, Oostwold, Groningen, NL: city added.
  - VIND/DXN, Noida International Airport, Jewar, Uttar Pradesh, IN: Elevation changed from from 642 to 652.54, city
    changed from "Noida", latitude changed from 28.17 to 28.175556, longitude changed from 77.61 to 77.606111.

* Supports Python 3.14 and 3.14t.

Version 20250909
================

* Added the following 60 airports:

  - AYAF/AFR, Afore Airstrip, Afore, Oro Province, PG.
  - AYBL/BAA, Bialla Airport, Bialla, West New Britain, PG.
  - AYCG/CGC, Cape Gloucester Airport, Cape Gloucester, West New Britain, PG.
  - AYDA/DAO, Dahamo Airstrip, Dabo, Western, PG.
  - AYDB/DBP, Debepare Airport, Debepare, Western, PG.
  - AYSS/TDS, Sasereme Airport, Sasereme, Western Province, PG.
  - DIAO/ABO, Aboisso Airport, Aboisso, Sud-Comoé, CI.
  - EDGY/KZG, Kitzingen Airport, Kitzingen, Bayern, DE.
  - EDQA/QCB, Bamberg-Breitenau Airfield, Bamberg, Bavaria, DE.
  - FHSH/HLE, Saint Helena Airport, Saint Helena, Saint Helena, SH.
  - FOGA/AKE, Akiéni Airport, Akiéni, Haut-Ogooué, GA.
  - HCAD/AAD, Adado Airport, Adado, Galguduud, SO.
  - LTCU/BGG, Bingöl Airport, Bingöl, Bingöl, TR.
  - MYAG    , Castaway Cay Airport, Castaway Cay, North Abaco, BS.
  - MZPB/DGA, Pelican Beach Airstrip, Dangriga, Stann Creek, BZ.
  - OERS/RSI, Red Sea International Airport, Hanak, Tabuk, SA.
  - OOAD/AOM, Adam Airport, Adam, Ad Dakhiliyah, OM.
  - OPKW/KCF, Kadanwari Airport, Kadanwari, Sindh, PK.
  - PAGN/AGN, Angoon Seaplane Base, Angoon, Alaska, US.
  - RCCM/CMJ, Qimei Airport, Qimei, Penghu, TW.
  - SMEG/EAX, Eduard Alexander Gummels International Airport, Paramaribo, Kwatta, SR.
  - SPGL/CGL, Chagual Airport, Chagual, La Libertad, PE.
  - SWRP    , Teles Pires Lodge, Apiacás, Mato Grosso, BR.
  - UHTG/AEM, Amgu Airport, Amgu, Primorsky Krai, RU.
  - UKBM/MXR, Myrhorod Air Base, Myrhorod, Poltava Oblast, UA.
  - UTAN/BKN, Balkanabat International Airport, Jebel, Balkan, TM.
  - UTTZ/OMN, Zomin Airport, Lyaylyakul, Jizzax, UZ.
  - VEAP/AHA, Maa Mahamaya Airport, Ambikapur, Chhattisgarh, IN.
  - VLFL/PCQ, Boun Neau Airport, Boun Neau, Phongsaly, LA.
  - VLNK/NEU, Nong Khang Airport, Nong Khang, Houaphan, LA.
  - VNRG    , Gulmi Resunga Airport, Resunga, Western-Region, NP.
  - VQGP/GLU, Gelephu Airport, Gelephu, Sarpang, BT.
  - VRNT/TMF, Thimarafushi Airport, Thimarafushi, Thaa, MV.
  - WAGA/GXM, Kuala Kurun, Kuala Kurun, Central Kalimantan, ID.
  - WIJI/KRC, Depati Parbo Airport, Sungai Penuh, Jambi, ID.
  - YPDA/PDN, Parndana Airport, Parndana, South Australia, AU.
  - ZBCD/CDE, Chengde Puning Airport, Chengde, Hebei, CN.
  - ZBSG/SZH, Shuozhou Zirun Airport, Shuozhou, Shanxi, CN.
  - ZGHC/HNI, Hechi Jinchengjiang Airport, Hechi, Guangxi, CN.
  - ZGSG/HSC, Shaoguan Guitou Airport, Shaoguan, Guangdong, CN.
  - ZHSY/WDS, Shiyan Wudangshan Airport, Shiyan, Hubei, CN.
  - ZLDL/HXD, Delingha Airport, Delingha, Qinghai, CN.
  - ZMTL/TNZ, Tosontsengel Airport, Tosontsengel, Zavkhan, MN.
  - ZSJG/JNG, Jining Da'an Airport, Jining, Shandong, CN.
  - ZUDA/DZH, Dazhou Jinya Airport, Dazhou, Sichuan, CN.
  - ZUHY/AHJ, Ngawa Hongyuan Airport, Hongyuan, Sichuan, CN.
  - ZUPL/APJ, Ali Pulan Airport, Burang, Tibet, CN.
  - ZUZH/PZI, Panzhihua Baoanying Airport, Panzhihua, Sichuan, CN.
  - ZWLK/DHH, Balikun Dahe Airport, Barkol, Xinjiang, CN.
  - ZWTP/TLQ, Turpan Jiaohe Airport, Turpan, Xinjiang, CN.
  - ZWZS/ZFL, Zhaosu Tianma Airport, Zhaosu, Xinjiang, CN.
  - ZYJX/JXA, Jixi Xingkaihu Airport, Jixi, Heilongjiang, CN.
  - _BFY/BFY, Bengbu Tenghu Airport, Bengbu, Anhui, CN.
  - _DEJ/DEJ, Tongren Deijan Airport, Deijan, Guizhou, CN.
  - _JNH/JNH, Jiaxing Nanhu Airport, Jiaxing, Zhejiang, CN.
  - _LHL/LHL, Lachin International Airport, Lachın, Laçın, AZ.
  - _LSG/LSG, Leshan Airport (under construction, unknown coordinates), Leshan, Sichuan, CN.
  - _MUM/MUM, Muli Airport, Malé, Meemu Atoll, MV.
  - _WNJ/WNJ, Weining Airport (under construction), Leshan, Guizhou, CN.
  - _ZSP/ZSP, Zhushan Majiadu Airport (under construction, unknown coordinates), Shiyan, Hubei, CN.

* Updated IATA (and potentially other data) for the following 89 airports:

  - BIFF    , Fáskrúðsfjörður Airport, Fáskrúðsfjörður, East, IS: iata changed from "FAS", name changed from
    "Faskrudsfjordur Airport", city changed from "Faskrudsfjordur".
  - EICM    , Galway Airport, Galway, Connaught, IE: iata deleted.
  - EILT    , Letterkenny Airport, Letterkenny, Ulster, IE: iata deleted.
  - ENFG    , Leirin Airport, , Oppland, NO: iata deleted.
  - ENRY    , Moss Airport Rygge, Rygge, Østfold, NO: iata deleted.
  - ENSN    , Skien Airport, Geiteryggen, Telemark, NO: iata deleted.
  - EPKZ    , Koszalin Zegrze Airport, , West Pomerania, PL: iata deleted.
  - EPRU    , Częstochowa-Rudniki Airport, Częstochowa, Silesia, PL: iata deleted.
  - EGYM/KNF, RAF Marham, Marham, England, GB: iata changed from "MRH".
  - ETNH/QCN, Hohn Airport, Hohn, Schleswig-Holstein, DE: iata added, city added.
  - EVDA    , Daugavpils Intrenational Airport, Daugavpils, Daugavpils-municipality, LV: iata deleted.
  - FMMC    , Malaimbandy Airport, Malaimbandy, , MG: iata deleted.
  - FMNF    , Avaratra Airport, Befandriana, , MG: iata deleted.
  - FMNP    , Mampikony Airport, Mampikony, , MG: iata deleted.
  - FOOM    , Mitzic Airport, Mitzic, Woleu-Ntem, GA: iata deleted.
  - FWDW    , Dwangwa Airport, Dwangwa, Central Region, MW: iata deleted.
  - FWMG    , Mangochi Airport, Mangochi, Southern Region, MW: iata deleted.
  - GLCP    , Cape Palmas Airport, Harper, Maryland, LR: iata deleted.
  - HAGH    , Ghinnir Airport, Ghinnir, Oromiya, ET: iata deleted.
  - HASD    , Soddu Airport, Soddu, , ET: iata deleted.
  - HEAX    , El Nouzha Airport, Alexandria, , EG: iata changed from "ALY".
  - LAVL/VLO, Vlora Internationa Airport, Vlora, Vlorë, AL: iata added, name changed from "Vlore Air Base", city changed
    from "Vlore", subd changed from "Vlore", elevation changed from 3 to 8, latitude changed from 40.4761 to 40.605556,
    longitude changed from 19.4742 to 19.426111.
  - LBHS    , Uzundzhovo Air Base, Haskovo, Khaskovo, BG: iata deleted.
  - LBSS    , Silistra Polkovnik Lambrinovo Airfield, Silistra, Razgrad, BG: iata deleted.
  - LBTG    , Bukhovtsi Airfield, Targovishte, Razgrad, BG: iata deleted.
  - LELC    , San Javier Airport, San Javier, Región de Murcia, ES: iata deleted.
  - LHMC    , Miskolc Airport, Miskolc, Borsod-Abauj-Zemplen, HU: iata deleted.
  - LIPD    , Udine / Campoformido Air Base, Udine, Friuli Venezia Giulia, IT: iata deleted.
  - LKHO    , Holesov Airport, Holesov, Zlin, CZ: iata deleted.
  - LPBR    , Braga Municipal Aerodrome, Braga, Braga, PT: iata deleted.
  - LPCH    , Chaves Airfield, Chaves, Vila Real, PT: iata deleted, name changed from "Chaves Airport".
  - LPCO    , Coimbra Airfield, Antanhol, Coimbra, PT: iata deleted, name changed from "Coimbra Airport".
  - MHBL    , Brus Laguna Airport, Brus Laguna, Gracias-a-Dios, HN: iata deleted.
  - MHRS    , Santa Rosa Copan Airport, Santa Rosa de Copan, Copan, HN: iata deleted.
  - MHUL    , Sulaco Airport, Sulaco, Comayagua, HN: iata deleted.
  - MMSL/CSW, Cabo San Lucas International Airport, Cabo San Lucas, Baja California Sur, MX: iata added.
  - MPLP    , Captain Ramon Xatruch Airport, La Palma, Darien, PA: iata deleted.
  - MRSR    , Playa Samara Airport, Playa Samara, Guanacaste, CR: iata deleted.
  - MTPX    , Port-de-Paix Airport, Port-de-Paix, Nord-Ouest, HT: iata deleted.
  - OEDM/DWD, Al Dawadmi Airport, Al Dawadmi, Ar-Riyaḑ, SA: iata added, name changed from "Prince Salman Bin Abdulaziz
    Airport", city added, elevation changed from 3026 to 3031, latitude changed from 24.4499 to 24.449722, longitude
    changed from 44.1212 to 44.121111.
  - OEDR    , King Abdulaziz Air Base, , Eastern Province, SA: iata deleted.
  - OIBP    , Persian Gulf International Airport, Asalouyeh, Bushehr, IR: iata deleted.
  - OMBY/XSB, Sir Bani Yas Airport, Sir Bani Yas, Abu Dhabi, AE: iata added, elevation changed from 10 to 14, latitude
    changed from 24.283 to 24.282196, longitude changed from 52.58117 to 52.582068.
  - OYAB/EAB, Abs Airport, Abs, Hajjah, YE: iata added, name changed from "Ibb Airport", city added, subd changed from
    "Sanaa", elevation changed from 0 to 650, latitude changed from 16.01075 to 16.011111, longitude changed from
    43.17811 to 43.177778.
  - OYBN    , Beihan Airport, , Shabwah, YE: iata deleted.
  - OYQN    , Qishn Airport, Qishn, Al-Mahrah, YE: iata deleted.
  - OYSH    , Sadah Airport, Sadah, Sa‘dah, YE: iata deleted.
  - RJBH    , Hiroshimanishi Airport, , Hiroshima, JP: iata deleted.
  - RJCR    , Rebun Airport Airport, , Hokkaido, JP: iata deleted.
  - RPMB    , General Santos International Airport, General Santos City, Soccsksargen, PH: iata added, name changed from
    "Rajah Buayan Air Base".
  - RPML    , Cagayan De Oro Airfield, Cagayan De Oro, Northern Mindanao, PH: name changed from "Lumbia Airfield", city
    changed from "Cagayan De Oro City".
  - RPMR/GES, General Santos International Airport, General Santos, Soccsksargen, PH: name changed from "Tambler
    Prinipal Airport", city changed from "South Cotabato".
  - SBCD/CFC, Caçador Airport, Caçador, Santa Catarina, BR: iata added, name changed from "Cacador Airport", city
    changed from "Cacador", latitude changed from -26.7884 to -26.788056, longitude changed from -50.9398 to -50.939999.
  - SDLO/PBA, Fazenda Pontal Airport, Cairu, Bahia, BR: iata added, elevation changed from 12 to 20.
  - SKSG/LPZ, San Gil Airport, San Gil, Santander, CO: iata added.
  - SMBN    , Albina Airport, Albina, Marowijne, SR: iata deleted.
  - SPAY/AYX, Teniente General Gerardo Perez Pinedo Airport, Atalaya, Junin, PE: iata changed from "ATG", elevation
    changed from 751 to 1900.
  - SPIS/PYZ, Pias Airport, Pataz, La Libertad, PE: iata added.
  - SPNM/PNM, Nuevo Mundo Airport, Nuevo Mundo, Cusco, PE: iata added.
  - SSCN/CEL, Canela Airport, Canela, Rio Grande do Sul, BR: iata changed from "QCN", elevation changed from 2723 to
    2713.
  - UASB    , Ekibastuz Airport, Ekibastuz, Pavlodar, KZ: iata deleted.
  - UAUR    , Arkalyk North Airport, Arkalyk, , KZ: iata deleted.
  - UCFP/IKG, Karakol Airport, Karakol, Issyk-Kul, KG: iata added.
  - UTKK/OQN, Kokand Airport, Kokand, Fergana, UZ: iata added.
  - VDKH    , Kampong Chhnang Airport, , Kampong Chhnang, KH: iata deleted.
  - VDKK    , Kaoh Kong Airport, Kaoh Kong, Koh Kong, KH: iata deleted.
  - VDMK    , Mondulkiri Airport, Sen Monorom, Mondolkiri, KH: iata deleted.
  - VDST    , Stung Treng Airport, Stung Treng, Stung Treng, KH: iata deleted.
  - VEDZ/DEP, Daporijo Airport, Daporijo, Arunachal Pradesh, IN: iata changed from "DAE", city added.
  - VGIS    , Ishurdi Airport, Ishurdi, Rajshahi-Division, BD: iata deleted.
  - VGSH    , Shamshernagar Airport, Shamshernagar, Sylhet, BD: iata deleted.
  - VIHX/HWR, Halwara International Airport, Ludhiana, Punjab, IN: iata added, name changed from "Halwara Air Force
    Station", city added.
  - VLAP    , Attopeu Airport, Attopeu, Attapu, LA: iata deleted.
  - VLSV    , Saravane Airport, Saravane, Salavan, LA: iata deleted.
  - VNBG    , Bajhang Airport, Bajhang, Far-Western, NP: iata deleted.
  - VNBL    , Baglung Airport, Baglung, Western Region, NP: iata deleted.
  - VNDL    , Darchula Airport, Darchula, Far-Western, NP: iata deleted.
  - VNGK    , Gorkha Airport, Gorkha, Western Region, NP: iata deleted.
  - VNMA    , Manang Airport, Ngawal, Western Region, NP: iata deleted.
  - VNRP    , Rolpa Airport, Rolpa, Mid-Western, NP: iata deleted.
  - VYCZ    , Chanmyathazi Airport, Mandalay, Mandalay, MM: iata deleted.
  - VYPA    , Hpa-N Airport, Hpa-N, Kayin, MM: iata deleted.
  - VYYE    , Ye Airport, Ye, Mon, MM: iata deleted.
  - WAWT    , Pongtiku Airport, Tanah Toraja-Celebes Island, South Sulawesi, ID: iata deleted.
  - WIBS    , Sungai Pakning Bengkalis Airport, Bengkalis-Sumatra Island, Riau, ID: iata deleted.
  - WIOS    , Sintang(Susilo) Airport, Sintang-Borneo Island, , ID: iata deleted.
  - WIPO/WYK, Gatot Subrato Airport, Batu Raja-Sumatra Island, Lampung, ID: iata added.
  - YBAF    , Brisbane Archerfield Airport, Brisbane, Queensland, AU: iata deleted.
  - YCFH/CFH, Clifton Hills Landing Strip, Clifton Hills Station, South Australia, AU: iata added, name changed from
    "Clifton Hills Airport", city changed from "Clifton Hills", elevation changed from 0 to 105, latitude changed from
    -27.0183 to -27.015879, longitude changed from 138.892 to 138.89275.

* Updated other data for the following 59 airports:

  - BIBD/BIU, Bíldudalur Airport, Bíldudalur, Westfjords, IS: name changed from "Bildudalur Airport", city changed from
    "Bildudalur".
  - BIBL/BLO, Hjaltabakki Airport, Blönduós, Northwest, IS: city changed from "Blonduos".
  - BIBV/BXV, Breiðdalsvík Airport, Breiðdalsvík, East, IS: name changed from "Breiddalsvik Airport", city changed from
    "Breiddalsvik".
  - BIDV/DJU, Djúpivogur Airport, Djúpivogur, East, IS: name changed from "Djupivogur Airport", city changed from
    "Djupivogur".
  - BIEG/EGS, Egilsstaðir Airport, Egilsstaðir, East, IS: name changed from "Egilsstadir Airport", city changed from
    "Egilsstadir".
  - BIFM/FAG, Fagurhólsmýri Airport, Fagurhólsmýri, East, IS: name changed from "Fagurholsmyri Airport", city changed
    from "Fagurholsmyri".
  - BIGF/GUU, Grundarfjörður Airport, Grundarfjörður, West, IS: name changed from "Grundarfjordur Airport", city changed
    from "Grundarfjordur".
  - BIGJ/GJR, Gjögur Airport, Gjögur, Westfjords, IS: name changed from "Gjogur Airport", city changed from "Gjogur".
  - BIGR/GRY, Grímsey Airport, Grímsey, Northeast, IS: name changed from "Grimsey Airport", city changed from "Grimsey".
  - BIHK/HVK, Hólmavík Airport, Hólmavík, Westfjords, IS: name changed from "Holmavik Airport", city changed from
    "Holmavik".
  - BIHN/HFN, Hornafjörðu Airport, Höfn, East, IS: name changed from "Hornafjordur Airport", city changed from
    "Hornafjordur".
  - BIHU/HZK, Húsavík Airport, Húsavík, Northeast, IS: name changed from "Husavik Airport", city changed from "Husavik".
  - BIIS/IFJ, Ísafjörður Airport, Ísafjörður, Westfjords, IS: name changed from "Isafjordur Airport", city changed from
    "Isafjordur".
  - BIKP/OPA, Kópasker Airport, Kópasker, Northeast, IS: name changed from "Kopasker Airport", city changed from
    "Kopasker".
  - BIKR/SAK, Sauðárkrókur Airport, Sauðárkrókur, Northwest, IS: name changed from "Saudarkrokur Airport", city changed
    from "Saudarkrokur".
  - BINF/NOR, Norðfjörður Airport, Norðfjörður, East, IS: name changed from "Nordfjordur Airport", city changed from
    "Nordfjordur".
  - BIOF/OFJ, Ólafsfjörður Airport, Ólafsfjörður, Northeast, IS: name changed from "Olafsfjordur Airport", city changed
    from "Olafsfjordur".
  - BIRG/RFN, Raufarhöfn Airport, Raufarhöfn, Northeast, IS: name changed from "Raufarhofn Airport", city changed from
    "Raufarhofn".
  - BIRL/MVA, Mývatn Airport, Reykjahlíð, Northeast, IS: name changed from "Reykjahlid Airport", city changed from
    "Myvatn".
  - BISI/SIJ, Siglufjörður Airport, Siglufjörður, Northeast, IS: name changed from "Siglufjordur Airport", city changed
    from "Siglufjordur".
  - BIST/SYK, Stykkishólmur Airport, Stykkishólmur, West, IS: name changed from "Stykkisholmur Airport", city changed
    from "Stykkisholmur".
  - BITE/TEY, Þingeyri (Thingeyri) Airport, Þingeyri, Westfjords, IS: name changed from "Tingeyri Airport", city changed
    from "Tingeyri".
  - BITN/THO, Þórshöfn (Thorshofn) Airport, Þórshöfn, Northeast, IS: name changed from "Thorshofn Airport", city changed
    from "Thorshofn".
  - BIVO/VPN, Vopnafjörður Airport, Vopnafjörður, East, IS: name changed from "Vopnafjordur Airport", city changed from
    "Vopnafjordur".
  - DAOI/CFK, Chlef Aboubakr Belkaid Airport, Chlef, Chlef, DZ: name changed from "Aboubakr Belkaid Chlef Airport",
    latitude changed from 36.217 to 36.216828, longitude changed from 1.34 to 1.340739.
  - FLND    , Peter Zuze Air Force Base, Ndola, Copperbelt, ZM: name changed from "Ndola Airport".
  - FZGA/LIQ, Lisala Airport, Lisala, Mongola, CD: city added, subd changed from "Equateur", latitude changed from
    2.17066 to 2.170984, longitude changed from 21.4969 to 21.497129, tz changed from "Africa/Kinshasa" to
    "Africa/Lubumbashi".
  - LFSL/BVE, Brive Souillac Airport, Nespouls, Nouvelle-Aquitaine, FR: city changed from "Limousin".
  - LPAR    , Alverca Airport, Alverca, Lisbon, PT: city changed from "Alverca do Ribatejo", subd changed from "Lisboa",
    latitude changed from 38.8833 to 38.885362, longitude changed from -9.0301 to -9.028311.
  - LPCB    , Castelo Branco Airport, Castelo Branco, Castelo Branco, PT: city added.
  - OENG/EAM, Nejran Airport, Nejran, Najran, SA: city added, subd added, elevation changed from 3982 to 3983.
  - OIAG/AKW, Aghajari Airport, Omidiyeh, Khuzestan, IR: city added.
  - RPMR/GES, General Santos International Airport, General Santos, Soccsksargen, PH: name changed from "Tambler
    Prinipal Airport", city changed from "South Cotabato".
  - RPMY/CGY, Laguindingan Intl, Laguindingan, Northern Mindanao, PH: city changed from "Cagayan de Oro".
  - SBSV/SSA, Deputado Luiz Eduardo Magalhaes International Airport, Salvador, Bahia, BR: latitude changed from
    -12.90861 to -12.908624, longitude changed from -38.3225 to -38.32288.
  - SNLB    , Fazenda Magdalena, Lábrea, Bahia, BR: name changed from "Livramento do Brumado Airport", city changed from
    "Livramento Do Brumado", elevation changed from 1559 to 466, latitude changed from -13.6506 to -9.203056, longitude
    changed from -41.8339 to -65.708611, tz changed from "America/Bahia" to "America/Manaus".
  - SSLI    , Fazenda Nova Piuva, Aquidauana, Mato Grosso do Sul, BR: name changed from "Estancia Portal do Sol
    Airport", city changed from "Itirapina", subd changed from "São Paulo", elevation changed from 2425 to 499, latitude
    changed from -22.16528 to -19.864331, longitude changed from -47.89278 to -55.512951, tz changed from
    "America/Sao_Paulo" to "America/Campo_Grande".
  - SSOU/AIR, Aripuanã Airport, Aripuanã, Mato Grosso, BR: subd changed from "Minas Gerais".
  - UBBA    , Akstafa Airport, Akstafa, Ağstafa, AZ: subd changed from "Agstafa".
  - UBBB/GYD, Heydar Aliyev International Airport, Baku, Bakı, AZ: subd changed from "Baki".
  - UBBG/GNJ, Ganja Airport, Ganja, Gəncə-City, AZ: subd changed from "Goygol-Rayon".
  - UBBN/NAJ, Nakhchivan Airport, Nakhchivan, Naxçıvan Muxtar Respublikası, AZ: subd changed from "Nakhichevan".
  - UBBZ/ZZE, Zangilan International Airport, Zangilan, Zəngilan, AZ: subd changed from "Zangilan".
  - VAOZ/ISK, Ozar Airport, Nasik, Maharashtra, IN: name changed from "Ozar Air Force Station".
  - VEAT/IXA, Agartala Airport, Agartala, Tripura, IN: elevation changed from 46 to 56, latitude changed from 23.887 to
    23.890667, longitude changed from 91.2404 to 91.239333.
  - VILD/LUH, Ludhiana Airport, Ludhiana, Punjab, IN: city added, latitude changed from 30.8547 to 30.855833, longitude
    changed from 75.9526 to 75.950556.
  - VNPK/PKR, Pokhara Airport, Pokhara, Western Region, NP: elevation changed from 2712 to 2696.
  - VRMO/GKK, Kooddoo Airport, Kooddoo, Gaafu Alifu Atoll, MV: subd changed from "Gaaf Alif", latitude changed from
    0.73333 to 0.733078, longitude changed from 73.43417 to 73.434202.
  - WAJJ/DJJ, Sentani International Airport, Jayapura-Papua Island, Papua, ID: name changed from "Sentani Airport".
  - WIEE/PDG, Minangkabau Airport, Ketaping/Padang-Sumatra Island, West Sumatra, ID: subd changed from "Ketaping".
  - WIMG    , Sutan Sjahrir Air Force Base, Padang-Sumatra Island, , ID: name changed from "Tabing Airport".
  - YGDW    , Granite Downs Airport, , South Australia, AU: elevation changed from 337 to 1122.
  - YMES    , RAAF Base East Sale, East Sale, Victoria, AU: city added.
  - YPKG/KGI, Kalgoorlie-Boulder Airport, Kalgoorlie, Western Australia, AU: name changed from "Kalgoorlie Boulder
    Airport", latitude changed from -30.7894 to -30.789444, longitude changed from 121.462 to 121.461667.
  - YTGT/GTS, The Granites Airport, The Granites, Northern Territory, AU: city added, elevation changed from 0 to 1299.
  - YWSL/SXE, West Sale Airport, West Sale, Victoria, AU: city added.
  - ZKPY/FNJ, Pyongyang International Airport, Pyongyang, South Pyongan, KP: name changed from "Sunan International
    Airport".
  - ZUTR/TEN, Tongren Fenghuang Airport, , Guizhou, CN: elevation changed from 0 to 2313.
  - _KBH/KBH, Buzwagi Airport, Kahama, Shinyanga, TZ: name changed from "Buzwagi", lid added to "TZ-0146".

* Removed the following 14 airports:

  - BIPA/PFJ, Patreksfjordur Airport, Patreksfjordur, Westfjords, IS.
  - ENSA    , Svea Airport, Svea, Svalbard, NO.
  - EPBP/BXP, Biala Podlaska Airport, Biala Podlaska, Lublin, PL.
  - ETEJ    , Bamberg-Breitenau Airport, Bamberg, Bayern, DE.
  - ETIN/KZG, Kitzingen Army Air Field, , Bayern, DE.
  - LFBV    , Brive-La Roche Airport, Brive-la-Gaillarde, Nouvelle-Aquitaine, FR.
  - MDSB    , Sabana de Mar Airport, Sabana de Mar, Hato-Mayor, DO.
  - OEDW/DWD, Dawadmi Domestic Airport, Dawadmi, Ar-Riyaḑ, SA.
  - SKIO    , Cicuco Airport, Limon, Bolivar, CO.
  - VDKT    , Kratie Airport, Kratie, Kratie, KH.
  - VLSN/NEU, Sam Neua Airport, , Houaphan, LA.
  - WALV/BYQ, Bunyu Airport, Bunju Island, North Kalimantan, ID.
  - WRKB    , Padhameleda Airport, Bajawa-Flores Island, East Nusa Tenggara, ID.
  - ZLJN/JNG, Jining Qufu Airport, Jining, Shandong, CN.


Version 20250811
================
* Updated IATA for the following 2 airports:

  - EPSY/SZY, Olsztyn-Mazury Airport, Szymany, Warmia-Mazury, PL: iata added.
  - UCFM/BSZ, Manas International Airport, Bishkek, Chuey, KG: iata changed from "FRU" [effective 09-Aug-2025].

* Updated other data for the following 11 airports:

  - LECH/CDT, Castellón Airport, Castellón de la Plana, Comunidad Valenciana, ES: name changed from "Castellongitude de
    la Plana Airport", subd changed from "Castellón".
  - LECN    , Castellón De La Plana Airport, Castellón de La Plana, Comunidad Valenciana, ES: name changed from
    "Castellongitude De La Plana Airport", city changed from "Castellongitude de La Plana".
  - VDBG/BBM, Battambang Airport, Battambang, Battambang, KH: subd added.
  - VDKC    , Kompong Cham Airport, Kompong Cham, Kampong Cham, KH: subd changed from "Kampong-Cham".
  - VDKH/KZC, Kampong Chhnang Airport, , Kampong Chhnang, KH: subd changed from "Kampong-Chhnang".
  - VDKK/KKZ, Kaoh Kong Airport, Kaoh Kong, Koh Kong, KH: subd changed from "Koh-Kong".
  - VDPP/PNH, Phnom Penh International Airport, Phnom Penh, Phnom Penh, KH: subd added.
  - VDSA/SAI, Siem Reap Angkor International Airport, Siem Reap, Siem Reap, KH: subd changed from "Siem-Reap".
  - VDSR    , Angkor International Airport, Siem Reap, Siem Reap, KH: subd changed from "Siem-Reap".
  - VDST/TNX, Stung Treng Airport, Stung Treng, Stung Treng, KH: subd changed from "Stung-Treng".
  - VDTI/KTI, Techo International Airport, Krong Ta Khmau, Kandal, KH: city changed from "Phnom Penh".

* Updated pre-commit.config.yaml (internal)

Version 20250706
================
* Updated IATA for the following 1 airports:

  - EPSY/SZY, Olsztyn-Mazury Airport, Szymany, Warmia-Mazury, PL: iata added. Reported by `cosypanther
    <https://github.com/cosypanther >`__ in issue `#45 <https://github.com/mborsetti/airportsdata/issues/45>`.


Version 20250622
================
* Added the following 2 airports:

  - LTDB/COV, Çukurova International Airport, Tarsus, Mersin, TR.
  - TVSA/SVD, Argyle International Airport, Argyle, Saint-George, VC.

* Updated other data for the following 16 airports:

  - BGGH/GOH, Nuuk Airport, Nuuk, Sermersooq, GL: name changed from "Godthaab / Nuuk Airport", subd added, latitude
    changed from 64.1909 to 64.1910, longitude changed from -51.6781 to -51.6780.
  - BGJN/JAV, Ilulissat Airport, Ilulissat, Avannaata, GL: subd added.
  - BGMQ/JSU, Maniitsoq Airport, Maniitsoq, Qeqqata, GL: subd added.
  - BGPT/JFR, Paamiut Airport, Paamiut, Sermersooq, GL: subd added.
  - BGQQ/NAQ, Qaanaaq Airport, Qaanaaq, Avannaata, GL: subd added.
  - BGSS/JHS, Sisimiut Airport, Sisimiut, Qeqqata, GL: subd added.
  - BGUK/JUV, Upernavik Airport, Upernavik, Avannaata, GL: subd added.
  - BGUQ/JQA, Qaarsut Airport, Uummannaq, Avannaata, GL: subd added.
  - DT70    , Medenine Airport, Medenine, Medenine, TN: subd changed from "Madanin".
  - DTKA/TBJ, Tabarka 7 Novembre Airport, Tabarka, Jendouba, TN: subd changed from "Jundubah".
  - DTNH/NBE, Enfidha-Hammamet International Airport, Enfidha, Sousse, TN: name changed from "Enfidha Zine El Abidine
    Ben Ali International Airport", subd changed from "Susah".
  - DTTB    , Bizerte-Sidi Ahmed Air Base, Sidi Ahmed, Bizerte, TN: name changed from "Sidi Ahmed Air Base", subd
    changed from "Banzart".
  - DTTG/GAE, Gabes Matmata International Airport, Gabès, Gabès, TN: city changed from "Gabes", subd changed from
    "Qabis".
  - DTTJ/DJE, Djerba Zarzis International Airport, Djerba, Medenine, TN: subd changed from "Madanin".
  - DTTX/SFA, Sfax Thyna International Airport, Sfax, Sfax, TN: subd changed from "Safaqis".
  - DTTZ/TOE, Tozeur Nefta International Airport, Tozeur, Tozeur, TN: subd changed from "Tawzar".

* Removed the following 1 airports:

  - TVSV/SVD, E. T. Joshua Airport, Kingstown, Saint-George, VC.


Version 20250523
================
* Removed LPCV/COV, Covilha Airport, , Castelo Branco, PT, closed and destroyed. Reported by `Andrii
  <https://github.com/AndriyKy>`__ in issue `#159 <https://github.com/mwgg/Airports/issues/159>`__ upstream.
* Changed ICAO of Nairobi's Enfidha airport from DTNZ (incorrect) to DTNH. Reported by `daman2k
  <https://github.com/daman2k>`__ in issue `#161 <https://github.com/mwgg/Airports/issues/161>`__ upstream.
* Mega-contribution by `Maxine Fonua <https://github.com/maxinefonua>`__ in issue `#44
  <https://github.com/mborsetti/airportsdata/issues/44>`, removing the following 35 airports confirmed as closed (via
  Google maps):

  - AGKW/KWS, Kwailabesi Airport, Kwailabesi, , SB.
  - CYXD/YXD, Edmonton City Centre (Blatchford Field) Airport, Edmonton, Alberta, CA.
  - DNTZ/NBE, Enfidha Zine El Abidine Ben Ali International Airport, Enfidha, Susah, TN.
  - EDWD/XLW, Lemwerder Airport, Lemwerder, Bremen, DE.
  - EFHF/HEM, Helsinki Malmi Airport, Helsinki, Uusimaa, FI.
  - EGCN/DSA, Robin Hood Doncaster Sheffield Airport, Doncaster, England, GB.
  - EGDL/LYE, RAF Lyneham, Lyneham, England, GB.
  - EGHD/PLH, Plymouth City Airport, Plymouth, England, GB.
  - EGPM/SCS, Scatsta Airport, Shetland Islands, Scotland, GB.
  - EGTG/FZO, Bristol Filton Airport, Bristol, England, GB.
  - EYPP/PNV, Panevezys Air Base, Panevezys, Panevezys, LT.
  - FWUU/ZZU, Mzuzu Airport, Mzuzu, Northern Region, MW.
  - LBSZ/SZR, Stara Zagora Airport, Stara Zagora, Khaskovo, BG.
  - LIPT/VIC, Vicenza Airport, Vicenza, Veneto, IT.
  - LLET/ETH, Eilat Airport, Eilat, Southern District, IL.
  - LLSD/SDV, Sde Dov Airport, Tel Aviv, Tel-Aviv, IL.
  - MHLE/LEZ, La Esperanza Airport, La Esperanza, Intibuca, HN.
  - NFNV/VAU, Vatukoula Airport, Vatukoula, Western, FJ.
  - NZTS/THH, Taharoa Aerodrome, Taharoa, Waikato, NZ.
  - RKJU/CHN, Jeon Ju Airport, Jeon Ju, Jeollabuk-do, KR.
  - RPLP/LGP, Legazpi City International Airport, Legazpi City, Bicol, PH.
  - SIXD/LVB, Fazenda da Paz Airport, Santana Do Livramento, Rio Grande do Sul, BR.
  - SKAN/ADN, Andes Airport, Andes, Antioquia, CO.
  - UKOH/KHE, Kherson International Airport, Kherson, Khersonska oblast, UA.
  - UMMM/MHP, Minsk 1 Airport, Minsk, , BY.
  - UWKJ/JOK, Yoshkar-Ola Airport, Yoshkar-Ola, Mariy-El, RU.
  - UWSS/RTW, Saratov Central Airport, Saratov, Saratov, RU.
  - VARK/RAJ, Rajkot Airport, Rajkot, Gujarat, IN.
  - VGCM/CLA, Comilla Airport, Comilla, Chittagong, BD.
  - VGSG/TKR, Thakurgaon Airport, Thakurgaon, Rangpur-Division, BD.
  - VYNT/NMT, Namtu Airport, Namtu, Shan, MM.
  - WADA/AMI, Selaparang Airport, Mataram-Lombok Island, West Nusa Tenggara, ID.
  - WIIG/PPJ, Pulau Panjang Airport, Tjipara-Java Island, Jakarta, ID.
  - YGLG/GEX, Geelong Airport, , Victoria, AU.
  - ZUDX/DAX, Dachuan Airport, Dazhou, Sichuan, CN.

* Also removed IATA from the following 14 airports, who no longer have commercial service:

  - CYKZ    , Toronto / Buttonville Municipal Airport, Markham, Ontario, CA: iata changed from "YKZ".
  - DNAK    , Akure Airport, Akure, Ondo, NG: iata changed from "AKR".
  - EDRZ    , Zweibrucken Airport, Zweibrucken, Rheinland-Pfalz, DE: iata changed from "ZQW".
  - EDWB    , Bremerhaven Airport, Bremerhaven, Bremen, DE: iata changed from "BRV".
  - EGMH    , Kent International Airport, Manston, England, GB: iata changed from "MSE".
  - FAPG    , Plettenberg Bay Airport, Plettenberg Bay, Western Cape, ZA: iata changed from "PBZ".
  - KBDH    , Willmar Municipal/John L Rice Field, Willmar, Minnesota, US: iata changed from "ILL".
  - LLOV    , Ovda International Airport, Eilat, Southern District, IL: iata changed from "VDA".
  - TAPH    , Codrington Airport, Codrington, Barbuda, AG: iata changed from "BBQ".
  - UKON    , Mykolaiv International Airport, Mykolaiv, Mykolaivska oblast, UA: iata changed from "NLV".
  - VDSR    , Angkor International Airport, Siem Reap, Siem-Reap, KH: iata changed from "REP".
  - VNMN    , Mahendranagar Airport, Mahendranagar, Far-Western, NP: iata changed from "XMG".
  - VVNT    , Nha Trang Air Base, Nha Trang, Khanh-Hoa, VN: iata changed from "NHA".
  - ZLSN    , Xiguan Airport, Xi'an, Shaanxi, CN: iata changed from "SIA".


Version 20250224
================
* Support for Python 3.9 has been dropped. As a reminder, older Python versions are supported for 3
  years after being superseded by a new major release (i.e. approximately 4 years after their initial release).
* Added Garowe airport, contributed by `nprihodko <https://github.com/nprihodko>`__ in PR `#43
  <https://github.com/mborsetti/airportsdata/issues/43>`__, validated and modified using ARINC data.
* One addition and various fixes for Portugal based on upstream PR, official eAIP, and official ISO-3166-2 subdivision
  names.
* Additions based on upstream PRs, including

  - Mollis Airport has a new ICAO identifier: LSZM, formerly used for the French part of EuroAirport Basel Mulhouse
    Freiburg.
  - French part of the EuroAirport Basel Mulhouse Freiburg lost its separate ICAO identifier, and is identified in this
    database using the pseudo-identifier of _MLH
* Implemented IATA code changes

Summary of changes
------------------
* Added the following 34 airports:

  - ESKS/SCR, Sälen/Scandinavian Mountains Airport, Rörbäcksnäs, Dalarna, SE.
  - FLSK/NLA, Simon Mwansa Kapwepwe International Airport, Ndola, Copperbelt, ZM.
  - HCMW/GGR, Garowe Airport, Garowe, Nugaal, SO.
  - HECP/CCE, Capital International Airport, New Administrative Capital, Cairo, EG.
  - KCGA/CGA, Craig Seaplane Base, Craig, Alaska, US.
  - KHYL/HYL, Clark Bay Seaplane Base, Hollis, Alaska, US.
  - KKAE/KAE, Kake Seaplane Base, Kake, Alaska, US.
  - KKWP/KWP, West Point Village Seaplane Base, West Point, Alaska, US.
  - KW39/RCE, Roche Harbor Seaplane Base, Roche Harbor, Washington, US.
  - LERL/CQM, Ciudad Real International Airport, Ciudad Real, Castilla–La Mancha, ES.
  - LPCB    , Castelo Branco Airport, , Castelo Branco, PT.
  - RPLK/DRP, Legazpi Bicol International Airport, Daraga, Albay, PH.
  - RPSP/TAG, Panglao Bohol International Airport, Panglao, Bohol, PH.
  - UTAE/KEA, Kerki International Airport, Kerki, Lebap, TM.
  - VRAH/HRF, Hoarafushi Airport, Hoarafushi, Haa Alif Atoll, MV.
  - VRCF/FND, Funadhoo Airport, Funadhoo, Shaviyani Atoll, MV.
  - VRQM/RUL, Maavaarulaa Airport, Gadhdhoo, Gaafu Dhaalu Atoll, MV.
  - WAQC/RTU, Maratua Airport, Maratua Island, North-Kalimantan, ID.
  - ZGCZ/HCZ, Chenzhou Beihu Airport, Chenzhou, Hunan, CN.
  - ZGYY/YYA, Yueyang Sanhe Airport, Yueyang, Hunan, CN.
  - ZHXY/XAI, Xinyang Minggang Airport, Xinyang, Henan, CN.
  - ZLHB/HBQ, Haibei Qilian Airport, Haibei, Qinghai, CN.
  - ZLLN/LNL, Longnan Chengxian Airport, Longnan, Gansu, CN.
  - ZSWA/WHA, Wuhu Xuanzhou Airport, Wuhu, Anhui, CN.
  - ZSYH/YHJ, Nanchang Yaohu Airport, Nanchang, Jiangxi, CN.
  - ZUBZ/BZX, Bazhong Enyang Airport, Bazhong, Sichuan, CN.
  - ZUGZ/GZG, Garze Gesar Airport, Garze, Sichuan, CN.
  - ZUWL/CQW, Wulong Chongqing Xiannvshan Airport, Wulong, Chongqing, CN.
  - ZUWS/WSK, Wushan Chongqing Airport, Wushan, Chongqing, CN.
  - ZWRQ/RQA, Ruoqiang Loulan Airport, Ruoqiang, Xinjiang, CN.
  - ZWTS/TWC, Tumxuk Tangwangcheng Airport, Tumxuk, Xinjiang, CN.
  - ZWYT/YTW, Yutian Wanfang Airport, Yutian, Xinjiang, CN.
  - _DEQ/DEQ, Deqing Moganshan Airport, Deqing, Zhejiang, CN.
  - _MLH/MLH, EuroAirport Basel-Mulhouse-Freiburg Airport, Saint-Louis, Haut-Rhin, FR.

* Updated IATA (and potentially other data) for the following 12 airports:

  - 2TE0/BZT, Eagle Air Park, Brazoria, Texas, US: iata added.
  - FIMA/AHG, Agalega Island Airstrip, Vingt Cinq, Agalega-Islands, MU: iata added.
  - FLND    , Ndola Airport, Ndola, Copperbelt, ZM: iata changed from "NLA" (NLA is now at Simon Mwansa Kapwepwe
    International Airport, just added)
  - KEDC/EDC, Austin Executive Airport, Austin, Texas, US: iata added.
  - KGYY/GYY, Gary/Chicago International Airport, Gary, Indiana, US: iata added.
  - KHSG/THP, Hot Springs County Airport, Thermopolis, Wyoming, US: iata added.
  - LPMR/QLR, Monte Real Airport, Monte Real, Leiria, PT: iata added, city added.
  - LSMP/VIP, Payerne Airport, Payerne, Vaud, CH: iata added, city added.
  - MYEY/TCV, Torch Cay Airport, Hog Cay, Exuma, BS: iata added, name changed from "Hog Cay Airport".
  - NV65/DRA, Desert Rock Airport, Mercury, Nevada, US: iata added.
  - SNCL/MXQ, Lorenzo Airport, Cairu, Bahia, BR: iata added.

* Updated other data for the following 58 airports:

  - HCMH/HGA, Egal International Airport, Hargeisa, Woqooyi Galbeed, SO: subd changed from "Woqooyi-Galbeed".
  - HCMI/BBO, Berbera Airport, Berbera, Woqooyi Galbeed, SO: subd changed from "Woqooyi-Galbeed".
  - HCMK/KMU, Kisimayu Airport, , Lower Juba, SO: subd changed from "Lower-Juba".
  - HDAS/AII, Ali-Sabieh Airport, Ali-Sabieh, Ali Sabieh, DJ: subd changed from "Ali-Sabieh".
  - HDCH    , Chabelley Airport, Chabelley, Ali Sabieh, DJ: subd changed from "Ali-Sabieh".
  - HE26    , Wadi Abu Shihat, , Red Sea, EG: subd changed from "Red-Sea".
  - HEDK/DAK, Dakhla Airport, , New Valley, EG: subd changed from "New-Valley".
  - HEGN/HRG, Hurghada International Airport, Hurghada, Red Sea, EG: subd changed from "Red-Sea".
  - HEGO    , El Gouna Airport, El Gouna, Red Sea, EG: subd changed from "Red-Sea".
  - HEKG/UVL, El Kharga Airport, , New Valley, EG: subd changed from "New-Valley".
  - HEMA/RMF, Marsa Alam International Airport, Marsa Alam, Red Sea, EG: subd changed from "Red-Sea".
  - HEMK/HMB, Sohag International Airport, Sohag, New Valley, EG: subd changed from "New-Valley".
  - HEOW/GSQ, Shark El Oweinat International Airport, , New Valley, EG: subd changed from "New-Valley".
  - HEPS/PSD, Port Said Airport, Port Said, Port Said, EG: subd changed from "Port-Said".
  - HHSB/ASA, Assab International Airport, Assab, Southern Red Sea, ER: city changed from "Asab", subd added.
  - HHTS/TES, Teseney Airport, Teseney, Gash-Barka, ER: name changed from "Tessenei Airport", city changed from
    "Tessenei", subd added.
  - LFKH    , St Jean D'Avelanne Airport, Saint-Jean-d'Avelanne, Pont-de-Beauvoisin, Auvergne-Rhone-Alpes, FR: name
    changed from "St Jean D'avelanne Airport", city changed from "Figari/Sud Corse".
  - LP77    , Santa Margarida Airport, , Santarém, PT: subd changed from "Santarem".
  - LPAR    , Alverca Airport, Alverca do Ribatejo, Lisboa, PT: city added, subd changed from "Lisbon".
  - LPAV    , Aveiro Airport, Aveiro, Aveiro, PT: city added.
  - LPAZ/SMA, Santa Maria Airport, Vila do Porto, Açores, PT: subd changed from "Azores".
  - LPBG/BGC, Braganca Airport, Bragança, Bragança, PT: city added, subd changed from "Braganca".
  - LPCH/CHV, Chaves Airport, Chaves, Vila Real, PT: subd changed from "Vila-Real".
  - LPCO/CBP, Coimbra Airport, Antanhol, Coimbra, PT: city added.
  - LPCR/CVU, Corvo Airport, Corvo, Açores, PT: subd changed from "Azores", elevation changed from 0 to 61.
  - LPCS/CAT, Cascais Airport, Cascais, Lisboa, PT: city added, subd changed from "Lisbon", elevation changed from 325
    to 326.
  - LPCV/COV, Covilha Airport, , Castelo Branco, PT: subd changed from "Castelo-Branco".
  - LPEV    , Évora Airport, Évora, Alentejo, PT: name changed from "Evora Airport", city added, subd changed from
    "Evora".
  - LPFL/FLW, Flores Airport, Santa Cruz das Flores, Açores, PT: subd changed from "Azores", elevation changed from
    112 to 108.
  - LPGR/GRW, Graciosa Airport, Santa Cruz da Graciosa, Açores, PT: subd changed from "Azores".
  - LPHR/HOR, Horta Airport, Horta, Açores, PT: subd changed from "Azores", elevation changed from 118 to 117.
  - LPIN    , Espinho Airport, Espinho, Porto, PT: city added.
  - LPJO    , Alijo Airport, Alijo, Vila Real, PT: subd changed from "Vila-Real".
  - LPLA/TER, Lajes Field, Lajes, Açores, PT: subd changed from "Azores", elevation changed from 180 to 193.
  - LPMA/FNC, Madeira Airport, Funchal, Madeira, PT: elevation changed from 192 to 191.
  - LPMF    , Monfortinho Airport, Monfortinho, Castelo Branco, PT: subd changed from "Castelo-Branco".
  - LPMI    , Mirandela Airport, Mirandela, Bragança, PT: subd changed from "Braganca".
  - LPMO    , Montargil Airport, Montargil, Évora, PT: subd changed from "Evora".
  - LPMT    , Montijo Airport, Montijo, Setúbal, PT: subd changed from "Setubal".
  - LPMU    , Mogadouro Airport, Mogadouro, Bragança, PT: subd changed from "Braganca".
  - LPOV    , Ovar Airport, Ovar, Aveiro, PT: city added.
  - LPPD/PDL, João Paulo II Airport, Ponta Delgada, Açores, PT: name changed from "Joao Paulo II Airport", subd changed
    from "Azores".
  - LPPI/PIX, Pico Airport, Pico Island, Açores, PT: subd changed from "Azores", elevation changed from 109 to 114.
  - LPPM/PRM, Portimão Airport, Portimão, Faro, PT: name changed from "Portimao Airport", city added.
  - LPPR/OPO, Francisco de Sá Carneiro Airport, Porto, Porto, PT: name changed from "Francisco de Sa Carneiro Airport",
    elevation changed from 228 to 227.
  - LPPS/PXO, Porto Santo Airport, Porto Santo, Madeira, PT: city changed from "Vila Baleira", elevation changed from
    341 to 340.
  - LPPT/LIS, Lisbon Portela Airport, Lisbon, Lisbon, PT: elevation changed from 374 to 355.
  - LPPV    , Praia Verde 23M Airport, Castro Marim, Faro, PT: city added.
  - LPSI/SIE, Sines Airport, Sines, Setúbal, PT: city added, subd changed from "Setubal".
  - LPSJ/SJZ, Sao Jorge Airport, Velas, Açores, PT: subd changed from "Azores".
  - LPSR    , Santarem Airport, Santarem, Santarém, PT: subd changed from "Santarem".
  - LPTN    , Tancos Airport, , Santarém, PT: subd changed from "Santarem".
  - LPVR/VRL, Vila Real Airport, Vila Real, Vila Real, PT: city added, subd changed from "Vila-Real", elevation changed
    from 1805 to 1832.
  - LPVZ/VSE, Viseu Airport, Viseu, Viseu, PT: city added.
  - LSZM    , Mollis Airport, Mollis, Glarus, CH: changed ICAO from LSZM; LSZM was used for the French side of
    EuroAirport Basel-Mulhouse-Freiburg Airport, airport that now has a single identifier.
  - MMSM/NLU, Felipe Angeles International Airport, Reyes Acozac, Mexico, MX: name changed from "Santa Lucia Air Force
    Base".
  - UTAV/CRZ, Turkmenabat International Airport, Turkmenabat, Lebap, TM: name changed from "Turkmenabat Airport", subd
    added.
  - ZGWZ/WUZ, Wuzhou Xijiang Airport, Wuzhou, Guangxi, CN: name changed from "Changzhoudao Airport", latitude changed
    from 23.4567 to 23.401389, longitude changed from 111.248 to 111.098611.
  - ZUYB/YBP, Yibin Wuliangye  Airport, Yibin, Sichuan, CN: name changed from "Yibin Caiba Airport", elevation changed
    from 924 to 1378, latitude changed from 28.80056 to 28.858, longitude changed from 104.545 to 104.525.

* Removed the following airport:

  - RPVT/TAG, Tagbilaran Airport, Tagbilaran City, Central Visayas, PH.



Version 20241001
================
* Contributions by `niclaswue
  <https://github.com/niclaswue>`__ in PRs `#40 <https://github.com/mborsetti/airportsdata/issues/40>`__, validated and
  modified using ARINC data:

  - DTNH/NBE, Enfidha–Hammamet International Airport, Enfidha, Sousse, TN (old ICAO code was DNTZ).
  - ESKS/SCR, Sälen/Scandinavian Mountains Airport, Rörbäcksnäs, Dalarna, SE.
  - LTCU/BGG, Bingöl Airport, Çeltiksuyu, Bingöl, TR.
  - LTCV/NKT, Şırnak Şerafettin Elçi Airport, Cizre, Şırnak, TR.
  - UTFF/FEG, Fergana Airport, Fergana, Fergana Region, UZ.

* Additional airports (added upstream):

  - OERS/RSI, Red Sea International Airport, Hanak, Tabuk, SA.
  - VTSY/BTZ, Yala Betong International Airport, Yarom, Yala, TH.
  - ZBSG/SZH, Shuozhou Zirun Airport, Shuozhou, Shanxi, CN.
  - ZSJG/JNG, Jining Da'an Airport, Jining, Shandong, CN.
  - ZWAL/ACF, Aral Talim Airport, Aral, Xinjiang, CN.

* Added IATA codes to the following airports:

  - CPV8/KEW, Keewaywin Airport, Keewaywin, Ontario, CA.
  - CTK6/ZKG, Kegaska Airport, Kegaska, Quebec, CA.
  - SBCD/CFC, Cacador Airport, Cacador, Santa Catarina, BR.
  - YWHI/WSY, Whitsunday Island Airport, , Queensland, AU.

* Removed IATA codes from the following 2 airports:

  - LTBE    , Bursa Airport, Bursa, Bursa, TR (BTZ is now VTSY).
  - YBAF    , Brisbane Archerfield Airport, Brisbane, Queensland, AU (ACF is now ZWAL).

* Removed the following 3 airports:

  - ULBC    , Cherepovets Airport, Cherepovets, Vologda, RU (new ICAO code is ULWC, already in database).
  - UTKF/FEG, Fergana Airport, Fergana, Fergana, U (new ICAO code is UTFF, already in database)
  - ZLJN/JNG, Jining Qufu Airport, Jining, Shandong, CN (closed on 28 December 2023).

Version 20240806
================
* Added K6N7/NYS, New York Skyports Inc Seaplane Base, New York, New York, US. Contributed by `maidough
  <https://github.com/maidough>`__ in PRs `#132 <https://github.com/mwgg/Airports/pull/132>`__, validated and modified
  using FAA data.


Version 20240728
================
* Added 40 new airports and fixed 56 ones:

  - Multiple additions and fixes contributed by `eatdostacos <https://github.com/eatdostacos>`__ in PRs `#119
    <https://github.com/mwgg/Airports/pull/119>`__, `#120  <https://github.com/mwgg/Airports/pull/120>`__, `#121
    <https://github.com/mwgg/Airports/pull/121>`__ and `#125 <https://github.com/mwgg/Airports/pull/125>`__, `Leon Brown
    <https://github.com/OBrown92>`__ in PR `#126 <https://github.com/mwgg/Airports/pull/126>` and `ezzaze
    <https://github.com/ezzaze>`__ in PR `#128  <https://github.com/mwgg/Airports/pull/128>`__ upstream, validated.
  - Fixed multiple Canadian airport names using NavCanada data from https://open.canada.ca/.
  - Added multiple IATA codes from airline database.

Detail of changes
-----------------
* Added the following 40 airports:

  - FNBJ/NBJ, Dr. Antonio Agostinho Neto International Airport, Luanda, Luanda, AO.
  - LTFO/RZV, Rize–Artvin Airport, , Rize, TR.
  - MMTL/TQO, Felipe Carrillo Puerto International Airport, Tulum, Quintana-Roo, MX.
  - UBBZ/ZZE, Zangilan International Airport, Zangilan, Zangilan, AZ.
  - VAHS/HSR, Rajkot International Airport, Rajkot, Gujarat, IN.
  - VDTI/KTI, Techo International Airport, Phnom Penh, Kandal, KH.
  - VEAH/AZH, Azamgarh Airport, Azamgarh, Uttar Pradesh, IN.
  - VECT/CWK, Chitrakoot Airport, Chitrakoot, Uttar Pradesh, IN.
  - VEHO/HGI, Donyi Polo Airport, Itanagar, Arunachal Pradesh, IN.
  - VEPY/PYG, Pakyong Airport, Pakyong, Sikkim, IN.
  - VERL    , Raxaul Airport, , Bihar, IN.
  - VIND/DXN, Noida International Airport, Noida, Uttar Pradesh, IN.
  - VISV/VSV, Shravasti Airport, Shravasti, Uttar Pradesh, IN.
  - VOKU/KJB, Kurnool Airport, Kurnool, Andhra Pradesh, IN.
  - VOSH/RQY, Shivamogga Airport, Shimoga, Karnataka, IN.
  - WBGY/SGG, Simanggang Airport, Simanggang, Sarawak, MY.
  - YGRM/GYZ, Gruyere Airport, , Western Australia, AU.
  - ZBAL/AXF, Alxa Left Banner Bayanhot Airport, Bayanhot, Inner Mongolia, CN.
  - ZBAR/RHT, Alxa Right Banner Badanjilin Airport, Badanjilin, Inner Mongolia, CN.
  - ZBEN/EJN, Ejina Banner Taolai Airport, , Inner Mongolia, CN.
  - ZBES/YIE, Aershan Yiershi Airport, Arxan, Inner Mongolia, CN.
  - ZBHZ/HUO, Huolinguole Huolinhe Airport, Holingol, Inner Mongolia, CN.
  - ZBMZ/NZH, Manzhouli Xijiao Airport, Manzhouli, Inner-Mongolia, CN.
  - ZBUC/UCB, Ulanqab Jining Airport, Ulanqab, Inner Mongolia, CN.
  - ZBUH/WUA, Wuhai Airport, Wuhai, Inner Mongolia, CN.
  - ZBYZ/RLK, Bayannaoer Tianjitai Airport, Bayannur, Inner Mongolia, CN.
  - ZBZL/NZL, Zhalantun Chengjisihan Airport, Zalantun, Inner Mongolia, CN.
  - ZGYL/YLX, Yulin Fumian Airport, Yulin, Guangxi, CN.
  - ZJQH/BAR, Qionghai Boao Airport, Qionghai, Hainan, CN.
  - ZUDC/DCY, Daocheng Yading Airport, Daocheng County, Sichuan, CN.
  - ZUDR/DDR, Rikaze Dingri Airport, , Tibet, CN.
  - ZUKJ/KJH, Kaili Huangping Airport, Kaili, Guizhou, CN.
  - ZULA/LZG, Langzhong Gucheng Airport, Langzhong, Sichuan, CN.
  - ZULB/LLB, Qiannan Libo Airport, , Guizhou, CN.
  - ZUMT/WMT, Zunyi Maotai Airport, Zunyi, Guizhou, CN.
  - ZUNP/HZH, Qiandongnan Liping Airport, , Guizhou, CN.
  - ZUPS/LPF, Liupanshui Yuezhao Airport, Liupanshui, Guizhou, CN.
  - ZWTK/HQL, Tashkurgan Khunjerab Airport, Tashkurgan, Xinjiang, CN.
  - ZYBS/NBS, Baishan Changbaishan Airport, Baishan, Jilin, CN.
  - ZYSQ/YSQ, Songyuan Chaganhu Airport, Songyuan, Jilin, CN.

* Updated ICAO (and potentially other data) for the following 2 airports:

  - VOVZ/VTZ, Vishakhapatnam Airport, Visakhapatnam, Andhra Pradesh, IN: icao changed from "VEVZ".
  - MMTL/TQO, Felipe Carrillo Puerto International Airport, Tulum, Quintana-Roo, MX: icao changed from "MMTU".

* Updated IATA (and potentially other data) for the following 12 airports:

  - BGSG    , Sermiligaaq Heliport, Sermiligaaq, Sermersooq, GL: iata changed from "SGG".
  - K1Z1/GCT, Grand Canyon Bar Ten Airstrip, Whitmore, Arizona, US: iata added.
  - K41U/NTJ, Manti-Ephraim Airport, Manti, Utah, US: iata added.
  - K44U/SBO, Salina-Gunnison Airport, Salina, Utah, US: iata added.
  - KGNU/GNU, Goodnews Airport, Goodnews, Alaska, US: iata added.
  - KL06/DTH, Furnace Creek Airport, Death Valley National Park, California, US: iata added.
  - LAKU/KFZ, Kukes Airport, Kukes, Kukes, AL: iata added.
  - PAAT/ATU, Casco Cove Cgs Airport, Attu, Alaska, US: iata added.
  - SNAB/JAW, Araripina Airport, Araripina, Pernambuco, BR: iata added.
  - SNSM/OPP, Salinopolis Airport, Salinopolis, Pará, BR: iata added.
  - SWKQ/NSR, Serra da Capivara Airport, Sao Raimundo Nonato, Piauí, BR: iata added.
  - UTNM    , Muynak Airport, Muynak, Karakalpakstan, UZ: iata changed from "MOK", name changed from "Muynaq Airport",
    city changed from "Muynaq".
  - VDKT    , Kratie Airport, Kratie, Kratie, KH: iata changed from "KTI".
  - VICX/KNU, Kanpur Chakeri Airport, Kanpur, Uttar Pradesh, IN: iata added, name changed from "Chakeri Air Force
    Station".
  - VIKA    , Old Kanpur Airport, Kanpur, Uttar Pradesh, IN: iata changed from "KNU", name changed from "Kanpur
    Airport", city added.

* Updated other data for the following 42 airports:

  - CCH2    , Upper Kent Airport, Upper Kent, New Brunswick, CA: city changed from "Clearview".
  - CYAM/YAM, Sault Ste Marie Airport, Sault Sainte Marie, Ontario, CA: city changed from "Sault Ste Marie".
  - CYCG/YCG, Castlegar Airport, Castlegar, British Columbia, CA: name changed from "Castlegar / West Kootenay Regional
    Airport".
  - CYHC/CXH, Vancouver Harbour Airport, Vancouver, British Columbia, CA: name changed from "Vancouver Harbour BC (Water
    Airport)", latitude changed from 49.2945 to 49.28333, longitude changed from -123.11133 to -123.1.
  - CYHM/YHM, John C. Munro Hamilton International Airport, Hamilton, Ontario, CA: name changed from "Hamilton Airport".
  - CYHZ/YHZ, Halifax Robert L. Stanfield International Airport, Halifax, Nova Scotia, CA: name changed from "Halifax /
    Stanfield International Airport".
  - CYJN/YJN, St-Jean Airport, Saint Jean, Quebec, CA: name changed from "St Jean Airport".
  - CYLL/YLL, Lloydminster Airport, Lloydminster, Alberta, CA: subd changed from "Saskatchewan".
  - CYMX/YMX, Montréal (Mirabel) Airport, Mirabel, Quebec, CA: name changed from "Montréal International (Mirabel)
    Airport".
  - CYQM/YQM, Moncton / Greater Moncton International Airport, Moncton, New Brunswick, CA: name changed from "Moncton /
    Greater Moncton Roméo Airport".
  - CYSN/YCM, St. Catharines Niagara District Airport, Niagara-on-the-lake, Ontario, CA: name changed from "St
    Catharines / Niagara District Airport".
  - CYTS/YTS, Timmins Victor M. Power Airport, Timmins, Ontario, CA: name changed from "Timmins (Victor M. Power)
    Airport".
  - CYTZ/YTZ, Billy Bishop Toronto City Airport, Toronto, Ontario, CA: name changed from "Toronto / Billy Bishop Toronto
    City Airport".
  - CYUL/YUL, Montréal-Pierre Elliott Trudeau International Airport, Dorval, Quebec, CA: name changed from "Montréal /
    Pierre Elliott Trudeau International Airport".
  - CYVC/YVC, La Ronge (Barber Field) Airport, La Ronge, Saskatchewan, CA: name changed from "La Ronge(Barber Field)
    Airport".
  - CYWG/YWG, Winnipeg James Armstrong Richardson International Airport, Winnipeg, Manitoba, CA: name changed from
    "Winnipeg / James Armstrong Richardson International Airport".
  - CYWH/YWH, Victoria Harbour Airport, Victoria, British Columbia, CA: name changed from "Victoria Harbour BC (Water
    Seaplane Base)", latitude changed from 48.42283 to 48.41667, longitude changed from -123.3875 to -123.36667.
  - CYXJ/YXJ, Fort St. John Airport, Fort Saint John, British Columbia, CA: name changed from "Fort St John Airport".
  - CYXY/YXY, Erik Nielsen Whitehorse International Airport, Whitehorse, Yukon, CA: name changed from "Whitehorse / Erik
    Nielsen International Airport".
  - CYYT/YYT, St. John's International Airport, Saint John, Newfoundland and Labrador, CA: city changed from "St.
    John's".
  - CYYZ/YYZ, Toronto Pearson International Airport, Mississauga, Ontario, CA: name changed from "Toronto / Lester B.
    Pearson International Airport".
  - CZBB/YDT, Boundary Bay Airport, Ladner, British Columbia, CA: name changed from "Vancouver / Boundary Bay Airport".
  - HESX/SPX, Sphinx International Airport, Giza, Giza, EG: subd changed from "Giza ".
  - KDCA/DCA, Ronald Reagan Washington Ntl Airport, Washington, Dist. Of Columbia, US: subd changed from "District of
    Columbia".
  - KHEF/MNZ, Manassas Regional/Harry P Davis Field, Washington, Dist. Of Columbia, US: subd changed from "District of
    Columbia".
  - KIAD/IAD, Washington Dulles International Airport, Washington, Dist. Of Columbia, US: subd changed from "District of
    Columbia".
  - MBAC    , Ambergris Cay International Airport, Big Ambergris Cay, Big Ambergris Cay, TC: country changed from "GB".
  - NFFA    , Ba Airport, Viti Levu Island, Western, FJ: city added.
  - SSKW/OAL, Cacoal Airport, Cacoal, Rondônia, BR: latitude changed from -11.49121 to -11.4955, longitude changed from
    -61.45261 to -61.45083.
  - VADN/NMB, Daman Airport, , Dadra and Nagar Haveli and Daman and Diu, IN: elevation changed from 33 to 42.
  - VEMH/LDA, Malda Airport, Malda, West Bengal, IN: latitude changed from 25.033 to 25.01116, longitude changed from
    88.133 to 88.1305.
  - VIDX    , Hindon Air Force Station, , Uttar Pradesh, IN: subd changed from "Rajasthan".
  - WAMI/TLI, Toli Toli Airport, Toli Toli-Celebes Island, , ID: latitude changed from 1.12361 to -1.02977, longitude
    changed from 120.79333 to 120.817.
  - YANG/WLP, West Angelas Airport, , Western Australia, AU: subd added.
  - YFDF/KFE, Fortescue - Dave Forrest Aerodrome, Cloudbreak Village, Western Australia, AU: subd changed from "Central
    Sulawesi", latitude changed from 0.0 to -22.2919, longitude changed from 119.42916 to 119.43722.
  - ZBCF/CIF, Chifeng Airport, Chifeng, Inner Mongolia, CN: elevation changed from 0 to 2018.
  - ZJYX    , Woody Island Airport, Woody Island, Hainan, CN: subd added.
  - ZLGY/GYU, Guyuan Liupanshan Airport, Guyuan, Ningxia Hui Autonomous Region, CN: subd changed from "Ningsia-Hui-
    Autonomous-Region".
  - ZSQD/TAO, Qingdao/Jiaodong Airport, Qingdao, Shandong, CN: name changed from "Liuting Airport", elevation changed
    from 33 to 30, latitude changed from 36.2661 to 36.365, longitude changed from 120.374 to 120.09833.
  - ZUAS/AVA, Anshun Huangguoshu Airport, Anshun, Guizhou, CN: subd changed from "Beijing".
  - ZUTR/TEN, Tongren Fenghuang Airport, , Guizhou, CN: subd changed from "Hunan".
  - ZUZY/ZYI, Zunyi Xinzhou Airport, Zunyi, Guizhou, CN: latitude changed from 27.81111 to 27.5895, longitude changed
    from 107.24611 to 107.0007.


Version 20240415
================
* Added IATA code and fixed spelling for UTNM/MOK, Muynaq Airport, Muynaq, Karakalpakstan, Uzbekhistan. Contributed
  by `1oKPro1 <https://github.com/1oKPro1>`__ in PR `#37 <https://github.com/mborsetti/airportsdata/pull/37>`__.
* Added OPRN, Nur Khan Air Base, Rawalpindi, Punjab, Pakistan.


Version 20240409
================
* Reduced file size by 10.2% by removing unnecessary decimal places (fake precision) in latitude and longitude values.
  These values are now rounded to 5 decimal places, which is equivalent to a high accuracy of about 1.11 meters or
  better.
* Added IATA code to KKCL/KCL, Chignik Lagoon Airport, Chignik Lagoon, Alaska, USA


Version 20240401
================
MEGA contribution from `Bohdan Chernykh <https://github.com/ForeverProglamer>`__ in PR `#38
<https://github.com/mborsetti/airportsdata/pull/38>`__:

- assign the right place to SQD IATA code
- assign the right place to GBI IATA code
- assign the right place to SHO IATA code
- assign the right place to BFJ IATA code
- assign the right place to YZY IATA code
- assign the right place to KBH IATA code
- assign the right place to LLJ IATA code
- assign the right places to NIU and NFO IATA codes
- use more accurate coordinates for TLI IATA code place
- assign the right place for CDT IATA code
- assign the right place to CGY IATA code
- assign the right place to YNT IATA code
- assign the right places to INC and YEH IATA codes
- use more accurate coordinates for ZYI IATA code place
- use more accurate coordinates for OAL IATA code place
- assign the right IATA code for a place with OIBP ICAO code


Version 20240316.1
==================
* Added VOGA/GOX, Manohar International Airport, Mopa, Goa, IN. Contributed by `eatdostacos
  <https://github.com/eatdostacos>`__ in PR `#114 <https://github.com/mwgg/Airports/pull/114>`__ upstream.
* Changed ICAO of BKPR/PRN, Pristina International Airport, Pristina, Kosovo (was LYPR). Contributed by `niclaswue
  <https://github.com/niclaswue>`__ in issue `#36 <https://github.com/mborsetti/airportsdata/issues/36>`__.
* Added the following 2 Nav Canada-towered Canadian airports:

  - CYHC/CXH, Vancouver Harbour BC (Water Airport), Vancouver, British Columbia, CA.
  - CYWH/YWH, Victoria Harbour BC (Water Seaplane Base), Victoria, British Columbia, CA.

* Updated data for the following 39 Nav Canada-towered Canadian airports:

  - CCH2, Upper Kent Airport, Clearview, New Brunswick, CA: city added, subd changed from "Maine".
  - CEP4, Ross International Airport, Coutts, Alberta, CA: subd changed from "Montana", tz changed from "America/Denver"
    to "America/Edmonton".
  - CEQ4, Del Bonita / Whetstone International Airport, Del Bonita, Alberta, CA: subd changed from "Montana", tz changed
    from "America/Denver" to "America/Edmonton".
  - CJF5, West Poplar Airport, West Poplar, Saskatchewan, CA: subd changed from "Montana", tz changed from
    "America/Denver" to "America/Regina".
  - CKK3, Scobey Border Station Airport, Coronach, Saskatchewan, CA: subd changed from "Montana", tz changed from
    "America/Denver" to "America/Regina".
  - CTQ2, Weller Airport, Stanstead, Quebec, CA: subd changed from "Vermont", tz changed from "America/New_York" to
    "America/Toronto".
  - CYCG/YCG, Castlegar / West Kootenay Regional Airport, Castlegar, British Columbia, CA: name changed from
    "Castlegar/West Kootenay Regional Airport".
  - CYEV/YEV, Inuvik (Mike Zubko) Airport, Inuvik, Northwest Territories, CA: name changed from "Inuvik Mike Zubko
    Airport".
  - CYFC/YFC, Fredericton International Airport, Fredericton, New Brunswick, CA: name changed from "Fredericton
    Airport".
  - CYGK/YGK, Kingston Airport, Kingston, Ontario, CA: name changed from "Kingston Norman Rogers Airport".
  - CYGL/YGL, La Grande Riviere Airport, Radisson, Quebec, CA: city changed from "La Grande Riviere".
  - CYHM/YHM, Hamilton Airport, Hamilton, Ontario, CA: name changed from "John C. Munro Hamilton International Airport".
  - CYHU/YHU, Montréal / St-Hubert Airport, Longueuil, Quebec, CA: name changed from "Montreal / Saint-Hubert Airport",
    city changed from "Montreal".
  - CYJN/YJN, St Jean Airport, Saint Jean, Quebec, CA: city changed from "St Jean".
  - CYKF/YKF, Kitchener / Waterloo Airport, Waterloo, Ontario, CA: name changed from "Waterloo Airport", city changed
    from "Kitchener".
  - CYKZ/YKZ, Toronto / Buttonville Municipal Airport, Markham, Ontario, CA: name changed from "Buttonville Municipal
    Airport", city changed from "Toronto".
  - CYMX/YMX, Montréal International (Mirabel) Airport, Mirabel, Quebec, CA: name changed from "Montreal International
    (Mirabel) Airport", city changed from "Montreal".
  - CYOW/YOW, Ottawa / Macdonald-Cartier International Airport, Ottawa, Ontario, CA: name changed from "Ottawa
    Macdonald-Cartier International Airport".
  - CYPA/YPA, Prince Albert (Glass Field) Airport, Prince Albert, Saskatchewan, CA: name changed from "Prince Albert
    Glass Field".
  - CYPK/YPK, Pitt Meadows Airport, Pitt Meadows, British Columbia, CA: iata added.
  - CYQB/YQB, Québec City Jean Lesage International Airport, Quebec City, Quebec, CA: name changed from "Quebec Jean
    Lesage International Airport", city changed from "Quebec".
  - CYQL/YQL, Lethbridge Airport, Lethbridge, Alberta, CA: name changed from "Lethbridge County Airport".
  - CYQM/YQM, Moncton / Greater Moncton Roméo Airport, Moncton, New Brunswick, CA: name changed from "Greater Moncton
    International Airport".
  - CYRC, Chicoutimi / St-Honoré Airport, Chicoutimi, Quebec, CA: name changed from "Chicoutimi St Honore Airport".
  - CYSB/YSB, Sudbury Airport, Falconbridge, Ontario, CA: city changed from "Sudbury".
  - CYSN/YCM, St Catharines / Niagara District Airport, Niagara-on-the-lake, Ontario, CA: name changed from "Niagara
    District Airport", city changed from "St Catharines".
  - CYTS/YTS, Timmins (Victor M. Power) Airport, Timmins, Ontario, CA: name changed from "Timmins/Victor M. Power".
  - CYTZ/YTZ, Toronto / Billy Bishop Toronto City Airport, Toronto, Ontario, CA: name changed from "Billy Bishop Toronto
    City Centre Airport".
  - CYUL/YUL, Montréal / Pierre Elliott Trudeau International Airport, Dorval, Quebec, CA: name changed from "Montreal /
    Pierre Elliott Trudeau International Airport", city changed from "Montreal".
  - CYUY/YUY, Rouyn-Noranda Airport, McWatters, Quebec, CA: name changed from "Rouyn Noranda Airport", city changed from
    "Rouyn-Noranda".
  - CYVC/YVC, La Ronge(Barber Field) Airport, La Ronge, Saskatchewan, CA: name changed from "La Ronge Airport".
  - CYVO/YVO, Val-d'Or Airport, Bourlamaque, Quebec, CA: city changed from "Val-d'Or".
  - CYVR/YVR, Vancouver International Airport, Richmond, British Columbia, CA: city changed from "Vancouver".
  - CYXC/YXC, Cranbrook / Canadian Rockies Airport, Cranbrook, British Columbia, CA: name changed from "Cranbrook
    Airport".
  - CYXJ/YXJ, Fort St John Airport, Fort Saint John, British Columbia, CA: city changed from "Fort St.John".
  - CYYY/YYY, Mont-Joli Airport, Mont Jolie, Quebec, CA: name changed from "Mont Joli Airport", city changed from "Mont-
    Joli".
  - CYYZ/YYZ, Toronto / Lester B. Pearson International Airport, Mississauga, Ontario, CA: name changed from "Lester B.
    Pearson International Airport", city changed from "Toronto".
  - CZBB/YDT, Vancouver / Boundary Bay Airport, Ladner, British Columbia, CA: city changed from "Boundary Bay".
  - CZVL, Edmonton / Villeneuve Airport, Saint Albert, Alberta, CA: city changed from "Edmonton".

* Fixed subdivision spelling for the following 3 US-DC airports to conform with ISO 3166-2:

  - KDCA/DCA, Ronald Reagan Washington Ntl Airport, Washington, District of Columbia, US: subd changed from "Dist. Of
    Columbia".
  - KHEF/MNZ, Manassas Regional/Harry P Davis Field, Washington, District of Columbia, US: subd changed from "Dist. Of
    Columbia".
  - KIAD/IAD, Washington Dulles International Airport, Washington, District of Columbia, US: subd changed from "Dist. Of
    Columbia".

* Updated 84 Indian airports, removing hypens in subdivision (e.g. Andhra-Pradesh is now Andhra Pradesh) to conform
  with ISO 3166-2 and making the following changes (partially contributed by `eatdostacos
  <https://github.com/eatdostacos>`__ in PR `#114 <https://github.com/mwgg/Airports/pull/114>`__ upstream):

  - VA1M, Karad Airport, , Maharashtra, IN: subd added.
  - VADN/NMB, Daman Airport, , Dadra and Nagar Haveli and Daman and Diu, IN: subd changed from "Daman-and-Diu".
  - VE91, Vijaynagar Advanced Landing Ground, , Arunachal Pradesh, IN: subd changed from "Sagain", tz changed from
    "Asia/Yangon" to "Asia/Kolkata".
  - VEMH/LDA, Malda Airport, Malda, West Bengal, IN: subd added.
  - VI57, Thoise Airport, , Ladakh, IN: subd changed from "Jammu-and-Kashmir".
  - VI65, Kargil Airport, , Ladakh, IN: subd changed from "Jammu-and-Kashmir".
  - VI66, Fukche Advanced Landing Ground, , Ladakh, IN: subd changed from "Jammu-and-Kashmir".
  - VIDD, Safdarjung Airport, , Delhi, IN: subd changed from "NCT".
  - VIDP/DEL, Indira Gandhi International Airport, New Delhi, Delhi, IN: subd changed from "NCT".
  - VILH/IXL, Leh Kushok Bakula Rimpochee Airport, Leh, Ladakh, IN: subd changed from "Jammu-and-Kashmir".
  - VO94, Campbell Bay Airport, , Andaman and Nicobar Islands, IN: subd changed from "Andaman-and-Nicobar".
  - VOAT/AGX, Agatti Airport, , Lakshadweep, IN: subd changed from "Laccadives".
  - VOCX/CBD, Car Nicobar Air Force Station, , Andaman and Nicobar Islands, IN: subd changed from "Andaman-and-Nicobar".
  - VOPB/IXZ, Vir Savarkar International Airport, Port Blair, Andaman and Nicobar Islands, IN: subd changed from
    "Andaman-and-Nicobar".
  - VOPC/PNY, Pondicherry Airport, , Puducherry, IN: subd changed from "Tamil-Nadu".
  - VORM, Ramnad Naval Air Station, Ramnad, Tamil Nadu, IN: subd added.


Version 20240310.1
===================
* Synchronized the database with data from the U.S. FAA `Airport/Facility Directory (AF/D)
  <https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dafd/>`__ effective 2024-Jan-25:

  - Added 195 new airports;
  - Updated data of 378 airports;
  - Removed 158 closed airports.
  - See full details in `CHANGES_240310.rst <https://github.com/mborsetti/airportsdata/blob/main/CHANGES_240310.rst>`__.
* Updated ICAO code of LLPL, Palmahim Air Base, Rishon LeZion, Israel (was LL59).
* Removed SC49, Oficina Victoria Airport, Oficina Victoria, Tarapaca, Chile (closed).
* Removed UT73, Maymanak Airport, Maynanak, Qashqadaryo, Uzbekistan (closed).


Version 20240309
===================
* Added MZBG/BGK, Big Creek Airport, Big Creek, Toledo, Belize.
* Added MZSL/MZE, Manatee Airport, Spanish Lookout, Cayo, Belize.
* Added SBVC/VDC, Glauber de Andrade Rocha Airport, Vitória da Conquista, Bahia, Brazil. Based on a contribution by
  `maidough <https://github.com/maidough>`__ in PR `#110 <https://github.com/mwgg/Airports/pull/110>`__ upstream, but
  with own research.
* Removed SBQV/VDC, Vitoria da Conquista Airport, Vitoria Da Conquista, Bahia, Brazil, decommissioned on 23 July 2019.
* Added SBHJ/JHF, São Paulo Catarina Executive Airport, São Roque, São Paulo, Brazil. Contributed by `maidough
  <https://github.com/maidough>`__ in PR `#110 <https://github.com/mwgg/Airports/pull/110>`__ upstream.
* Added IATA codes to 218 airports, for a total of 7,814.


Version 20240207
==================
* Added VEAY/AYJ, Maharishi Valmiki International Airport, Ayodhya, Uttar Pradesh, India. Contributed by `Vedant Modi
  <https://github.com/thevedantmodi>`__ in issue `#35 <https://github.com/mborsetti/airportsdata/issues/35>`__.


Version 20240202
==================
* Added ZHEC/EHU, Ezhou Huahu Airport, Ezhou, Hubei, China. Contributed by `HaGoijer  <https://github.com/HaGoijer>`__
  in issue `#34 <https://github.com/mborsetti/airportsdata/issues/34>`__.


Version 20240119
==================
* Changed IATA code of LUKK/RMO, Chișinău International Airport, Chișinău, Chișinău Municipality, Moldova from KIV.
  The change was effective on 18 Jnauary 2024 per `Wikipedia
  <https://en.wikipedia.org/wiki/Chi%C8%99in%C4%83u_International_Airport>`__; the new code is confirmed by the
  airport's `website <https://airport.md/en/about-us/airport-history>`__. Originally contributed upstream by
  `drewblin <https://github.com/drewblin>`__ in PR `#107 <https://github.com/mwgg/Airports/pull/107>`__.


Version 20231230
==================
* Changed IATA code of YTNG/ZBL, Thangool Airport, Biloela, Queensland, Australia from THG. IATA confusingly lists both
  codes for this airport, but the only commercial service there (by Link Airways) uses the ZBL code. Based on a
  contribution by `BhagyalakshmiMurugesan <https://github.com/BhagyalakshmiMurugesan-ninja>`__ in issue `#33
  <https://github.com/mborsetti/airportsdata/issues/33>`__, but with own research.
* Added LETL/TEV, Teruel Airport, Teruel, Aragón, Spain, Based on a contribution upstream by `Gabriel Campo
  <https://github.com/gamma-ninja>`__ in upstream issue `#106 <https://github.com/mwgg/Airports/issues/106>`__,  but
  with data from ARINC.
* Localized subdivision names for Spain.
* Added MMTU/TQO, Felipe Carrillo Puerto International Airport, Tulum, Quintana Roo, Mexico, opened on 1 December
  2023.


Version 20231017
==================
* Addded VDSA/SAI, Siem Reap Angkor International Airport, Siem Reap, Siem-Reap, Cambodia, opened on 05 October
  2023 and replacing VDSR/REP (see `here
  <http://www.civilaviation.gov.kh/images/pdf/ANS/AIP_SUP_2023/AIRAC%20AIP%20SUP%20A5-A6-A7-A8-A9%202023%20EFFICTIVE%2005%20OCT%2023.pdf>`__).


Version 20231007
==================
* Added support for Python 3.12.
* Removed support for Python 3.8 (This does not affect users of the the CSV files). As a reminder, older Python
  versions are supported for 3 years after being obsoleted by a new major release (i.e. about 4 years since their
  original release).
* Added VOKN/CNN, Kannur International Airport, Mattannur, Kerala, India. Based on a contribution upstream by `Ryan-DL
  <https://github.com/Ryan-DL>`__ in PRs `#99 <https://github.com/mwgg/Airports/pull/99>`__
  and `#93 <https://github.com/mwgg/Airports/pull/93>`__, but with official data from Indian AIP.
* Fixed IATA code and name of UELL/NER, Chulman Neryungri Airport, Chulman, Chukot, Russia.


Version 20230906
================
* Fixed regression in 20230905 where Python installation would not include the data files.


Version 20230905
================
* Fixed names of airports, cities, subdivisions (which now match `ISO 3166-2
  <https://en.wikipedia.org/wiki/ISO_3166-2:UA#Current_codes>`__ names) and timezones for Ukraine (contributed by
  `YURII D. <https://github.com/dejurin>`__ via pull request `#30
  <https://github.com/mborsetti/airportsdata/pull/30>`__).
* Fixed script for various Norwegian airports, which lacked accents etc.
* Internal:

  - Upgraded build environment to ``build`` using ``pyproject.toml``, eliminating ``setup.py``.
  - Consolidated tool config files into ``pyproject.toml`` where possible.
  - Simplified timezone testing.
  - Added testing to reach (hopefully) 100% coverage.
  - Upgraded ``tox`` testing framework.
  - Support Python 3.12 (version 3.12.0-rc.1).


Version 20230717
================
* Added new airport LRBV/GHV, Braşov-Ghimbav International Airport, Braşov, Transylvania, Romania (contributed by `Jonas
  Eberle <https://github.com/jonaseberle>`__ in issue `#28 <https://github.com/mborsetti/airportsdata/issues/28>`__).


Version 20230716
================
* Fixed ICAO location identifier in HSSK/KRT, Khartoum International Airport, Khartoum, Sudan (reported by `Jonas Eberle
  <https://github.com/jonaseberle>`__ in issue `#25 <https://github.com/mborsetti/airportsdata/issues/25>`__).
* Fixed altitude and coordinates of SECQ, Coaque Airport, Coaque, Ecuador (reported by `angelabinoyy
  <https://github.com/angelabinoyy>`__ in issue `#26 <https://github.com/mborsetti/airportsdata/issues/26>`__).


Version 20230630
=================
* Added a net of 1,036 IATA location identifiers. Based on contributions upstream by `Justin Dixson
  <https://github.com/JDShadowline>`__ in PRs `#91 <https://github.com/mwgg/Airports/pull/91>`__
  and `#93 <https://github.com/mwgg/Airports/pull/91>`__, but with extensive deduplication and fixes.
* Removed the following entries:
  - FEFL/BEM, Bossembele Airport, Bossembele, Ombella-M'Poko, Central African Republic (closed; "mature trees now
  overhang the former runway");
  - FLLS, Lusaka International Airport, Lusaka, Lusaka, Zambia (replaced by, or renamed as, FLLK);
  - MDPO/EPS, Samana El Portillo Airport, Samana, Samana, Dominican Republic (closed February 2012);
  - MPHO/BLB, Howard Airport, Panama City, Panama, Panama (closed in 1999, became MPPA);
  - OPRN, Benazir Bhutto International Airport, Islamabad, Punjab, Pakistan (closed 3 May 2018, replaced by OPIS);
  - SCEV, El Avellano Airport, Frutillar, Los-Lagos, CL (closed, now a development);
  - SWFJ/FEJ, Feijo Airport, Feijo, Brazil (closed 2008, replaced by SNOU);
  - SWRP/AIR, Aripuana Airport, Aripuana, Mato Grosso do Sul, Brazil (closed, now woods);
  - URFF/SIP, Simferopol International Airport, Simferopol, Republic-of-Crimea, Russia (in Ukraine, duplicate of UKFF);
  - VTBH/KKM, Sa Pran Nak Airport, Lop-Buri, Thailand (correct identifier VTBL);
  - WAOM/MTW, Beringin Airport, Murateweh-Borneo Island, Central Kalimantan, Indonesia (closed 10 September 2020).


Version 20230624
=================
* Added \_OUK/OUK, Out Skerries Airstrip, Shetland, Scotland, Great Britain, LID: EG78. This is a landing strip
  which has an IATA location identifier but no ICAO one, and is not present in GB'S AIP. As such, a pseudo-IATA location
  identifier of ``_OUK`` is used in this database. This airstrip is often identified as ``EG78`` (which is not an
  ICAO location identifier) and this value is used as a pseudo-LID. Based on the upstream PR `#89
  <https://github.com/mwgg/Airports/issues/89>`__ by `Oren Geva <https://github.com/o4oren>`__.
* Added IATA location identifier and fixed information on UESG/BGN, Belaya Gora Airport, Belaya Gora, Sakha Republic,
  Russia (based on the upstream PR `#88 <https://github.com/mwgg/Airports/issues/88>`__ by `tdewin
  <https://github.com/tdewin>`__).
* Removed ETUR/BGN, Brugge Air Base, Nordrhein-Westfalen, Germany, closed on 15 June 2001.
* Added VCRI/HRI, Mattala Rajapaksa International Airport, Hambantota, Southern Province, Sri Lanka (based on
  the upstream PR `#90 <https://github.com/mwgg/Airports/issues/90>`__ by `Justin Dixson
  <https://github.com/JDShadowline>`__).
* Added IATA code to VCCN/KTY, Katukurunda Airport, Kalutara, Western Province, Sri Lanka.
* Updated airport names and province names for airports in Sri Lanka.



Version 20230617
=================
* Multiple fixes and additions suggested by `Nicolas Bridoux <https://github.com/Bridouille>`__ upstream in issue `#86
  <https://github.com/mwgg/Airports/issues/86>`__.
* Added collection of links to national `Aeronautical Information Publications (AIP) or equivalent <https://github
  .com/mborsetti/airportsdata/blob/main/README_AIP.rst>`__.
* Added IATA code to KLAL/LAL, Lakeland Linder International Airport, Lakeland, Florida, USA (reported by `Scott
  Boutang <https://github.com/sboutang>`__ in issue `#23 <https://github.com/mborsetti/airportsdata/issues/23>`__).
* Added IATA codes to multiple KL** airports.


Version 20230528
==================
* Added IATA Multi Airport City Location Identifiers as database file ``iata_macs.csv`` and in a dict
  (containing data of the city's airports) returned by a new Python function; see `README_IATA.rst
  <https://github.com/mborsetti/airportsdata/blob/main/README_IATA.rst>`__) for complete information (requested by
  `Étienne Corbillé <https://github.com/etiennecrb>`__ in issue `#19
  <https://github.com/mborsetti/airportsdata/issues/19>`__).


Version 20230524
==================
* Fixed timezone of KECP/ECP, Northwest Florida Beaches International Airport, Panama City, Florida, USA
  (reported by `DonalChilde <https://github.com/DonalChilde>`__ in issue `#21
  <https://github.com/mborsetti/airportsdata/issues/21>`__).


Version 20230510
==================
* Updated city of EDDF/FRA, Frankfurt am Main International Airport, Frankfurt am Main, Hesse, Germany to remove
  erroneous hyphenation (requested by `Magic Mike <https://github.com/deezknuts>`__ in issue `#20
  <https://github.com/mborsetti/airportsdata/issues/20>`__).


Version 20230509
==================
* Updated Kuwait International's ICAO Location Indicator from OKBK to OKKK. Confirmed with ICAO data.
  (Contributed upstream by `Toni Vicente <https://github.com/arv187>`__ in in PR `#85
  <https://github.com/mwgg/Airports/pull/85>`__).


Version 20230408
==================
* Changed IATA location identifier of UBBG/GNJ, Ganja Airport, Ganja, Goygol-Rayon, Azerbaijan. (Contributed
  upstream by `Vladislav Kobyakov <https://github.com/ayakudere>`__ in in PR `#82
  <https://github.com/mwgg/Airports/pull/82>`__).


Version 20230323
==================
* Added ZUTF/TFU, Chengdu/Tianfu Airport, Tianfu, Sichuan, China


Version 20230303
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
  <https://github.com/vsimakhin>`__ in in PR `#78 <https://github.com/mwgg/Airports/pull/78>`__).


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
* Added Python static type testing using ``mypy``.


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
+===============
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
* The source distribution is now available on PyPI to support certain packagers like ``fpm`` (contributed by Joe Groocock
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
Initial working release of ``airportdata`` as a reworked fork of https://github.com/mwgg/Airports. Changes below are
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
