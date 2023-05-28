"""Tests."""
import sys
import warnings
from pathlib import Path

import airportsdata

import pytest

try:  # required for < Python 3.9
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo  # type: ignore[no-redef]

pylatest_only = pytest.mark.skipif(
    sys.version_info < (3, 11),
    reason='Data quality and integrity is only checked once, with latest Python version',
)


airports_icao = airportsdata.load('ICAO')
iso_3166_1 = {
    'AF',
    'AX',
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
    'PR',
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
    'SJ',
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
    'VI',
    'WF',
    'EH',
    'YE',
    'ZM',
    'ZW',
}  # As of 2020-11-06
# There is no ISO 3166-1 country code for the Republic of Kosovo, however 'XK' is a self assigned code that is used by
# many international organisations per https://en.wikipedia.org/wiki/ISO_3166-2:RS#Note
iso_3166_1.add('XK')
tz_deprecated = {
    'Africa/Asmera',
    'Africa/Timbuktu',
    'America/Argentina/ComodRivadavia',
    'America/Atka',
    'America/Buenos_Aires',
    'America/Catamarca',
    'America/Coral_Harbour',
    'America/Cordoba',
    'America/Ensenada',
    'America/Fort_Wayne',
    'America/Godthab',
    'America/Indianapolis',
    'America/Jujuy',
    'America/Knox_IN',
    'America/Louisville',
    'America/Mendoza',
    'America/Montreal',
    'America/Porto_Acre',
    'America/Rosario',
    'America/Santa_Isabel',
    'America/Shiprock',
    'America/Virgin',
    'Antarctica/South_Pole',
    'Asia/Ashkhabad',
    'Asia/Calcutta',
    'Asia/Chongqing',
    'Asia/Chungking',
    'Asia/Dacca',
    'Asia/Harbin',
    'Asia/Istanbul',
    'Asia/Kashgar',
    'Asia/Katmandu',
    'Asia/Macao',
    'Asia/Rangoon',
    'Asia/Saigon',
    'Asia/Tel_Aviv',
    'Asia/Thimbu',
    'Asia/Ujung_Pandang',
    'Asia/Ulan_Bator',
    'Atlantic/Faeroe',
    'Atlantic/Jan_Mayen',
    'Australia/ACT',
    'Australia/Canberra',
    'Australia/LHI',
    'Australia/North',
    'Australia/NSW',
    'Australia/Queensland',
    'Australia/South',
    'Australia/Tasmania',
    'Australia/Victoria',
    'Australia/West',
    'Australia/Yancowinna',
    'Brazil/Acre',
    'Brazil/DeNoronha',
    'Brazil/East',
    'Brazil/West',
    'Canada/Atlantic',
    'Canada/Central',
    'Canada/Eastern',
    'Canada/Mountain',
    'Canada/Newfoundland',
    'Canada/Pacific',
    'Canada/Saskatchewan',
    'Canada/Yukon',
    'CET',
    'Chile/Continental',
    'Chile/EasterIsland',
    'CST6CDT',
    'Cuba',
    'EET',
    'Egypt',
    'Eire',
    'EST',
    'EST5EDT',
    'Etc/GMT',
    'Etc/GMT+0',
    'Etc/GMT+1',
    'Etc/GMT+10',
    'Etc/GMT+11',
    'Etc/GMT+12',
    'Etc/GMT+2',
    'Etc/GMT+3',
    'Etc/GMT+4',
    'Etc/GMT+5',
    'Etc/GMT+6',
    'Etc/GMT+7',
    'Etc/GMT+8',
    'Etc/GMT+9',
    'Etc/GMT-0',
    'Etc/GMT-1',
    'Etc/GMT-10',
    'Etc/GMT-11',
    'Etc/GMT-12',
    'Etc/GMT-13',
    'Etc/GMT-14',
    'Etc/GMT-2',
    'Etc/GMT-3',
    'Etc/GMT-4',
    'Etc/GMT-5',
    'Etc/GMT-6',
    'Etc/GMT-7',
    'Etc/GMT-8',
    'Etc/GMT-9',
    'Etc/GMT0',
    'Etc/Greenwich',
    'Etc/UCT',
    'Etc/Universal',
    'Etc/UTC',
    'Etc/Zulu',
    'Europe/Belfast',
    'Europe/Nicosia',
    'Europe/Tiraspol',
    'Factory',
    'GB',
    'GB-Eire',
    'GMT',
    'GMT+0',
    'GMT-0',
    'GMT0',
    'Greenwich',
    'Hongkong',
    'HST',
    'Iceland',
    'Iran',
    'Israel',
    'Jamaica',
    'Japan',
    'Kwajalein',
    'Libya',
    'MET',
    'Mexico/BajaNorte',
    'Mexico/BajaSur',
    'Mexico/General',
    'MST',
    'MST7MDT',
    'Navajo',
    'NZ',
    'NZ-CHAT',
    'Pacific/Johnston',
    'Pacific/Ponape',
    'Pacific/Samoa',
    'Pacific/Truk',
    'Pacific/Yap',
    'Poland',
    'Portugal',
    'PRC',
    'PST8PDT',
    'ROC',
    'ROK',
    'Singapore',
    'Turkey',
    'UCT',
    'Universal',
    'US/Alaska',
    'US/Aleutian',
    'US/Arizona',
    'US/Central',
    'US/East-Indiana',
    'US/Eastern',
    'US/Hawaii',
    'US/Indiana-Starke',
    'US/Michigan',
    'US/Mountain',
    'US/Pacific',
    'US/Samoa',
    'UTC',
    'W-SU',
    'WET',
    'Zulu',
}  # from https://www.php.net/timezones.others 2020-11-08; UTC kept in the list as it's non-geographical


def test_loading() -> None:
    """Test no errors in loading module."""
    assert airports_icao


@pylatest_only
def test_data_quality() -> None:
    """Test data quality. Fields are "icao","iata","name","city","subd","country","elevation","lat","lon","tz",
    "lid"."""
    for key, airport in airports_icao.items():
        assert key == airport['icao']
        assert key.isupper()
        assert len(key) == 4
        if key[0] != '_':
            assert key.isalnum()
        else:
            assert key[1:].isalpha()
        if airport['iata']:
            assert airport['iata'].isalpha() and airport['iata'].isupper() and len(airport['iata']) == 3
        assert isinstance(airport['name'], str)
        assert isinstance(airport['city'], str)
        assert isinstance(airport['subd'], str)
        assert isinstance(airport['country'], str)
        assert airport['country'] in iso_3166_1
        assert isinstance(airport['elevation'], float)
        assert isinstance(airport['lat'], float)
        assert isinstance(airport['lon'], float)
        assert ZoneInfo(airport['tz'])
        if airport['tz'] in tz_deprecated:
            warnings.warn(
                DeprecationWarning(
                    f'"{key}": tz "{airport["tz"]}" is deprecated; replace with correct one\n'
                    f'(see https://github.com/eggert/tz/blob/master/backward)'
                )
            )
        if airport['lid']:
            assert len(airport['lid']) in {3, 4}
            assert airport['lid'].isupper()
            assert airport['lid'].isalnum()
            if len(airport['lid']) == 4:
                assert not airport['lid'].isalpha()


@pylatest_only
def test_load_integrity() -> None:
    """Test that there are no ICAO code duplicates in the CSV file."""
    csv_len = bytearray(Path(__file__).parent.parent.joinpath('airportsdata', 'airports.csv').read_bytes()).count(b'\n')
    assert csv_len - 1 == len(airports_icao)  # 1 is header line


@pylatest_only
def test_iata_integrity() -> None:
    """Test that there are no IATA code duplicates and that the load function works correctly."""
    iata = [airport['iata'] for airport in airports_icao.values() if airport['iata']]
    if len(set(iata)) != len(iata):
        assert set([x for x in iata if iata.count(x) > 1]) == set()  # show duplicate(s)
    assert list(airportsdata.load('IATA').keys()) == iata  # items returned are identical to those we just built


@pylatest_only
def test_lid_integrity() -> None:
    """Test that there are no LID duplicates and that the load function works correctly."""
    lid = [airport['lid'] for airport in airports_icao.values() if airport['lid']]
    if len(set(lid)) != len(lid):
        assert set([x for x in lid if lid.count(x) > 1]) == set()  # show duplicate(s)
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
