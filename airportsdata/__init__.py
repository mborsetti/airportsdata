#!/usr/bin/env python3

"""
Extensive database of current data for nearly every airport and landing strip in the world
"""

import csv
import os
import sys

from typing import Dict
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__project_name__ = __package__
# Release numbering follows the release data
__version__ = '20201203'
__min_python_version__ = (3, 6)
__author__ = 'Mike Borsetti <mike@borsetti.com>'
__copyright__ = 'Copyright 2020- Mike Borsetti'
__license__ = 'MIT'
__url__ = f'https://github.com/mborsetti/{__project_name__}'

Airports = TypedDict('Airports', {'icao': str, 'iata': str, 'name': str, 'city': str, 'subd': str,
                                  'country': str, 'elevation': float, 'lat': float, 'lon': float, 'tz': str})


def load(code_type: str = 'ICAO') -> Dict[str, Airports]:
    """Loads airport data into a dict

    :param code_type: optional argument defining the key in the dictionary: 'ICAO' (default if omitted) or 'IATA'
    :type code_type: str
    :return: a dict of dicts, each entry having the following keys:
        'icao': ICAO 4-character code or FAA 3-character code
        'iata': IATA 3-letter code or an empty string
        'name': official name (latin script)
        'city': city
        'subd': subdivision (e.g. state, province, region, etc.)
        'country': ISO 3166-1 alpha 2-code + 'XK' for Kosovo
        'elevation': MSL elevation (the highest point of the landing area) in feet
        'lat': latitude (decimal)
        'lon': longitude (decimal)
        'tz': timezone expressed in tz database name (IANA-compliant) string (empty string for 'AQ' Antarctica).
            Originally sourced from [TimeZoneDB] (https://timezonedb.com)
    :rtype: dict
    """
    # with open(os.path.join(dir, 'airports.json'), encoding='utf8') as f:
    #     airports = json.load(f)
    # if code_type.lower() == 'icao':
    #     return airports
    # else:
    #     return {airport['iata']: airport for airport in dict(airports).values() if airport['iata']}
    #
    #
    this_dir, _ = os.path.split(__file__)
    key = 'icao' if code_type.lower() == 'icao' else 'iata'
    airports = {}
    with open(os.path.join(this_dir, 'airports.csv'), encoding='utf8') as f:
        fieldnames = f.readline().replace('"', '').rstrip().split(',')
        reader = csv.DictReader(f, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            airports[row[key]] = row
    airports.pop('', None)
    return airports


# Python 3.9 code used to save the dict to CSV:
# with open('airports.csv', 'w', encoding='utf8', newline='') as f:
#     fieldnames = airports[list(airports.keys())[0]].keys()
#     writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writeheader()
#     for data in airports.values():
#         writer.writerow(data)
