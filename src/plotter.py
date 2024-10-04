import fire

import parsesvg.parse as parsesvg
import axidraw.movements as axidraw

HASHICONF_SVG = "static/example.svg"

def plot(svg=HASHICONF_SVG):
   # Parse the SVG file and extract path data
    raw_paths = parsesvg.parse_file(HASHICONF_SVG)
    # Convert the path data into Path objects
    parsed_paths = parsesvg.parse_paths(raw_paths)
    # Generate movement instructions for the AxiDraw plotter
    movements = axidraw.generate_movements(parsed_paths)

    print(movements)

if __name__ == '__main__':
  fire.Fire(plot)
