import sys, os

sys.stderr.write("test2\n")
os.write(2,b"test3\n")