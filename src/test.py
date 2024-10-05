# Melissa's test script using axidraw plotter API
# For more information, see https://axidraw.com/doc/py_api/#installation

from pyaxidraw import axidraw   
ad = axidraw.AxiDraw() #connect to AxiDraw
ad.moveto(0, 0) # Move to the origin to start clean
ad.plot_setup("/svg/hashiconf24base.svg") # Load the SVG file
ad.plot_run() # Plot the SVG file
