"""Sort the database and save with integers as integers and with lat/lon precision of 5 digits"""

import csv
from datetime import datetime
import shutil
from pathlib import Path
import airportsdata

from update_readme_counts import load_airportsdata

module_dir = Path(__file__).parent.parent.joinpath('airportsdata')


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
            assert airport['elevation'] == elevation  # noqa: S101 removed when compiling
        airport['lat'] = round(airport['lat'], 6)
        airport['lon'] = round(airport['lon'], 6)
    # Save them
    with data_path.joinpath('airports.csv').open('w', encoding='utf-8', newline='') as f:
        fieldnames = airports[list(airports.keys())[0]].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for data in airports.values():
            writer.writerow(data)


if __name__ == '__main__':
    data_path = Path(__file__).parent.parent.joinpath('airportsdata')
    # make a backup
    make_backup(data_path)
    # load airports
    airports = load_airportsdata(this_dir=module_dir)
    # fix and resave them
    fix_and_save_airports(airports, data_path)
