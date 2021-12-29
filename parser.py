"""
"Rubrica" (c) by Ignacio Slater M.
"Rubrica" is licensed under a
Creative Commons Attribution 4.0 International License.
You should have received a copy of the license along with this
work. If not, see <https://creativecommons.org/licenses/by/4.0/>.
"""

import pandas

from html_tags import h1, h2, li, ul


def parse_scores(groups: pandas.DataFrame, cat: str) -> tuple[str, float]:
    data = groups.get_group(cat)
    score = 0
    ret = ""
    for row in data.iterrows():
        row_data = row[1][:5]

        if not isinstance(row_data[3], str) and row_data[3] != 0:
            ret += li(f"{row_data[1]:+.2f}x{row_data[2]} {row_data[0]}")
            score += row_data[1] * row_data[2]
            if str(row_data[4]) != 'nan':
                ret += ul(li(row_data[4]))
    return ul(ret), score


def subsec(groups: pandas.DataFrame, name: str, total: float, cat: str) -> str:
    ret, score = parse_scores(groups, cat)
    return h2(f"{name} ({max(total + score, 0):.1f}/{total})") + ul(ret)


def parse_sec(groups: pandas.DataFrame, name: str, total: float, cat: str) -> str:
    ret, score = parse_scores(groups, cat)
    return h1(f"{name} ({max(total + score, 0):.1f}/{total})") + ul(ret)


def subsecs_to_html(sections: tuple[tuple], groups: pandas.DataFrame) -> str:
    return "\n".join([subsec(groups, *sec) for sec in sections])


def secs_to_html(sections: tuple[tuple], groups: pandas.DataFrame) -> str:
    html = ""
    for sec in sections:
        match sec:
            case (sec_name, scores):
                html += h1(sec_name) + parse_scores(groups, scores)[0]
            case (sec_name, [*subsecs], *_):
                html += h1(sec_name) + subsecs_to_html(subsecs, groups)
            case _:
                html += parse_sec(groups, *sec)
    return html
