Checked every airport's time zone against the IANA zone boundaries and corrected 695 of them, plus the subdivision of
680 airports (mostly in Brazil). Also realigned the airports of Nigeria with ARINC data, adding 14 of them.

- ZHSY/WDS, Shiyan Wudangshan Airport, Shiyan, Hubei, CN: elevation changed from 0 to 1125 (not AIP-verified; the
  airport is not in the AIP of China). Contributed by [Jianing Wang](https://github.com/jianingfcm).
- Corrected the time zone of the following 193 airports, whose local time was wrong. Source: IANA tz database zone
  boundaries (timezone-boundary-builder, via timezonefinder):

  - Chile, Aysén region (36), to "America/Coyhaique" (UTC−3 all year since IANA tzdata 2025b; **requires tzdata 2025b
    or later**, so older operating system time zone databases will not find it): SCAL, SCAS, SCBA, SCBC, SCBR, SCCC,
    SCCR, SCCY, SCEB, SCEX, SCEY, SCFC, SCHH, SCHR, SCIH, SCII, SCIO, SCLJ, SCLO, SCMA, SCMC, SCMK, SCND, SCOO, SCPH,
    SCPK, SCQO, SCRB, SCRC, SCRE, SCRF, SCRU, SCSZ, SCTP, SCVE, SCVS.
  - Chile, Magallanes region (3), to "America/Punta_Arenas": SCFM, SCGZ, SCNT.
  - Brazil, western Pará (41), from "America/Manaus" to "America/Santarem" (all of Pará is UTC−3): SDUA, SDVU, SDWC,
    SDWX, SILS, SIRJ, SISZ, SITD, SIUJ, SIUX, SIXM, SIYT, SIYW, SJBN, SJDG, SJFG, SJGA, SJGE, SJIY, SJJA, SJKR, SJND,
    SJOH, SJPG, SJQX, SJSE, SJTS, SNCB, SNEH, SNFL, SNIF, SNJZ, SNLD, SNTJ, SNXD, SNXM, SNYR, SSMN, SSRT, SSXN, SWXO.
  - Brazil, airports near state borders (24): to "America/Sao_Paulo" SDEP, SIFH, SJNJ, SNEW, SNSX, SWEC, SWGW, SWJK,
    SWNH, SWOO, SWRT, SWXA; to "America/Cuiaba" SDUS, SISE, SJNW, SSOU, SWAY, SWCN, SWDF, SWSD, SWST; to
    "America/Belem" SNKJ, SNNP, SWGS.
  - Brazil, other (3): SBFN/FEN (Fernando de Noronha) to "America/Noronha"; SWEI/ERN (Eirunepé) to "America/Eirunepe";
    SWJP to "America/Manaus".
  - Canada, Yukon (7), from "America/Vancouver" to "America/Whitehorse" (CYMA, CYQH, CYZW, CZFA) or "America/Dawson"
    (CYDA, CYDB, CYOC).
  - Canada, other (2): CYGR/YGR (Îles-de-la-Madeleine) to "America/Halifax"; CRB5 (Anticosti Island) to
    "America/Toronto".
  - Russia (8): Sakhalin oblast to "Asia/Sakhalin" (UHSB, UHSH, UHSK, UHSM, UHSO, UHSS); UNBU to "Asia/Barnaul"; UEMH
    to "Asia/Khandyga".
  - Papua New Guinea: AYBK/BUA (Buka) to "Pacific/Bougainville".
  - Australia: YBOV (Border Village) to "Australia/Eucla".
  - DR Congo: FZGA/LIQ (Lisala, Mongala) to "Africa/Kinshasa".
  - Mexico (2), border municipalities following US daylight saving time, to "America/Matamoros": MM38, MM82.
  - US (64), airports on the wrong side of a time zone line: to "America/Chicago" 2FL0, 2FL3, 3IN9, 56FD, 5FD1, 5FL8,
    5KS2, 5KS4, 68FD, 72IN, 74FD, 75FL, 88IN, 8KY3, FA55, FD26, FD35, FD94, IN04, IN39, IN41, KMAI, KPAM, NE73, SD59,
    SD73, SD77, TN99; to "America/New_York" 29KY, 34FL, 3KY0, K7A3, KRZR, TN13, TN51; to "America/Denver" 22UT, 84NE,
    9NE6, CO08, ND10, NE33; to "America/Boise" ID09, ID10, ID76, K1DA, K3U0, KU91, OR16; to "America/Los_Angeles"
    07ID, K1U1, K2U5, KC48, KC64, KE85, KS92; to "America/Phoenix" 04AZ, 45AZ, 88AZ; to "America/Nome" PAAM, PAKO,
    PASN; to "America/Indiana/Indianapolis" 3IN3, IN26; to "America/Indiana/Tell_City" 21IN.

- Corrected the time zone of the following 9 airports from local sources:

  - CBX5, Tungsten (Cantung) Airport, Tungsten, Northwest Territories, CA: tz changed from "America/Edmonton" to
    "America/Whitehorse" (the mine keeps Yukon time; Yukon News, 8 March 2013).
  - CCE4/YBI, Black Tickle Airport, Black Tickle, Newfoundland and Labrador, CA: tz changed from "America/Halifax" to
    "America/Goose_Bay" (Canada Flight Supplement: UTC−4(3); Newfoundland time is kept only south of Black Tickle).
  - CNM5/KIF, Kingfisher Lake Airport, and CYAQ/XKS, Kasabonika Airport, Ontario, CA: tz changed from "America/Toronto"
    to "America/Winnipeg" (Canada Flight Supplement: UTC−6(5); IANA tz: the Big Trout Lake area follows Winnipeg).
  - CYEU/YEU, Eureka Airport, Eureka, Nunavut, CA: tz changed from "America/Rankin_Inlet" to "America/Atikokan"
    (Canada Flight Supplement: UTC−5 all year).
  - CFK3, Fontas Airport, Alberta, CA: tz changed from "America/Vancouver" to "America/Edmonton" (the aerodrome is in
    the County of Northern Lights, Alberta, not at Fontas, BC).
  - FZFH, Mokaria-Yamoleka Airport, CD: subdivision changed from "Tshopo" to "Mongala" and tz from "Africa/Lubumbashi"
    to "Africa/Kinshasa" (the ARP is in Bumba territory, Mongala).
  - IN69, Blackmon Field, Monterey, Indiana, US: tz changed from "America/Indiana/Indianapolis" to
    "America/Indiana/Knox" (the field is in Starke County per the US Census geocoder).
  - UWUK/OKT, Oktyabrskiy Airport, Kzyl-Yar, RU: subdivision changed from "Bashkortostan" to "Tatarstan" and tz from
    "Asia/Yekaterinburg" to "Europe/Moscow" (the airport is in Bavlinsky district, Tatarstan).

- Replaced the `tz` of 493 airports with the IANA zone for their location that has the same current UTC offsets, so
  that historical times convert correctly too (e.g. Alaska's Seward Peninsula to "America/Nome", southwestern
  Saskatchewan to "America/Swift_Current", Michigan to "America/Detroit", Sarawak and Sabah to "Asia/Kuching", Broken
  Hill to "Australia/Broken_Hill") (not itemized).
- Corrected the subdivision of 680 airports from their ARP (OpenStreetMap administrative boundaries via Nominatim), not
  itemized: 522 Brazilian airports in Mato Grosso were labelled "Mato Grosso do Sul"; 11 Acre airports were labelled
  "Distrito Federal"; 31 Sakha Republic airports (including Yakutsk) were labelled "Chukot"; western Pará airports were
  labelled "Amazonas"; and 47 Brazilian airports had none. Brazil's Federal District is now spelled "Distrito Federal"
  (ISO 3166-2:BR) and Russia's Sakha Republic "Sakha" throughout.
- Updated ICAO designators for the following 2 airports (source: ARINC):

  - DNEK, Eket Airport, Eket, Akwa Ibom, NG (was DN55); ARP, city and elevation also updated.
  - DNES, Escravos Airport, Escravos, Delta, NG (was DN56); ARP, city and elevation also updated.

- Added the following 14 airports (source: ARINC, except DNOG and _PHG):

  - DNAI/QUO, Victor Attah International Airport, Uyo, Akwa Ibom, NG.
  - DNAN/CHE, Chinua Achebe International Airport, Umueri, Anambra, NG.
  - DNBA, Bauchi Airport, Bauchi, Bauchi, NG.
  - DNBB, Bebi Airstrip, Bebi, Cross River, NG.
  - DNBC/BCU, Sir Abubakar Tafawa Balewa Airport, Bauchi, Bauchi, NG.
  - DNBK, Sir Ahmadu Bello Airport, Birnin Kebbi, Kebbi, NG.
  - DNBY, Bayelsa International Cargo Airport, Yenagoa, Bayelsa, NG.
  - DNDS, Dutse Airport, Dutse, Jigawa, NG.
  - DNFB, Finima Airport, Finima, Rivers, NG.
  - DNFD, Forcados Terminal Airport, Forcados, Delta, NG.
  - DNKT/DKA, Katsina Airport, Katsina, Katsina, NG.
  - DNOG/GWI, Gateway International Airport, Iperu, Ogun, NG (elevation unknown).
  - DNSU/QRW, Osubi Airport, Warri, Delta, NG. Contributed by [Jianing Wang](https://github.com/jianingfcm), who
    also reported EKK (already listed as DNET, Ekiti Agro-Allied International Cargo Airport).
  - _PHG/PHG, Port Harcourt City Airport, Port Harcourt, Rivers, NG (no ICAO location indicator found; elevation
    unknown).

- Updated IATA locator (and potentially other data) for the following airport (source: ARINC):

  - DNAK/AKR, Akure Airport, Akure, Ondo, NG: iata AKR added, elevation changed from 1100 to 1108, latitude changed from
    7.24674 to 7.246667, longitude changed from 5.30101 to 5.301.

- Updated other data for the following 6 Nigerian airports (ARP and elevation source: ARINC; subdivisions to
  ISO 3166-2:NG names):

  - DNAA/ABV, Nnamdi Azikiwe International Airport, Abuja, Abuja Federal Capital Territory, NG: subdivision changed from
    "FCT", elevation changed from 1123 to 1122, latitude changed from 9.00679 to 9.006667, longitude changed from
    7.26317 to 7.263.
  - DNBE/BNI, Benin Airport, Benin City, Edo, NG: city changed from "Benin", elevation changed from 258 to 259, latitude
    changed from 6.31698 to 6.316667, longitude changed from 5.5995 to 5.598833.
  - DNCA/CBQ, Margaret Ekpo International Airport, Calabar, Cross River, NG: subdivision changed from "Cross-River",
    elevation changed from 210 to 209, latitude changed from 4.97602 to 4.976167, longitude changed from 8.3472 to
    8.347167.
  - DNEN/ENU, Akanu Ibiam International Airport, Enugu, Enugu, NG: city changed from "Enegu", elevation changed from 466
    to 514, latitude changed from 6.47427 to 6.473667, longitude changed from 7.56196 to 7.558833.
  - DNGO/GMO, Gombe Lawanti International Airport, Gombe, Gombe, NG: subdivision changed from "Bauchi", elevation
    changed from 1590 to 1589, latitude changed from 10.29833 to 10.298, longitude changed from 10.89639 to 10.899167.
  - DNMN/MXJ, Minna Airport, Minna, Niger, NG: elevation changed from 834 to 898, latitude changed from 9.65217 to
    9.652167, longitude changed from 6.46226 to 6.462167.

- Also updated the latitude, longitude and/or elevation of 15 Nigerian airports where no change exceeded 0.1 degrees or
  30 feet (not itemized). Source: ARINC.
