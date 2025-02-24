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
