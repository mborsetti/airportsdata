"""Updates counts in readme.rst file."""

import airportsdata

icao_count = len(airportsdata.load('ICAO'))
iata_count = len(airportsdata.load('IATA'))

with open('README.rst') as f:
    README_rst = f.read()
README_rst = README_rst.splitlines(keepends=True)
out_lines = []
for line in README_rst:
    if line.startswith('.. |ICAO| replace::'):
        line = f'.. |ICAO| replace:: {icao_count:,}\n'
    elif line.startswith('.. |IATA| replace::'):
        line = f'.. |IATA| replace:: {iata_count:,}\n'
    out_lines.append(line)
README_rst = ''.join(out_lines)
with open('README.rst', 'w', newline='\n') as f:
    f.write(README_rst)

print(f'Updated counts of entries in README.rst to ICAO={icao_count:,} '
      f'and IATA={iata_count:,}')
