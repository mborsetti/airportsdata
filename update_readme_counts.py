"""Updates counts in readme.rst file."""

import airportsdata

icao_count = len(airportsdata.load('ICAO'))
iata_count = len(airportsdata.load('IATA'))

print(f'Updating counts in README.rst to ICAO={icao_count} IATA={iata_count}')

with open('README.rst') as f:
    README_rst = f.read()
README_rst = README_rst.splitlines(keepends=True)
for line in README_rst:
    if line.startswith('.. |ICAO| replace::'):
        line = f'.. |ICAO| replace:: {icao_count:6}'
    elif line.startswith('.. |ICAO| replace::'):
        line = f'.. |ICAO| replace:: {iata_count:6}'
README_rst = ''.join(README_rst)
with open('README.rst', 'w') as f:
    f.write(README_rst)
