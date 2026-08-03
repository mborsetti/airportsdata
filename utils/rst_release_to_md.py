"""Convert ``RELEASE.rst`` (a narrow RST subset) to ``RELEASE.md`` for the GitHub Release body.

Run as a pre-commit hook so the bundled ``RELEASE.md`` consumed by ``softprops/action-gh-release``
stays in sync with the human-edited ``RELEASE.rst``. Only the constructs that actually appear in
``RELEASE.rst`` are supported (see :func:`convert`); reach for pandoc if anything more general is
ever needed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# RST permits any of these as section-underline characters. Only backticks appear in
# RELEASE.rst today, but the rest are accepted defensively so a future header style change
# doesn't silently slip through.
_UNDERLINE_CHARS = frozenset('`=-~^\'":+*#<>')

# Non-greedy double-backtick literal (``foo``) -> single-backtick code span.
_INLINE_LITERAL = re.compile(r'``([^`]+)``')


def convert(rst: str) -> str:
    """Convert a small subset of reStructuredText to GitHub-flavoured Markdown.

    Supported constructs:
        * Section heading -- ``Title\\n<line of one repeated punctuation char of >= length>``
          becomes ``## Title``.
        * Inline literal -- ````foo```` becomes ``\\`foo\\```.
        * Top-level bullet -- ``* item`` becomes ``- item`` (``*`` can be misread as emphasis
          by stricter Markdown parsers).
        * Bold (``**foo**``), nested bullets, blank lines and bullet continuation lines pass
          through unchanged.

    Args:
        rst: The reStructuredText source.

    Returns:
        Markdown text. A trailing newline is preserved iff ``rst`` had one.
    """
    lines = rst.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        # Heading: non-empty line followed by an underline of one repeated char of >= length.
        if (
            line.strip()
            and i + 1 < n
            and lines[i + 1]
            and len(set(lines[i + 1])) == 1
            and lines[i + 1][0] in _UNDERLINE_CHARS
            and len(lines[i + 1]) >= len(line.rstrip())
        ):
            out.append(f'## {line.rstrip()}')
            i += 2
            continue
        if line.startswith('* '):
            line = '- ' + line[2:]
        # Inline literals run after heading detection, so backtick underlines can never match.
        line = _INLINE_LITERAL.sub(r'`\1`', line)
        out.append(line)
        i += 1
    text = '\n'.join(out)
    if rst.endswith('\n'):
        text += '\n'
    return text


def main(paths: list[str]) -> int:
    """Convert every ``*.rst`` path on the command line to its sibling ``*.md``.

    Returns 1 if any output file was created or updated (so the pre-commit hook fails on first
    run and passes on a re-run), 0 otherwise. Mirrors the contract of
    ``tools/update_schema_hashes.py``.

    Args:
        paths: Source ``.rst`` paths, typically supplied by pre-commit via ``sys.argv[1:]``.

    Returns:
        Process exit code: 1 on any change, 0 otherwise.
    """
    changed = 0
    for path_str in paths:
        src = Path(path_str)
        if not src.is_file():
            continue
        new_content = convert(src.read_text(encoding='utf-8'))
        dst = src.with_suffix('.md')
        try:
            existing = dst.read_text(encoding='utf-8')
        except FileNotFoundError:
            existing = ''
        if existing != new_content:
            dst.write_text(new_content, encoding='utf-8', newline='\n')
            changed += 1
            print(f'Updated {dst}')
    return 1 if changed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
