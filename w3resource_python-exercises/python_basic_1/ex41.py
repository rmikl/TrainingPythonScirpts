from os.path import realpath
import pathlib

file_path = input("Please give a full file path: ")

def check_if_file_exist(file_path):

    full_path_dir = str(pathlib.Path(__file__).parent.absolute())
    full_file_path = full_path_dir + "/" + file_path

    try :
        file = open(full_file_path,'r')
    except FileNotFoundError:
        print("File doesnt exist")
        quit()
    print("File exist")

check_if_file_exist(file_path)