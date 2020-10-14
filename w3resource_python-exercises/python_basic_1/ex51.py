import cProfile

cProfile.run("2+2")

def print_string(string):
    print(string)

cProfile.run('print_string("hello")')