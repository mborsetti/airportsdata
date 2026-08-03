- Version numbering reverted to the historical 8-digit `YYYYMMDD` UTC-date form. The dotted `YYYY.MM.DD`
  form introduced in version 2026.03.15 sorts *below* the pre-existing 8-digit versions under PEP 440
  (e.g. `20260315` > `2026.8.3`), so PyPI and unpinned installs kept resolving version 20260315 as the
  latest. The dotted releases (2026.03.25 through 2026.08.03) remain installable from PyPI when pinned exactly.

- Updated other data for the following airport:

  - SSRS/BRB, Barreirinhas Airport, Barreirinhas, Maranhão, BR: city added.
