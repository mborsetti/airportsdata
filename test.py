"""Tests"""

import os
from glob import glob

from flake8.api import legacy as flake8

import airportsdata

airports = airportsdata.load()
iso_3166_1 = ['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS',
              'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN',
              'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG',
              'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ',
              'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH',
              'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU',
              'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP',
              'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV',
              'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM',
              'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW',
              'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH',
              'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI',
              'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH',
              'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY',
              'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW', 'XK']
# There is no ISO 3166-1 country code for Kosovo, however "XK" is a self assigned code is used by many international
# organisations per https://en.wikipedia.org/wiki/ISO_3166-2:RS and is added to the list above


def test_data():
    """Test data integrity"""
    for key, airport in airports.items():
        assert key == airport['icao']
        assert isinstance(airport['icao'], str)
        assert len(airport['icao']) in (4, 3)
        assert isinstance(airport['iata'], str)
        assert len(airport['iata']) in (0, 3)
        assert isinstance(airport['name'], str)
        assert isinstance(airport['city'], str)
        assert isinstance(airport['subd'], str)
        assert isinstance(airport['country'], str)
        assert airport['country'] in iso_3166_1
        assert len(airport['country']) == 2
        assert isinstance(airport['elevation'], float)
        assert isinstance(airport['lat'], float)
        assert isinstance(airport['lon'], float)
        assert isinstance(airport['tz'], str)
        if airport['country'] != 'AQ':
            assert len(airport['tz'])
            assert '/' in airport['tz']


def test_iata_integrity():
    """Test that there are no IATA code duplicates and that the function works correctly"""
    iata = [airport['iata'] for airport in airports.values() if airport['iata']]
    assert len(iata) == len(set(iata))
    assert list(airportsdata.load(code_type='IATA').keys()) == iata
    import sys
    if sys.version_info >= (3, 8):
        print(f'{len(airports)=:,}')
        print(f'{len(iata)=:,}')


def test_flake8():
    """Test that we conform to PEP-8."""
    style_guide = flake8.get_style_guide(ignore=['A', 'W503'])
    py_files = [y for x in os.walk(os.path.abspath('airportsdata')) for y in glob(os.path.join(x[0], '*.py'))]
    report = style_guide.check_files(py_files)
    assert report.get_statistics('E') == [], 'Flake8 found violations'
