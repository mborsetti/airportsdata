"""Updates counts in readme.rst file.  Requires Python 3.10."""
from pathlib import Path

import airportsdata

icao_count = len(airportsdata.load('ICAO'))
iata_count = len(airportsdata.load('IATA'))

readme_file = Path('README.rst')
readme = readme_file.read_text()
out_lines = readme.splitlines(keepends=True)
for i, line in enumerate(out_lines):
    if line.startswith('.. |ICAO| replace::'):
        out_lines[i] = f'.. |ICAO| replace:: {icao_count:,}\n'
    elif line.startswith('.. |IATA| replace::'):
        out_lines[i] = f'.. |IATA| replace:: {iata_count:,}\n'
out = ''.join(out_lines)

if out != readme:
    print(f'Updated counts in README.rst to ICAO={icao_count:,} and IATA={iata_count:,}')
    readme_file.write_text(out)
else:
    print(f'No changes to counts in README.rst: ICAO={icao_count:,} and IATA={iata_count:,}')
