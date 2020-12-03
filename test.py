"""Tests"""

import os
import warnings
from glob import glob

import airportsdata

from flake8.api import legacy as flake8

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo

airports = airportsdata.load()
airports_iata = airportsdata.load('IATA')
iso_3166_1 = [
    'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD',
    'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'CV',
    'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU',
    'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI',
    'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW',
    'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE',
    'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG',
    'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ',
    'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS',
    'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF',
    'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS',
    'ES', 'LK', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR',
    'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE',
    'ZM', 'ZW', 'XK']  # As of 2020-11-06
# There is no ISO 3166-1 country code for Kosovo, however "XK" is a self assigned code is used by many
# international organisations per https://en.wikipedia.org/wiki/ISO_3166-2:RS and is the list above
tz_deprecated = [
    'Africa/Asmera', 'Africa/Timbuktu', 'America/Argentina/ComodRivadavia', 'America/Atka', 'America/Buenos_Aires',
    'America/Catamarca', 'America/Coral_Harbour', 'America/Cordoba', 'America/Ensenada', 'America/Fort_Wayne',
    'America/Godthab', 'America/Indianapolis', 'America/Jujuy', 'America/Knox_IN', 'America/Louisville',
    'America/Mendoza', 'America/Montreal', 'America/Porto_Acre', 'America/Rosario', 'America/Santa_Isabel',
    'America/Shiprock', 'America/Virgin', 'Antarctica/South_Pole', 'Asia/Ashkhabad', 'Asia/Calcutta', 'Asia/Chongqing',
    'Asia/Chungking', 'Asia/Dacca', 'Asia/Harbin', 'Asia/Istanbul', 'Asia/Kashgar', 'Asia/Katmandu', 'Asia/Macao',
    'Asia/Rangoon', 'Asia/Saigon', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Ujung_Pandang', 'Asia/Ulan_Bator',
    'Atlantic/Faeroe', 'Atlantic/Jan_Mayen', 'Australia/ACT', 'Australia/Canberra', 'Australia/LHI', 'Australia/North',
    'Australia/NSW', 'Australia/Queensland', 'Australia/South', 'Australia/Tasmania', 'Australia/Victoria',
    'Australia/West', 'Australia/Yancowinna', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West',
    'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific',
    'Canada/Saskatchewan', 'Canada/Yukon', 'CET', 'Chile/Continental', 'Chile/EasterIsland', 'CST6CDT', 'Cuba', 'EET',
    'Egypt', 'Eire', 'EST', 'EST5EDT', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12',
    'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0',
    'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3',
    'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich',
    'Etc/UCT', 'Etc/Universal', 'Etc/UTC', 'Etc/Zulu', 'Europe/Belfast', 'Europe/Nicosia', 'Europe/Tiraspol', 'Factory',
    'GB', 'GB-Eire', 'GMT', 'GMT+0', 'GMT-0', 'GMT0', 'Greenwich', 'Hongkong', 'HST', 'Iceland', 'Iran', 'Israel',
    'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'MST',
    'MST7MDT', 'Navajo', 'NZ', 'NZ-CHAT', 'Pacific/Johnston', 'Pacific/Ponape', 'Pacific/Samoa', 'Pacific/Truk',
    'Pacific/Yap', 'Poland', 'Portugal', 'PRC', 'PST8PDT', 'ROC', 'ROK', 'Singapore', 'Turkey', 'UCT', 'Universal',
    'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii',
    'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Samoa', 'UTC', 'W-SU', 'WET',
    'Zulu']  # from https://www.php.net/timezones.others 2020-11-08


def test_data():
    """Test integrity of the data"""
    for key, airport in airports.items():
        assert key == airport['icao']
        assert airport['icao'].isupper() and len(airport['icao']) in (4, 3)
        assert airport['icao'].isalnum()
        assert isinstance(airport['name'], str)
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
            warnings.warn(DeprecationWarning(f'"{key}": tz "{airport["tz"]}" is deprecated; replace with correct one\n'
                                             f'(see https://github.com/eggert/tz/blob/master/backward)'))


def test_iata_integrity():
    """Test that there are no IATA code duplicates and that the function works correctly"""
    iata = [airport['iata'] for airport in airports.values() if airport['iata']]
    assert len(iata) == len(set(iata))  # no duplicate
    assert list(airports_iata.keys()) == iata  # items returned is identical to those we just built


def test_flake8():
    """Test that we conform to PEP-8"""
    style_guide = flake8.get_style_guide(ignore=['A', 'W503'])
    py_files = [y for x in os.walk(os.path.abspath('airportsdata')) for y in glob(os.path.join(x[0], '*.py'))]
    report = style_guide.check_files(py_files)
    assert report.get_statistics('E') == [], 'Flake8 found violations'


def test_print_database_size():
    """Print database size"""
    print()
    print(f'Number of airports  : {len(airports):6,}')
    print(f'Number of IATA codes: {len(airports_iata):6,}')
