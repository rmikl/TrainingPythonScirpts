import pathlib
from os.path import realpath

print(pathlib.Path().absolute())
print(realpath(__file__))
