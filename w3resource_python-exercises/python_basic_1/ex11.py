#i've modify excercise a bit to be a little more difficult
import subprocess, re, pydoc

#output of help("modules") to string output
command = """python -c"help('modules')" """
proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, )
output = str(proc.communicate()[0])

new_line = """
"""

#formatting output of help
o = output.replace("\\n", new_line).replace("ex"," ")
while '  ' in o:
    o = o.replace('  ',' ')
o = o.replace(new_line, " ")
list_o = o.split(" ")

#printing every help that is valid
print(list_o)
for i in list_o:
    try:
        print(pydoc.render_doc(i,renderer=pydoc.plaintext))
    except ImportError:
        print("")
    except IndexError:
        print("")