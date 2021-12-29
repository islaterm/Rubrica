"""
"Rubrica" (c) by Ignacio Slater M.
"Rubrica" is licensed under a
Creative Commons Attribution 4.0 International License.
You should have received a copy of the license along with this
work. If not, see <https://creativecommons.org/licenses/by/4.0/>.
"""


def h1(s: str) -> str:
    """
    Surrounds a string with _h1_ html tag.
    """
    return f"<h1>{s}</h1>\n"


def h2(s: str) -> str:
    """
    Surrounds a string with _h2_ html tag.
    """
    return f"<h2>{s}</h2>\n"


def li(s: str) -> str:
    """
    Surrounds a string with _li_ html tag.
    """
    return f"<li>{s}</li>\n"


def ul(s: str) -> str:
    """
    Surrounds a string with _ul_ html tag.
    """
    return f"<ul>{s}</ul>\n"


def p(s: str) -> str:
    """
    Surrounds a string with _p_ html tag.
    """
    return f"<p>{s}</p>\n"
