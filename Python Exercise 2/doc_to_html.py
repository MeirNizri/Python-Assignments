"""
This is a python script that gets as input
(1) name of a Python file that contains a particular module
(2) name of an html output file
the script creates an HTML file that documents the module: the names of the functions in the module,
and the documentation of each function.
"""

import sys

# get the module and html file name
module_name = sys.argv[1][:-3]
html_name = sys.argv[2]

# import and get all the functions name in the module
module = __import__(module_name)
module_functions = [x for x in dir(module) if "__" not in x]

# write the head of the html file, than all functions documentations, and finally the end of the html file
with open(html_name, 'w') as html_file:
    html_file.write(f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n</head>\n<body>'
                    f'<h1 style="text-align:center">All the functions and their documentations in the module {module_name}')
    for func in module_functions:
        html_file.write(f'\n<h2>{func}</h2>'
                        f'{eval("module."+func+".__doc__")}')
    html_file.write('</body>\n</html>')