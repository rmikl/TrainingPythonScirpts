import os, pathlib
from datetime import datetime
stat = os.stat(pathlib.Path(__file__).absolute())
print(datetime.fromtimestamp(stat.st_birthtime).strftime('%Y-%m-%d %H:%M:%S'))



