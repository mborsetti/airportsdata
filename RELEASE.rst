* Fixed names of airports, cities, subdivisions (which now match `ISO 3166-2
  <https://en.wikipedia.org/wiki/ISO_3166-2:UA#Current_codes>`__ names) and timezones for Ukraine (contributed by
  `YURII D. <https://github.com/dejurin>`__ via pull request `#30
  <https://github.com/mborsetti/airportsdata/issues/30>`__).
* Fixed script for various Norwegian airports, which lacked accents etc.
* Internal:

  - Upgraded build environment to ``build`` using ``pyproject.toml``, eliminating ``setup.py``.
  - Consolidated tool config files into ``pyproject.toml`` where possible.
  - Simplified timezone testing.
  - Added testing to reach (hopefully) 100% coverage.
  - Upgraded ``tox`` testing framework.
  - Support Python 3.12 (version 3.12.0-rc.1).

**Notice**

Support for Python 3.8 will be removed on or about 5 October 2023. Older Python versions are supported for 3 years
after being obsoleted by a new major release (i.e. about 4 years since their original release). This will not affect
the CSV file.
