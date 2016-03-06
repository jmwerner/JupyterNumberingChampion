from os.path import basename
import json
import sys

input_file_name = sys.argv[1]

notebook = json.loads(open(input_file_name).read())

number_to_add = -1

for cell_number in range(0, len(notebook['cells'])):
    if 'execution_count' in notebook['cells'][cell_number]:
        notebook['cells'][cell_number]['execution_count'] = notebook['cells'][cell_number]['execution_count'] + number_to_add
    if 'outputs' in notebook['cells'][cell_number]:
        for output_number in range(0, len(notebook['cells'][cell_number]['outputs'])):
            if 'execution_count' in notebook['cells'][cell_number]['outputs'][output_number]:
                notebook['cells'][cell_number]['outputs'][output_number]['execution_count'] = notebook['cells'][cell_number]['outputs'][output_number]['execution_count'] + number_to_add


with open(input_file_name, 'w') as fp:
    json.dump(notebook, fp)

print(basename(sys.argv[1]) + " has been overwritten")
