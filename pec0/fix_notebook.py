import json

file_path = '/home/manuel/uned/aprendizaje-profundo/pec0/main.ipynb'

with open(file_path, 'r') as f:
    notebook = json.load(f)

# Find the cell with imports
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        # Check if this is the import cell
        if any('import tensorflow' in line for line in source):
            # Check if load_ext is already there
            if not any('%load_ext tensorboard' in line for line in source):
                # Add newline to the last element if it doesn't have one
                if source[-1].endswith('\n'):
                    pass
                else:
                    source[-1] += '\n'
                
                source.append('%load_ext tensorboard')
                print("Added %load_ext tensorboard")
            else:
                print("Already present")
            break

with open(file_path, 'w') as f:
    json.dump(notebook, f, indent=1)

print("Done")
