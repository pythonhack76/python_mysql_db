import os
import pathlib
import collections


percorso = pathlib.Path.cwd() 
suffisso = percorso.suffix
nome = percorso.name 

#printa albero delle directories 
def tree(directory):
    print(f' + {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '  ' * depth
        print(f'{spacer}+ {path.name}')


tree(pathlib.Path.cwd())

# with open(percorso, mode='r') as fid:
#     headers = [line.strip() for line in fid if line.startswith('#')]
# print('\n'.join(headers))


