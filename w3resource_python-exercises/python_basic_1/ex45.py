import subprocess

command = input("give command to execute: ")
args = input("give command arguments: ")
subprocess.run([command, args])