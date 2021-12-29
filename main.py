"""
"Rubrica" (c) by Ignacio Slater M.
"Rubrica" is licensed under a
Creative Commons Attribution 4.0 International License.
You should have received a copy of the license along with this
work. If not, see <https://creativecommons.org/licenses/by/4.0/>.
"""
import sys
import urllib.parse
from pathlib import Path
import pyclip

import pandas

from html_tags import p
from parser import secs_to_html

SRC_CODE = (("Funcionalidad", 1.5, "F"), ("Diseño", 2.5, "D"))
SECTIONS = (
    ("Código fuente", SRC_CODE, 4), ("Coverage", 1, "C"), ("Javadoc", 0.5, "J"),
    ("Resumen", 0.5, "R"),
    ("Adicionales", "A"))

if __name__ == '__main__':
    path = Path(sys.argv[2])
    df = pandas.read_excel(str(path.as_posix()).replace('"', '').replace("'", ""), header=None)
    groups = df.groupby(df[5])

    meta = groups.get_group("N")
    nombre_estudiante = list(meta[1])[0]

    html = f'{p(f"Nota: {list(meta[3])[1]:.1f}")} {p(f"Ayudante: {sys.argv[1]}")}' + \
           secs_to_html(SECTIONS, groups) + (
               f"<br/><br/>Comentarios: {list(meta[1])[1]}" if list(meta[1])[1] != "nan" else "")
    try:
        file_name = f"Comentarios_{urllib.parse.quote_plus(nombre_estudiante)}.html"
    except TypeError:
        file_name = f"Comentarios_.html"
    with open(path.parent / file_name, 'w') as f:
        f.write(html)
    pyclip.copy(html)
