"""Sort the database and save with integers as integers and with lat/lon precision of 5 digits"""

import csv
import shutil
from datetime import datetime
from pathlib import Path

import airportsdata

module_dir = Path(__file__).parent.parent.joinpath('airportsdata')


def load_airportsdata(
    code_type: airportsdata.CodeType = 'ICAO',
    filename: str = 'airports.csv',
    data_dir: Path = module_dir,
) -> dict[str, airportsdata.Airport]:
    """Loads airport data into a dict

    :param code_type: optional argument defining the key in the dictionary: 'ICAO' (default if omitted),
    'IATA' (for IATA Location Codes) or 'LID' (for U.S. FAA Location Identifiers).

    :return: a dict of dicts, each entry having the following keys:
        'icao': ICAO 4-letter Location Indicator or 4-alphanumeric FAA/TC LID
        'iata': IATA 3-letter Location Code or an empty string
        'name': Official name (diacritized latin script)
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
    key = code_type.lower()
    if key not in ('icao', 'iata', 'lid'):
        raise ValueError(f'code_type must be one of ICAO, IATA or LID; received {code_type}')
    airports: dict[str, airportsdata.Airport] = {}
    with data_dir.joinpath(filename).open(encoding='utf8') as f:
        reader = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            if row['elevation'] == (elevation_int := int(row['elevation'])):
                row['elevation'] = elevation_int
            airports[row[key]] = row  # type: ignore[assignment]
    airports.pop('', None)
    return airports


def make_backup(data_path: Path) -> None:
    """Make a backup of the airports files"""
    date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    shutil.copy2(data_path.joinpath('airports.csv'), (data_path.joinpath(f'.airports_bak_{date_time}.csv')))


def fix_and_save_airports(airports: dict[str, airportsdata.Airport], data_path: Path) -> None:
    """Save airports to file after cleanup"""
    # Sort them
    airports = {k: v for k, v in sorted(airports.items(), key=lambda x: x[0])}
    # Integers elevation and lat/lon rounded to 5 decimals
    for airport in airports.values():
        elevation = airport['elevation']
        if elevation == int(elevation):
            airport['elevation'] = int(elevation)
            assert airport['elevation'] == elevation
        airport['lat'] = round(airport['lat'], 6)
        airport['lon'] = round(airport['lon'], 6)
    # Save them
    with data_path.joinpath('airports.csv').open('w', encoding='utf-8', newline='') as f:
        fieldnames = airports[next(iter(airports.keys()))].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for data in airports.values():
            writer.writerow(data)


if __name__ == '__main__':
    data_path = Path(__file__).parent.parent.joinpath('airportsdata')
    # make a backup
    make_backup(data_path)
    # load airports
    airports = load_airportsdata(data_dir=module_dir)
    # fix and resave them
    fix_and_save_airports(airports, data_path)
