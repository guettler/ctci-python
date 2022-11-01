from pathlib import Path


def copy_file(source_path, target_path):

    with open(source_path, 'r') as firstfile, open(target_path, 'w') as targetfile:
        for line in firstfile:
            targetfile.write(line)

