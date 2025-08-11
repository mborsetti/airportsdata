"""Updates counts in readme.rst file.  Requires Python >= 3.10."""

import csv
from pathlib import Path

from airportsdata import IATAMAC, Airport, CodeType

module_dir = Path(__file__).parent.parent.joinpath('airportsdata')


def load_airportsdata(
    code_type: CodeType = 'ICAO',
    filename: str = 'airports.csv',
    data_dir: Path = module_dir,
) -> dict[str, Airport]:
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
    airports: dict[str, Airport] = {}
    with data_dir.joinpath(filename).open(encoding='utf8') as f:
        reader = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            if row['elevation'] == (elevation_int := int(row['elevation'])):
                row['elevation'] = elevation_int
            airports[row[key]] = row  # type: ignore[assignment]
    airports.pop('', None)
    return airports


def load_iata_macs(
    filename: str = 'iata_macs.csv',
    this_dir: Path = Path(__file__).parent,
) -> dict[str, IATAMAC]:
    """Loads IATA's Multi Airport Cities (for the "purpose of pricing, fare construction and mileage creation")
    data into a dict.

    :return: a dict of dicts, each entry having the following keys:
        'name': The IATA city name,
        'country': The IATA country code,
        'airports': a dict with the same data returned by load() for each airport that makes up the Multi Airport
           City, where the key is the airport's IATA code.
    """
    airports = load_airportsdata('IATA', data_dir=this_dir)
    iata_macs: dict[str, IATAMAC] = {}
    row_d: dict[str, str]
    with this_dir.joinpath(filename).open(encoding='utf8') as f:
        reader = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC)
        multi_airport_city_code = ''
        name = ''
        country = ''
        airport = ''
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
                iata_macs[multi_airport_city_code] = {
                    'name': name,
                    'country': country,
                    'airports': {airport: airports[airport]},
                }
            else:
                iata_macs[multi_airport_city_code]['airports'][airport] = airports[airport]
    return iata_macs


def update_readme_counts() -> None:
    icao_count = len(load_airportsdata('ICAO', data_dir=module_dir))
    iata_count = len(load_airportsdata('IATA', data_dir=module_dir))
    lid_count = len(load_airportsdata('LID', data_dir=module_dir))

    readme_file = module_dir.parent.joinpath('README.rst')
    readme = readme_file.read_text()
    out_lines = readme.splitlines(keepends=True)
    for i, line in enumerate(out_lines):
        if line.startswith('.. |ICAO| replace::'):
            out_lines[i] = f'.. |ICAO| replace:: {icao_count:,}\n'
        elif line.startswith('.. |IATA| replace::'):
            out_lines[i] = f'.. |IATA| replace:: {iata_count:,}\n'
        elif line.startswith('.. |LID| replace::'):
            out_lines[i] = f'.. |LID| replace:: {lid_count:,}\n'
            break
    out = ''.join(out_lines)
    if out != readme:
        print(f'Updated counts in README.rst to ICAO={icao_count:,}, IATA={iata_count:,} and LID={lid_count:,}')
        readme_file.write_text(out, newline='\n')
    else:
        print(f'No changes to counts in README.rst: ICAO={icao_count:,}, IATA={iata_count:,} and LID={lid_count:,}')


def update_readme_iata_counts() -> None:
    iata_macs_count = len(load_iata_macs(this_dir=module_dir))
    iata_macs_apts_count = sum(len(a['airports']) for a in load_iata_macs(this_dir=module_dir).values())

    readme_file = module_dir.parent.joinpath('README_IATA.rst')
    readme = readme_file.read_text()
    out_lines = readme.splitlines(keepends=True)
    for i, line in enumerate(out_lines):
        if line.startswith('.. |IATA_MACs| replace::'):
            out_lines[i] = f'.. |IATA_MACs| replace:: {iata_macs_count:,}\n'
        if line.startswith('.. |IATA_MACs_apts| replace::'):
            out_lines[i] = f'.. |IATA_MACs_apts| replace:: {iata_macs_apts_count:,}\n'
            break
    out = ''.join(out_lines)
    if out != readme:
        print(
            f'Updated counts in README_IATA.rst to IATA_MACs={iata_macs_count:,} and '
            f'IATA_MACs_apts={iata_macs_apts_count:,}'
        )
        readme_file.write_text(out, newline='\n')
    else:
        print(
            f'No changes to counts in README_IATA.rst: IATA_MACs={iata_macs_count:,} and '
            f'IATA_MACs_apts={iata_macs_apts_count:,}'
        )


if __name__ == '__main__':
    update_readme_counts()
    update_readme_iata_counts()
