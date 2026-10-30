"""Tests."""

__lazy_modules__ = ['importlib.resources']

import sys
from importlib.resources import files
from pathlib import Path

import pytest

sys.path.insert(1, str(Path(__file__).parent.parent))

import airportsdata

pylatest_only = pytest.mark.skipif(
    sys.version_info < (3, 14),
    reason='Data quality and integrity is only checked once, with latest Python version',
)


airports_icao = airportsdata.load('ICAO')
iso_3166_1 = {
    'AF',
    'AX',  # Åland Islands, also part of FI
    'AL',
    'DZ',
    'AS',
    'AD',
    'AO',
    'AI',
    'AQ',
    'AG',
    'AR',
    'AM',
    'AW',
    'AU',
    'AT',
    'AZ',
    'BS',
    'BH',
    'BD',
    'BB',
    'BY',
    'BE',
    'BZ',
    'BJ',
    'BM',
    'BT',
    'BO',
    'BQ',
    'BA',
    'BW',
    'BV',
    'BR',
    'IO',
    'BN',
    'BG',
    'BF',
    'BI',
    'CV',
    'KH',
    'CM',
    'CA',
    'KY',
    'CF',
    'TD',
    'CL',
    'CN',
    'CX',
    'CC',
    'CO',
    'KM',
    'CG',
    'CD',
    'CK',
    'CR',
    'CI',
    'HR',
    'CU',
    'CW',
    'CY',
    'CZ',
    'DK',
    'DJ',
    'DM',
    'DO',
    'EC',
    'EG',
    'SV',
    'GQ',
    'ER',
    'EE',
    'SZ',
    'ET',
    'FK',
    'FO',
    'FJ',
    'FI',
    'FR',
    'GF',
    'PF',
    'TF',
    'GA',
    'GM',
    'GE',
    'DE',
    'GH',
    'GI',
    'GR',
    'GL',
    'GD',
    'GP',
    'GU',
    'GT',
    'GG',
    'GN',
    'GW',
    'GY',
    'HT',
    'HM',
    'VA',
    'HN',
    'HK',
    'HU',
    'IS',
    'IN',
    'ID',
    'IR',
    'IQ',
    'IE',
    'IM',
    'IL',
    'IT',
    'JM',
    'JP',
    'JE',
    'JO',
    'KZ',
    'KE',
    'KI',
    'KP',
    'KR',
    'KW',
    'KG',
    'LA',
    'LV',
    'LB',
    'LS',
    'LR',
    'LY',
    'LI',
    'LT',
    'LU',
    'MO',
    'MG',
    'MW',
    'MY',
    'MV',
    'ML',
    'MT',
    'MH',
    'MQ',
    'MR',
    'MU',
    'YT',
    'MX',
    'FM',
    'MD',
    'MC',
    'MN',
    'ME',
    'MS',
    'MA',
    'MZ',
    'MM',
    'NA',
    'NR',
    'NP',
    'NL',
    'NC',
    'NZ',
    'NI',
    'NE',
    'NG',
    'NU',
    'NF',
    'MK',
    'MP',
    'NO',
    'OM',
    'PK',
    'PW',
    'PS',
    'PA',
    'PG',
    'PY',
    'PE',
    'PH',
    'PN',
    'PL',
    'PT',
    'PR',  # Puerto Rico, also part of US
    'QA',
    'RE',
    'RO',
    'RU',
    'RW',
    'BL',
    'SH',
    'KN',
    'LC',
    'MF',
    'PM',
    'VC',
    'WS',
    'SM',
    'ST',
    'SA',
    'SN',
    'RS',
    'SC',
    'SL',
    'SG',
    'SX',
    'SK',
    'SI',
    'SB',
    'SO',
    'ZA',
    'GS',
    'SS',
    'ES',
    'LK',
    'SD',
    'SR',
    'SJ',  # Svalbard and Jan Mayen, also part of NO
    'SE',
    'CH',
    'SY',
    'TW',
    'TJ',
    'TZ',
    'TH',
    'TL',
    'TG',
    'TK',
    'TO',
    'TT',
    'TN',
    'TR',
    'TM',
    'TC',
    'TV',
    'UG',
    'UA',
    'AE',
    'GB',
    'US',
    'UM',
    'UY',
    'UZ',
    'VU',
    'VE',
    'VN',
    'VG',
    'VI',  # The United States Virgin Islands, also part of US
    'WF',
    'EH',
    'YE',
    'ZM',
    'ZW',
}  # As of 2020-11-06
# There is no ISO 3166-1 country code for the Republic of Kosovo, however 'XK' is a self assigned code that is used by
# many international organisations per https://en.wikipedia.org/wiki/ISO_3166-2:RS#Note
iso_3166_1.add('XK')  # disputed by RS
subdiv = {  # ISO 3166-2 subdivisions for certain countries https://en.wikipedia.org/wiki/ISO_3166-2
    'CA': {
        'Ontario',
        'Quebec',
        'Nova Scotia',
        'New Brunswick',
        'Manitoba',
        'British Columbia',
        'Prince Edward Island',
        'Saskatchewan',
        'Alberta',
        'Newfoundland and Labrador',
        'Northwest Territories',
        'Yukon',
        'Nunavut',
    },
    'IN': {
        'Andhra Pradesh',
        'Arunachal Pradesh',
        'Assam',
        'Bihar',
        'Chhattisgarh',
        'Goa',
        'Gujarat',
        'Haryana',
        'Himachal Pradesh',
        'Jharkhand',
        'Karnataka',
        'Kerala',
        'Madhya Pradesh',
        'Maharashtra',
        'Manipur',
        'Meghalaya',
        'Mizoram',
        'Nagaland',
        'Odisha',
        'Punjab',
        'Rajasthan',
        'Sikkim',
        'Tamil Nadu',
        'Telangana',
        'Tripura',
        'Uttar Pradesh',
        'Uttarakhand',
        'West Bengal',
        'Andaman and Nicobar Islands',
        'Chandigarh',
        'Dadra and Nagar Haveli and Daman and Diu',
        'Delhi',
        'Jammu and Kashmir',
        'Ladakh',
        'Lakshadweep',
        'Puducherry',
    },
    'US': {
        'Alabama',
        'Alaska',
        'Arizona',
        'Arkansas',
        'California',
        'Colorado',
        'Connecticut',
        'Delaware',
        'Florida',
        'Georgia',
        'Hawaii',
        'Idaho',
        'Illinois',
        'Indiana',
        'Iowa',
        'Kansas',
        'Kentucky',
        'Louisiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnesota',
        'Mississippi',
        'Missouri',
        'Montana',
        'Nebraska',
        'Nevada',
        'New Hampshire',
        'New Jersey',
        'New Mexico',
        'New York',
        'North Carolina',
        'North Dakota',
        'Ohio',
        'Oklahoma',
        'Oregon',
        'Pennsylvania',
        'Rhode Island',
        'South Carolina',
        'South Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont',
        'Virginia',
        'Washington',
        'West Virginia',
        'Wisconsin',
        'Wyoming',
        'District of Columbia',
        # 'American Samoa',  # using own ISO 3166-1 country code
        # 'Guam',  # using own ISO 3166-1 country code
        # 'Northern Mariana Islands',  # using own ISO 3166-1 country code
        'Puerto Rico',  # also has own ISO 3166-1 country code
        # 'United States Minor Outlying Islands',  # using own ISO 3166-1 country code
        'Virgin Islands',  # also has own ISO 3166-1 country code
    },
}


def test_loading() -> None:
    """Test no errors in loading module."""
    assert airports_icao


@pylatest_only
def test_data_quality() -> None:
    """Test data quality.

    Fields are icao, iata, name, city, subd, country, elevation, lat, lon, tz, lid.
    """
    for icao, airport in airports_icao.items():
        assert icao == airport['icao']
        assert icao.isupper()
        assert len(icao) == 4
        if icao[0] != '_':
            assert icao.isalnum()
        else:
            assert icao[1:].isalpha()
        # ICAO airport codes do not begin with I, J, X, or Q.
        # In Russia, the Latin letter X is used to designate government, military, and experimental aviation
        # airfields in internal airfield codes similar in structure and purpose to ICAO codes but not used
        # internationally.
        # Codes beginning with I (Ixx and Ixxx) are often used for navigational aids such as radio beacons.
        # The Q code is reserved for international radiocommunications and non-geographical special use.
        if icao != airport['lid'] and airport['country'] != 'RU' and icao != 'XBRO':
            assert icao[0] not in ('I', 'J', 'Q', 'X')
        if airport['iata']:
            assert airport['iata'].isalpha()
            assert airport['iata'].isupper()
            assert len(airport['iata']) == 3
        assert isinstance(airport['name'], str)
        assert isinstance(airport['city'], str)
        assert isinstance(airport['subd'], str)
        assert isinstance(airport['country'], str)
        if airport['lat'] <= -60:  # Antarctica
            assert airport['country'] == 'AQ'
            assert airport['tz'].startswith('Antarctica/')
        else:
            assert airport['country'] in iso_3166_1
        if airport['country'] in subdiv and airport['subd'] not in subdiv[airport['country']]:
            print(airport)
            assert airport['subd'] in subdiv[airport['country']]
        assert isinstance(airport['elevation'], float)
        assert isinstance(airport['lat'], float)
        assert -90 <= airport['lat'] <= 90
        assert isinstance(airport['lon'], float)
        assert -180 <= airport['lon'] <= 180
        if airport['lid']:
            assert len(airport['lid']) in {3, 4, 7}  # 7 is ICAO
            if len(airport['lid']) == 7:
                assert airport['lid'][:2].isalpha()
                assert airport['lid'][2] == '-'
                assert airport['lid'][3:].isdigit()
            elif len(airport['lid']) == 4:
                assert not airport['lid'].isalpha()
                assert airport['lid'].isupper()
                assert airport['lid'].isalnum()
            else:
                assert airport['lid'].isupper()
                assert airport['lid'].isalnum()


@pylatest_only
def test_tz_current() -> None:
    """Test that every tz is a current IANA name, i.e. one listed in zone.tab of the tzdata package.

    zone.tab keeps per-country names that are now links (e.g. Europe/Oslo) but drops retired ones (e.g.
    Pacific/Enderbury), which OS time zone databases may no longer ship. Skipped where tzdata is not installed (it is
    only a test requirement on Windows): checking once is enough.
    """
    zone_country = _zone_tab_countries()
    not_current = {icao: airport['tz'] for icao, airport in airports_icao.items() if airport['tz'] not in zone_country}
    assert not not_current, f'tz not in IANA zone.tab (retired or invalid): {not_current}'


@pylatest_only
def test_tz_country() -> None:
    """Test that every tz is one of the airport's own country per IANA zone.tab (not a neighbour's at the same time).

    Exceptions are our country conventions: US territories PR and VI coded US, Svalbard/Jan Mayen (SJ) coded NO, Åland
    (AX) coded FI, and Kosovo (XK, which has no zone of its own) on Europe/Belgrade.
    """
    zone_country = _zone_tab_countries()
    exceptions = {('US', 'PR'), ('US', 'VI'), ('NO', 'SJ'), ('FI', 'AX'), ('XK', 'RS')}
    wrong_country = {
        icao: (airport['country'], airport['tz'])
        for icao, airport in airports_icao.items()
        if (tz_country := zone_country.get(airport['tz'])) is not None
        and tz_country != airport['country']
        and (airport['country'], tz_country) not in exceptions
    }
    assert not wrong_country, f'tz of another country per IANA zone.tab: {wrong_country}'


def _zone_tab_countries() -> dict[str, str]:
    """Return {tz: ISO 3166-1 country code} from zone.tab of the tzdata package, skipping the test if not installed."""
    pytest.importorskip('tzdata')
    zone_tab = files('tzdata').joinpath('zoneinfo', 'zone.tab').read_text(encoding='utf-8')
    zone_country = {}
    for line in zone_tab.splitlines():
        if line and not line.startswith('#'):
            country, _, tz = line.split('\t')[:3]
            zone_country[tz] = country
    return zone_country


@pylatest_only
def test_load_integrity() -> None:
    """Test that there are no ICAO code duplicates in the CSV file."""
    csv_len = len(Path(__file__).parent.parent.joinpath('airportsdata', 'airports.csv').read_text().splitlines())
    # csv_len = (
    #     bytearray(Path(__file__).parent.parent.joinpath('airportsdata', 'airports.csv').read_bytes()).count(b'\n')
    # )
    if csv_len - 1 != len(airports_icao):  # 1 is header line
        csv = Path(__file__).parent.parent.joinpath('airportsdata', 'airports.csv').read_text()
        icao = set()
        icao_dupes = []
        for line in csv.splitlines()[1:]:
            if line.split(',')[0] in icao:
                icao_dupes.append(line.split(',')[0])
            else:
                icao.add(line.split(',')[0])
        assert icao_dupes == []  # show duplicate(s)


@pylatest_only
def test_iata_integrity() -> None:
    """Test that there are no IATA code duplicates and that the load function works correctly."""
    iata = [airport['iata'] for airport in airports_icao.values() if airport['iata']]
    if len(set(iata)) != len(iata):
        assert {x for x in iata if iata.count(x) > 1} == set()  # show duplicate(s)
    assert list(airportsdata.load('IATA').keys()) == iata  # items returned are identical to those we just built


@pylatest_only
def test_lid_integrity() -> None:
    """Test that there are no LID duplicates and that the load function works correctly."""
    lid = [airport['lid'] for airport in airports_icao.values() if airport['lid']]
    if len(set(lid)) != len(lid):
        assert {x for x in lid if lid.count(x) > 1} == set()  # show duplicate(s)
    assert list(airportsdata.load('LID').keys()) == lid  # items returned are identical to those we just built


@pylatest_only
def test_csv_is_sorted() -> None:
    """Test that database is sorted alphabetically."""
    assert list(airports_icao.keys()) == sorted(airports_icao.keys())


@pylatest_only
def test_iata_macs() -> None:
    """Test that iata_macs are being returned and that NYC has the correct airports."""
    airports_iata = airportsdata.load('IATA')
    iata_macs = airportsdata.load_iata_macs()
    assert len(iata_macs) == 41
    assert list(iata_macs['NYC']['airports'].keys()) == ['JFK', 'LGA']
    for key, mac in iata_macs.items():
        assert key.isupper()
        assert len(key) == 3
        assert key.isalpha()
        assert key.isupper()
        assert isinstance(mac['name'], str)
        assert isinstance(mac['country'], str)
        assert mac['country'] in iso_3166_1
        for iata, airport in mac['airports'].items():
            assert airports_iata[iata] == airport


@pylatest_only
def test_wrong_key() -> None:
    """Test that you receive an error when using the wrong key."""
    with pytest.raises(ValueError, match='code_type must be one of ICAO, IATA or LID; received wrong_key'):
        airportsdata.load('wrong_key')  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]


@pylatest_only
def test_lid_loading() -> None:
    """Test retrieval by LID."""
    assert airportsdata.load('LID')['AK03'] == airports_icao['PAWT']
