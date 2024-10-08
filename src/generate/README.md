# Setup

If using pipenv, first create a virtual environment and install the dependencies:

```bash
pipenv shell
```

Then install the dependencies:

```bash
pipenv install
```

# Running the application

To run the application, execute the following command:

```bash
python generate.py
```

You will be prompted to enter the number of random images you want to generate. 

```shell
How many images would you like to generate?: 
```

Then you will be asked to specify the output folder, by default the local folder 
`output` will be used.

```shell
What is the output folder? (output): 
```

The images will be generated in the specified folder split into three different images.
One with the suffix `_blue`, one with the suffix `_orange` and one with the suffix `_combined`.
They are grouped by using a random and unique ID.
