# HashiConf Art Plotter 2024

## To Do

_ either edit parse.py to separate colors for plots and return one movement plan for purple and one for orange, or create a file that will split the SVGs by color. Splitting SVGs into 2, one per color probably preferred for flexibility based on unknown plotter availability
_ Plotter control functionality for pen up, pen down, return to 0, in plotter.py -Melissa currently in progress
_ Plotter movement plan execution
_ Accept a seed as input to print a movement plan


## Installing the dependencies

To install the dependencies, run the following command from the root of the project:

```shell
make install
```

## Usage

Plotting a piece of art can be done by running:

```bash
$ poetry run python src/plotter.py
$ poetry run python src/plotter.py --svg="static/example.svg"
```

## Contributing

## Requirements

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)  
