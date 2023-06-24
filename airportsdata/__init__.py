#!/usr/bin/env python3

"""
Extensive database of location and timezone data for nearly every airport and landing strip in the world.
"""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Literal, TypedDict

__project_name__ = __package__
# Release numbering follows the release date
__version__ = '20230624'
__min_python_version__ = (3, 8)
__author__ = 'Mike Borsetti <mike@borsetti.com>'
__copyright__ = 'Copyright 2020- Mike Borsetti'
__license__ = 'MIT'
__url__ = f'https://github.com/mborsetti/{__project_name__}'

Airport = TypedDict(
    'Airport',
    {
        'icao': str,
        'iata': str,
        'name': str,
        'city': str,
        'subd': str,
        'country': str,
        'elevation': float,
        'lat': float,
        'lon': float,
        'tz': str,
        'lid': str,
    },
)
CodeType = Literal['ICAO', 'IATA', 'LID']
IATAMAC = TypedDict('IATAMAC', {'name': str, 'country': str, 'airports': Dict[str, Airport]})


def load(code_type: CodeType = 'ICAO') -> Dict[str, 'Airport']:
    """Loads airport data into a dict

    :param code_type: optional argument defining the key in the dictionary: 'ICAO' (default if omitted),
    'IATA' (for IATA Location Codes) or 'LID' (for U.S. FAA Location Identifiers).

    :return: a dict of dicts, each entry having the following keys:
        'icao': ICAO 4-letter Location Indicator or 4-alphanumeric FAA/TC LID
        'iata': IATA 3-letter Location Code or an empty string
        'name': Official name (latin script)
        'city': City
        'subd': Subdivision (e.g. state, province, region, etc.)
        'country': ISO 3166-1 alpha 2-code (plus 'XK' for Kosovo)
        'elevation': MSL elevation (the highest point of the landing area) in feet
        'lat': Latitude (decimal)
        'lon': Longitude (decimal)
        'tz': Timezone expressed as a tz database name (IANA-compliant) or empty string for country 'AQ' (Antarctica).
            Originally sourced from [TimeZoneDB](https://timezonedb.com)
        'lid': The FAA Location Identifier (for US country only; others is blank)
    """
    # with open(os.path.join(dir, 'airports.json'), encoding='utf8') as f:
    #     airports = json.load(f)
    # if code_type.lower() == 'icao':
    #     return airports
    # else:
    #     return {airport['iata']: airport for airport in dict(airports).values() if airport['iata']}
    #
    #
    key = code_type.lower()
    if key not in ('icao', 'iata', 'lid'):
        raise ValueError(f'code_type must be one of ICAO, IATA or LID; received {code_type}')
    this_dir = Path(__file__).parent
    airports: Dict[str, Airport] = {}
    with this_dir.joinpath('airports.csv').open(encoding='utf8') as f:
        reader = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            airports[row[key]] = row  # type: ignore[assignment]
    airports.pop('', None)
    return airports


def load_iata_macs() -> dict[str, IATAMAC]:
    """Loads IATA's Multi Airport Cities (for the "purpose of pricing, fare construction and mileage creation")
    data into a dict.

    :return: a dict of dicts, each entry having the following keys:
        'name': The IATA city name,
        'country': The IATA country code,
        'airports': a dict with the same data returned by load() for each airport that makes up the Multi Airport
           City, where the key is the airport's IATA code.
    """
    # with open(os.path.join(dir, 'airports.json'), encoding='utf8') as f:
    #     airports = json.load(f)
    # if code_type.lower() == 'icao':
    #     return airports
    # else:
    #     return {airport['iata']: airport for airport in dict(airports).values() if airport['iata']}
    #
    #
    airports = load('IATA')
    this_dir = Path(__file__).parent
    iata_macs: dict[str, IATAMAC] = {}
    with this_dir.joinpath('iata_macs.csv').open(encoding='utf8') as f:
        reader = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row_d in reader:
            for key, value in row_d.items():
                if key == 'Country':
                    country = value
                elif key == 'City Code':
                    multi_airport_city_code = value
                elif key == 'City Name':
                    name = value
                elif key == 'Airport Code':
                    airport = value
            if multi_airport_city_code not in iata_macs:
                iata_macs[multi_airport_city_code] = {  # type: ignore[assignment]
                    'name': name,
                    'country': country,
                    'airports': {airport: airports[airport]},
                }
            else:
                iata_macs[multi_airport_city_code]['airports'][airport] = airports[airport]
    return iata_macs


# Python 3.9 code used to save the dict to CSV:
# with open('airports.csv', 'w', newline='') as f:
#     fieldnames = airports[list(airports.keys())[0]].keys()
#     writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writeheader()
#     for data in airports.values():
#         writer.writerow(data)
