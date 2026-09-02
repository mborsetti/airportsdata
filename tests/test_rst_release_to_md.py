"""Tests for the RELEASE.rst -> RELEASE.md converter."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(1, str(Path(__file__).parent.parent))

from utils.rst_release_to_md import convert


def test_heading() -> None:
    assert convert('Version 20260902\n================\n') == '## Version 20260902\n'


def test_top_level_bullet() -> None:
    assert convert('* item\n') == '- item\n'


def test_inline_literal() -> None:
    assert convert('Use ``YYYYMMDD`` here.\n') == 'Use `YYYYMMDD` here.\n'


def test_passthrough() -> None:
    rst = '**bold**\n\n- nested\n  continuation\n'
    assert convert(rst) == rst


def test_no_trailing_newline_is_preserved() -> None:
    assert convert('* item') == '- item'


@pytest.mark.parametrize(
    ('rst', 'expected'),
    [
        # Anonymous (``__``) and named (``_``) hyperlink targets.
        ('`Yaniv Levy <https://github.com/yanivlevydfs>`__\n', '[Yaniv Levy](https://github.com/yanivlevydfs)\n'),
        ('`keep a changelog <https://keepachangelog.com/>`_\n', '[keep a changelog](https://keepachangelog.com/)\n'),
        # Two links on one line.
        (
            '`#97 <https://example.com/pull/97>`__ and `#95 <https://example.com/issues/95>`__.\n',
            '[#97](https://example.com/pull/97) and [#95](https://example.com/issues/95).\n',
        ),
    ],
)
def test_external_link(rst: str, expected: str) -> None:
    assert convert(rst) == expected


def test_external_link_wrapped_before_url() -> None:
    """A 120-column wrap falling between the link text and its target still converts."""
    rst = 'in PR `#97\n    <https://github.com/mborsetti/airportsdata/pull/97>`__.\n'
    assert convert(rst) == 'in PR [#97](https://github.com/mborsetti/airportsdata/pull/97).\n'


def test_external_link_wrapped_inside_text() -> None:
    """A wrap inside the link text collapses to a single space."""
    rst = '`Yaniv\n    Levy <https://github.com/yanivlevydfs>`__\n'
    assert convert(rst) == '[Yaniv Levy](https://github.com/yanivlevydfs)\n'


def test_inline_literal_is_not_read_as_a_link() -> None:
    """Double-backtick literals belong to _INLINE_LITERAL, even when they contain angle brackets."""
    assert convert('``<not a link>``\n') == '`<not a link>`\n'


def test_backtick_underline_is_still_a_heading() -> None:
    """Link handling runs after heading detection, so a backtick underline cannot be mistaken for one."""
    assert convert('Title\n`````\n') == '## Title\n'


def test_release_rst_round_trip() -> None:
    """The bundled RELEASE.md is in sync with RELEASE.rst when the latter is present (it is untracked)."""
    root = Path(__file__).parent.parent
    rst = root / 'RELEASE.rst'
    if not rst.is_file():
        pytest.skip('RELEASE.rst is local scratch and is not checked in')
    assert convert(rst.read_text(encoding='utf-8')) == (root / 'RELEASE.md').read_text(encoding='utf-8')
