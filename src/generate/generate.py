from rich.prompt import Prompt
from rich.progress import track
import drawsvg as draw
import random
import uuid
import os

imgs = int(Prompt.ask("How many images would you like to generate?", default=10))
output = Prompt.ask("What is the output folder?", default="output")

CANVAS_HEIGHT = 504
CANVAS_WIDTH = 360

# Tweak to create greater variety in the images
MAX_ITERATIONS = 16
MIN_ITERATIONS = 11

# Create the output folder
os.makedirs(output, exist_ok=True)

# Generate the images
for img in track(range(imgs), description="Generating images"):
  d = draw.Drawing(CANVAS_WIDTH, CANVAS_HEIGHT, origin=(0,0))

  def draw_arc(d, x, h, color):
      rh = h/2
      rx = CANVAS_HEIGHT - rh - x

      l = draw.Arc(0, rx, rh, -90, 90, cw=True, stroke=color, stroke_width=1, fill='none')
      d.append(l)

  d.clear()


  # draw the orange arcs
  iterations = random.randint(MIN_ITERATIONS, MAX_ITERATIONS)
  max_gap = int(CANVAS_HEIGHT / iterations)

  orange = draw.Group()
  for i in range(iterations):
    # randomize the gap size between the arcs
    rg = random.randint(0, max_gap)

    # the first arc should be at the top of the canvas
    if i == 0:
      size = rg = 0

    size = CANVAS_HEIGHT - (max_gap * i) - rg

    draw_arc(orange, 0, size, 'orange')

    # draw the extra arcs
    if i == 13:
      height = CANVAS_HEIGHT - (size * 3)
      draw_arc(orange, size, height, 'orange')

      height = CANVAS_HEIGHT - (size * 6)
      draw_arc(orange, size, height, 'orange')

    if i == 12:
      height = CANVAS_HEIGHT - (size * 3)
      draw_arc(orange, size, height, 'orange')

  # draw blue
  iterations = random.randint(MIN_ITERATIONS, MAX_ITERATIONS)
  max_gap = int(CANVAS_HEIGHT / iterations)

  # to draw the blue arcs we can flip the canvas horizontally and use the same function
  blue = draw.Group(transform='scale(1,-1) translate(0,-504)')
  for i in range(iterations):
    rg = random.randint(0, max_gap)
    size = CANVAS_HEIGHT - (max_gap * i) - rg

    draw_arc(blue, 0, size, 'blue')

  line_r = random.randint(1,2)

  line_color = 'orange'
  if line_r == 2:
    line_color = 'blue'

  line = draw.Group()
  # draw the vertical line
  l = draw.Line(0, 0, 0, 504, stroke=line_color, stroke_width=1)
  line.append(l)

  # generate a unique id for the file
  id = uuid.uuid4()
  
  # Save the blue layer
  d.clear()

  if line_color == 'blue':
    d.append(line)

  d.append(blue)
  d.save_svg(f'{output}/{id}_blue.svg')

  # Save the orange layer
  d.clear()

  if line_color == 'orange':
    d.append(line)

  d.append(orange)
  d.save_svg(f'{output}/{id}_orange.svg')

  # Save the combined layers
  d.clear()
  d.append(line)
  d.append(blue)
  d.append(orange)
  d.save_svg(f'{output}/{id}_combined.svg')


