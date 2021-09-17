import sass
from os import path

DIR=path.join(path.dirname(__file__), "..", "build", "potree")

with open(path.join(DIR, "potree.css")) as f:
    potree_css = f.read()

potree_css = "#potree{ " + potree_css + "}"

output = path.join(DIR, "potree.isolated.min.css")
with open(output, 'w') as f:
    f.write(sass.compile(string=potree_css, output_style="compressed"))
    print("Wrote %s" % output)
