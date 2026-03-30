# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Global style, Python code style, tooling and workflow rules live in `~/.claude/CLAUDE.md` and are authoritative — don't duplicate here.  Only exception is that no `mb_*.py` shared libraries are used.

## Project Overview

`airportsdata` is a Python package providing an extensive database of location and timezone data for nearly every airport and landing strip in the world. The data is stored in CSV files and loaded into Python dicts keyed by ICAO, IATA, or FAA LID codes. Published to PyPI with calendar-based versioning (e.g. `2026.03.25`).

## Utilities
```bash
# Sort airports.csv alphabetically and normalize elevation/lat/lon precision
python utils/sort_and_fix.py

# Update airport counts in README.rst and README_IATA.rst
python utils/update_readme_counts.py
```

## Architecture

- **`airportsdata/__init__.py`** — The entire public API. Exports `load(code_type)` and `load_iata_macs()`. Defines `Airport` (TypedDict), `CodeType` (Literal), and `IATAMAC` (TypedDict). Version is set here as `__version__`.
- **`airportsdata/airports.csv`** — The core database. Must be sorted alphabetically by ICAO code. All fields are quoted (QUOTE_NONNUMERIC).
- **`airportsdata/iata_macs.csv`** — IATA Multi Airport Cities data.
- **`tests/test_airportsdata.py`** — Data quality/integrity tests are gated behind `@pylatest_only` (only run on Python >= 3.13). The `test_loading` test runs on all versions.
- **`utils/sort_and_fix.py`** — Sorts the CSV, normalizes elevation to int where possible, rounds lat/lon to 6 decimals. Creates a timestamped backup before modifying.
- **`utils/update_readme_counts.py`** — Updates airport count substitution variables in README.rst files.

## Key Conventions

- Single quotes for strings (configured in ruff).
- Line length limit: 120 characters.
- The CSV must remain sorted alphabetically by ICAO code (`test_csv_is_sorted` enforces this).
- No duplicate ICAO, IATA, or LID codes allowed (tests enforce uniqueness).
- Timezone values must be valid IANA tz database names and must not use deprecated timezone names.
- Country codes must be valid ISO 3166-1 alpha-2 (plus `XK` for Kosovo).
- Dot-prefixed Python files in the repo root (`.ca_data.py`, `.fix_data.py`, etc.) are personal/internal utility scripts, not part of the package.

## .personal_utils

Internal maintenance scripts for updating the database. These are not part of the published package and have external dependencies (`httpx`, `msgpack`, `deepdiff`, `tqdm`, and a private `mb_httpx` module from `~/Documents/python/main_server_python`).

- **`faa_data.py`** — The primary data update tool for US airports. Downloads FAA Location Identifiers (LIDs) from `fly.faa.gov/rmt/data_file/locid_db.csv` and per-airport details from FAA's Airport Data and Information Portal (ADIP) API. Key functions:
  - `update_data_to_latest_adif()` — Main entry point. Compares all FAA ADIP data against the current database, generates added/changed/removed lists, and saves results to `airportsdata/airports2.csv` (not overwriting the main file directly).
  - `adip_to_airport()` — Converts FAA ADIP records to `airportsdata.Airport` format, including name normalization (expanding abbreviations like Rgnl→Regional, Intl→International), state-to-country mapping (FAA state codes → ISO 3166-1), pseudo-ICAO generation (prepending `K` to 3-char LIDs), and timezone lookup via `timezonedb.com` API.
  - `find_missing_entries()` / `find_extra_entries()` — Cross-reference FAA LIDs against the database to find airports we're missing or that no longer exist.
  - `airports_us()` / `airports_no_us()` — Filter the database by FAA geography (US + territories: AS, FM, GU, MH, MP, PW, PR, VI, UM).
  - Cached data files: `.faa_all_lids.json` (all FAA LIDs), `.faa_adips.msgpack` (full ADIP data), `.tz_cache.json` (timezonedb.com results).
- **`iata_codes_sabre.py`** — Cross-checks IATA codes against the Sabre EncodeDecode plugin data (extracted from a local Sabre Red 360 installation). Key functions:
  - `load_new_and_save_iata_codes()` — Extracts IATA codes from the latest Sabre plugin zip and saves a dated JSON snapshot (`.iata_codes_sabre_YYMMDD.json`).
  - `find_errors_in_current_dataset()` — Finds US IATA codes in Sabre but missing from the database, showing nearby airports within 3 km. Also flags airports where coordinates differ by >10 km.
  - `recent_changes()` — Diffs the current Sabre data against the previous JSON snapshot to show additions, removals, and modifications.
  - Includes a `distance()` helper for great-circle distance (WGS-84) calculations.
- **`changes.py`** — Generates CHANGELOG-style diff text between `airports_old.csv` and `airports.csv` using `deepdiff`. Used to prepare release notes. Run with `print_changes(faa=True)` to include FAA deletion reasons.
